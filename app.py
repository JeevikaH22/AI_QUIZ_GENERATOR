from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
key=os.getenv("API_KEY")
genai.configure(api_key=key)

model = genai.GenerativeModel("gemini-flash-latest")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')

    elif request.method == 'POST':
        v1 = request.form.get('topic', 'General Knowledge')
        v2 = int(request.form.get('num_questions', 5))
        v3 = request.form.get('difficulty', 'Medium')

        prompt = (
            f"Generate a quiz on {v1}. "
            f"Create {v2} questions with {v3} difficulty level. "
            f"Each question should have 4 options and highlight the correct answer after user chooses the option. "
            f"Make sure all the result is in HTML format apply proper CSS to it so that it looks "
            f"attractive and interactive. Do not wrap the response in markdown code blocks like ```html. "
            f"Return ONLY the raw HTML code."
        )

        response = model.generate_content(prompt)
        
        raw_html = response.text
        if raw_html.startswith("```html"):
            raw_html = raw_html.split("```html", 1)[1]
        elif raw_html.startswith("```"):
            raw_html = raw_html.split("```", 1)[1]
        
        if raw_html.endswith("```"):
            raw_html = raw_html.rsplit("```", 1)[0]
            
        clean_html = raw_html.strip()

        return render_template('result.html', result=clean_html)

if __name__ == '__main__':
    app.run(debug=True)