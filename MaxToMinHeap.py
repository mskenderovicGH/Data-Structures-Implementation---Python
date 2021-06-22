# this function will convert max heap to min heap

def maxtomin(heap):
    parents = (len(heap)-2)//2
    for i in range(parents+1):
        if heap[2 * i + 1] < heap [i]:
            heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]

        if (2 * i + 2) < len(heap) and heap[2 * i + 2] < heap[i]:
            heap[i], heap[2 * i + 2] = heap[2 * i + 2], heap[i]

if __name__ == '__main__':
    niz=[210, 100, 23, 2, 5, 7, -14, 4]
    for i in range((len(niz)-1)//2):
        maxtomin(niz)
    print(niz)
