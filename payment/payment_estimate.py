from datetime import datetime
import random
import xlsxwriter


# month_payment_estimate = input("Enter your month payment estimation: ")
# print(f"Payment Estimation = {month_payment_estimate} Baht.") 
# month_payment_estimate = int(month_payment_estimate)
month_payment_estimate = 2972400

# amount_slip_list = input("Enter your amount_slip_list: ")
# amount_slip_list = amount_slip_list.split(',')
# print(f"Amount of slip list = {amount_slip_list} slips.")
amount_slip_list=[31,6,30,36,22,38,8,15,0,7,11,31,30,11,17,6,8,16,41,34,5,13,17,19,14,27,36,7,9,10,46]

def get_random_per_day(month_payment_estimate, amount_slip_list):
    rand_list = list()
    total = 0
    for index, item in enumerate(amount_slip_list):
        item = int(item)
        if index == len(amount_slip_list)-1:
            rand = month_payment_estimate - total
        else:
            rand_from  = item*4900
            rand_to = item*5100
            rand = random.randint(rand_from,rand_to)
            temp = rand%5
            rand = rand - temp
        rand_list.append(rand)
        day = index+1
        print(day, rand)
        total+=rand
    print(total)
    print(rand_list)
    return rand_list

def get_random_per_bill(rand_list, amount_slip_list):
    estimate_result = dict()
    date_num = 1
    for bill_amount, total_payment in zip(amount_slip_list, rand_list):
        print(f"\n----------------- {total_payment}")
        bill_amount=int(bill_amount)
        print(bill_amount, total_payment)
        total=0
        if bill_amount:
            ss = total_payment/bill_amount
            fr = int(ss) - 1500
            tt = int(ss) + 1500
        else:
            fr, tt = 0,0
        day_result = list()
        for x in range(bill_amount):
            r=random.randint(fr,tt)
            if x == bill_amount-1:
                r = total_payment-total
            elif x == bill_amount-2:
                x = int((total_payment-total)/2)
                r = r=random.randint(x-500,x+500)
            elif x == bill_amount-4:
                x = int((total_payment-total)/4)
                r = r=random.randint(x-100,x+100)
            elif x == bill_amount-8:
                x = int((total_payment-total)/8)
                r = r=random.randint(x-100,x+100)
            temp = r%5
            r = r-temp
            total+=r
            print(f"            {r}")
            day_result.append(r)
        estimate_result[date_num] = day_result
        date_num = date_num + 1
    return estimate_result

def gen_excel(estimate_result):
    print(estimate_result)
    workbook = xlsxwriter.Workbook('Expenses01.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0
    order=estimate_result.keys()
    for key in order:
        row += 1
        worksheet.write(row, col,     key)
        i =1
        for item in estimate_result[key]:
            worksheet.write(row, col + i, item)
            i += 1
    workbook.close()
    return None

random_per_day_lst = get_random_per_day(month_payment_estimate, amount_slip_list)
estimate_result = get_random_per_bill(random_per_day_lst, amount_slip_list)

gen_excel(estimate_result)

# 31,6,30,36,22,38,8,15,0,7,11,31,30,11,17,6,8,16,41,34,5,13,17,19,14,27,36,7,9,10,46

