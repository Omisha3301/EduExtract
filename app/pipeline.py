from ocr_parser import extract_text_from_pdf
from insights_llm import get_structured_summary
from book_finder import find_books_on_amazon

def process_syllabus(uploaded_pdf):
    # 1. OCR + Text Extraction
    extracted_text = extract_text_from_pdf(uploaded_pdf)

    # 2. Handle error before LLM call
    if isinstance(extracted_text, dict) and "error" in extracted_text:
        return extracted_text["error"], [], [], []

    # 3. LLM for Summary, Sequence, Prereqs, Book List
    result = get_structured_summary(extracted_text)
    summary = result.get("summary", "")
    sequence = result.get("learning_sequence", [])
    prerequisites = result.get("prerequisites", [])
    books_raw = result.get("books", [])

    # 4. Search Amazon for Book URLs
    books = find_books_on_amazon(books_raw)

    return summary, sequence, prerequisites, books
