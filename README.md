# Reading Vault voices

Public files that the [Reading Vault](https://github.com/B0xfan/reading-vault)
Obsidian plugin downloads for its natural (Kokoro) voices:

- `lexicon/`: English pronunciation lists (American and British), used to
  turn words into the sounds the voice model reads. From
  [misaki](https://github.com/hexgrad/misaki), Apache-2.0.
- `samples/`: short voice samples, so a voice can be heard before
  downloading anything.

The voice model itself is downloaded from Hugging Face
([onnx-community/Kokoro-82M-v1.0-ONNX](https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX)).

Everything here is under the Apache License 2.0 (`LICENSE`), with attribution
in `NOTICE`. The plugin downloads files by commit, and checks each one against
a fingerprint it carries, so a file here never changes under it.
