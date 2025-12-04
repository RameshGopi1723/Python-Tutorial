def si(principle, time, interest):
    return (principle*time*interest) / 100


principle = 100000
time = 2
interest = 12

output = si(principle = principle, time = time, interest = interest)

print(output)