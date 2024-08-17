pool_volume = int(input())
first_pipe_debit_per_hour = int(input())
second_pipe_debit_per_hour = int(input())
hours = float(input())

first_pipe_contribution = first_pipe_debit_per_hour * hours
second_pipe_contribution = second_pipe_debit_per_hour * hours
water_amount = first_pipe_contribution + second_pipe_contribution
water_amount_in_percents = water_amount / pool_volume * 100
first_pipe_contribution_in_percents = first_pipe_contribution / water_amount * 100
second_pipe_contribution_in_percents = second_pipe_contribution / water_amount * 100

if first_pipe_contribution + second_pipe_contribution <= pool_volume:
    print(f"The pool is {water_amount_in_percents}% full. Pipe 1: {first_pipe_contribution_in_percents :.2f}%. "
          f"Pipe 2: {second_pipe_contribution_in_percents :.2f}%")
else:
    spillage = first_pipe_contribution + second_pipe_contribution - pool_volume
    print(f"For {hours} hours the pool overflows with {spillage} liters.")
