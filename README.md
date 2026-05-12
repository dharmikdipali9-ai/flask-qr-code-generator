# 🔳 Flask QR Code Generator

A powerful and secure **QR Code Generator Web App** built using **Flask** 🐍.  
This application allows users to generate QR codes from text or URLs and optionally **encrypt the data 🔒** for secure sharing.

---

## 🚀 Live Demo

https://flask-qr-code-generator-lao0.onrender.com


---



## ✨ Features

- 🔗 Generate QR codes from text or URLs  
- 🔒 Encrypt data using **Fernet (cryptography)**  
- 📥 Download QR codes as images  
- 🖼️ Image processing using Pillow (PIL)  
- ⚡ Fast and lightweight Flask backend  
- 🌐 Simple and user-friendly web interface  

---

## 🛠️ Tech Stack

- 🐍 Python  
- 🌐 Flask  
- 🔐 Cryptography (Fernet)  
- 🔳 qrcode  
- 🖼️ Pillow (PIL)  
- 🔗 urllib  
- 🧠 base64  

---

## 📂 Project Structure

flask-qr-code-generator/
│── app.py
│── templates/
│── static/
│── requirements.txt
│── README.md

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/dharmikdipali9-ai/flask-qr-code-generator.git

```

Navigate to project folder:

```bash
cd flask-qr-code-generator
```

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate 
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Flask app:

```bash
python app.py
```

Open your browser:

```bash
http://127.0.0.1:5000
```

## 🔐 Encryption Details

This app uses Fernet symmetric encryption from the cryptography library to secure sensitive data before generating QR codes.

## 📸 Screenshots

## 🔳 QR Code Generator-app

<img width="1361" height="683" alt="qr-code-app" src="https://github.com/user-attachments/assets/250385f7-92cd-4b53-8404-cae55cf45dd0" />


## 🔓 Decode Secret QR

<img width="1365" height="681" alt="decode-page" src="https://github.com/user-attachments/assets/cd7fcb1e-0fa0-4646-b0d4-efb3dfb347a4" />


## 💡 Author
Made with ❤️ by Dipali Dharmik
