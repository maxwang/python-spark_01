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
    # notes have to use hive support when saving data to disk
    spark = create_spark_session()
    databases = [row for row in spark.sql("SHOW DATABASES").collect()]
    print(databases)
    spark.catalog.setCurrentDatabase("auditlog")
    spark.sql("SELECT Database, Id, TableName, RecordId FROM auditlog.ps_audit LIMIT 50").show()
    spark.stop() 

if __name__ == "__main__":
    main()