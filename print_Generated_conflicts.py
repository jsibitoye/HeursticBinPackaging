def print_conflicts(generated_conflicts):
    
    #print out generated conlict table 
    #print(type(generated_conflicts))
    print("\nGENERATED CONFLICT TABLE")
    
    for task, conflicts_dict in generated_conflicts.items():
        # Filter tasks that have a conflict value of 1 and are not the same task (avoid self-referencing)
        conflicts_one = [other_task for other_task, conflict_value in conflicts_dict.items() if conflict_value == 1 and other_task != task]
        if conflicts_one:  # Only print if there is at least one conflict
            print(f"{task}: {', '.join(conflicts_one)}")
    

    # Print the conflicts where the conflict value is 1
    #print(generated_conflicts)