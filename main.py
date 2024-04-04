import asyncio
import signal
from logic.main import run
from server.game import serve


async def main():
    stop_event = asyncio.Event()
    event_queue = asyncio.Queue()

    game_server = asyncio.create_task(serve(stop_event, event_queue))
    game_driver = asyncio.create_task(run(stop_event, event_queue))

    loop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, stop_event.set)
    loop.add_signal_handler(signal.SIGTERM, stop_event.set)

    await asyncio.gather(game_driver, game_server)


if __name__ == "__main__":
    asyncio.run(main())


