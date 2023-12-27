from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

data = [(1,"2023-12-06"),(2,None),(3,"2023-12-06"),(None,"2023-12-06"),(None, None)]
spark = SparkSession.builder.appName("example").getOrCreate()
df_x = spark.createDataFrame(data = data, schema = ("id","value"))
df1 = df_x.withColumn("new_value",coalesce(df_x.value,df_x.id,lit("default_value")))

df1.show()