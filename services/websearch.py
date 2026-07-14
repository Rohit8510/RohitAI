from duckduckgo_search import DDGS


async def web_search(query: str):

    try:

        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    query,
                    max_results=5
                )
            )

        if not results:
            return "No results found."

        text = "🌐 Internet Search Results:\n\n"

        for i, item in enumerate(results, start=1):

            text += (
                f"{i}. {item['title']}\n"
                f"{item['body']}\n"
                f"{item['href']}\n\n"
            )

        return text

    except Exception as e:

        return f"❌ Search Error:\n{str(e)}"
