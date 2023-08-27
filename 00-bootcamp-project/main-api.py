import configparser
import csv

import requests


parser = configparser.ConfigParser()
parser.read("pipeline.conf")
host = parser.get("api_config", "host")
port = parser.get("api_config", "port")

API_URL = f"http://{host}:{port}"
DATA_FOLDER = "data"

tables = ["events", "users", "orders"]
dates = ["2021-02-10", "2020-10-23", "2021-02-10"]

for table, date in zip(tables, dates):
    response = requests.get(f"{API_URL}/{table}/?created_at={date}")
    data = response.json()
    with open(f"{DATA_FOLDER}/{table}.csv", "w") as f:
        writer = csv.writer(f)
        header = data[0].keys()
        writer.writerow(header)

        for each in data:
            writer.writerow(each.values())


# # ลองดึงข้อมูลจาก API เส้น users และเขียนลงไฟล์ CSV
# # YOUR CODE HERE
# response = requests.get(f"{API_URL}/{data}/?created_at={date}")
# data = response.json()
# with open(f"{DATA_FOLDER}/users.csv", "w")  as f:
#     writer = csv.writer(f)
#     header = data[0].keys()
#     writer.writerow(header)

#     for each in data:
#         writer.writerow(each.values())


# # ลองดึงข้อมูลจาก API เส้น orders และเขียนลงไฟล์ CSV
# # YOUR CODE HERE
# response = requests.get(f"{API_URL}/{data}/?created_at={date}")
# data = response.json()
# with open(f"{DATA_FOLDER}/orders.csv", "w")  as f:
#     writer = csv.writer(f)
#     header = data[0].keys()
#     writer.writerow(header)

#     for each in data:
#         writer.writerow(each.values())