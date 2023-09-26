from heapq import heappush, heappop

def heap_sort(data: list[int]) -> list [int]:
    heap: list[int] = []
    for elem in data:
        heappush(heap,elem)
    result: list[int] = []
    while heap:
        result.append(heappop(heap))
    return result


if __name__ == '__main__':
    print(heap_sort([1,7,5,8,9,7,5,4,6,2]))