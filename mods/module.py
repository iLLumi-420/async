import asyncio
import aiohttp
import time




url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey=GZU5N3ZE942VPFBM'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT','AAPL', 'GOOG', 'TSLA', 'MSFT','AAPL', 'GOOG', 'TSLA', 'MSFT',]

results = {}

start = time.time()

def get_tasks(session):
    tasks = {}
    for symbol in symbols:
        tasks[symbol] = asyncio.create_task(session.get(url.format(symbol)))
    return tasks

async def get_data():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)

        completed, pending = await asyncio.wait(tasks.values())

        for symbol, task in tasks.items():
            if task in completed:
                try:
                    response = await task
                    result = await response.json()
                    results[symbol] = result

                except Exception as e:
                    print(f'Error for symbol {symbol}: {e}')

            else:
                print(f'Task for symbol {symbol} did not finish')
        
        for task in pending:
            task.cancel()
        



asyncio.run(get_data())

end = time.time()
total = end-start

print(f'It took {total} time to get the results')




