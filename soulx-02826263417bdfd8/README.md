# SoulX serverless: corresponding-source materials

Image: `sha256:02826263417bdfd8fb4492a1c422c08975082d17786def813b56dabd00dbcb24`

Docker Hub tag intended for distribution:
`gggggrandddd/soulx-serverless:build-20261023T002041Z`

This repository is a source-and-notice companion for that specific binary image.
It is not the model image, a model checkpoint archive, or an NVIDIA binary mirror.
Each component remains under its own license. No repository-wide license replaces
component licenses. Original copyright, license and Debian packaging notices
are retained within the unmodified source archives.

## Sources and provenance

`source-manifest.json` records exact source versions, covered binary components,
official download URLs, archive sizes and SHA256 hashes. Ubuntu source sets include
the `.dsc`, upstream source tarball(s) and Debian/Ubuntu patch/packaging archives.
PyPI source distributions are pinned to the exact installed version and checked
against official release metadata. Sources are downloaded as data; no source or
package installation script is executed by the collector.

The large source archives are intended as GitHub Release assets, not Git blobs.
The final Docker Hub description must link directly to the source release, with
clear directions to `source-manifest.json` and the source archives. The archive
release must remain available for as long as the linked binary is offered.
Do not publish a link to a release that does not exist yet.

The manifest starts as a conservative list of copyleft source candidates from
the saved image SBOM. A downloaded/verified archive is not automatically a legal
clearance: mixed/alternative license metadata and bundled native dependencies
must be checked before claiming a complete corresponding-source distribution.
The collector does not manufacture `redistribution-clearance.json`.

## Build and changes

Ubuntu components are upstream distribution binaries; this project has not
modified their source. The source sets retain distro build scripts and patches.
For Ubuntu source packages, unpack using the matching `.dsc` and `dpkg-source -x`;
consult `debian/rules`, `debian/control` and `debian/copyright` in that source set.
For Python components, consult the retained source distribution's build metadata.
These directions do not guarantee a byte-for-byte reproduction of the image.

The application uses unmodified upstream SoulX source revision
`9bc03de06bb0de82cd6bc477804512ae06144bf2`.
SoulX Pro (DiT + WAN VAE) component licensing is identified in the pinned model
card. No Lite/LTX model archive is included in this companion.

The image locally corrects Decord wheel metadata, as described in its existing
third-party notice. Source/license obligations for any native libraries bundled
inside third-party wheels need their own provenance check; a Python package's
license field is not sufficient evidence for all its bundled binaries.

## NVIDIA components

NVIDIA CUDA/cuDNN binary packages and model weights are deliberately excluded
from this source repository. CUDA/cuDNN retain their own licenses in the image.
The CUDA 12.8 redistribution terms and component list are at:
https://docs.nvidia.com/cuda/archive/12.8.0/eula/index.html
A `Proprietary` classifier alone does not establish a distribution prohibition.
This companion does not grant rights beyond the upstream licenses.

## Scope

The inventory is based on the existing saved SoulX SBOM and license report.
It is not a review of EchoMimic's final image. No Docker builds, GPU jobs or image
publication are performed by the source collector.
