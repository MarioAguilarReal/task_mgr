import requests

BASE_URL = "http://127.0.0.1:5000/tasks"

def delete_task(id):
    url = "%s/%s" % (BASE_URL, id)
    response = requests.delete(url)
    if response.status_code == 204:
        print("Deleted successful")
    else:
        print("Deleted failed")


if __name__ == "__main__":
    print("Delete a task by filling out the prompts below:")
    id = input("ID:")
    delete_task(id)
