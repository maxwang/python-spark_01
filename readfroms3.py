import os
import sys
from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession
from pyspark.sql.functions import count

def create_spark_session():
    return SparkSession.builder \
        .appName("ParquetReader") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.profile.ProfileCredentialsProvider") \
        .config("spark.hadoop.fs.s3a.aws.profile", "AdaxProd") \
        .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com") \
        .config("spark.sql.warehouse.dir", "s3a://adax-prod-rds/") \
        .enableHiveSupport() \
        .getOrCreate()

def main():
    spark = create_spark_session()
    df = spark.read.parquet("s3a://adax-prod-rds/AuditLogs/DBAuditTrail-PARQUET/adax-app-env-propertyshares.adaxonline.com/Configuration_AdaxObjects/2024/8/12/AuditLog_1_57088b42-9b1f-4d02-b866-1ee69d13e65a.parquet")
    df.show(5)

if __name__ == "__main__":
    main()