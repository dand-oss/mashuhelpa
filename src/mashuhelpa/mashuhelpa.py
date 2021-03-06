"""
mashuhelpa allows use of Mashumaro without inheriting from base classes
"""
from typing import Union, Optional, Callable, Dict, Mapping, TypeVar, Type
from types import MappingProxyType
from functools import partial
import json
import yaml
import msgpack
import dataclasses

from mashumaro.serializer.base.metaprogramming import CodeBuilder


json_DEFAULT_DICT_PARAMS = {
    "use_bytes": False,
    "use_enum": False,
    "use_datetime": False,
}
json_EncodedData = Union[str, bytes, bytearray]
json_Encoder = Callable[[Dict], json_EncodedData]
json_Decoder = Callable[[json_EncodedData], Dict]
json_T = TypeVar("T", bound="DataClassJSONMixin")

yaml_DEFAULT_DICT_PARAMS = {
    "use_bytes": False,
    "use_enum": False,
    "use_datetime": False,
}
yaml_EncodedData = Union[str, bytes]
yaml_Encoder = Callable[[Dict], yaml_EncodedData]
yaml_Decoder = Callable[[yaml_EncodedData], Dict]
yaml_T = TypeVar("T", bound="DataClassYAMLMixin")

msgpack_DEFAULT_DICT_PARAMS = {
    "use_bytes": True,
    "use_enum": False,
    "use_datetime": False,
}
msgpack_EncodedData = Union[str, bytes, bytearray]
msgpack_Encoder = Callable[[Dict], msgpack_EncodedData]
msgpack_Decoder = Callable[[msgpack_EncodedData], Dict]
msgpack_T = TypeVar("T", bound="DataClassMessagePackMixin")


def build_mashumaro(cls: TypeVar) -> bool:

    try:
        # don't build it twice...
        # support inherit class
        return getattr(cls, f"__is_mashu_built_{cls.__name__}__")

    except AttributeError:

        builder = CodeBuilder(cls)
        builder.add_from_dict()
        builder.add_to_dict()

        # done
        setattr(cls, f"__is_mashu_built_{cls.__name__}__", True)

    return True


def to_dict(
    inst: object,
    use_bytes: bool = False,
    use_enum: bool = False,
    use_datetime: bool = False,
) -> dict:
    pass


def from_dict(
    cls,
    d: Mapping,
    use_bytes: bool = False,
    use_enum: bool = False,
    use_datetime: bool = False,
) -> dataclasses.dataclass:
    pass


def to_json(
    inst: json_T,
    encoder: Optional[json_Encoder] = json.dumps,
    dict_params: Optional[Mapping] = MappingProxyType({}),
    **encoder_kwargs,
) -> json_EncodedData:

    return encoder(
        inst.to_dict(**dict(json_DEFAULT_DICT_PARAMS, **dict_params)), **encoder_kwargs
    )


def from_json(
    cls: Type[json_T],
    data: json_EncodedData,
    decoder: Optional[json_Decoder] = json.loads,
    dict_params: Optional[Mapping] = MappingProxyType({}),
    **decoder_kwargs,
) -> json_T:

    return cls.from_dict(
        decoder(data, **decoder_kwargs), **dict(json_DEFAULT_DICT_PARAMS, **dict_params)
    )


def to_yaml(
    inst: yaml_T,
    encoder: Optional[yaml_Encoder] = yaml.dump,
    dict_params: Optional[Mapping] = MappingProxyType({}),
    **encoder_kwargs,
) -> yaml_EncodedData:

    return encoder(
        inst.to_dict(**dict(yaml_DEFAULT_DICT_PARAMS, **dict_params)), **encoder_kwargs
    )


def from_yaml(
    cls: Type[yaml_T],
    data: yaml_EncodedData,
    decoder: Optional[yaml_Decoder] = yaml.safe_load,
    dict_params: Optional[Mapping] = MappingProxyType({}),
    **decoder_kwargs,
) -> yaml_T:

    return cls.from_dict(
        decoder(data, **decoder_kwargs), **dict(yaml_DEFAULT_DICT_PARAMS, **dict_params)
    )


def to_msgpack(
    inst: msgpack_T,
    encoder: Optional[msgpack_Encoder] = partial(msgpack.packb, use_bin_type=True),
    dict_params: Optional[Mapping] = MappingProxyType({}),
    **encoder_kwargs,
) -> msgpack_EncodedData:

    return encoder(
        inst.to_dict(**dict(msgpack_DEFAULT_DICT_PARAMS, **dict_params)),
        **encoder_kwargs,
    )


def from_msgpack(
    cls: Type[msgpack_T],
    data: msgpack_EncodedData,
    decoder: Optional[msgpack_Decoder] = partial(msgpack.unpackb, raw=False),
    dict_params: Optional[Mapping] = MappingProxyType({}),
    **decoder_kwargs,
) -> msgpack_T:

    return cls.from_dict(
        decoder(data, **decoder_kwargs),
        **dict(msgpack_DEFAULT_DICT_PARAMS, **dict_params),
    )
