# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: users.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'users.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0busers.proto\x12\x05users\"!\n\x0eGetUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"0\n\x0fGetUserResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"!\n\x11\x43reateUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"$\n\x12\x43reateUserResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\x8a\x01\n\x0bUserService\x12\x38\n\x07GetUser\x12\x15.users.GetUserRequest\x1a\x16.users.GetUserResponse\x12\x41\n\nCreateUser\x12\x18.users.CreateUserRequest\x1a\x19.users.CreateUserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'users_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETUSERREQUEST']._serialized_start=22
  _globals['_GETUSERREQUEST']._serialized_end=55
  _globals['_GETUSERRESPONSE']._serialized_start=57
  _globals['_GETUSERRESPONSE']._serialized_end=105
  _globals['_CREATEUSERREQUEST']._serialized_start=107
  _globals['_CREATEUSERREQUEST']._serialized_end=140
  _globals['_CREATEUSERRESPONSE']._serialized_start=142
  _globals['_CREATEUSERRESPONSE']._serialized_end=178
  _globals['_USERSERVICE']._serialized_start=181
  _globals['_USERSERVICE']._serialized_end=319
# @@protoc_insertion_point(module_scope)
