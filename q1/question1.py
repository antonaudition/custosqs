import heapq


# heap seems like a middle of the road solution with nlogn complexity
# for smaller lists it might be faster to sort and loop, depending on underlying representation of the list
def foo(values):
    heapq.heapify(values)
    lowest = 0
    while values:
        head = heapq.heappop(values)
        if head != lowest+1:
            return lowest+1
        lowest = head
    return -1
