talktime_used = int(input("enter talktime "))
messages_used = int(input("enter messages "))

default_price = 100

additional_talktime_cost = 1.0
additional_message_cost = 0.15

additional_talktime = talktime_used - 50
additional_message = messages_used - 50

total_price = default_price + 3 + (additional_talktime)*additional_talktime_cost + additional_message*additional_message_cost
print(f"total price:"{})
