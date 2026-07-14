import aiosqlite
import config


async def save_message(user_id: int, role: str, message: str):

    async with aiosqlite.connect(config.DATABASE_PATH) as db:

        await db.execute(
            """
            INSERT INTO memory(user_id, role, message)
            VALUES (?, ?, ?)
            """,
            (user_id, role, message),
        )

        await db.commit()


async def get_history(user_id: int):

    async with aiosqlite.connect(config.DATABASE_PATH) as db:

        cursor = await db.execute(
            """
            SELECT role, message
            FROM memory
            WHERE user_id=?
            ORDER BY id DESC
            LIMIT ?
            """,
            (user_id, config.MAX_HISTORY * 2),
        )

        rows = await cursor.fetchall()

    rows.reverse()

    history = []

    for role, message in rows:
        history.append(
            {
                "role": role,
                "content": message,
            }
        )

    return history


async def clear_history(user_id: int):

    async with aiosqlite.connect(config.DATABASE_PATH) as db:

        await db.execute(
            "DELETE FROM memory WHERE user_id=?",
            (user_id,),
        )

        await db.commit()