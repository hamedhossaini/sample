def salary(hour, per_hour):
    if hour > 13:
        return "You aren't allowed to word too much!"
    else:
        total = hour * per_hour
        return total
# Enter hours and your hourly salary below        
print(salary())        