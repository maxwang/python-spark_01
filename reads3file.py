import os
import sys
import boto3
from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession
from pyspark.sql.functions import count

def create_spark_session():
    return SparkSession.builder \
        .appName("ParquetReader") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.profile.ProfileCredentialsProvider") \
        .config("spark.hadoop.fs.s3a.aws.profile", "AdaxProd") \
        .getOrCreate()

def main():
    AWS_PROFILE = "AdaxProd"  
    BUCKET_NAME = "adax-prod-rds"
    S3_PARQUET_PATH = "/AuditLogs/DBAuditTrail-PARQUET/adax-app-env-propertyshares.adaxonline.com/Configuration_AdaxObjects/2024/8/12/AuditLog_1_57088b42-9b1f-4d02-b866-1ee69d13e65a.parquet"  # Path in S3
    LOCAL_PARQUET_PATH = "/tmp/sample.parquet"  # Local storage path

    
    spark = create_spark_session()
    df = spark.read.parquet("s3a://adax-prod-rds/AuditLogs/DBAuditTrail-PARQUET/adax-app-env-propertyshares.adaxonline.com/Configuration_AdaxObjects/2024/8/12/AuditLog_1_57088b42-9b1f-4d02-b866-1ee69d13e65a.parquet")
    df.show()

if __name__ == "__main__":
    main()