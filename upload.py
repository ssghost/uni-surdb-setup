from surrealdb import Surreal
import pandas as pd
import asyncio

async def upload():
    df = pd.read_parquet("./uniswap_v3_pools.parquet").to_json()
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("uniswap", "uniswap")
        await db.delete("uniswap_v3_pools")
        await db.create("uniswap_v3_pools", df)

if __name__ == "__main__":
    asyncio.run(upload())
