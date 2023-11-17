# Description:
Program intended to learn the basics of python threading and multiprocessing  

## Notes:
Followed the following videos for practice
 - Threading
   - https://www.youtube.com/watch?v=IEEhzQoKtQU
  9:40

     - Creating and destroying threads comes with overhead cost

 - Multiprocessing
   - https://www.youtube.com/watch?v=fKl2JW_qrso


---

There are 2 kinds of tasks:
 - CPU Bound
   - CPU Bound tasks work best with multiprocessing

   - Works Best when:
     - Running tasks that involve a lot of data crunching
     - Making lots of calculations

 - IO Bound
   - IO Bound tasks work best with threading

   - Works Best when:
     - Running input and output operations that need to be completed
     - Reading/Writing from the file system
     - File system operations
     - Network operations
     - Downloading files

