import random

def generate_tasks(num_tasks):
    
    #remove the comment below to test manually or execute with randomly generated Tasks
    """
    tasks = [
    {'id': 'T1', 'duration': 20},
    {'id': 'T2', 'duration': 10},
    {'id': 'T3', 'duration': 7},
    {'id': 'T4', 'duration': 10}
    ]
    return tasks
    """
    tasks = []
    for i in range(1, num_tasks + 1):
        task = {
            'id': f'T{i}',
            'duration': random.randint(1, 20)  # Random task duration between 1 and 20 minutes
        }
        tasks.append(task)
    return tasks

# Variable Initializations