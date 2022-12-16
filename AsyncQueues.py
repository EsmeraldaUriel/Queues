import argparse
import asyncio
from collections import Counter
from urllib.parse import urljoin
from bs4 import BeautifulSoup

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


if __name__ == "__main__":
    asyncio.run(main(parse_args()))


async def fetch_html(session, url):
    async with session.get(url) as response:
        if response.ok and response.content_type == "text/html":
            return await response.text()