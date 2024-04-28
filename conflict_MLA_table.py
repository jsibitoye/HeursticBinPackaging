import random

def generat_conflicts(conflict_Total):
    # Define the number of tasks
    
    #remove the comment below to test manually or execute with randomly generated conflicts
    """conflicts = {
    'T1': {'T1': 2, 'T2': 1, 'T3': 2, 'T4': 2,},
    'T2': {'T1': 1, 'T2': 2, 'T3': 2, 'T4': 1,},
    'T3': {'T1': 2, 'T2': 2, 'T3': 2, 'T4': 2,},
    'T4': {'T1': 2, 'T2': 1, 'T3': 2, 'T4': 2}
    }
    return conflicts"""
    
    
    conflicts = {}
    task_ids = [f"T{i}" for i in range(1, conflict_Total + 1)]

    for task_id in task_ids:
        conflicts[task_id] = {}
        for other_task_id in task_ids:
            if task_id == other_task_id:
                conflicts[task_id][other_task_id] = 2
            else:
                # Assign a conflict status of 0 (no conflict) or 1 (conflict) randomly
                # Make sure both task_id and other_task_id reflect the same conflict status
                if other_task_id in conflicts and task_id in conflicts[other_task_id]:
                    conflicts[task_id][other_task_id] = conflicts[other_task_id][task_id]
                else:
                    conflicts[task_id][other_task_id] = random.randint(0, 1) +1
    return conflicts

"""conflicts = generat_conflicts(5)
for x in conflicts:
    print(x, ":",conflicts[x])"""