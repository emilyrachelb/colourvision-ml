import PIL
from PIL import Image
import requests
from io import BytesIO
from matplotlib.pyplot import imshow
import numpy as np
import coremltools

green_img = 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/2016-08-28_Green_apples.jpg/1600px-2016-08-28_Green_apples.jpg'
yellow_img = 'https://stmed.net/wallpaper-28398'
red_img =


response = requests.get(img_url)

img = PIL.Image.open(BytesIO(response.content))
imshow(np.asarray(img))

img = img.resize([299,299], PIL.Image.ANTIALIAS)
coreml_model = coremltools.models.MLModel('./colourvision.mlmodel')

img = img.resize([299,299], PIL.Image.ANTIALIAS)
coreml_inputs = {'Mul__0': img}
coreml_output = coreml_model.predict(coreml_inputs, useCPUOnly=False)
probs = coreml_output['final_result__0'].flatten()
label_idx = np.argmax(probs)

# This label file comes with the model
label_file = 'colourvision_labels.txt'
with open(label_file) as f:
    labels = f.readlines()
print('Label = {}'.format(labels[label_idx]))