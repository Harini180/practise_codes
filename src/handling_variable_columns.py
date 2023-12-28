from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
spark = SparkSession.builder.appName("example").getOrCreate()

df = spark.read.text("../resource/employee_sample.text")
df_new = df.withColumn("value",split("value",','))
df1 = df_new.select("value",size("value"))
max_column_value = df1.select(max(size("value"))).collect()[0][0]
for i in range(max_column_value):
    df1 = df1.withColumn("col"+str(i),df1['value'][i])
df1 = df1.drop("value","size(value)")
df1.show()