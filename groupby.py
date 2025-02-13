import os
import sys
from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession
from pyspark.sql.functions import count

def create_spark_session():
    return SparkSession.builder \
        .appName("ParquetReader") \
        .master("local[*]") \
        .getOrCreate()

def main():
    spark = create_spark_session()
    csv_file = os.path.join("data", "268_Configuration.csv") 
    df = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load(csv_file)
    
    grouped_df = df.select("ConfigurationId", "RawValue", "Active") \
        .filter(df.Active == 1) \
        .groupBy("ConfigurationId") \
        .agg(count("RawValue").alias("Total")) \
        .orderBy("Total", ascending=False)

    grouped_df.show(n=10, truncate=True)
    print("Total Rows = %d" % grouped_df.count())
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