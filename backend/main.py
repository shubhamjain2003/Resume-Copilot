from pathlib import Path

from parser import extract_text_from_pdf
from parser import split_resume_sections

from embeddings import get_embeddings

from vectorstore import store_sections

BASE_DIR = Path(__file__).resolve().parent.parent

pdf_path = BASE_DIR / "data" / "resumes" / "resume.pdf"

text = extract_text_from_pdf(str(pdf_path))

sections = split_resume_sections(text)

print("\nResume Sections Found:\n")

for section in sections:
    print("•", section)

embeddings = get_embeddings(
    list(sections.values())
)

print("\nCreating embeddings...")

store_sections(
    sections,
    embeddings
)

print("\nStored in ChromaDB successfully ✅")