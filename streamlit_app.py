import streamlit as st
import pandas as pd
from llm_runner import generate_response

st.set_page_config(page_title="Prompt Evaluation UI", layout="wide")

# Header
st.title("🧪 Prompt Evaluation Benchmark")
st.write("Enter a prompt, review the LLM's output, and score it below.")

# Prompt input
prompt = st.text_area("✍️ Prompt", height=150)

# Generate button
if st.button("Generate Response"):
    with st.spinner("Running model..."):
        response = generate_response(prompt)
        st.session_state["response"] = response

# Show response if available
if "response" in st.session_state:
    st.markdown("### 🤖 LLM Output")
    st.code(st.session_state["response"])

    st.markdown("### 🧠 Evaluate Output")

    factuality = st.slider("Factual Accuracy (0 = wrong, 5 = perfect)", 0, 5, 3)
    clarity = st.slider("Clarity & Coherence (0 = incoherent, 5 = clear)", 0, 5, 3)
    tone = st.slider("Tone (0 = bad, 5 = appropriate)", 0, 5, 3)
    notes = st.text_area("📝 Notes (optional)")

    if st.button("Save to CSV"):
        row = {
            "prompt": prompt,
            "response": st.session_state["response"],
            "factuality": factuality,
            "clarity": clarity,
            "tone": tone,
            "notes": notes,
        }
        df = pd.DataFrame([row])
        try:
            old = pd.read_csv("prompt_eval_log.csv")
            df = pd.concat([old, df], ignore_index=True)
        except FileNotFoundError:
            pass
        df.to_csv("prompt_eval_log.csv", index=False)
        st.success("Saved ✅")
