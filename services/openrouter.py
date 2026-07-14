import base64
import httpx
import config


async def ask_ai(messages):

    headers = {
        "Authorization": f"Bearer {config.OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/",
        "X-Title": "RohitAI"
    }

    system_prompt = {
        "role": "system",
        "content": """
You are RohitAI, an intelligent AI assistant similar to ChatGPT.

Rules:
- Reply in user's language.
- Hindi → Hindi
- Hinglish → Hinglish
- English → English
- Marathi → Marathi

- Use emojis naturally 😊🔥🚀❤️
- Don't overuse emojis.
- Explain coding answers step by step.
- Format code using markdown.
- Be friendly.
- Give complete answers.
"""
    }

    payload = {
        "model": config.MODEL,
        "messages": [system_prompt] + messages,
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

    except httpx.HTTPStatusError as e:

        return f"❌ API Error ({e.response.status_code})\n{e.response.text}"

    except httpx.ReadTimeout:

        return "⏳ AI response aane me time lag raha hai."

    except Exception as e:

        return f"❌ Error:\n{str(e)}"


# ===========================
# IMAGE ANALYSIS
# ===========================

async def ask_image(
    image_path,
    prompt="Describe this image in detail."
):

    with open(image_path, "rb") as f:
        image_base64 = base64.b64encode(
            f.read()
        ).decode()

    headers = {
        "Authorization": f"Bearer {config.OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/",
        "X-Title": "RohitAI"
    }

    payload = {

        "model": config.MODEL,

        "messages": [

            {

                "role": "user",

                "content": [

                    {
                        "type": "text",
                        "text": prompt
                    },

                    {
                        "type": "image_url",
                        "image_url": {
                            "url":
                            f"data:image/jpeg;base64,{image_base64}"
                        }
                    }

                ]

            }

        ],

        "max_tokens": config.MAX_TOKENS

    }

    try:

        async with httpx.AsyncClient(
            timeout=config.REQUEST_TIMEOUT
        ) as client:

            response =
