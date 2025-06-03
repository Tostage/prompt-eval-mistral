# Prompt Evaluation Sandbox

This project simulates the real-world LLM evaluation tasks. It allows a human reviewer to input prompts, generate model completions and score the responses using a structured UI.


##  Project Purpose

This tool was built to showcase:
- ✅ Your judgment accuracy for factuality, tone, and clarity
- ✅ Your ability to replicate Outlier-style annotation workflows
- ✅ A lightweight app that mimics human-in-the-loop evaluation tasks


##  How It Works

Using the app, you can:
1. Input a natural language prompt
2. Generate a response from an open-source language model
3. Evaluate the response using 3 sliders:
   - **Factual Accuracy (0–5)**
   - **Clarity & Coherence (0–5)**
   - **Tone Appropriateness (0–5)**
4. Optionally leave comments or reviewer notes
5. Save all evaluations to a `.csv` file for auditing or submission


##  Technologies Used

- `Streamlit` for the interactive front end
- `transformers` and `pytorch` to run open LLMs like `pythia-1b-deduped`
- `pandas` to log scored results to CSV


##  Example Prompt Evaluation

**Prompt:**  
> Explain the greenhouse effect

**Model Response:**  
> The greenhouse effect is when carbon monoxide traps heat in Earth's atmosphere.

**Evaluation:**  
- Factuality: 2/5  
- Clarity: 4/5  
- Tone: 5/5  
- Notes: CO confused with CO₂; explanation mostly clear but scientifically incorrect


##  File Structure
prompt-eval-sandbox/
├── llm_runner.py # Runs the LLM model
├── streamlit_app.py # Streamlit front-end app
├── prompt_eval_log.csv # Evaluation results (CSV)
├── requirements.txt # Python dependencies
└── README.md # This file


##  How to Run the App

### 1. Clone the repository

```bash
git clone https://github.com/your-username/prompt-eval-sandbox.git
cd prompt-eval-sandbox
pip install -r requirements.txt
streamlit run streamlit_app.py

Sample Dataset
 - 10 reviewed prompts, responses and evaluation scores are included.

 - prompt_eval_log.csv — demonstrates ability to detect hallucination, assess tone shifts and evaluate clarity.
