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
    schema = "`Id` INT, `First` STRING, `Last` STRING, `Url` STRING, `Published` STRING, `Hits` INT"
    data = [[1, "Jules", "Damji", "https://tinyurl.1", "1/4/2016", 4535], 
             [2, "Brooke","Wenig", "https://tinyurl.2", "5/5/2018", 8908], 
             [3, "Denny", "Lee", "https://tinyurl.3", "6/7/2019", 7659], 
             [4, "Tathagata", "Das", "https://tinyurl.4", "5/12/2018", 10568], 
             [5, "Matei","Zaharia", "https://tinyurl.5", "5/14/2014", 40578], 
             [6, "Reynold", "Xin", "https://tinyurl.6", "3/2/2015", 25568], 
             [7, "Michael", "Armbrust", "https://tinyurl.7", "5/27/2014", 22568], 
             [8, "Dong", "Liang", "https://tinyurl.8", "10/28/2019", 3587], 
             [9, "Wen", "Sheng", "https://tinyurl.9", "10/7/2019", 2259], 
             [10, "Yan", "Wang", "https://tinyurl.10", "12/1/2015", 2856]]
    
    print(data);
    df = spark.createDataFrame(data, schema)
    print(df)
    df.show()
if __name__ == "__main__":
    main()