from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

# Initialize Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Sample data and schema
data = [("1234567891234567", "AAA"), ("5678912345671234", "BBB"), ("9123456712345678", "CCC"),
        ("1234567812341122", "DDD"), ("1234567812341342", "EEE")]

schema = StructType([StructField("card_number_user", StringType(), True),
                    StructField("user_name", StringType(), True)])

# Create DataFrame
df_2 = spark.createDataFrame(data=data, schema=schema)

# Show the DataFrame
df_2.show()

df3 = 