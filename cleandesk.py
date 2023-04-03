from pathlib import Path  # python library for handling files and paths on operating system
from time import sleep

#  watchdog is a library that is a cross-platform API to monitor file system events
from watchdog.observers import Observer

from desktop_cleaner.EventHandler import EventHandler

if __name__ == '__main__':
    watch_path = Path.home() / 'Downloads'
    destination_root = Path.home() / 'Downloads' / 'Principal Shelf'
    event_handler = EventHandler(watch_path=watch_path, destination_root=destination_root)

    observer = Observer()
    observer.schedule(event_handler, f'{watch_path}', recursive=True)
    observer.start()

    try:
        while True:
            sleep(60)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
