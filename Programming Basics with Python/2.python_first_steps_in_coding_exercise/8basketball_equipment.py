yearly_fee = int(input())

basketball_shoes = yearly_fee - yearly_fee * 0.40
basketball_clothes = basketball_shoes - basketball_shoes * 0.20
basketball_ball = basketball_clothes / 4
basketball_accesories = basketball_ball / 5

total_sum = yearly_fee + basketball_accesories + basketball_ball + basketball_clothes + basketball_shoes

print(total_sum)
