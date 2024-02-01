from surrealdb import Surreal
import pandas as pd
import asyncio

def dec_utf(x):
    return x.decode('utf-8')
    
async def upload_parq():
    for i in range(9):    
        df = pd.read_parquet(f"./uniswap_v3_pools_{str(i)}.parquet")
        df["event__pool"].apply(dec_utf)
        df.to_json(default_handler=str)
        async with Surreal("ws://localhost:8000/rpc") as db:
            await db.signin({"user": "root", "pass": "root"})
            await db.use("uniswap", "uniswap")
            await db.delete("uniswap_v3_pools_{str(i)}")
            await db.create(df)

async def upload_json():
    for i in range(9):
        with open(f"./uniswap_v3_pools_{str(i)}.json") as f:
            df = f.read()
        async with Surreal("ws://localhost:8000/rpc") as db:
            await db.signin({"user": "root", "pass": "root"})
            await db.use("uniswap", "uniswap")
            await db.delete("uniswap_v3_pools_{str(i)}")
            await db.create(df)

if __name__ == "__main__":
    asyncio.run(upload_parq())
    asyncio.run(upload_json())
