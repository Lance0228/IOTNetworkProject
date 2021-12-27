from django.shortcuts import render
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.conf import settings

import os
import os.path as osp
import sys
BUILD_DIR = osp.join(osp.dirname(osp.abspath(__file__)), "../build/service/")
sys.path.insert(0, BUILD_DIR)

import json
import grpc
import fib_pb2
import fib_pb2_grpc
import log_pb2
import log_pb2_grpc

import paho.mqtt.client as mqtt

from .models import History

FIB_SERVER = "127.0.0.1:8080"
LOG_SERVER = "127.0.0.1:8081"
MQTT_PORT = 1883
DOCKER_IP = "127.0.0.1"
DOCKER_PORT = 1883

# Create your views here.
class FibView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def __init__(self):
        self.client = mqtt.Client()
        self.client.connect(host=DOCKER_IP, port=int(DOCKER_PORT))

    def post(self, request):
        decoded = request.body.decode('utf-8')
        body = json.loads(decoded)
        data = body['order']
        with grpc.insecure_channel(FIB_SERVER) as channel:
            stub = fib_pb2_grpc.FibCalculatorStub(channel)

            request = fib_pb2.FibRequest()
            order = int(data)
            request.order = order 
            response = stub.Compute(request)
            
            history = History(success=True, order = order, result = response.value)
            self.client.publish(topic="history", payload=order)
            
            return Response(data={ 'success': True, 'data': response.value }, status=200)

class LogView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        with grpc.insecure_channel(LOG_SERVER) as channel:
            stub = log_pb2_grpc.LogServiceStub(channel)

            request = log_pb2.LogRequest()
            response = stub.Get(request)

            return Response(data={ 'success': True, 'history': response.history[:] }, status=200)
