import requests
import json


url = "https://jobs.rbc.com/ca/en/c/technology-%7C-analytics-%7C-research-jobs?from=20&s=5"
response = requests.get(url)

y = response.text.split('phApp.ddo =')
z = y[1].split("phApp.experimentData")[0]

a = z[:len(z)-2]

y = json.loads(a)

jobs = y["eagerLoadRefineSearch"]["data"]

len(jobs)


