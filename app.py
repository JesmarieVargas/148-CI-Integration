from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def handle_sum():
    data = request.json
    return jsonify({'result': data['num1'] + data['num2']})

if __name__ == '__main__':
    app.run(debug=True)