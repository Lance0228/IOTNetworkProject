# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: log.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='log.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tlog.proto\"\x0c\n\nLogRequest\"\x1e\n\x0bLogResponse\x12\x0f\n\x07history\x18\x01 \x03(\x03\x32.\n\nLogService\x12 \n\x03Get\x12\x0b.LogRequest\x1a\x0c.LogResponseb\x06proto3'
)




_LOGREQUEST = _descriptor.Descriptor(
  name='LogRequest',
  full_name='LogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=25,
)


_LOGRESPONSE = _descriptor.Descriptor(
  name='LogResponse',
  full_name='LogResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='history', full_name='LogResponse.history', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=57,
)

DESCRIPTOR.message_types_by_name['LogRequest'] = _LOGREQUEST
DESCRIPTOR.message_types_by_name['LogResponse'] = _LOGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogRequest = _reflection.GeneratedProtocolMessageType('LogRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGREQUEST,
  '__module__' : 'log_pb2'
  # @@protoc_insertion_point(class_scope:LogRequest)
  })
_sym_db.RegisterMessage(LogRequest)

LogResponse = _reflection.GeneratedProtocolMessageType('LogResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGRESPONSE,
  '__module__' : 'log_pb2'
  # @@protoc_insertion_point(class_scope:LogResponse)
  })
_sym_db.RegisterMessage(LogResponse)



_LOGSERVICE = _descriptor.ServiceDescriptor(
  name='LogService',
  full_name='LogService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=59,
  serialized_end=105,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='LogService.Get',
    index=0,
    containing_service=None,
    input_type=_LOGREQUEST,
    output_type=_LOGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOGSERVICE)

DESCRIPTOR.services_by_name['LogService'] = _LOGSERVICE

# @@protoc_insertion_point(module_scope)
