from fastapi import FastAPI
import pandas as pd


app = FastAPI()

@app.get("/ping")
def ping():
return {"status": "ok"}


@app.get("/sample")
def sample():
df = pd.read_parquet("data/sample/tweets_sample.parquet")
return df.head(5).to_dict(orient="records")