import can_place_MLA_task as cpt
import print_Generated_conflicts as pc

def schedule_measurement_tasks(tasks, conflicts, bin_capacity):
    
    #Print generated Task
    #print (tasks)
    
    #print Generated Conflicts
    pc.print_conflicts (conflicts)
    
    """Schedule tasks into daily slots based on MLA constraints.
    Sort tasks by their duration in descending order - execute longer duration first"""
    tasks_sorted = sorted(tasks, key=lambda x: x['duration'], reverse=True)
    schedule = []
    for task in tasks_sorted:
        scheduled = False
        for slot in schedule:
            if sum(t['duration'] for t in slot) + task['duration'] <= bin_capacity:
                if cpt.can_place_task(slot, task, conflicts):
                    slot.append(task)
                    scheduled = True
                    break
        if not scheduled:
            schedule.append([task])

    return schedule