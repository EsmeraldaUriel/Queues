from queues2 import Queue

fifo = Queue("1st", "2nd", "3rd")
print("In line: ", len(fifo))

for element in fifo:
    print(element)

print("In line: ", len(fifo))