# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='riakclient.proto',
  package='',
  serialized_pb='\n\x10riakclient.proto\"/\n\x0cRpbErrorResp\x12\x0e\n\x06\x65rrmsg\x18\x01 \x02(\x0c\x12\x0f\n\x07\x65rrcode\x18\x02 \x02(\r\"\'\n\x12RpbGetClientIdResp\x12\x11\n\tclient_id\x18\x01 \x02(\x0c\"&\n\x11RpbSetClientIdReq\x12\x11\n\tclient_id\x18\x01 \x02(\x0c\"<\n\x14RpbGetServerInfoResp\x12\x0c\n\x04node\x18\x01 \x01(\x0c\x12\x16\n\x0eserver_version\x18\x02 \x01(\x0c\"3\n\tRpbGetReq\x12\x0e\n\x06\x62ucket\x18\x01 \x02(\x0c\x12\x0b\n\x03key\x18\x02 \x02(\x0c\x12\t\n\x01r\x18\x03 \x01(\r\":\n\nRpbGetResp\x12\x1c\n\x07\x63ontent\x18\x01 \x03(\x0b\x32\x0b.RpbContent\x12\x0e\n\x06vclock\x18\x02 \x01(\x0c\"\x82\x01\n\tRpbPutReq\x12\x0e\n\x06\x62ucket\x18\x01 \x02(\x0c\x12\x0b\n\x03key\x18\x02 \x02(\x0c\x12\x0e\n\x06vclock\x18\x03 \x01(\x0c\x12\x1c\n\x07\x63ontent\x18\x04 \x02(\x0b\x32\x0b.RpbContent\x12\t\n\x01w\x18\x05 \x01(\r\x12\n\n\x02\x64w\x18\x06 \x01(\r\x12\x13\n\x0breturn_body\x18\x07 \x01(\x08\";\n\nRpbPutResp\x12\x1d\n\x08\x63ontents\x18\x01 \x03(\x0b\x32\x0b.RpbContent\x12\x0e\n\x06vclock\x18\x02 \x01(\x0c\"4\n\tRpbDelReq\x12\x0e\n\x06\x62ucket\x18\x01 \x02(\x0c\x12\x0b\n\x03key\x18\x02 \x02(\x0c\x12\n\n\x02rw\x18\x03 \x01(\r\"%\n\x12RpbListBucketsResp\x12\x0f\n\x07\x62uckets\x18\x01 \x03(\x0c\" \n\x0eRpbListKeysReq\x12\x0e\n\x06\x62ucket\x18\x01 \x02(\x0c\"-\n\x0fRpbListKeysResp\x12\x0c\n\x04keys\x18\x01 \x03(\x0c\x12\x0c\n\x04\x64one\x18\x02 \x01(\x08\"F\n\x0cRpbMapRedReq\x12\x0f\n\x07request\x18\x01 \x02(\x0c\x12\x14\n\x0c\x63ontent_type\x18\x02 \x02(\x0c\x12\x0f\n\x07timeout\x18\x03 \x01(\r\">\n\rRpbMapRedResp\x12\r\n\x05phase\x18\x01 \x01(\r\x12\x10\n\x08response\x18\x02 \x01(\x0c\x12\x0c\n\x04\x64one\x18\x03 \x01(\x08\"\xc9\x01\n\nRpbContent\x12\r\n\x05value\x18\x01 \x02(\x0c\x12\x14\n\x0c\x63ontent_type\x18\x02 \x01(\x0c\x12\x0f\n\x07\x63harset\x18\x03 \x01(\x0c\x12\x18\n\x10\x63ontent_encoding\x18\x04 \x01(\x0c\x12\x0c\n\x04vtag\x18\x05 \x01(\x0c\x12\x17\n\x05links\x18\x06 \x03(\x0b\x32\x08.RpbLink\x12\x10\n\x08last_mod\x18\x07 \x01(\r\x12\x16\n\x0elast_mod_usecs\x18\x08 \x01(\r\x12\x1a\n\x08usermeta\x18\t \x03(\x0b\x32\x08.RpbPair\"%\n\x07RpbPair\x12\x0b\n\x03key\x18\x01 \x02(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"3\n\x07RpbLink\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\x0c\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x0b\n\x03tag\x18\x03 \x01(\x0c')




