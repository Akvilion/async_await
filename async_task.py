import time
from datetime import datetime
import asyncio


def timeTo(func):
    async def wrapper(*args, **kwargs):
        a = datetime.now()
        await func(*args, **kwargs)
        b = datetime.now()
        print(b-a)
    return wrapper


@timeTo
async def waiter():

    # taskers дозволяють запускати завдання одночасно і чекати відповіді

    task1 = asyncio.create_task(cook('паста', 8))  
    task2 = asyncio.create_task(cook('цезар', 3))
    task3 = asyncio.create_task(cook('котлєта', 16))

    await task1
    await task2
    await task3


async def cook(order, timer):
    print(f'Новий заказ {order}')
    await asyncio.sleep(timer)
    print(f'{order} - готовий')


asyncio.run(waiter())
