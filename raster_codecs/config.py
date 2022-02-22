from dataclasses import asdict, dataclass
from typing import Any, Dict


@dataclass
class _ConfigMixin:
    def get_config(self):
        config = asdict(self)
        config["id"] = self.__class__.__name__.lower()
        return config

    @classmethod
    def from_config(cls, config: Dict[str, Any]):
        return cls(**config)  # type:ignore
