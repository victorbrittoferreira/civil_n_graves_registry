import asyncio

async def say(what, when):
    await asyncio.sleep(when)
    print(what)
    if when == 5:
       loop = asyncio.get_event_loop()
       loop.stop()

loop =  asyncio.new_event_loop()
for i in range(5, -1, -1):
    loop.create_task(say(f'hello world {i}', i))
    print(f"co-rotina {i} criada")
loop.run_forever()
loop.close()