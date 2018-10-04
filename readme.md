# colourvision-ml
ML Framework for [ColourVision](https://github.com/samantharachelb/colourvision)

### Training the model
- Run the preflight module `python preflight.py` to gather everything needed
to create and train the model.
- Run the training module `python train.py` to train a model
based on the Inception-V3 Model.

### Flags
The following flags apply just to `train.py`
- `tpu` The Cloud TPU that should be used for training. This should either be
the name used when creating the Cloud TPU, or a `grpc://ip.address.of.tpu:8470` url.
