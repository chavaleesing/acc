import random
import xlsxwriter
from datetime import datetime, timedelta

def random_generate(month_payment_estimate, amount_slip_list):
    total_slip = sum(amount_slip_list)
    minimum = (month_payment_estimate/total_slip) * 0.3
    minimum = minimum - (minimum%5)
    array = [minimum] * total_slip

    remain = month_payment_estimate - sum(array)
    while remain > 0:
        a = random.randint(0, total_slip - 1)
        rand_added_up = random.choice([5,15,15,25,50,115,135,405,665])
        array[a] += rand_added_up
        remain -= rand_added_up
    if remain != 0:
        array[0] += remain
    print(array)
    print(sum(array))
    return array

def generate_excel(estimate_result, amount_slip_list):
    workbook = xlsxwriter.Workbook('Expenses.xlsx')
    worksheet = workbook.add_worksheet()
    from_date = datetime(2021,12,1).date()
    row = 0
    col = 0
    val = estimate_result
    for amount_slip in amount_slip_list:
        print(from_date, amount_slip)
        worksheet.write(col, row, str(from_date))
        for i in range(amount_slip):
            col += 1
            worksheet.write(col, row, val.pop(0))
        col = 0
        row += 1
        from_date = from_date + timedelta(days=1)
    workbook.close()

month_payment_estimate = 856215
amount_slip_list=[3,2,8,22,15,10,5,2,3,2,8,0,5,3,7,3,4,5,7,4,1,7,1,3,5,5,2,5,9,0,20]
estimate_result = random_generate(month_payment_estimate, amount_slip_list)
generate_excel(estimate_result, amount_slip_list)

# def get_random_per_day(month_payment_estimate, amount_slip_list):
#     rand_list = list()
#     total = 0
#     for index, item in enumerate(amount_slip_list):
#         item = int(item)
#         if index == len(amount_slip_list)-1:
#             rand = month_payment_estimate - total
#         else:
#             rand_from  = item*2900
#             rand_to = item*6200
#             rand = random.randint(rand_from,rand_to)
#             temp = rand%5
#             rand = rand - temp
#         rand_list.append(rand)
#         day = index+1
#         print(day, rand)
#         total+=rand
#     print(total)
#     print(rand_list)
#     return rand_list

# def get_random_per_bill(rand_list, amount_slip_list):
#     estimate_result = dict()
#     date_num = 1
#     for bill_amount, total_payment in zip(amount_slip_list, rand_list):
#         print(f"\n----------------- {total_payment}")
#         bill_amount=int(bill_amount)
#         print(bill_amount, total_payment)
#         total=0
#         if bill_amount:
#             ss = total_payment/bill_amount
#             fr = int(ss) - 1500
#             tt = int(ss) + 1500
#         else:
#             fr, tt = 0,0
#         day_result = list()
#         for x in range(bill_amount):
#             r=random.randint(fr,tt)
#             if x == bill_amount-1:
#                 r = total_payment-total
#             elif x == bill_amount-2:
#                 x = int((total_payment-total)/2)
#                 r = r=random.randint(x-500,x+500)
#             elif x == bill_amount-4:
#                 x = int((total_payment-total)/4)
#                 r = r=random.randint(x-500,x+500)
#             elif x == bill_amount-8:
#                 x = int((total_payment-total)/8)
#                 r = r=random.randint(x-100,x+100)
#             elif x == bill_amount-10:
#                 x = int((total_payment-total)/10)
#                 r = r=random.randint(x-100,x+100)
#             elif x == bill_amount-13:
#                 x = int((total_payment-total)/13)
#                 r = r=random.randint(x-100,x+100)
#             temp = r%5
#             r = r-temp
#             total+=r
#             print(f"            {r}")
#             day_result.append(r)
#         estimate_result[date_num] = day_result
#         date_num = date_num + 1
#     return estimate_result

# def gen_excel(estimate_result):
#     print(estimate_result)
#     workbook = xlsxwriter.Workbook('Expenses02.xlsx')
#     worksheet = workbook.add_worksheet()

#     row = 0
#     col = 0
#     order=estimate_result.keys()
#     for key in order:
#         col += 1
#         worksheet.write(col, row,     key)
#         i =1
#         for item in estimate_result[key]:
#             worksheet.write(col, row + i, item)
#             i += 1
#     workbook.close()
#     return None

# random_per_day_lst = get_random_per_day(month_payment_estimate, amount_slip_list)
# estimate_result = get_random_per_bill(random_per_day_lst, amount_slip_list)

# gen_excel(estimate_result)

# 31,6,30,36,22,38,8,15,0,7,11,31,30,11,17,6,8,16,41,34,5,13,17,19,14,27,36,7,9,10,46