_RPBERRORRESP = descriptor.Descriptor(
  name='RpbErrorResp',
  full_name='RpbErrorResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='errmsg', full_name='RpbErrorResp.errmsg', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='errcode', full_name='RpbErrorResp.errcode', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=20,
  serialized_end=67,
)


_RPBGETCLIENTIDRESP = descriptor.Descriptor(
  name='RpbGetClientIdResp',
  full_name='RpbGetClientIdResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='client_id', full_name='RpbGetClientIdResp.client_id', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=69,
  serialized_end=108,
)


_RPBSETCLIENTIDREQ = descriptor.Descriptor(
  name='RpbSetClientIdReq',
  full_name='RpbSetClientIdReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='client_id', full_name='RpbSetClientIdReq.client_id', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=110,
  serialized_end=148,
)


_RPBGETSERVERINFORESP = descriptor.Descriptor(
  name='RpbGetServerInfoResp',
  full_name='RpbGetServerInfoResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='node', full_name='RpbGetServerInfoResp.node', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='server_version', full_name='RpbGetServerInfoResp.server_version', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=150,
  serialized_end=210,
)


_RPBGETREQ = descriptor.Descriptor(
  name='RpbGetReq',
  full_name='RpbGetReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='bucket', full_name='RpbGetReq.bucket', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='key', full_name='RpbGetReq.key', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='r', full_name='RpbGetReq.r', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=212,
  serialized_end=263,
)


_RPBGETRESP = descriptor.Descriptor(
  name='RpbGetResp',
  full_name='RpbGetResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='content', full_name='RpbGetResp.content', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vclock', full_name='RpbGetResp.vclock', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=265,
  serialized_end=323,
)


_RPBPUTREQ = descriptor.Descriptor(
  name='RpbPutReq',
  full_name='RpbPutReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='bucket', full_name='RpbPutReq.bucket', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='key', full_name='RpbPutReq.key', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vclock', full_name='RpbPutReq.vclock', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='content', full_name='RpbPutReq.content', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='w', full_name='RpbPutReq.w', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dw', full_name='RpbPutReq.dw', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='return_body', full_name='RpbPutReq.return_body', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=326,
  serialized_end=456,
)


_RPBPUTRESP = descriptor.Descriptor(
  name='RpbPutResp',
  full_name='RpbPutResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='contents', full_name='RpbPutResp.contents', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vclock', full_name='RpbPutResp.vclock', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=458,
  serialized_end=517,
)


_RPBDELREQ = descriptor.Descriptor(
  name='RpbDelReq',
  full_name='RpbDelReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='bucket', full_name='RpbDelReq.bucket', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='key', full_name='RpbDelReq.key', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rw', full_name='RpbDelReq.rw', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=519,
  serialized_end=571,
)


_RPBLISTBUCKETSRESP = descriptor.Descriptor(
  name='RpbListBucketsResp',
  full_name='RpbListBucketsResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='buckets', full_name='RpbListBucketsResp.buckets', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=573,
  serialized_end=610,
)


_RPBLISTKEYSREQ = descriptor.Descriptor(
  name='RpbListKeysReq',
  full_name='RpbListKeysReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='bucket', full_name='RpbListKeysReq.bucket', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=612,
  serialized_end=644,
)


_RPBLISTKEYSRESP = descriptor.Descriptor(
  name='RpbListKeysResp',
  full_name='RpbListKeysResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='keys', full_name='RpbListKeysResp.keys', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='done', full_name='RpbListKeysResp.done', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=646,
  serialized_end=691,
)


_RPBMAPREDREQ = descriptor.Descriptor(
  name='RpbMapRedReq',
  full_name='RpbMapRedReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='request', full_name='RpbMapRedReq.request', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='content_type', full_name='RpbMapRedReq.content_type', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timeout', full_name='RpbMapRedReq.timeout', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=693,
  serialized_end=763,
)


