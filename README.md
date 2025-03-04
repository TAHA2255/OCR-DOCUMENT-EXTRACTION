# Document OCR Extraction Web App

This is a **Streamlit-based web application** that allows users to **upload documents (PDF, JPG, PNG)**, extract text from them using **Tesseract OCR**, and display the extracted text on the webpage.

## Features

- 📂 Upload **PDF, JPG, PNG** files.
- 🖼️ Convert **PDF pages to images** using `pdf2image`.
- 📝 Extract text from images using `pytesseract` (Tesseract OCR).
- 📄 Display extracted text in a text area on the webpage.

## Technologies Used

- **Python** 🐍
- **Streamlit** (for the web UI)
- **Tesseract OCR** (for text extraction)
- **pdf2image** (for PDF to image conversion)
- **Pillow (PIL)** (for image processing)

---

## Installation & Setup

### Prerequisites

Make sure you have the following installed:

- **Python (>=3.8)**
- **Tesseract OCR**
- **Poppler (for PDF conversion)**

### Step 1: Clone the Repository

```sh
git clone https://github.com/your-username/document-ocr-extraction.git
cd document-ocr-extraction
```

### Step 2: Install Dependencies

Create a virtual environment (optional but recommended):

```sh
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```

Install required packages:

```sh
pip install -r requirements.txt
```

### Step 3: Install Tesseract OCR

#### **Windows**

Download and install Tesseract OCR from: [Tesseract Download](https://github.com/UB-Mannheim/tesseract/wiki)

After installation, add the Tesseract path to your environment variables:

```sh
setx TESSDATA_PREFIX "C:\Program Files\Tesseract-OCR"
```

#### **macOS (Homebrew)**

```sh
brew install tesseract
```

#### **Linux (Ubuntu/Debian)**

```sh
sudo apt update
sudo apt install tesseract-ocr -y
```

### Step 4: Install Poppler (for PDF processing)

#### **Windows**

Download Poppler from: [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases)

Extract it and add the `bin` folder to your PATH.

#### **macOS (Homebrew)**

```sh
brew install poppler
```

#### **Linux (Ubuntu/Debian)**

```sh
sudo apt install poppler-utils -y
```

---

## Running the Application

```sh
streamlit run app.py
```

This will open a browser window with the application.

---

## Project Structure

```
📂 document-ocr-extraction
├── 📄 app.py              # Main Streamlit application
├── 📜 requirements.txt    # Python dependencies
├── 📜 README.md           # Project documentation
└── 📂 assets/             # Sample files (optional)
```

---

## Usage

1. Upload a **PDF, PNG, or JPG** file.
2. If a **PDF** is uploaded, it will be **converted into images**.
3. Extracted text will be displayed in a **text area**.

---

## Contributing

Feel free to submit **pull requests** or report issues!

---

## License

This project is licensed under the **MIT License**.

---

## Contact

For any questions, reach out via [GitHub Issues](https://github.com/your-username/document-ocr-extraction/issues).

🚀 **Happy Coding!** 🎉

