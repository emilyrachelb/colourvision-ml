# colourvision-ml
ML Framework for [ColourVision](https://github.com/samantharachelb/colourvision)

### Training the model
- Run the preflight module `python preflight.py` to gather everything needed
to create and train the model.
- Run the training module `python train.py` to train a model
based on the Inception-V3 Model.

### Flags
Flags for `train.py`
###### Cloud TPU Flags
- `tpu` — The Cloud TPU that should be used for training. This should either be
the name used when creating the Cloud TPU, or a `grpc://ip.address.of.tpu:8470` url.
Default value is 'None'

- `gcp_project` — The project name for the Cloud TPU-enabled project. If not specified,
an attempt will be made to automatically detect the GCE project from the metadata.

- `tpu_zone` — The GCE zone where the Cloud TPU is located. If not specified, an
attempt will be made to automatically detect the GCE project from the metadata.

###### Model Specific Flags
- `data_dir` — The where the input data is stored. Defaults to the current directory.

- `model_dir`,
