filename = 'C:/Users/Equipo/Desktop/python/100DaysOfCode/100DaysOfCode/python/python-crash-course/chapter10-filesAndExceptions/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))