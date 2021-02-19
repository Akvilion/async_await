import time
from datetime import datetime
import asyncio


def timeTo(func):
    async  def wrapper(*args, **kwargs):
        a = datetime.now()
        await func(*args, **kwargs)
        b = datetime.now()
        print(b-a)
    return wrapper


@timeTo
async def waiter():
    await cook('паста', 8)
    await cook('цезар', 3)
    await cook('котлєта', 16)


async def cook(order, timer):
    print(f'Новий заказ {order}')
    await asyncio.sleep(timer)  # асинхронна функція
    print(f'{order} - готовий')


asyncio.run(waiter())
