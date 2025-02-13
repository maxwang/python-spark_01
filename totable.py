import os
import sys
from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession
from pyspark.sql.functions import count

def create_spark_session():
    return SparkSession.builder \
        .appName("ParquetReader") \
        .enableHiveSupport() \
        .master("local[*]") \
        .getOrCreate()

def main():
    spark = create_spark_session()
    
    spark.sql("CREATE DATABASE IF NOT EXISTS auditlog LOCATION '/opt/bitnami/spark/data/auditlog'")
    spark.sql("USE auditlog")

    if not os.path.exists('data/') or not any(fname.endswith('.parquet') for fname in os.listdir('data/')):
        print("Error: 'data/' directory does not exist or contains no Parquet files.")
        return

    df = spark.read.parquet("data/*.parquet")
    df.createOrReplaceTempView("temp_ps_audit")
    schema = df.schema

    df.printSchema() 

    spark.sql(f"""
        CREATE TABLE IF NOT EXISTS ps_audit ({', '.join([f'{field.name} {field.dataType.simpleString()}' for field in schema])})
        USING PARQUET
        LOCATION 'data/'
    """)

    df = spark.read.parquet("data/*.parquet")
    df.write.mode("append").saveAsTable("auditlog.ps_audit")
    spark.sql("SELECT COUNT(*) FROM auditlog.ps_audit").show()

    spark.stop()


    # training = spark.read.csv(csv_file)
    # test = spark.read.csv(csv_file)
    # Load training data
    # lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)
    # Fit the model
    # lrModel = lr.fit(training)
    # Predict
    # lrModel.transform(test)

if __name__ == "__main__":
    main()