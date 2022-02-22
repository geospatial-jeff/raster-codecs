import enum
from dataclasses import dataclass
from typing import Optional

import imagecodecs
from numcodecs import register_codec
from numcodecs.abc import Codec

from raster_codecs.config import _ConfigMixin


class Colorspace(enum.Enum):
    rgb = "rgb"
    ycbcr = "ycbcr"


@dataclass
class Jpeg(_ConfigMixin, Codec):
    optimize: Optional[bool] = None
    smoothing: Optional[int] = None
    level: Optional[int] = None
    colorspace: Optional[Colorspace] = None
    lossless: Optional[bool] = None
    bitspersample: Optional[int] = None
    header: Optional[bool] = None

    def encode(self, buf):
        colorspace = self.colorspace.value if self.colorspace else self.colorspace
        return imagecodecs.jpeg_encode(
            buf,
            level=self.level,
            colorspace=colorspace,
            outcolorspace=colorspace,
            optimize=self.optimize,
            smoothing=self.smoothing,
            lossless=self.lossless,
            bitspersample=self.bitspersample,
        )

    def decode(self, buf, out=None):
        colorspace = self.colorspace.value if self.colorspace else self.colorspace
        return imagecodecs.jpeg_decode(
            buf,
            bitspersample=self.bitspersample,
            header=self.header,
            colorspace=colorspace,
            # TODO: Figure out how to support quantization table
            outcolorspace=colorspace,
            out=out,
        )


Jpeg._register()
