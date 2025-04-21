from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Initialize Flask app
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 

MODEL_PATH = '/Users/abhishek_ks/Desktop/Python project/model/model.h5'
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(file_path):
    """
    Preprocesses the image for model prediction.
    Args:
        file_path (str): Path to the image file.
    Returns:
        numpy.ndarray: Preprocessed image ready for prediction.
    """
    try:
        img = load_img(file_path, target_size=(64, 64))  
        img_array = img_to_array(img) 
        img_array = np.expand_dims(img_array, axis=0)  
        return img_array
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        return None

@app.route('/')
def home():
    return "Blood Group Prediction Service is Running!"

# Corrected class labels mapping
class_labels = {
    0: "A+", 1: "A-", 2: "AB+", 3: "AB-", 
    4: "B+", 5: "B-", 6: "O+", 7: "O-"
}

@app.route('/predict', methods=['POST'])
def predict():
    print("Request received at /predict")

    if 'file' not in request.files:
        print("No file part in request.")
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        print("No file selected.")
        return jsonify({'error': 'No file selected'}), 400

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    print(f"File saved at: {file_path}")

    try:
        img = preprocess_image(file_path)
        if img is None:
            print("Failed to preprocess image.")
            return jsonify({'error': 'Failed to preprocess image'}), 500
        
        print(f"Image shape after preprocessing: {img.shape}")
        
        predictions = model.predict(img)
        predicted_class = int(np.argmax(predictions[0]))

        if predicted_class in class_labels:
            predicted_label = class_labels[predicted_class]
        else:
            print(f"Invalid class index: {predicted_class}")
            return jsonify({'error': 'Invalid class index predicted'}), 500

        confidence = float(np.max(predictions[0]))

        print(f"Predicted Label: {predicted_label}, Confidence: {confidence}")

        return jsonify({
            'predicted_class': predicted_class,
            'predicted_label': predicted_label,
            'confidence': confidence
        })
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted file: {file_path}")

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    print("Starting Flask app...")
    app.run(debug=True)
