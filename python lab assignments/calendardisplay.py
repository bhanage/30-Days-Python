# Q.1. Write a program that asks the user how many days are in a particular month, and what day of
# the week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for
# that month. For example, here is the output for a 30-day month that begins on day 4 (Thursday):
# S M T W T F S
#         1 2 3
# 4 5 6 7 8 9 10
# 11 12 13 14 15 
# 16 17 18 19 20 
# 21 22 23 24 25
# 26 27 28 29 30

no_of_days = int(input("Enter the number of days for month: "))
start_of_week_no = int(input("Enter the week number for e.g 0 for Monday,1 for Tuesday etc"))
print(f'S{" ":2}M{" ":2}T{" ":2}W{" ":2}T{" ":2}F{" ":2}S{" ":2}')
cnt=1
for i in range((start_of_week_no+1)*-1,no_of_days+1,1):
    print(f'{i:2}' if i > 0 else ' ',end=' ')
    if cnt%7 == 0:    
        print('')
    cnt+=1
    

    