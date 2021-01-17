import asyncio

from arsenic import get_session
from arsenic.browsers import Firefox
from arsenic.services import Geckodriver


async def example():
    async with get_session(Geckodriver(), Firefox()) as session:
        await session.get('https://github.com/hde/arsenic')
        # wait up 5 seconds for `strong` tag
        strong = await session.wait_for_element(5, 'strong')
        print(await strong.get_text())


if __name__ == '__main__':
    asyncio.run(example())