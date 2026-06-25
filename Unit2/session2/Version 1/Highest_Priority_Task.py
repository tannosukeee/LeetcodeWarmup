def get_highest_priority_task(tasks):
    max = 0
    name = ""
    for key in tasks:
        if tasks[key] > max:
            max = tasks[key]
            name = key
    tasks.pop(name)
    return name

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)