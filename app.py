from retriever import retrieve
from sarvam_llm import generate_response
from cag import refine_answer
from voice import speak, listen


def run_pipeline(query):
    
    # Step 1: Retrieve context
    context = retrieve(query)
    context_text = "\n".join(context)

    # Step 2: RAG
    rag_prompt = f"""
    Use the following context to answer:

    {context_text}

    Question: {query}
    """

    initial_answer = generate_response(rag_prompt)

    # Step 3: CAG
    final_answer = refine_answer(query, initial_answer)

    return final_answer


def jarvis_mode():
    speak("Hello, I am Jarvis. How can I assist you?")

    while True:
        query = listen()

        if query is None:
            continue

        # Exit condition
        if "exit" in query or "stop" in query:
            speak("Goodbye!")
            break

        answer = run_pipeline(query)
        speak(answer)


if __name__ == "__main__":
    mode = input("Type 'voice' for Jarvis or 'text' for normal: ")

    if mode == "voice":
        jarvis_mode()
    else:
        while True:
            query = input("Ask something: ")
            answer = run_pipeline(query)
            print("\nFinal Answer:", answer)