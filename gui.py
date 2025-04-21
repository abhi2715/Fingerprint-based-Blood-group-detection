import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import os

# Flask endpoint URL
FLASK_URL = "http://127.0.0.1:5000/predict"

def predict_blood_group():
    if not selected_file.get():
        messagebox.showerror("Error", "Please select an image file first.")
        return
    
    file_path = selected_file.get()
    
    try:
        with open(file_path, 'rb') as file:
            files = {'file': (os.path.basename(file_path), file, 'image/jpeg')}
            print(f"Sending request to Flask with: {file_path}")
            response = requests.post(FLASK_URL, files=files)
        
        print(f"Response received: {response.status_code}")
        
        if response.status_code == 200:
            result_json = response.json()
            print(f"Response JSON: {result_json}")
            
            predicted_label = result_json.get('predicted_label', 'Unknown')
            confidence = result_json.get('confidence', 'Unknown')

            result_text.set(f"Predicted Blood Group: {predicted_label}\nConfidence: {confidence:.2f}")

            print(f"Predicted Blood Group: {predicted_label}")
            print(f"Confidence: {confidence:.2f}")
            print("-----------------")
        else:
            messagebox.showerror("Error", f"Prediction failed: {response.text}")
    
    except Exception as e:
        messagebox.showerror("Error", f"Prediction failed: {str(e)}")

def browse_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if file_path:
        selected_file.set(file_path)

root = tk.Tk()
root.title("Blood Group Prediction from Fingerprint")

selected_file = tk.StringVar()
result_text = tk.StringVar()  

tk.Label(root, text="Select Fingerprint Image").pack(pady=10) 
tk.Entry(root, textvariable=selected_file, width=50).pack()
tk.Button(root, text="Browse", command=browse_file).pack(pady=5)

tk.Button(root, text="Predict", command=predict_blood_group, bg="green", fg="white").pack(pady=10)

root.mainloop()
