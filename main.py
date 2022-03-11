def less():
    month = 0
    marks = 0
    days = 2
    sumdays = 0
    while(marks<=70 and month<9):
        marks+= days*2+3
        sumdays+=days
        month+=1
        days += 1
    print("Количество уходов в загул: ", month-1)
    print("Количество прогулов: ", sumdays-days+1)

print("Чтобы не быть очисленным, Василий может допустить следующее количество")
less()