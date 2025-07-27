from qdrant_client import AsyncQdrantClient
from qdrant_client.http import models
import asyncio

# async create collection

async def create_collection():
    client = AsyncQdrantClient("localhost", port=6333)

    # Create a collection
    await client.create_collection(
        collection_name="async_collection_3",
        vectors_config=models.VectorParams(size=4,
                                           distance=models.Distance.EUCLID),
    )

    print(await client.get_collections())

# Run the code

asyncio.run(create_collection())