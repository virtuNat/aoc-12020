# distutils: language=c++

from libcpp.unordered_map cimport unordered_map

def van_eck(list seed, unsigned long length=0):
    cdef unsigned long last, temp, size, idx
    cdef unordered_map[unsigned long, unsigned long] seq
    seq.reserve(length)
    for size in range(len(seed)):
        last = seed[size]
        seq[last] = size
    for idx in range(size, length - 1):
        if seq.find(last) != seq.end():
            temp = idx - seq[last]
        else:
            temp = 0
        seq[last] = idx
        last = temp
    return last
