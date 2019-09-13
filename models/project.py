import requests
from api.gitlab_api import *
from db.connection import *

db = Connection.connect()

path = '/todos'
projects = requests.get(GitlabApi.load(path))

print(projects.status_code)

if projects.status_code != 200:
    raise Exception('api error')

project_collection = db['projects']
for project in projects.json():
    if not project_collection.find_one({'id': project['id']}):
        row = project_collection.insert_one(project)
        print(row)


