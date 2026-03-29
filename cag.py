from sarvam_llm import generate_response

def refine_answer(query, initial_answer):
    
    prompt = f"""
    Question: {query}
    
    Initial Answer: {initial_answer}
    
    Check if the answer is correct.
    If wrong or incomplete, correct it.
    If correct, improve clarity.
    """

    final_answer = generate_response(prompt)
    
    return final_answer