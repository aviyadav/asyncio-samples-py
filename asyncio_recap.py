import asyncio
from random import randint
from time import perf_counter

from typing import AsyncIterable

# from req_http import http_get, http_get_sync
from req_http import http_get_sync
from req_http_aio import http_get

MAX_POKEMON = 898

def get_random_pokemon_name_sync() -> str:
    """Get a random Pokémon name synchronously."""
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    return http_get_sync(pokemon_url)["name"]

async def get_random_pokemon_name() -> str:
    """Get a random Pokémon name asynchronously."""
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    return (await http_get(pokemon_url))["name"]

async def next_pokemon(total: int) -> AsyncIterable[str]:
    """Asynchronous generator to yield Pokémon names."""
    for _ in range(total):
        name = await get_random_pokemon_name()
        yield name


def main1() -> None:
    time_start = perf_counter()

    for _ in range(20):
        pokemon_name = get_random_pokemon_name_sync()
        print(f"Random Pokémon (sync): {pokemon_name}")
    time_end = perf_counter()
    print(f"Time taken (sync): {time_end - time_start:.2f} seconds")

async def main2() -> None:
    time_start = perf_counter()

    names = [name async for name in next_pokemon(20)]
    print("Random Pokémon (async generator):")
    for name in names:
        print(f" - {name}")

    # async for name in next_pokemon(20):
    #     print(f"Random Pokémon (async generator): {name}")


    # for _ in range(20):
    #     pokemon_name = await get_random_pokemon_name()
    #     print(f"Random Pokémon (async): {pokemon_name}")

    time_end = perf_counter()
    print(f"Time taken (async non parallel ): {time_end - time_start:.2f} seconds")

async def main3() -> None:
    time_start = perf_counter()
    result = await asyncio.gather(
        *[get_random_pokemon_name() for _ in range(20)]
        )
    print("Random Pokémon (async gather):")
    for pokemon_name in result:
        print(f" - {pokemon_name}")
    time_end = perf_counter()
    print(f"Time taken (async ): {time_end - time_start:.2f} seconds")


if __name__ == "__main__":
    # main1()
    asyncio.run(main2())
    asyncio.run(main3())
