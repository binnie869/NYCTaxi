import brewery
from brewery import ds
import sys

sources = [
    {"file": "trip_data_12.csv",
     "fields": ["medallion", "hack_license", "vendor_id", "rate_code", \
                    "pickup_datetime", "dropoff_datetime", "passenger_count", \
                        "trip_time_in_secs", "trip_distance", "pickup_longitude", \
                            "pickup_latitude", "dropoff_longitude", "dropoff_latitude" ]},
    {"file": "trip_fare_12.csv",
     "fields": ["medallion", "hack_license", "vendor_id", "pickup_datetime", "payment_type", \
                    "fare_amount", "surcharge", "mta_tax", "tip_amount", "tolls_amount", \
                         "total_amount"]}
]

out = ds.CSVDataTarget("merged.csv")
out.fields = brewery.FieldList(all_fields)
out.initialize()

for source in sources:

    path = source["file"]

# Initialize data source: skip reading of headers
# use XLSDataSource for XLS files
# We ignore the fields in the header, because we have set-up fields
# previously. We need to skip the header row.

    src = ds.CSVDataSource(path,read_header=False,skip_rows=1)

    src.fields = ds.FieldList(source["fields"])

    src.initialize()


    for record in src.records():

   # Add file reference into ouput - to know where the row comes from
        record["file"] = path
        out.append(record)

# Close the source stream

src.finalize()
