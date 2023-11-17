import time, threading

start = time.perf_counter()

def funct():
  print("Sleeping 1 second")
  time.sleep(1)
  print("Done Sleeping")

""" Old Way """
# funct()
# funct()

# Creates a thread. `target=` identifies the function that the tread is running. Don't want to execute the function so omit the `()`
# thread1 = threading.Thread(target=funct)
# thread2 = threading.Thread(target=funct)


"""
  Despite a thread being created, nothing is being done with the threads, therefore the thread needs to be told to start
"""

# Threads being told to start and run their functions
# thread1.start()
# thread2.start()


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
