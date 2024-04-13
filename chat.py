import fitz  # PyMuPDF
import openai

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def get_answer_from_chatgpt(question, context):
    openai.api_key = 'your_api_key'
    
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", 
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": f"Question: {question}\n\nContext: {context}\n\nAnswer:"}
      ],
      max_tokens=150,
      stop=["\n"],
      temperature=0.5
    )
   
    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    pdf_path = "total.pdf"  # PDF 파일 경로
    user_question = input("질문을 입력하세요: ")  # 사용자 질문 입력

    # PDF에서 텍스트 추출
    pdf_text = extract_text_from_pdf(pdf_path)

    # ChatGPT를 사용하여 질문에 답변
    answer = get_answer_from_chatgpt(user_question, pdf_text)
    print("답변:", answer)
