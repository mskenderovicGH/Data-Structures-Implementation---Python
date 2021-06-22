# this function will check if heap is as it should be

def heap_check(heap):
    i=0
    while (2 * i + 1) < len(heap):
        if heap[i] < heap[2*i+1] and heap[i] < heap[2*i+1]:
            print('ok')
        else:
            print('bad')
            return False
        i = i + 1
    return True

if __name__ == '__main__':

    heap = [1,2,3,9,5,6,7,8]

    print(heap_check(heap))
