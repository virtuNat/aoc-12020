from cpython.mem cimport PyMem_Malloc, PyMem_Free

def play(tuple cups, unsigned long size, unsigned long reps):
    cdef unsigned long cup_len, i, curr, dest, t1, t2, t3
    cup_len = len(cups)
    if size < cup_len: size = cup_len

    cdef unsigned long *clist = <unsigned long*>PyMem_Malloc(size * sizeof(unsigned long))
    if not clist:
        raise MemoryError()
    try:
        for i in range(cup_len - 1):
            clist[cups[i]] = cups[i + 1]
        for i in range(cup_len, size):
            clist[i] = i + 1
        curr = cups[0]
        if size > cup_len:
            clist[cups[-1]] = cup_len
            clist[size - 1] = curr
        else:
            clist[cups[-1]] = curr

        for _ in range(reps):
            t1 = clist[curr]; t2 = clist[t1]; t3 = clist[t2]
            dest = (curr + size - 1) % size
            while dest == t1 or dest == t2 or dest == t3:
                dest = (dest + size - 1) % size
            clist[curr] = clist[t3]
            clist[dest], clist[t3] = t1, clist[dest]
            curr = clist[curr]
        return [i for i in clist[:size]]
    finally:
        PyMem_Free(clist)
