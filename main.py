import os
from pyspark.sql import SparkSession

def create_spark_session():
    return SparkSession.builder \
        .appName("ParquetReader") \
        .master("local[*]") \
        .getOrCreate()

def load_parquet_file(spark, file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return spark.read.parquet(file_path)

def push_to_spark(df, spark_table):
    print("Pushing to Spark")
    df.createOrReplaceTempView(spark_table)
    # teenagers = spark.sql("SELECT name FROM parquetFile WHERE age >= 13 AND age <= 19")
    # teenagers.show()


def main():
    SPARK_MASTER_URL = "spark://172.24.0.2:7077" 
    SPARK_TABLE = "my_table"
    spark = create_spark_session()

    # Update with the correct path to your Parquet file
    file_path = os.path.join("data", "AuditLog.parquet")

    try:
        df = load_parquet_file(spark, file_path)
        df.show(5)  # Show sample data
        df.printSchema()  # Print schema
        # print(f"Total Rows: {df.count()}")  # Count rows
        push_to_spark(df, SPARK_TABLE)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        spark.stop()  # Stop Spark session

if __name__ == "__main__":
    main()
