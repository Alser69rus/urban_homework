import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял шар {i}")
    print(f"Силач {name} закончил соревнования.")


async def start_tournament(participants):
    tasks = []
    print("Начало турнира")
    for strongman in participants:
        name, power = strongman
        print(f"Заявлен силач {name} мощью в {power} очков.")
        tasks.append(asyncio.create_task(start_strongman(name, power)))
    for task in tasks:
        await task
    print("Турнир завершен.")


if __name__ == "__main__":
    participants = [
        ("Pasha", 3),
        ("Denis", 4),
        ("Apollon", 5),
    ]
    asyncio.run(start_tournament(participants))
