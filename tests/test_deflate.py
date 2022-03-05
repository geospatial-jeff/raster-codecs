import numpy as np
import numpy.testing
import zarr

from raster_codecs import Deflate


def test_zarr_compatibility():
    data = np.arange(10000, dtype="uint8").reshape(100, 100)
    compressor = Deflate(level=6)
    z = zarr.array(data, chunks=(1000, 1000), compressor=compressor)
    numpy.testing.assert_array_equal(z[:256, :256], data[:256, :256])


def test_config_roundtrip():
    compressor = Deflate(level=0)
    config = compressor.get_config()
    assert Deflate.from_config(config) == compressor
