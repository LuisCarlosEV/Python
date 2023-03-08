import asyncio

async def main():
    print("Hello...")
    await asyncio.sleep(5)
    print("... World!!!")

async def func1():
    for i in range(11):
        print(i)

print("Inicio")
asyncio.run(main())
asyncio.run(func1())
print("Fin")