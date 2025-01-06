import os
from io import BytesIO
from pdfminer.high_level import extract_text
from docx import Document
import openai
from django.conf import settings

def process_text_with_chatgpt(prompt):
    """
    Process text using OpenAI's ChatGPT API.
    :param prompt: The input prompt for ChatGPT.
    :return: The response text from ChatGPT.
    """
    from openai import OpenAI
    client = OpenAI()
    openai.api_key = os.environ['OPENAI_API_KEY']


    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[{"role": "system", "content": "You are a legal assistant."},
                      {"role": "user", "content":
                        "Summarize the following legal document and provide the output as JSON with keys: "
                        "'summary', 'key_points', 'relevant_cases', and 'legal_issues'.\n\n" + prompt}]
    )
    response_content = completion.choices[0].message.content

    # Clean the response
    if response_content.startswith("```json"):
        response_content = response_content[7:]
    if response_content.endswith("```"):
        response_content = response_content[:-3]

    # Parse the cleaned JSON
    import json
    return json.loads(response_content)


def extract_text_from_pdf(file):
    """
    Extract text from a PDF file.
    :param file: str, path to the PDF file.
    :return: str, extracted text.
    """
    try:
        file.seek(0)
        pdf_content = file.read()

        # Use pdfminer to extract text from the in-memory content
        text = extract_text(BytesIO(pdf_content))# Pass the content as a BytesIO object

        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"


def extract_text_from_docx(file_path):
    """
    Extract text from a DOCX file.
    :param file_path: str, path to the DOCX file.
    :return: str, extracted text.
    """
    try:
        doc = Document(file_path)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return text
    except Exception as e:
        return f"Error extracting text from DOCX: {e}"


def extract_text_from_txt(file_path):
    """
    Extract text from a TXT file.
    :param file_path: str, path to the TXT file.
    :return: str, extracted text.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as e:
        return f"Error extracting text from TXT: {e}"

def extract_text_from_file(file):
    """
    Extract text from a file based on its extension.
    :param file: str, path to the file.
    :return: str, extracted text.
    """
    _, ext = os.path.splitext(file.name.lower())

    if ext == ".pdf":
        return extract_text_from_pdf(file)
    elif ext == ".docx":
        return extract_text_from_docx(file)
    elif ext == ".txt":
        return extract_text_from_txt(file)
    else:
        return "Unsupported file format."


