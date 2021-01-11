deposited_sum = float(input())
deposit_term = int(input())
intereset_percentage = float(input())

interest = deposited_sum * (intereset_percentage / 100)
interest_per_month = interest / 12
total_sum = deposited_sum + interest_per_month * deposit_term

print(total_sum)