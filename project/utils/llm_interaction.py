from transformers import pipeline # it use for LLM 
#llm  model answer the question based on given context 

# It will take query and context as argument and generate the result based on given query 
def ask_llama2(query, context):
   
    nlp = pipeline("text2text-generation", model="google/flan-t5-base") # it is good for hugging face
    contexts = "\n".join([f"{key}: {value}" for key, value in context.items()])
    prompt = f"Context:\n{contexts}\n\nQuestion: {query}\n\nAnswer:"
    response = nlp(prompt, max_length=200, num_return_sequences=1)
    return response[0]['generated_text']
