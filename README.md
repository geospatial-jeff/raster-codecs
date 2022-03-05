# numcodecs-raster
Provides a lightweight wrapper over [imagecodecs](https://github.com/cgohlke/imagecodecs) implementing the
[numcodecs](https://github.com/zarr-developers/numcodecs) interface.  This lets us use the compressions provided by `imagecodecs` in zarr arrays.

The `numcodecs` interface is built around python's buffer protocol.  Numpy implements this buffer protocol, and 
`imagecodecs` is built around numpy.  So this all works out pretty well.

## Supported compressions
- JPEG
- Deflate
