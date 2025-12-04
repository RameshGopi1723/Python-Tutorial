#sequenceNumber Function
def sequenceNumber(start, stop, step):
    for i in range(start, stop, step):
        print(i)

start_input = int(input("Enter the start value: "))
stop_input = int(input("Enter the stop value: "))
step_input = int(input("Enter the step value: "))
output = sequenceNumber(start = start_input, stop = stop_input, step = step_input)

print(output)