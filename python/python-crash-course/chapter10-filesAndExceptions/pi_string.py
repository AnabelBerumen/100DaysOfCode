from cmath import pi


filename = 'C:/Users/Equipo/Desktop/python/100DaysOfCode/100DaysOfCode/python/python-crash-course/chapter10-filesAndExceptions/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()

birthday = input("Enter your birthdat, in the form ddmmyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi")
else:
    print("Your birthday does not appear in the first million digits of pi")


