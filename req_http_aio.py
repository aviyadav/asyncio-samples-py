import aiohttp

JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]

async def http_get(url: str) -> JSONObject:
    """Perform an asynchronous HTTP GET request and return the JSON response."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()  # Raise an error for bad responses
            return await response.json()