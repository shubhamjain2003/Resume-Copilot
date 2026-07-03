from embeddings import get_query_embedding
from vectorstore import search_sections, get_section
from rag import ask_gemini


def ask_resume(question):

    question_lower = question.lower()

    # -------- Rule-based routing --------
    if "experience" in question_lower or "work" in question_lower or "job" in question_lower:
        context = get_section("Experience")

    elif "project" in question_lower:
        context = get_section("Projects")

    elif "skill" in question_lower or "language" in question_lower:
        context = get_section("Technical Skills")

    elif "education" in question_lower or "college" in question_lower:
        context = get_section("Education")

    elif "achievement" in question_lower or "jee" in question_lower:
        context = get_section("Achievements")

    else:
        # Fall back to vector search
        query_embedding = get_query_embedding(question)
        results = search_sections(query_embedding)
        context = "\n\n".join(results["documents"][0])

    print("\n========== CONTEXT ==========\n")
    print(context)

    answer = ask_gemini(context, question)

    return answer   

if __name__ == "__main__":

    while True:

        question = input("\nAsk about your resume (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        answer = ask_resume(question)

        print("\nAnswer:\n")
        print(answer)