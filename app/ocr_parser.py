import os
import json
import tempfile
from dotenv import load_dotenv
from mistralai import Mistral, DocumentURLChunk

load_dotenv()
api_key = os.getenv("LLM_API_KEY")
client = Mistral(api_key=api_key)

def extract_text_from_pdf(uploaded_file):
    # Step 1: Save Streamlit's in-memory file to disk
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Step 2: Upload PDF to Mistral
    with open(tmp_path, "rb") as f:
        uploaded_pdf = client.files.upload(
            file={
                "file_name": "uploaded_file.pdf",
                "content": f,
            },
            purpose="ocr"
        )

    # Step 3: Get signed URL for OCR
    signed_url = client.files.get_signed_url(file_id=uploaded_pdf.id)

    # Step 4: Call OCR
    pdf_response = client.ocr.process(
        document=DocumentURLChunk(document_url=signed_url.url),
        model="mistral-ocr-latest",
        include_image_base64=False
    )

    # Step 5: Return the markdown text from first page (or all pages)
    ocr_markdown = "\n\n".join([page.markdown for page in pdf_response.pages])
    
    os.remove(tmp_path)
    
    keywords = ["syllabus", "course", "module", "curriculum", "topics"]
    if not any(keyword in ocr_markdown.lower() for keyword in keywords):
        return {
            "error": "The uploaded PDF does not appear to be a syllabus or course document."
        }
    


    return ocr_markdown
