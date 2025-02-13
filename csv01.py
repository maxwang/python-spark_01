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
    log_df = spark.read.text(csv_file).repartition(8)
    print(log_df.rdd.getNumPartitions())
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