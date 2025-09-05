import dlt

#Products Expectations

products_expectations = {
    "rule_1" : "product_id is not null",
    "rule_2" : "price >= 0"
}

#Inggesting products
@dlt.table(
    name = 'products_stg'
)
@dlt.expect_all(products_expectations)
def products_stg():
    df = spark.readStream.table("dltprac.source.products")
    return df
