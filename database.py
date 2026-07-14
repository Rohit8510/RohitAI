import os
import aiosqlite
import config


CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


async def init_database():

    os.makedirs("data", exist_ok=True)

    async with aiosqlite.connect(config.DATABASE_PATH) as db:

        await db.execute(CREATE_TABLE)

        await db.commit()