import pytest
from task_manager import TaskManager

class TestTaskManager:
    def test_add_task(self):
        manager = TaskManager()
        task = manager.add_task("Test Task", "Test Description", "high")
        
        assert task['title'] == "Test Task"
        assert task['priority'] == "high"
        assert len(manager.get_all_tasks()) == 1
    
    def test_delete_task(self):
        manager = TaskManager()
        task = manager.add_task("Test Task", "Test Description", "medium")
        manager.delete_task(task['id'])
        
        assert len(manager.get_all_tasks()) == 0