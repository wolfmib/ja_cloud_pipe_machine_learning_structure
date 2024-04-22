import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the trained model
model = load_model('cats_and_dogs_classifier.h5')

# Define the path to the new image
image_path = 'temp_load/test_chat.jpg'

# Load the image
img = image.load_img(image_path, target_size=(150, 150))

# Preprocess the image
img_tensor = image.img_to_array(img)  # Convert the image to a numpy array
img_tensor = np.expand_dims(img_tensor, axis=0)  # Add batch dimension
img_tensor /= 255.  # Model expects input in the range [0, 1]

# Predict the class of the image
prediction = model.predict(img_tensor)

# Interpret the output
# Assuming the output of the model is binary:
# '0' is for 'Cat' and '1' is for 'Dog'
print(f"prediciotn is {prediction}")
if prediction < 0.5:
    print(f"The image with path {image_path} is a Cat.")
else:
    print(f"The image with path {image_path} is a Dog.")