_RPBMAPREDRESP = descriptor.Descriptor(
  name='RpbMapRedResp',
  full_name='RpbMapRedResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='phase', full_name='RpbMapRedResp.phase', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='response', full_name='RpbMapRedResp.response', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='done', full_name='RpbMapRedResp.done', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=765,
  serialized_end=827,
)


_RPBCONTENT = descriptor.Descriptor(
  name='RpbContent',
  full_name='RpbContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='value', full_name='RpbContent.value', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='content_type', full_name='RpbContent.content_type', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='charset', full_name='RpbContent.charset', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='content_encoding', full_name='RpbContent.content_encoding', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vtag', full_name='RpbContent.vtag', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='links', full_name='RpbContent.links', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_mod', full_name='RpbContent.last_mod', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_mod_usecs', full_name='RpbContent.last_mod_usecs', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='usermeta', full_name='RpbContent.usermeta', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=830,
  serialized_end=1031,
)


_RPBPAIR = descriptor.Descriptor(
  name='RpbPair',
  full_name='RpbPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='RpbPair.key', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='RpbPair.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1033,
  serialized_end=1070,
)


_RPBLINK = descriptor.Descriptor(
  name='RpbLink',
  full_name='RpbLink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='bucket', full_name='RpbLink.bucket', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='key', full_name='RpbLink.key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tag', full_name='RpbLink.tag', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1072,
  serialized_end=1123,
)


_RPBGETRESP.fields_by_name['content'].message_type = _RPBCONTENT
_RPBPUTREQ.fields_by_name['content'].message_type = _RPBCONTENT
_RPBPUTRESP.fields_by_name['contents'].message_type = _RPBCONTENT
_RPBCONTENT.fields_by_name['links'].message_type = _RPBLINK
_RPBCONTENT.fields_by_name['usermeta'].message_type = _RPBPAIR

class RpbErrorResp(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBERRORRESP
  
  # @@protoc_insertion_point(class_scope:RpbErrorResp)

class RpbGetClientIdResp(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBGETCLIENTIDRESP
  
  # @@protoc_insertion_point(class_scope:RpbGetClientIdResp)

class RpbSetClientIdReq(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBSETCLIENTIDREQ
  
  # @@protoc_insertion_point(class_scope:RpbSetClientIdReq)

class RpbGetServerInfoResp(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBGETSERVERINFORESP
  
  # @@protoc_insertion_point(class_scope:RpbGetServerInfoResp)

class RpbGetReq(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBGETREQ
  
  # @@protoc_insertion_point(class_scope:RpbGetReq)

class RpbGetResp(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBGETRESP
  
  # @@protoc_insertion_point(class_scope:RpbGetResp)

class RpbPutReq(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBPUTREQ
  
  # @@protoc_insertion_point(class_scope:RpbPutReq)

class RpbPutResp(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBPUTRESP
  
  # @@protoc_insertion_point(class_scope:RpbPutResp)

class RpbDelReq(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBDELREQ
  
  # @@protoc_insertion_point(class_scope:RpbDelReq)

class RpbListBucketsResp(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBLISTBUCKETSRESP
  
  # @@protoc_insertion_point(class_scope:RpbListBucketsResp)

class RpbListKeysReq(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBLISTKEYSREQ
  
  # @@protoc_insertion_point(class_scope:RpbListKeysReq)

class RpbListKeysResp(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBLISTKEYSRESP
  
  # @@protoc_insertion_point(class_scope:RpbListKeysResp)

class RpbMapRedReq(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBMAPREDREQ
  
  # @@protoc_insertion_point(class_scope:RpbMapRedReq)

class RpbMapRedResp(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBMAPREDRESP
  
  # @@protoc_insertion_point(class_scope:RpbMapRedResp)

class RpbContent(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBCONTENT
  
  # @@protoc_insertion_point(class_scope:RpbContent)

class RpbPair(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBPAIR
  
  # @@protoc_insertion_point(class_scope:RpbPair)

class RpbLink(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBLINK
  
  # @@protoc_insertion_point(class_scope:RpbLink)

# @@protoc_insertion_point(module_scope)
