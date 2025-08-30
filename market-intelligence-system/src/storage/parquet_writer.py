import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def write_parquet(data: list, path: str):
df = pd.DataFrame(data)
table = pa.Table.from_pandas(df)
pq.write_table(table, path, compression="snappy")