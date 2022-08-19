### main.py
if you want to run the code continuously even after the board is reset then place your code in the main.py. the board will always automatically 
run this code if it is present on the board.

_______________________________________________

### deepsleep and motion examples
these are examples. you can copy them to your board and then use REPL to import either one to start it. it will run until the board is reset. after which you would need to import the code again to make it run. the deepsleep will only make one loop as once its gone into deepsleep, its effectively reset itself and therefor the code would need imported again. 