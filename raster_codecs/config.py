from dataclasses import asdict, dataclass
from typing import Any, Dict

from numcodecs import register_codec


@dataclass
class _ConfigMixin:
    def get_config(self):
        config = asdict(self)
        config["id"] = self.__class__.__name__.lower()
        return config

    @classmethod
    def from_config(cls, config: Dict[str, Any]):
        if "id" in config:
            config = config.copy()
            del config["id"]
        return cls(**config)  # type:ignore

    @classmethod
    def _register(cls):
        register_codec(cls, codec_id=cls.__name__.lower())
