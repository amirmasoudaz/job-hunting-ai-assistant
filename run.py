import asyncio

from modules.hunter import Hunter


if __name__ == "__main__":
    hunter = Hunter(
        user_name="AmirMasoud Azadfar",
        platform="glassdoor",
        renew_descriptions=False,
        batch_process=True)
    asyncio.run(hunter.data.prepare_data())
    asyncio.run(hunter.process_apps())
