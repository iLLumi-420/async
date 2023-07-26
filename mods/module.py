import asyncio
import aiohttp
import time




url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey=GZU5N3ZE942VPFBM'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT','AAPL', 'GOOG', 'TSLA', 'MSFT','AAPL', 'GOOG', 'TSLA', 'MSFT',]

results = []

start = time.time()

def get_tasks(session):
    tasks = []
    for symbol in symbols:
        tasks.append(session.get(url.format(symbol)))
    return tasks

async def get_data():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)

        for response in responses:
            results.append(await response.json())


asyncio.run(get_data())

end = time.time()
total = end-start

print(f'It took {total} time to get the results')


