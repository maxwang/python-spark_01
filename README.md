# PySpark Parquet Demo

## Overview
This project demonstrates how to use Python with Apache Spark to process data stored in Apache Parquet format. It covers setting up PySpark, reading and writing Parquet files, and performing basic transformations.

## Prerequisites
Ensure you have the following installed:
- Python 3.7+
- Apache Spark (>= 3.0)
- Java (>= 8, required for Spark)
- pip and virtualenv (recommended for dependency management)

## Installation

* 1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/pyspark-parquet-demo.git
   cd pyspark-parquet-demo
   ```
* 2. Set up a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
   pip install -r requirements.txt
   ```
* 3. Ensure `SPARK_HOME` is set properly:
   ```sh
   export SPARK_HOME=/path/to/spark
   export PATH=$SPARK_HOME/bin:$PATH
   ```

* 4. Windows settings for HADOOP

    * 4.1 clone this repo: `https://github.com/cdarlint/winutils`
    * 4.2 Set HADOOP_HOME environment variable to the root path of your version
    * 4.3 Add to the PATH environment variable, %HADOOP_HOME%\bin
