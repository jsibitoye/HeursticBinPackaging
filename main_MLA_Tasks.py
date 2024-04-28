#Import Task List
import schedule_MLA_measurment_taks as smt
import task_MLA_Table as measurement_tasks
#import Conlict List
import conflict_MLA_table as task_conflicts

# Bin capacity and daily maximum duration (24 hours = 1440 minutes for full day capacity)
daily_max_duration = 1440
bin_capacity = 20 
Max_daily_slot_schedule = 1440/bin_capacity

# CHANGE THE VALUE BELOW TO INCREASE OR DECREASE TASKS up to 200
task_Total_Count = 40 

#check if total number of tasks generated is not above 200 - this is to make sure we stay within the 24 hr execution limit
if task_Total_Count<=200: 
    task_table = measurement_tasks.generate_tasks(task_Total_Count)
    conflict_table = task_conflicts.generat_conflicts(task_Total_Count)

print("Total Generated Task duration:", sum(t['duration'] for t in task_table))

if sum(t['duration'] for t in task_table) <= daily_max_duration:            
    # Execute the bin packing algorithm
    scheduled_tasks = smt.schedule_measurement_tasks(task_table, conflict_table, bin_capacity)
    
    
    #print scheduled tasks output
    print("\n SCHEDULED TASK OUTPUT")
    for i, bin in enumerate(scheduled_tasks, 1):
        # Extract and print only the IDs and Task Durations from each task in the bin
        task_descriptions = ',  '.join(f"{task['id']} ({task['duration']} min)" for task in bin)
        print(f"Bin {i}: {task_descriptions} \n")
else:
    print("Task schedule on table exceed 24 hour executable constraints")