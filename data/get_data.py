from huggingface_hub import InferenceClient

client = InferenceClient(api_key="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")

messages = [
	{ "role": "user", "content": "ecrit moi un post linkedin en 500 caracteres en francais" }
]

stream = client.chat.completions.create(
    model="codellama/CodeLlama-34b-Instruct-hf", 
	messages=messages, 
	temperature=0.5,
	max_tokens=2048,
	top_p=0.7,
	stream=True
)
theme = ''
for chunk in stream:
    
    if chunk.choices[0].delta.content == '.': 
        theme += chunk.choices[0].delta.content
        theme += "\n"
        
    else:
        theme += chunk.choices[0].delta.content
print(theme)