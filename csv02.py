import os
from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession

def create_spark_session():
    return SparkSession.builder \
        .appName("ParquetReader") \
        .master("local[*]") \
        .getOrCreate()

def main():
    spark = create_spark_session()
    csv_file = os.path.join("data", "268_Configuration.csv")
    log_df = spark.read.csv(header=True, inferSchema=True, path=csv_file)
    log_df.show(5)
    spark.stop()

if __name__ == "__main__":
    main()