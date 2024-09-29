import gradio as gr
from gradio_client import Client, handle_file
import re
from thefuzz import fuzz

# hugging face clients for both OCR options
surya_ocr_client = Client("artificialguybr/Surya-OCR")
got_ocr_client = Client("stepfun-ai/GOT_official_online_demo")

# Global variable to store the extracted OCR text
extracted_text = ""

def ocr_extraction(image, ocr_model):
    global extracted_text
    if image is None:
        return "Please upload an image first."
    
    try:
        if ocr_model == "Surya OCR":
            client = surya_ocr_client
            result = client.predict(
                image=handle_file(image),
                langs="en",
                api_name="/ocr_workflow"
            )
            text_matches = re.findall(r"text='(.*?)'", str(result))
            extracted_text = "\n".join(text_matches)
        elif ocr_model == "GOT OCR":
            client = got_ocr_client
            result = client.predict(
                image=handle_file(image),
                got_mode="plain texts OCR",
				fine_grained_mode="box",
                ocr_color="red",
                ocr_box="Hello!!",
                api_name="/run_GOT"
            )
            extracted_text = result[0]
        else:
            return "Invalid OCR model selected."
        
        return extracted_text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def search_keyword(keyword, search_type):
    global extracted_text
    if not extracted_text:
        return "No OCR text found. Please extract text from an image first."
    if not keyword:
        return extracted_text
    
    if search_type == "Direct Search":
        highlighted_text = re.sub(f"({re.escape(keyword)})", r'<span style="background-color: yellow;">\1</span>', extracted_text, flags=re.IGNORECASE)
    else:  # Nearest Search
        words = extracted_text.split()
        highlighted_words = []
        for word in words:
            if fuzz.ratio(word.lower(), keyword.lower()) >= 80:  # Adjust threshold as needed
                highlighted_words.append(f'<span style="background-color: yellow;">{word}</span>')
            else:
                highlighted_words.append(word)
        highlighted_text = " ".join(highlighted_words)
    
    return highlighted_text

with gr.Blocks(theme=gr.themes.Soft()) as gr_interface:
    gr.Markdown("# 📷 OCR Text Extraction and Advanced Keyword Search 🔍")
    
    with gr.Row():
        with gr.Column(scale=1):
            image_input = gr.Image(type="filepath", label="Upload Image")
            ocr_model_dropdown = gr.Dropdown(
                choices=["Surya OCR", "GOT OCR"],
                value="Surya OCR",
                label="Select OCR Model"
            )
            ocr_button = gr.Button("Extract Text", variant="primary")
        
        with gr.Column(scale=2):
            extracted_text_output = gr.Textbox(
                label="Extracted Text",
                placeholder="Text extracted from the image will appear here.",
                lines=10
            )
    
    with gr.Row():
        with gr.Column(scale=1):
            keyword_input = gr.Textbox(label="Enter keyword to search")
            search_type = gr.Radio(["Direct Search", "Nearest Search"], label="Search Type", value="Direct Search")
            search_button = gr.Button("Search Keyword", variant="secondary")
        
        with gr.Column(scale=2):
            highlighted_output = gr.HTML(label="Highlighted Text")
    
    ocr_button.click(
        fn=ocr_extraction,
        inputs=[image_input, ocr_model_dropdown],
        outputs=extracted_text_output
    )
    
    search_button.click(
        fn=search_keyword,
        inputs=[keyword_input, search_type],
        outputs=highlighted_output
    )

gr_interface.launch(share=True)             remove the fuzzy logic from the code and drop[ that feature