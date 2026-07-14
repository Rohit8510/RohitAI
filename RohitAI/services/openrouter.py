import httpx
import config


async def ask_ai(messages):

    headers = {
        "Authorization": f"Bearer {config.OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/",
        "X-Title": "RohitAI"
    }

    payload = {
        "model": config.MODEL,
        "messages": messages,
        "temperature": config.TEMPERATURE,
        "max_tokens": config.MAX_TOKENS
    }

    try:

        async with httpx.AsyncClient(
            timeout=config.REQUEST_TIMEOUT
        ) as client:

            response = await client.post(
                config.OPENROUTER_URL,
                headers=headers,
                json=payload
            )

            response.raise_for_status()

            data = response.json()

            return data["choices"][0]["message"]["content"]

    except Exception as e:

        return f"❌ Error:\n{str(e)}"