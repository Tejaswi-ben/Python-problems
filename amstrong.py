# Number is Armstrong or Not
num = int(input("Enter the number: "))
s = num
b = len(str(num))
sum = 0

while num != 0:
    n = num % 10
    sum = sum + (n ** b)
    num = num // 10  # Integer division

if s == sum:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")
