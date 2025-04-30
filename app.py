from flask import Flask, render_template, request, jsonify
from chatbot_engine import get_answer

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chatbot_response():
    user_input = request.form['messageText']
    response = get_answer(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
