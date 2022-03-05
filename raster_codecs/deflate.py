from dataclasses import dataclass

import imagecodecs
from numcodecs.abc import Codec

from raster_codecs.config import _ConfigMixin


@dataclass
class Deflate(_ConfigMixin, Codec):
    # Match the default imagecodecs default
    # https://github.com/cgohlke/imagecodecs/blob/master/imagecodecs/_imagecodecs.py#L655
    level: int = 6

    def encode(self, buf):
        return imagecodecs.zlib_encode(buf, level=self.level)

    def decode(self, buf, out=None):
        return imagecodecs.zlib_decode(buf, out=out)


Deflate._register()
