import PIL
from PIL import Image
import requests
from io import BytesIO
from matplotlib.pyplot import imshow
import numpy as np
import coremltools

img_url = 'https://upload.wikimedia.org/wikipedia/commons/9/93/Golden_Retriever_Carlos_%2810581910556%29.jpg'
response = requests.get(img_url)

img = PIL.Image.open(BytesIO(response.content))
imshow(np.asarray(img))

img = img.resize([299,299], PIL.Image.ANTIALIAS)
coreml_model = coremltools.models.MLModel('../colourvision/ColourModel.mlmodel')

img = img.resize([299,299], PIL.Image.ANTIALIAS)
coreml_inputs = {'Mul__0': img}
coreml_output = coreml_model.predict(coreml_inputs, useCPUOnly=False)
probs = coreml_output['final_result__0'].flatten()
label_idx = np.argmax(probs)

# This label file comes with the model
label_file = 'retrained_labels.txt'
with open(label_file) as f:
    labels = f.readlines()
print('Label = {}'.format(labels[label_idx]))