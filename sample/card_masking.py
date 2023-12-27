from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
spark = SparkSession.builder.appName("example").getOrCreate()

data = [("1234567891234567","AAA"), ("5678912345671234","BBB"),("9123456712345678","CCC"), ("1234567812341122","DDD"), ("1234567812341342","EEE")]
schema= StructType([ StructField("card_number_user",StringType(),True),
                     StructField("user_name",StringType(),True)])

df_2 = spark.createDataFrame(data = data, schema = schema)


def udf_func(s):
    # new_col = expr("lpad(substring(card_number_user,-4,4), length(card_number_user),'*')")
    # return new_col
    s = s
    l = len(s)
    s1 = len(s[0:l - 4])
    s2 = ""
    for i in range(0, s1):
        s2 = "*" + s2
    s2 = s2 + s[l - 4:l]
    return s2


masking_udf = udf(udf_func, StringType())

# Use the UDF in a DataFrame transformation
df_new = df_2.withColumn("masked_card_number", masking_udf(df_2.card_number_user))

df_new.show()
