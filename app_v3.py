from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

user_data = {}

@app.route('/')
def index():
    return render_template('index_v3.html')

@app.route('/user_info', methods=['POST'])
def user_info():
    global user_data
    user_data = request.json
    return jsonify(user_data), 200

@app.route('/display_user')
def display_user():
    return render_template('display_user_v3.html', user=user_data)

if __name__ == '__main__':
    app.run(debug=True)
