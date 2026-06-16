from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AQ.Ab8RN6LmBChTQNk1pfCeu6BmjTlUKhl0UnZ4sKqdoZWA1XG41A")

model = genai.GenerativeModel("gemini-2.5-flash")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():

    article = request.form['article']

    prompt = f"""
Analyze this news article.

Provide:
1. Credibility Score (0-100)
2. Prediction (Real/Fake)
3. Reason
4. Summary

Article:
{article}
"""

    response = model.generate_content(prompt)
    result = response.text

    return render_template('result.html', result=result)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
