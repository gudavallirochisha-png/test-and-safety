from typing import Any, Dict, List, Optional
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase
from backend.app.database.connection import get_database


class BaseRepository:
    def __init__(self, collection_name: str, db: Optional[AsyncIOMotorDatabase] = None):
        self.collection_name = collection_name
        self._db = db

    @property
    def collection(self) -> AsyncIOMotorCollection:
        database = self._db if self._db is not None else get_database()
        return database[self.collection_name]

    async def insert(self, document: Dict[str, Any]) -> Dict[str, Any]:
        result = await self.collection.insert_one(document)
        document["_id"] = str(result.inserted_id)
        return document

    async def find_one(self, query: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        doc = await self.collection.find_one(query)
        if doc and "_id" in doc:
            doc["_id"] = str(doc["_id"])
        return doc

    async def find_all(
        self,
        query: Dict[str, Any] = None,
        sort_by: str = "created_at",
        ascending: bool = False,
        page: int = 1,
        limit: int = 50,
    ) -> List[Dict[str, Any]]:
        if query is None:
            query = {}

        skip = (page - 1) * limit
        order = 1 if ascending else -1
        cursor = self.collection.find(query).sort(sort_by, order).skip(skip).limit(limit)

        docs = []
        async for doc in cursor:
            if "_id" in doc:
                doc["_id"] = str(doc["_id"])
            docs.append(doc)
        return docs

    async def count(self, query: Dict[str, Any] = None) -> int:
        if query is None:
            query = {}
        return await self.collection.count_documents(query)

    async def update_one(self, query: Dict[str, Any], update_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        result = await self.collection.update_one(query, {"$set": update_data})
        if result.modified_count > 0 or result.matched_count > 0:
            return await self.find_one(query)
        return None

    async def delete_one(self, query: Dict[str, Any]) -> bool:
        result = await self.collection.delete_one(query)
        return result.deleted_count > 0
