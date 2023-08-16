import json
import os

from google.cloud import bigquery
from google.oauth2 import service_account


DATA_FOLDER = "data"

# ตัวอย่างการกำหนด Path ของ Keyfile ในแบบที่ใช้ Environment Variable มาช่วย
# จะทำให้เราไม่ต้อง Hardcode Path ของไฟล์ไว้ในโค้ดของเรา
# keyfile = os.environ.get("KEYFILE_PATH")

keyfile = os.environ.get("KEYFILE_PATH")
service_account_info = json.load(open(keyfile))
credentials = service_account.Credentials.from_service_account_info(service_account_info)
project_id = "deb2-395109"
client = bigquery.Client(
    project=project_id,
    credentials=credentials,
)

# Addressess
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
)

data = "addresses"
file_path = f"{DATA_FOLDER}/{data}.csv"
with open(file_path, "rb") as f:
    table_id = f"{project_id}.deb_bootcamp_project.{data}"
    job = client.load_table_from_file(f, table_id, job_config=job_config)
    job.result()

table = client.get_table(table_id)
print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

# ----------

# Events
job_config_partition = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    time_partitioning=bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.DAY,
        field="created_at",
    ),
)

dt = "2021-02-10"
partition = dt.replace("-", "")
data = "events"
file_path = f"{DATA_FOLDER}/{data}.csv"
with open(file_path, "rb") as f:
    table_id = f"{project_id}.deb_bootcamp_project.{data}${partition}"
    job = client.load_table_from_file(f, table_id, job_config=job_config_partition)
    job.result()

table = client.get_table(table_id)
print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

# ถึงตรงนี้เราโหลดข้อมูลไปแล้ว 2 ชุด ยังเหลืออีก 5 ชุดที่ต้องโหลดเพิ่ม
# YOUR CODE HERE

partition_tables = [{"name":"users", "dt": "2020-10-23"}, {"name":"orders", "dt": "2021-02-10"}]
 
for data in partition_tables:
    dt = data["dt"]
    name = data['name']
    partition = dt.replace("-", "")
    file_path = f"{DATA_FOLDER}/{name}.csv"
    with open(file_path, "rb") as f:
        table_id = f"{project_id}.deb_bootcamp_project.{name}${partition}"
        job = client.load_table_from_file(f, table_id, job_config=job_config_partition)
        job.result()

    table = client.get_table(table_id)
    print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

normal_tables = ["order_items", "promos", "products"]
for data in normal_tables:
    file_path = f"{DATA_FOLDER}/{data}.csv"
    with open(file_path, "rb") as f:
        table_id = f"{project_id}.deb_bootcamp_project.{data}"
        job = client.load_table_from_file(f, table_id, job_config=job_config)
        job.result()

    table = client.get_table(table_id)
    print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

