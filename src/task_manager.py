class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, title, description, priority):
        task = {
            'id': self.next_id,
            'title': title,
            'description': description,
            'priority': priority,
            'status': 'pending',
            'created_at': '2024-11-15'
        }
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def get_all_tasks(self):
        return self.tasks
    
    def update_task(self, task_id, updates):
        for task in self.tasks:
            if task['id'] == task_id:
                task.update(updates)
                return task
        return None
    
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]