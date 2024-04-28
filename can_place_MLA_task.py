def can_place_task(scheduled_tasks, new_task, conflicts):
    """Check if the new_task can be scheduled in this same bin without exceeding MLA conflicts rules."""
    for existing_task in scheduled_tasks:
        
        """if MLA is 1, then scheduling is round-robin with no concurrent execution; 
        if MLA is 2, you can stack 2 non-conflicting jobs within the same bin,"""
        
        if conflicts[new_task['id']][existing_task['id']] ==1 :
            #print ("Conflict Detected", new_task['id'], "Conflicts with", existing_task['id'])
            return False
    return True
