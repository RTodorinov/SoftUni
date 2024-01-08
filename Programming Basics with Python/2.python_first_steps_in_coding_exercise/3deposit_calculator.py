deposit = float(input())
deposit_term_in_monts = int(input())
yearly_percent = float(input()) / 100

sum_deposit = deposit + deposit_term_in_monts * ((deposit * yearly_percent) / 12)

print(sum_deposit)
