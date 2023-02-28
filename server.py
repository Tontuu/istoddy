#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import requests
import json as Json

def get_tasks(token):
    url = "https://api.todoist.com/rest/v2/tasks"
    try:
        response = requests.get(url, headers={"Authorization": f"Bearer {token}"})
        tasks = response.json()
        return tasks
    except requests.exceptions.JSONDecodeError as e:
        raise SystemExit(f"ERROR: Invalid token")

def sanatize_tasks(tasks):
    new_tasks = []
    for task in tasks:
        if task["due"]:
            date = task["due"]["date"]
            date = "/".join(date.split('-')[:0:-1])
        else:
            date = "agora"

        new_tasks.append({
            "content": task["content"],
            "due-date": date,
            "priority": task["priority"],
            "description": task["description"],
            })

    new_tasks = sorted(new_tasks, key=lambda task: int(task["priority"]), reverse=True) 
    return new_tasks

def sync_with_home(tasks, filepath):
    result_str = ""
    for task in tasks:
        result_str += f"# {task['content']} para {task['due-date']}\n"
        if task["description"]:
            result_str += f"\t - {task['description']}\n"

    try:
        with open(filepath, "a+") as f:
            f.write(result_str)
        print("Sucessfully synced to-dos file with Todoist!")
    except FileNotFoundError as e:
        raise SystemExit(f"ERROR: Unable to load file: {e}")

def sync(tasks, filepath):
    # TODO: Check if task content differs from home file, if yes, add to todoist
    tasks = sanatize_tasks(tasks)
    sync_with_home(tasks, filepath)

def main():
    load_dotenv()

    TOKEN = os.getenv("ACCESS_TOKEN")
    TODO_FILEPATH = os.getenv("TODO_FILEPATH")

    tasks = get_tasks(TOKEN)

    # sync(tasks, TODO_FILEPATH)


if __name__ == "__main__":
    main()
    exit(0)
