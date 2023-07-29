from flask import Flask, render_template, request
import pdfplumber

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_pdf_to_text():
    file = request.files['pdf_file']
    if file:
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return render_template('result.html', text=text)
    else:
        return "No file selected!"

if __name__ == '__main__':
    app.run(debug=True)
