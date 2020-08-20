import random

def generate_random_integers(_sum, n):  
    mean = int(_sum / n)
    variance = int(0.3 * mean)

    min_v = mean - variance
    max_v = mean + int(0.15 * mean)
    array = [min_v] * n
    print(min_v)
    print(max_v)

    diff = _sum - min_v * n

    for i in [0,1,2,-1,-2,-3]:
        delta = random.randint(variance, min_v) + random.randint(int(variance*0.1), variance)
        diff -= delta
        array[i] = array[i] + delta

    for i in range(len(array)):
        ss = random.randint(10, int(mean*0.01))
        array[i] = array[i] + ss
        diff -= ss

    while diff > 0:
        a = random.randint(0, n - 1)
        if array[a] >= max_v:
            continue
        delta = random.randint(100, variance)
        array[a] += delta
        diff -= delta
        if array[a] >= max_v:
            delta2 = random.randint(int(variance*0.3), int(variance*0.8))
            array[a] -= delta2
            diff += delta


    if _sum != sum(array):
        temp = int((_sum -sum(array))/(n-6))
        for x in range(3,n-2):
            array[x] = array[x] + temp
    
    if _sum != sum(array):
        temp = _sum -sum(array)
        a = random.randint(0, n - 1)
        array[a] = array[a] + temp


    print(array)
    print(sum(array))

generate_random_integers(5000000,30)