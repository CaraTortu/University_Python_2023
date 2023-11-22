import json
import requests

url: str = "https://jsonplaceholder.typicode.com/todos"
json_data: dict = requests.get(url).json()
users: dict = {}

for task in json_data:
    if users.get(task["userId"]) == None:
        users[task["userId"]] = 0

    if task["completed"]:
        users[task["userId"]] += 1

highest_task_done = max(users.values())
users_with_highest_task = filter(lambda id: users[id] == highest_task_done, users.keys())
users_with_highest_task = list(map(str, users_with_highest_task))

print(f"Users that completed the most tasks: {', '.join(users_with_highest_task)}")

tasks_to_keep: list[dict] = list(filter(lambda x: str(x["userId"]) in users_with_highest_task, json_data))

with open("filtered_data_file.json", "w") as f:
    json.dump(tasks_to_keep, f)

