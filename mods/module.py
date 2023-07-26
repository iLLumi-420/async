import asyncio
import aiohttp
import time




url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey=GZU5N3ZE942VPFBM'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT']

results = []

start = time.time()

async def get_data():
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            print(f'Gettig data for symbol {symbol}')
            response = await session.get(url.format(symbol))
            results.append(await response.json())


asyncio.run(get_data())

for result in results:
    print(result)

end = time.time()
total = end-start

print(f'It took {total} time to get the results')


