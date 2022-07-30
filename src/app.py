from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [ { "done": False, "label": "Sample Todo 1" }]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_data = jsonify(todos)
    return json_data

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    del todos[(position)]
    return 'Item something'

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)