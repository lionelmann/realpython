def celsius(num):
    conversion = (num * (9 / 5)) + 32
    return conversion

def fahrenheit(num):
    conversion = (num - 32) * (5/9)
    return conversion


prompt = input("Enter a temperature in C: ")

num = float(prompt)

print("Your temperature in F: {}".format(fahrenheit(num)))

prompt = input("Enter a temperature in F: ")

num = float(prompt)

print("Your temperature in C: {}".format(celsius(num)))
