
numbers = [5, 20, 30, 30, 50]
delval = int(input('Enter the deletion value: '))
while True:
    try:
        numbers.remove(delval)
    except: 
        break  
if len(numbers)==5:
    numbers.clear() 
# ******************************
# Make your Code
# ******************************

print (numbers)
