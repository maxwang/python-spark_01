import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

# Load the customers.csv dataset
data_df = spark.createDataFrame([("Brooke", 20), ("Denny", 31), ("Jules", 30), ("TD", 35), ("Brooke", 25)], ["name", "age"])

avg_df = data_df.groupBy("name").agg(avg("age"))

# Show the first few rows of the DataFrame
print(avg_df)

# below line does not work, throw the exception, with 
# avg_df.show(5)

# def create_spark_session():
#     return SparkSession.builder \
#         .appName("ParquetReader") \
#         .master("local[*]") \
#         .config("spark.python.worker.reuse", "false") \
#         .getOrCreate()

# def main():
#     spark = create_spark_session()

#     data_df = spark.createDataFrame([("Brooke", 20), ("Denny", 31), ("Jules", 30), ("TD", 35), ("Brooke", 25)], ["name", "age"])

#     avg_df = data_df.groupBy("name").agg(avg("age"))

#     display(avg_df)

#     # for row in avg_df.collect():
#     #     print(row)
#     # avg_df.show()

#     # spark.stop()

# if __name__ == "__main__":
#     main()

