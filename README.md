# 🖼 K-Means Image Compression

<p align="center">
Machine Learning based image compression using K-Means clustering
</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-blue">
<img src="https://img.shields.io/badge/Machine%20Learning-KMeans-orange">
<img src="https://img.shields.io/badge/Computer%20Vision-Image%20Processing-green">
<img src="https://img.shields.io/badge/GUI-Tkinter-purple">

</p>

---

# 🚀 Overview

This project demonstrates **image compression using the K-Means clustering algorithm**.

The application provides a **simple graphical user interface (GUI)** that allows users to load an image and reduce the number of colors using machine learning.

The idea is called **Color Quantization**, where millions of pixel colors are grouped into a small number of representative colors.

This project demonstrates how **unsupervised machine learning can be applied to computer vision and image compression problems**.

---

# 🎥 Demo

## Application Demo

<img width="1920" height="1080" alt="Ảnh màn hình 2026-03-17 lúc 17 48 02" src="https://github.com/user-attachments/assets/ce697e04-b2a9-4c83-88bf-0a7d3a33c2d9" />


Example workflow:

```
Load Image
     ↓
Apply K-Means Clustering
     ↓
Reduce Color Palette
     ↓
Display Compressed Image
```

---

# ✨ Features

### 📂 Image Selection

Users can select images from their computer.

Supported formats:

* JPG
* PNG
* BMP
* GIF

---

### 🖥 Side-by-Side Image Comparison

The interface shows:

```
Original Image   |   Compressed Image
```

This allows easy visual comparison of the compression result.

---

### 🧠 Machine Learning Compression

The program applies **K-Means clustering** to group pixel colors.

Example:

```
Input pixels
↓
[120, 90, 200]
[121, 92, 198]
[10, 200, 40]
```

Grouped into clusters:

```
Cluster 1 → purple tones
Cluster 2 → green tones
Cluster 3 → red tones
```

Each pixel is replaced by the nearest **cluster centroid**.

---

### 🎨 Color Quantization

The image color palette is reduced from **millions of colors** to only **3 representative colors**.

Example palette:

```
Cluster 1 → █████
Cluster 2 → █████
Cluster 3 → █████
```

---

# 🧠 Algorithm Explanation

K-Means is an **unsupervised learning algorithm** used for clustering data.

In this project, each **pixel color** is treated as a data point in **3D space**:

```
(R, G, B)
```

---

## Algorithm Workflow

```
Input Image
      │
      ▼
Convert Image → Pixel Array
      │
      ▼
Apply K-Means Clustering
      │
      ▼
Find Dominant Colors
      │
      ▼
Replace Pixel Colors
      │
      ▼
Reconstruct Image
```

---

# 📊 Color Cluster Visualization

Each cluster represents a **dominant color group in the image**.

Example color palette:

| Cluster | Dominant Color |
| ------- | -------------- |
| 1       | 🟥             |
| 2       | 🟩             |
| 3       | 🟦             |

This demonstrates how **K-Means reduces color complexity while preserving visual structure**.

---

# 📉 Compression Analysis

| Property   | Original Image | Compressed Image |
| ---------- | -------------- | ---------------- |
| Colors     | ~16 million    | 3                |
| Image Size | Larger         | Smaller          |
| Detail     | High           | Simplified       |

Applications of this technique include:

* image compression
* image segmentation
* computer vision preprocessing
* dataset simplification

---

# 🖥 Application Interface

The GUI application contains:

### Controls

```
[ Select Image ]
[ Compress Image ]
```

### Display Panels

```
Left Panel  → Original Image
Right Panel → Compressed Image
```

Built with **Tkinter** for simplicity and accessibility.

---

# 🛠 Technologies Used

### Programming Language

Python

---

### Machine Learning

* scikit-learn (K-Means)

---

### Image Processing

* Pillow (PIL)

---

### Numerical Computing

* NumPy

---

### GUI

* Tkinter

---

### Visualization

* Matplotlib

---

# ⚙ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/kmeans-image-compression.git
cd kmeans-image-compression
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install numpy pillow scikit-learn matplotlib
```

---

# ▶ Run Application

```bash
python a.py
```

The GUI window will open.

---

# 📌 Usage

1️⃣ Click **Select Image**

2️⃣ Choose an image from your computer

3️⃣ Click **Compress Image**

4️⃣ The algorithm runs **K-Means clustering**

5️⃣ The compressed image appears on the right side

---

# 📁 Project Structure

```
project
│
├── a.py
│   Main application logic
│
├── requirements.txt
│   Project dependencies
│
├── README.md
│   Documentation
│
├── demo
│   ├── demo.gif
│   ├── original.png
│   └── compressed.png
```

---

# 🎓 Educational Value

This project demonstrates important concepts from:

* Machine Learning
* Computer Vision
* Unsupervised Learning
* Clustering Algorithms
* Image Processing

It is a good **beginner-friendly ML project** to understand how machine learning can process visual data.

---

# 🔮 Future Improvements

Possible improvements include:

* Adjustable **K value**
* Image compression statistics
* Faster clustering for large images
* Interactive color palette visualization
* Support for large image datasets

---

# 👨‍💻 Author

Developed by **Phuc Vo**

If you find this project useful, consider giving it a ⭐ on GitHub.

---

⭐ Machine Learning + Computer Vision demonstration project.
