# import dlt

# #Create Streaming table

# @dlt.table(
#     name = 'first_stream_table'
# )

# def first_stream_table():

#     df = spark.readStream.table('dltprac.source.orders')
#     return df


# #Create Materialized View

# @dlt.table(
#     name = 'first_mat_table'
# )

# def first_mat_table():
#     df = spark.read.table('dltprac.source.orders')
#     return df


# #Create Batch View

# @dlt.view(
#     name = 'first_batch_view'
# )
# def first_batch_view():
#     df = spark.read.table('dltprac.source.orders')
#     return df

# #Create Streaming View

# @dlt.view(
#     name = 'first_stream_view'
# )
# def first_stream_view():
#     df = spark.readStream.table('dltprac.source.orders')
#     return df


