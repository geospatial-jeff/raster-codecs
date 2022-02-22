# numcodecs-raster
Provides a lightweight wrapper over [imagecodecs](https://github.com/cgohlke/imagecodecs) implementing the
[numcodecs](https://github.com/zarr-developers/numcodecs) interface.  This has several benefits:
- Allows the use of compressions provided by `imagecodecs` in zarr arrays.
- `imagecodecs` and `numcodecs` support very different compressions.  The former implements compressions specific
   to raster data (ex. jpeg, lzw, deflate) while the latter implements compressions that are more general to binary
   data (ex. blosc, zstd, lz4, msgpack).  Aligning the two under the same interface lets us utilize both with the same
   code!

This allows us to use the compressions provided
by `imagecodecs` in zarr arrays.

The `numcodecs` interface is built around python's buffer protocol.  Numpy implements this buffer protocol, and 
`imagecodecs` is built around numpy.  So this all works out pretty well.

## Supported compressions
- JPEG