import asyncio
import requests

JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]

def http_get_sync(url: str) -> JSONObject:
    """Perform a synchronous HTTP GET request and return the JSON response."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

async def http_get(url: str) -> JSONObject:
    """Perform an asynchronous HTTP GET request and return the JSON response."""
    return await asyncio.to_thread(http_get_sync, url)