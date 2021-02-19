import time
from datetime import datetime

def timeTo(func):
    def wrapper(*args, **kwargs):
        a = datetime.now()
        func(*args, **kwargs)
        b = datetime.now()
        print(b-a)
    return wrapper


@timeTo
def waiter():
    cook('паста', 8)
    cook('цезар', 3)
    cook('котлєта', 16)


def cook(order, timer):
    print(f'Новий заказ {order}')
    time.sleep(timer)  # синхронна функція має бути замінена на асинхронну!
    print(f'{order} - готовий')


waiter()
