import boto3
import pandas as pd

#criar um cliente para interagir com o amazon s3
s3_client = boto3.client('s3')

s3_client.upload_file("raw-data/MICRODADOS_ENEM_2020.txt",
                        "datalake-natalia",
                        "raw-data/consumer-zone/MICRODADOS_ENEM_2020.csv")