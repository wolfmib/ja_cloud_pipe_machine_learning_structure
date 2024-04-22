## 2024-04-22, use multi my_app2.py 




import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Load the trained model
model = load_model('cats_and_dogs_classifier.h5')


# Define the directory path that contains the images
image_dir = 'temp_load/'


# List all the jpg files in the directory
image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]


# Results dictionary to store each file's prediction
results = {}



for image_file in image_files:
    # Load the image
    img_path = os.path.join(image_dir, image_file)
    img = image.load_img(img_path, target_size=(150, 150))

    # Preprocess the image
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)  # Add batch dimension
    img_tensor /= 255.  # Normalize the image to the [0, 1] range

    #import matplotlib.pyplot as plt

    # Inside the loop just before prediction
    #plt.imshow(img_tensor[0])
    #plt.title(f"Preprocessed Image - {image_file}")
    #plt.show()


    # Predict the class of the image
    prediction = model.predict(img_tensor)

    # Determine the class (assuming binary classification: 0=cat, 1=dog)
    print(f"{image_file} >> {prediction}")
    
    class_label = 'Dog' if prediction[0,0] > 0.5 else 'Cat'

    # Store the result
    results[image_file] = class_label


# Interpret the output
# Assuming the output of the model is binary:
# '0' is for 'Cat' and '1' is for 'Dog'


import time

# Function to write prediction results to a file with a timestamp prefix
def write_prediction_result(msg):
    # Get current timestamp
    current_time = time.strftime("%Y%m%d_%H%M%S")
    
    output_message = f"{current_time}_output.txt"
    output_message += f"\nPrediction: {msg}\n"
    
    # Write the output message to a file in the temp_load folder
    with open(f"temp_load/{current_time}_output.txt", "w") as file:
        file.write(output_message)


# printout with results
all_msg = ""
for photo_file in results:

    get_msg = f"The image with name {photo_file} is a {results[photo_file]}.\n"
    print(f"{get_msg}\n")
    all_msg += get_msg


## wirte all mgs
write_prediction_result(all_msg)
