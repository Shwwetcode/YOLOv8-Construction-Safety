# Real-Time Construction Site Safety Monitoring with YOLOv8

![Project Demo GIF](demo.gif)![construction-safety](https://github.com/user-attachments/assets/d3e22618-e6fd-4b15-b4c3-6be2f30c0748)


## 📖 Overview

This project is an end-to-end computer vision system designed to enhance worker safety by automatically monitoring Personal Protective Equipment (PPE) compliance on construction sites. Using the YOLOv8 object detection model, this system can identify **hardhats**, **safety vests**, and **masks** in real-time from both images and video streams.

This repository contains the complete workflow, from data preparation and model training to inference on new media.

---

## ✨ Features

- **High-Performance Detection:** Built on the state-of-the-art YOLOv8 architecture.
- **Custom-Trained Model:** Fine-tuned on a specific construction site safety dataset for high accuracy.
- **Multi-Object Tracking:** Capable of detecting 10 distinct classes, including compliant and non-compliant PPE.
- **Versatile Inference:** Can perform detection on both static images and high-framerate video files.
- **Reproducible Environment:** Includes a complete guide for setting up the environment and replicating the training process.

---

## 🛠️ Technology Stack

- **Model:** YOLOv8n
- **Framework:** PyTorch, Ultralytics
- **Key Libraries:** Roboflow, OpenCV, NumPy
- **Language:** Python 3.11+

---

## ⚙️ Setup and Installation

To get this project running locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Shwwetcode/YOLOv8-Construction-Safety.git](https://github.com/Shwwetcode/YOLOv8-Construction-Safety.git)
    cd YOLOv8-Construction-Safety
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Usage

### Training
To re-train the model on the dataset, run the training script. Ensure your dataset is structured correctly and the `ppe_data.yaml` file points to the correct paths.
```bash
python train.py
```

### Prediction (Inference)
To perform detection on a new image or video, update the `model_path` and `source_image` variables in the `predict.py` script, then run:
```bash
python predict.py
```
The output media with bounding boxes will be saved in the `runs/detect/` directory.
