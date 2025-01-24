if __name__ == '__main__':
    from vars import corpus_of_documents, user_prompt, user_input, base_prompt
    from jaccard import return_response
    from openai import OpenAI

    relevant_document = return_response(user_input, corpus_of_documents)                                                   
    full_response = []
    
    prompt = base_prompt.format(user_input=user_input, relevant_document=relevant_document)            
    
    client = OpenAI()
    response = client.chat.completions.create(                                                         
        model="gpt-4",
        temperature=1,
        messages=[{"role": "system", "content": prompt}]
    )
                                                                                                       
    print(response.choices[0].message.content)
