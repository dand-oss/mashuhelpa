"""Allow use of Mashumaro without inheriting from base classes."""
import json
from functools import partial
from types import MappingProxyType
from typing import Any
from typing import Callable
from typing import Dict
from typing import Mapping
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import Union

import msgpack
import yaml
from mashumaro import DataClassJSONMixin
from mashumaro import DataClassMessagePackMixin
from mashumaro import DataClassYAMLMixin
from mashumaro.serializer.base.metaprogramming import CodeBuilder


json_DEFAULT_DICT_PARAMS = {
    "use_bytes": False,
    "use_enum": False,
    "use_datetime": False,
}
json_encoded_str = Union[str, bytes, bytearray]
json_encoder = Callable[[Dict], json_encoded_str]
json_decoder = Callable[[json_encoded_str], Dict]

yaml_DEFAULT_DICT_PARAMS = {
    "use_bytes": False,
    "use_enum": False,
    "use_datetime": False,
}
yaml_encoded_str = Union[str, bytes]
yaml_encoder = Callable[[Dict], yaml_encoded_str]
yaml_decoder = Callable[[yaml_encoded_str], Dict]

msgpack_DEFAULT_DICT_PARAMS = {
    "use_bytes": True,
    "use_enum": False,
    "use_datetime": False,
}
msgpack_encoded_str = Union[str, bytes, bytearray]
msgpack_encoder = Callable[[Dict], msgpack_encoded_str]
msgpack_decoder = Callable[[msgpack_encoded_str], Dict]


def build_mashumaro(cls: TypeVar) -> bool:
    """Add mashumaro CodeBuilder to class."""
    ret_code = True
    try:
        # don't build it twice...
        # support inherit class
        ret_code = getattr(cls, f"__is_mashu_built_{cls.__name__}__")

    except AttributeError:
        builder = CodeBuilder(cls)
        builder.add_from_dict()
        builder.add_to_dict()

        # done
        setattr(cls, f"__is_mashu_built_{cls.__name__}__", True)
    return ret_code


def to_json(
    inst: DataClassJSONMixin,
    encoder: json_encoder = json.dumps,
    dict_params: Optional[Mapping] = MappingProxyType({}),
    **encoder_kwargs: Any,
) -> json_encoded_str:
    """Convert to JSON."""
    return encoder(
        inst.to_dict(**dict(json_DEFAULT_DICT_PARAMS, **dict_params)),
        **encoder_kwargs,
    )


def from_json(
    cls: Type[DataClassJSONMixin],
    en_str: json_encoded_str,
    decoder: json_decoder = json.loads,
    dict_params: Optional[Mapping] = MappingProxyType({}),
    **decoder_kwargs: str,
) -> DataClassJSONMixin:
    """Convert from JSON."""
    return cls.from_dict(
        decoder(en_str, **decoder_kwargs),
        **dict(json_DEFAULT_DICT_PARAMS, **dict_params),
    )


def to_yaml(
    inst: DataClassYAMLMixin,
    encoder: yaml_encoder = yaml.dump,
    dict_params: Optional[Mapping] = MappingProxyType({}),
    **encoder_kwargs: str,
) -> yaml_encoded_str:
    """Convert to YAML."""
    return encoder(
        inst.to_dict(**dict(yaml_DEFAULT_DICT_PARAMS, **dict_params)),
        **encoder_kwargs,
    )


def from_yaml(
    cls: Type[DataClassYAMLMixin],
    en_str: yaml_encoded_str,
    decoder: yaml_decoder = yaml.safe_load,
    dict_params: Optional[Mapping] = MappingProxyType({}),
    **decoder_kwargs: str,
) -> DataClassYAMLMixin:
    """Convert from YAML."""
    return cls.from_dict(
        decoder(en_str, **decoder_kwargs),
        **dict(yaml_DEFAULT_DICT_PARAMS, **dict_params),
    )


def to_msgpack(
    inst: DataClassMessagePackMixin,
    encoder: msgpack_encoder = partial(msgpack.packb, use_bin_type=True),
    dict_params: Optional[Mapping] = MappingProxyType({}),
    **encoder_kwargs: str,
) -> msgpack_encoded_str:
    """Convert to msgpack."""
    return encoder(
        inst.to_dict(**dict(msgpack_DEFAULT_DICT_PARAMS, **dict_params)),
        **encoder_kwargs,
    )


def from_msgpack(
    cls: Type[DataClassMessagePackMixin],
    en_str: msgpack_encoded_str,
    decoder: msgpack_decoder = partial(msgpack.unpackb, raw=False),
    dict_params: Optional[Mapping] = MappingProxyType({}),
    **decoder_kwargs: str,
) -> DataClassMessagePackMixin:
    """Convert from msgpack."""
    return cls.from_dict(
        decoder(en_str, **decoder_kwargs),
        **dict(msgpack_DEFAULT_DICT_PARAMS, **dict_params),
    )
