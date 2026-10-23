# Decord binary caveat: source publication is not image clearance

The official Decord 0.6.0 manylinux wheel retained during project preparation
contains FFmpeg libraries with both `--enable-nonfree` and the embedded string
`nonfree and unredistributable`. The local wheel metadata correction does not
change those native bytes. This review did not extract the local Docker image;
it inspected the wheel used by the Docker dependency configuration.

Upstream evidence:
- https://github.com/dmlc/decord/blob/v0.6.0/tools/build_manylinux2010.sh
- https://github.com/FFmpeg/FFmpeg/blob/n4.1.6/configure
- https://ffmpeg.org/legal.html

Decord's Apache-2.0 license metadata does not replace its bundled libraries'
terms. The source archives in this companion do not resolve this binary issue
and must not be presented as clearance to redistribute the original image.

A targeted repair can rebuild Decord 0.6.0 against the distribution FFmpeg
libraries already present, preserving Python/CUDA/PyTorch/model versions.
The original bundled native libraries must be absent from every published layer;
removing them only in an added Docker layer is insufficient. A fresh final stage
or verified flattened repack is required. Such a changed image receives a new
ID and requires its own security result. No Docker operation was run by this
review, and no original image is approved or published.
