from flask import Flask, request, jsonify, render_template
import fitz  # PyMuPDF
import openai

app = Flask(__name__)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    pdf_path = "total.pdf"  # PDF 파일 경로
    context = extract_text_from_pdf(pdf_path)

    answer = get_answer_from_chatgpt(question, context)
    return jsonify({'answer': answer})

def get_answer_from_chatgpt(question, context):
    openai.api_key = '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'

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Question: {question}\n\nContext: {context}\n\nAnswer:"}
        ],
        max_tokens=3000,
        stop=["\n"],
        temperature=0.5
    )
    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    app.run(debug=True)

