# Dependencies
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg19 import preprocess_input
import re
import base64
from PIL import Image
from io import BytesIO

#function to convert image to from base64 to Python Imaging Library(PIL) image 
def base64_to_pil(img_base64): 
    image_data = re.sub('^data:image/.+;base64,', '', img_base64)
    pil_image = Image.open(BytesIO(base64.b64decode(image_data)))
    return pil_image

# load model
model = load_model('saved_models/keras_cifar10_trained_model.h5')

# define global variables
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat',
               'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

# define predict function with variables that changes for new input

def predict_new(image_new):
    # Preprocess image for scaling and normalization for h5 model
    img = image_new.resize((32, 32))
    x = image.img_to_array(img)
    x = preprocess_input(x)
    img = np.reshape(img, [1, 32, 32, 3])
    # return array value with the highest probability
    classes = np.argmax(model.predict(img), axis=1)
    names = [class_names[i] for i in classes]
    return names
