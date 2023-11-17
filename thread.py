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
thread1 = threading.Thread(target=funct)
thread2 = threading.Thread(target=funct)


"""
  Despite a thread being created, nothing is being done with the threads, therefore the thread needs to be told to start
"""

# Threads being told to start and run their functions
thread1.start()
thread2.start()

"""
  Without anything else, the program will stop the timer as the program continues after the treads start
  Output:
    Sleeping 1 second
    Sleeping 1 second
    Finished in 0.0 second(s) <- Incorrect location
    Done Sleeping
    Done Sleeping

  To ensure that the current threads finish before the rest of the code gets executed, the join() method is used
"""

# join() method forces threads to finish before continuing
thread1.join()
thread2.join()

"""
  With join(), program now runs correctly:
  Output:
    Sleeping 1 second
    Sleeping 1 second
    Done Sleeping
    Done Sleeping
    Finished in 1.0 second(s)
"""


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
