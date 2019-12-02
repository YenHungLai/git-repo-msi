import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.utils.dirsnapshot import DirectorySnapshot

# my_event_handler = LoggingEventHandler()


# def on_deleted():
#     print('hello')


# my_event_handler.on_deleted = on_deleted

# Observer().schedule(my_event_handler,
#                     'C:/Users/Jacob/Desktop/watchdog_practice', recursive=True)

# Observer().start()
# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:  
#     Observer().stop()

# Observer().join()


snapshot = DirectorySnapshot(
    'C:/Users/Jacob/Desktop/watchdog_practice', recursive=True)
print(snapshot)
