from os.path import expanduser, join, abspath

from pyspark.sql import SparkSession
from pyspark import HiveContext, SQLContext
from pyspark.sql import Row

# warehouse_location points to the default location for managed databases and tables
warehouse_location = abspath('spark-warehouse')

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL Hive integration example") \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport() \
    .getOrCreate()

sc = spark.sparkContext
hiveContext = HiveContext(sc)
hiveContext.sql("CREATE TABLE IF NOT EXISTS src (key INT, value STRING) USING hive")
print ("Create Table")
hiveContext.sql("INSERT INTO src VALUES (1, '1'), (2, '2'), (3, '3'), (4, '1'), (5, '2'), (6, '3'), (7, '1'), (8, '2'), (9, '3'), (10, '1')")
hiveContext.sql("INSERT INTO src VALUES (11, '2'), (12, '3'), (13, '1'), (14, '2'), (15, '3'), (16, '1'), (17, '2'), (18, '3'), (19, '1'), (20, '2')")
print ("Insert Into Table")