from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [
    {'label': 'Sample Todo 1', 'done': False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print('incoming request with the following body', request_body)

    if 'label' not in request_body or 'done' not in request_body:
        return jsonify({'error': 'Missing label or done key'}), 400
    
    todos.append(request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if 0 <= position <len(todos): del todos[position]
    else:
        return jsonify({'error': 'Position out of range'}),400
    
    return jsonify(todos)

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)