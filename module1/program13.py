def calculate_avg(*scores,**credit):
    if len(scores) == 0:
        print("no scores entered")

    avg_score = sum(scores)/len(scores)

    bonus = credit.get("bonus",0)

    total = avg_score + bonus

    return avg_score , bonus , total


avg, bonus, total = calculate_avg(80.32,45,32,bonus=5)
print(avg)
print(bonus)
print(total)
