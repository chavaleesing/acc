import random
import xlsxwriter

def generate_random_integers(_sum, n):  
    mean = int(_sum / n)
    variance = int(0.3 * mean)

    min_v = mean - variance
    max_v = mean + int(0.15 * mean)
    array = [min_v] * n
    # print(min_v)
    # print(max_v)

    diff = _sum - min_v * n

    for i in [0,1,2,-1,-2,-3]:
        delta = random.randint(int(variance*0.65), int(variance*0.8))
        diff -= delta
        array[i] = array[i] + delta

    for a in range(len(array)):
        if diff < 0:
            break
        if array[a] >= max_v:
            continue
        delta = random.randint(int(variance*0.4), int(variance*0.8))
        array[a] += delta
        diff -= delta
        if array[a] >= max_v:
            delta2 = random.randint(int(variance*0.3), int(variance*0.7))
            array[a] -= delta2
            diff += delta


    if _sum != sum(array):
        temp = int((_sum -sum(array))/(n))
        for x in range(n):
            array[x] = array[x] + temp

    if _sum != sum(array):
        temp = _sum - sum(array)
        array[0] = array[0] + temp


    print(array)
    print(sum(array))
    return array


def gen_excel(array, array2):
    workbook = xlsxwriter.Workbook('Expenses02.xlsx')
    worksheet = workbook.add_worksheet()

    col = 0

    for v1, v2 in zip(array, array2):
        row = 0
        worksheet.write(col, row, v1)
        worksheet.write(col, row+1, v1*0.07)
        worksheet.write(col+1, row, v2)
        worksheet.write(col+1, row+1, 0)
        col += 2
    workbook.close()
    return None

arr1 = generate_random_integers(35309218,31)
arr2 = generate_random_integers(1612588,31)
gen_excel(arr1, arr2)