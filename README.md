```bash
# Install protobuf compiler
$ sudo apt-get install protobuf-compiler

# Install buildtools
$ sudo apt-get install build-essential make

# Install grpc packages
$ pip3 install -r requirements.txt
```

## Compile protobuf schema to python wrapper

```bash
cd grpc_server/fibServer && make
cd grpc_server/logServer && make
cd rest-server && make

```

## Run the eclipse mosquitto docker container

```bash
sudo docker run -d -it -p 1883:1883 -v $(pwd)/grpc_server/logServer/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
```

## Run gRPC server and REST logServer

```bash
cd grpc_server/fibServer && python3 server.py --ip 0.0.0.0 --port 8080 

# open a new terminal
cd grpc_server/logServer && python3 server.py  --port 8081 

# open a new terminal
cd rest-server 
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000 
```



## Commands to run

**Send to server**

`curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/rest/fibonacci -d "{\"order\":\"{NUMBER}\"}"`



**To Get History**

`curl 127.0.0.1:8000/rest/logs`

