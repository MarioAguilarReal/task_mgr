import requests

BASE_URL = "http://127.0.0.1:5000/tasks"

def update_task(id, summary, description):
    task_data = {
        "summary": summary,
        "description": description
    }

    url = "%s/%s" % (BASE_URL, id)

    response = requests.put(url, json=task_data)
    if response.status_code == 204:
        print("Updated successful")
    else:
        print("Updated failed")


if __name__ == "__main__":
    print("Update a task by filling out the prompts below:")
    id = input("ID:")
    summary = input("Summary: ")
    description = input("Description: ")
    update_task(id, summary, description)
