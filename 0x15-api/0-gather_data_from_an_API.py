#!/usr/bin/python3
'''
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''
import requests
from sys import argv


def get_employeeID_info(user_input):
    url =  'https://jsonplaceholder.typicode.com/'
    user_request = url + 'users/{}'.format(user_input)
    employee = requests.get(user_request).json()
    task_req = url + 'todos?userId={}'.format(employee.get('id'))
    task = requests.get(task_req).json()
    return {"employee": employee, "tasks": task}

def completed_task(data):
    total = len(data.get('task'))
    completed_task = [x fo x in data.get('tasks') if x.get('completed')]
    completed = len(completed_task)
    employee = data.get('employee').get('name')
    print('Employee', user.get('name'),
          'is done with task({}/{}):'.
          format(employee, completed, total)
    for tsk in completed_task:
          print('\t {}'.format(tsk.get('title')))


if '__name__'=='__main__':
    data = get_employeeID_info(argv[1])
    completed_task(data)
