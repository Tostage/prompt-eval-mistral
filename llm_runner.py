from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load the Mistral model
model_name = "TheBloke/Mistral-7B-Instruct-v0.1-GGUF"


print("[LOADING MODEL] This may take a minute...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_response(prompt, max_tokens=200):
    output = generator(prompt, max_new_tokens=max_tokens, do_sample=True)[0]["generated_text"]
    return output
