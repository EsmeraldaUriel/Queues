import argparse
import asyncio
from collections import Counter
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import sys
from typing import NamedTuple

import aiohttp


class Job(NamedTuple):
    url: str
    depth: int = 1


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


def parse_links(url, html):
    soup = BeautifulSoup(html, features="html.parser")
    for anchor in soup.select("a[href]"):
        href = anchor.get("href").lower()
        if not href.startswith("javascript:"):
            yield urljoin(url, href)




