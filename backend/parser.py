import fitz  # PyMuPDF
import re


def extract_text_from_pdf(pdf_path):
    """
    Extract all text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF.

    Returns:
        str: Extracted text.
    """

    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


def split_resume_sections(text):
    """
    Split a resume into logical sections.

    Returns:
        dict
        Example:
        {
            "Education": "...",
            "Experience": "...",
            "Projects": "...",
            "Technical Skills": "...",
            "Achievements": "..."
        }
    """

    # Section titles present in your resume
    section_titles = [
        "Education",
        "Experience",
        "Projects",
        "Technical Skills",
        "Achievements",
    ]

    # Build regex pattern
    pattern = r"(?=(" + "|".join(map(re.escape, section_titles)) + r"))"

    matches = list(re.finditer(pattern, text))

    sections = {}

    for i, match in enumerate(matches):

        title = match.group(1)

        start = match.start()

        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(text)

        content = text[start:end].strip()

        sections[title] = content

    return sections