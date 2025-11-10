from flask import Flask, jsonify, request
from task_manager import TaskManager

app = Flask(__name__)
task_manager = TaskManager()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(task_manager.get_all_tasks())

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = task_manager.add_task(
        title=data['title'],
        description=data.get('description', ''),
        priority=data.get('priority', 'medium')
    )
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = task_manager.update_task(task_id, data)
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task_manager.delete_task(task_id)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)