# Project_OCR

This project focuses on Optical Character Recognition (OCR) using Gradio to provide an intuitive interface for users. The web app allows users to extract text from images using two OCR models and perform a direct keyword search within the extracted text. It is deployed on Hugging Face at [this endpoint](https://huggingface.co/spaces/hardiksharma6555/Project_OCR), and it can also be run locally.

## Features

1. **OCR Models**: The app supports two OCR models:
   - **Surya OCR**: Extracts text using the `artificialguybr/Surya-OCR` model.
   - **GOT OCR**: Extracts text using the `stepfun-ai/GOT_official_online_demo` model.

2. **Text Extraction**: Once an image is uploaded, users can select one of the OCR models to extract text from the image.

3. **Keyword Search**: After extracting text, users can search for specific keywords, which will be highlighted within the text.

## Installation and Running Locally

To run the project locally, follow these steps:

### 1. Clone the repository:
```bash
git clone https://huggingface.co/spaces/hardiksharma6555/Project_OCR
cd Project_OCR
```

### 2. Install dependencies:
Ensure you have Python 3.x installed. Install the required dependencies using:
```bash
pip install -r requirements.txt
```

### 3. Run the app:
To launch the app locally, run the following command:
```bash
python app.py
```

The app will be available at `http://localhost:7860/` in your browser.

## Usage

### Web Version:
The app is deployed on Hugging Face Spaces and can be accessed [here](https://huggingface.co/spaces/hardiksharma6555/Project_OCR).

### Local Version:
After launching the app locally, you can upload an image, select an OCR model, extract text, and search for keywords directly in the extracted text.

## File Descriptions

- `app.py`: The main Gradio application script.
- `requirements.txt`: List of required Python packages for the project.

## How It Works

1. **Image Upload**: Users upload an image file from which they want to extract text.
2. **OCR Model Selection**: Users select an OCR model (either "Surya OCR" or "GOT OCR").
3. **Text Extraction**: The selected model extracts text from the uploaded image, which is displayed in the text box.
4. **Keyword Search**: Users can input a keyword to search for within the extracted text, and the keyword is highlighted in the results.

## License

This project is licensed under the MIT License.

---

### Metadata (For Hugging Face)
```yaml
title: Project_OCR
app_file: app.py
sdk: gradio
sdk_version: 4.44.0
```

This metadata is used to configure the Hugging Face Spaces project.