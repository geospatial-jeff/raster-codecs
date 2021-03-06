import numpy as np
import numpy.testing
import zarr

from raster_codecs import Jpeg


def test_zarr_compatibility():
    data = np.arange(10000, dtype="uint8").reshape(100, 100)
    compressor = Jpeg(lossless=True)
    z = zarr.array(data, chunks=(1000, 1000), compressor=compressor)
    numpy.testing.assert_array_equal(z[:256, :256], data[:256, :256])


def test_config_roundtrip():
    compressor = Jpeg(lossless=True)
    config = compressor.get_config()
    assert Jpeg.from_config(config) == compressor
