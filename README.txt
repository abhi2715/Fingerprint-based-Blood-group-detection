Project Title:
Blood Group Detection Based on Fingerprints Using CNN

Description:
This project uses Convolutional Neural Networks (CNNs) to classify blood groups based on fingerprint images. The system is trained on a labeled dataset of fingerprint images categorized into 8 blood groups and is deployed using a simple Python-based GUI.
Directory Structure:

.
├── app.py                                                  # Flask web application
├── gui.py                                                  # Tkinter GUI app
├── dataset/
│      └── dataset_blood_group/
│              ├── 0_A+/
│              ├── 1_A-/
│              ├── 2_AB+/
│              ├── 3_AB-/
│              ├── 4_B+/
│              ├── 5_B-/
│              ├── 6_O+/
│              └── 7_O-/
├── model/
│      └── model.h5                                      # Trained CNN model
├── notebook/
│      └── bloodgroupdetectionsectionH.ipynb
├── uploads/                                              # Stores uploaded fingerprint images
├── venv/                                                    # Python virtual environment
└── README/
        ├── Team_Number_1_IML_Project.pdf    # Final project report
        ├── blood_group_detection.pptx           # Project presentation
        └── README.txt                           # This file

Setup Instructions:
    1 Create virtual environment & install dependencies:
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate          # Windows

pip install tensorflow keras flask opencv-python pillow numpy seaborn matplotlib bumpy reqeusts pandas sklearn os shutil collection 

Train the Model:
jupyter notebook notebook/bloodgroupdetectionsectionH.ipynb

Run GUI App:
python gui.py

Run Web App:
python app.py

Dataset Overview:
    • 8 blood group categories:
        ◦ A+, A−, B+, B−, AB+, AB−, O+, O−
    • Each subfolder contains fingerprint images named and grouped accordingly.
    • Download the dataset from kaggle repository - https://www.kaggle.com/datasets/rajumavinmar/finger-print-based-blood-group-dataset

Model Folder (model/):
This folder contains the pre-trained Convolutional Neural Network (CNN) model used for predicting blood groups from fingerprint images.
    • model.h5

Uploads Folder (uploads/):
This folder is used to temporarily store fingerprint images that are needs to be uploaded via the web interface (app.py) and GUI app (GUI.py)



