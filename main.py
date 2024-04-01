import requests
from datetime import datetime
from my_variables import *

USERNAME = MY_PIXE_USERNAME
TOKEN = MY_PIXE_TOKEN
USER_ENDPOINT = "https://pixe.la/v1/users"
USER_PARAM = {
	"token": TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes",
}

# create_account = requests.post(url=USER_ENDPOINT, json=USER_PARAM)

GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{USERNAME}/graphs"
GRAPH_PARAM = {
	"id" : "graph01",
	"name": "Daily Programming Graph",
	"unit": "hours",
	"type": "float",
	"color": "ajisai"
}
HEADERS = {
	"X-USER-TOKEN" : TOKEN
}

generate_graph = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_PARAM, headers=HEADERS)

# today = datetime.now()
today = datetime(year=202, month = 12, day=10)

POST_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_PARAM["id"]}"
POST_PARAM = {
	"date": today.strftime("%Y%m%d"),
	"quantity": f"{2+.5}"
}

# add_activity = requests.post(url=POST_ENDPOINT, json=POST_PARAM, headers=HEADERS)




MODIFY_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_PARAM["id"]}/20231207"
MODIFY_PARAM = {
	"quantity": f"{2+.45}",
}

# modify_activity = requests.put(url=MODIFY_ENDPOINT, json=MODIFY_PARAM, headers=HEADERS)
DELETE_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_PARAM["id"]}/20231210"
DELETE_PARAM = {
	"quantity": f"{0}",
}

# delete_activity = requests.put(url=DELETE_ENDPOINT, json=DELETE_PARAM, headers=HEADERS)


# ####### ADD ACTIVITY IN BULK FROM CSV file
import pandas as pd

data = pd.read_csv("CSV_DATA.csv")
dates_list = list(data.FormattedDate)
hours_list = list(data.Hours)
data_dict = {dates_list[i]: hours_list[i] for i in range(len(dates_list))}
print(data_dict)
for key in data_dict:
	X_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_PARAM["id"]}/{key}"
	X_PARAM = {
		"quantity": f"{data_dict[key]}",
	}
	modify_activity = requests.put(url=X_ENDPOINT, json=X_PARAM, headers=HEADERS)
	print(modify_activity.text)

# modify_activity = requests.put(url=MODIFY_ENDPOINT, json=MODIFY_PARAM, headers=HEADERS)

