from backend.services.llm import generate_text
from backend.services.retriever import fetch_context
from backend.services.docx_export import create_docx
from models.prompts import build_prompt


def generate_essay_pipeline(profile, tone):
    # 1. Retrieve context
    context = fetch_context(profile["interests"])

    # 2. Build prompt
    prompt = build_prompt(profile, context, tone)

    # 3. Generate essay
    essay = generate_text(prompt)

    # 4. Create DOCX
    docx_path = create_docx("College Essay", essay)

    return {
        "essay": essay,
        "docx_path": docx_path
    }