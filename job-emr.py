from pyspark.sql.functions import mean, min, max, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

#Ler os dados do Enem 2020
enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-natalia/raw-data/enem/")
    
)    

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://datalake-natalia/staging/enem")
)