from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
spark = SparkSession.builder.appName("example").getOrCreate()

json_data = '{"ID": 2,"Name":"Dhuruvan"kumar","city":"Hyd"}'
data = [(101,json_data)]
schema = ['col1','col2']
customers_df = spark.createDataFrame(data , schema)
customers_df.show(truncate=False)

df_new1 = customers_df.withColumn("id",split(customers_df.col2,',').getItem(0) ).withColumn("name",split(customers_df.col2,',').getItem(1) ).withColumn("city",split(customers_df.col2,',').getItem(2) ).drop(col("_corrupt_record"))

df_new2 = df_new1.withColumn("id",split(df_new1.id,':').getItem(1)).withColumn("name",split(df_new1.name,':').getItem(1)).withColumn("city",regexp_replace(split(df_new1.city,':').getItem(1), '}', ''))

df_new2 = df_new2.withColumn("name",trim(regexp_replace("name",'"',' '))).withColumn("city",regexp_replace("city",'"',' ')).drop("col2")
df_new2 = df_new2.withColumnRenamed("col1","dept_id")
df_new2.show(truncate=False)