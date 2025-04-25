import os
from mistralai import Mistral, DocumentURLChunk, ImageURLChunk, TextChunk
import json
from dotenv import load_dotenv

load_dotenv()  # Must be called before accessing os.environ
api_key = os.getenv("LLM_API_KEY")
client = Mistral(api_key=api_key)
def get_structured_summary(ocr_markdown):
    prompt_text = (
        f"This is a syllabus in markdown format:\n\n{ocr_markdown}\n\n"
        "Please extract and return a structured response in JSON with the following keys only:\n"
        "- summary: a detailed course overview\n"
        "- learning_sequence: list of modules or topics in the logical order of learning\n"
        "- prerequisites: logical list of concepts or courses needed before starting this one\n"
        "- books: list of recommended textbooks (only book titles)(extracted from the markdown itself)\n"
        "Return the output as **only JSON**, no commentary or extra text."
    )

    chat_response = client.chat.complete(
        model="ministral-8b-latest",
        messages=[{
            "role": "user",
            "content": [TextChunk(text=prompt_text)],
        }],
        response_format={"type": "json_object"},
        temperature=0,
    )

    try:
        return json.loads(chat_response.choices[0].message.content)
    except Exception as e:
        print("⚠️ Error parsing LLM response:", e)
        return {
            "summary": "Error in LLM response.",
            "learning_sequence": [],
            "prerequisites": [],
            "books": []
        }

