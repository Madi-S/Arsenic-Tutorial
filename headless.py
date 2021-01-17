import asyncio

from arsenic import get_session
from arsenic import services
from arsenic import browsers

service = services.Chromedriver()
browser = browsers.Chrome(chromeOptions={
    'args': ['--headless', '--disable-gpu']
})

async def main():
    async with get_session(service, browser) as session:
        r = await session.get('https://arsenic.readthedocs.io/en/latest/reference/supported-browsers.html#headless-firefox')
        print(r)


if __name__ == '__main__':
    asyncio.run(main())