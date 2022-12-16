import argparse
import asyncio
from collections import Counter

import aiohttp


async def main(args):
    session = aiohttp.ClientSession()
    try:
        links = Counter()
        display(links)
    finally:
        await session.close()


def display(links):
    for url, count in links.most_common():
        print(f"{count:>3} {url}")