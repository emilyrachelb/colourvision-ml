import PIL
from PIL import Image
import requests
from io import BytesIO
from matplotlib.pyplot import imshow
import numpy as np
import coremltools

class Tests:
    DIRECTORY = [
        './imageset/blue',
        './imageset/brown',
        './imageset/green',
        './imageset/grey',
        './imageset/orange',
        './imageset/purple',
        './imageset/red',
        './imageset/yellow'
    ]

    def __init__(self):
        for x in range(0, len(self.DIRECTORY)):
            working_directory = self.DIRECTORY[x]
            files = os.listdir(working_directory)

            for file in files:
                img = PIL.Image.open(working_directory + "/" + file)
                imshow(np.asarray(img))

                img = img.resize([299, 299], PIL.Image.ANTIALIAS)
                coreml_model = coremltools.models.MLModel('./colourvision.mlmodel')

                coreml_inputs = {'Mul__0': img}
                coreml_output = coreml_model.predict(coreml_inputs, useCPUOnly=False)
                probs = coreml_output['final_result__0'].flatten()
                label_idx = np.argmax(probs)

                # This label file comes with the model
                label_file = 'colourvision_labels.txt'
                with open(label_file) as f:
                    labels = f.readlines()
                print('File: {}  Label = {}'.format(working_directory + "/" + file, labels[label_idx]))