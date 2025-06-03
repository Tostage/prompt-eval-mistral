from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_name = "tiiuae/falcon-7b-instruct"

print("[LOADING MODEL] This may take a minute...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_response(prompt, max_tokens=200):
    output = generator(prompt, max_new_tokens=max_tokens, do_sample=True)[0]["generated_text"]
    return output
