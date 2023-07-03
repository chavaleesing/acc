import random
import xlsxwriter
from datetime import datetime, timedelta

def random_generate(month_payment_estimate, amount_slip_list):
    total_slip = sum(amount_slip_list)
    minimum = (month_payment_estimate/total_slip) * 0.22
    minimum = minimum - (minimum%5)
    array = [minimum] * total_slip

    remain = month_payment_estimate - sum(array)
    while remain > 0:
        a = random.randint(0, total_slip - 1)
        rand_added_up = random.choice([155,175,195,150,115,135,305])
        array[a] += rand_added_up
        remain -= rand_added_up
    if remain != 0:
        array[0] += remain
    print(array)
    print(sum(array))
    return array

def generate_excel(estimate_result, amount_slip_list):
    workbook = xlsxwriter.Workbook('พค.xlsx')
    worksheet = workbook.add_worksheet()
    from_date = datetime(2023,3,1).date()
    row = 0
    col = 0
    val = estimate_result
    for amount_slip in amount_slip_list:
        # print(from_date, amount_slip)
        worksheet.write(col, row, str(from_date))
        for i in range(amount_slip):
            col += 1
            worksheet.write(col, row, val.pop(0))
        col = 0
        row += 1
        from_date = from_date + timedelta(days=1)
    workbook.close()

month_payment_estimate = 1737775
amount_slip_list=[13,16,17,11,12,8,20,0,9,9,15,10,13,10,12,9,11,12,14,12,12,12,9,14,13,12,13,10,6,8,8]
estimate_result = random_generate(month_payment_estimate, amount_slip_list)
generate_excel(estimate_result, amount_slip_list)
