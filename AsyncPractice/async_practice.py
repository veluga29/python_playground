import time
import asyncio

#1. Synchronous Programming
# def main():
#     print('time')
#     foo('text')
#     print('finished')


# def foo(text):
#     print(text)
#     time.sleep(2)
    
# main()
#2. Asynchronous Programming
# Asyncio, Coroutine = async, await

async def main():
    print('time')
    task = asyncio.create_task(foo('test'))
    await asyncio.sleep(0.5)
    print('finished')
    await asyncio.sleep(1)
    
async def foo(text):
    await asyncio.sleep(1)
    print(text)
    await asyncio.sleep(1)
    print(text)
    
asyncio.run(main()) 


#
# time
# finished
# test


