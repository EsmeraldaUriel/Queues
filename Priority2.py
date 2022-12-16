from heapq import heappush
from heapq import heappop

fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

heappop(fruits)

print("The basket now Contains: ", fruits)
# As you can see the apple is removed and the remaining fruits is shuffled
