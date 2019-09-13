import requests
from api.gitlab_api import *

path = '/todos'
projects = requests.get(GitlabApi.load(path))

print(projects.status_code)

if projects.status_code != 200:
    raise Exception('api error')

for project in projects.json():
    print(project['userId'], project['title'])


