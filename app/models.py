import time

import ormar

from app.db import metadata, database


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Item(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'items'

    id: int = ormar.Integer(primary_key=True)
    value: str = ormar.String(max_length=500)
    timestamp: int = ormar.Integer(default=time.time())
