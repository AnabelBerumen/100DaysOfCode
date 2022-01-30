from random import randint
class Die:
    def __init__(self, sides = 6):
        self.sides = sides
    

    def roll_die(self,times):

        for i in range(times):
            print((randint(1,self.sides)))
    

dice = Die()

#Poner las veces que quieres tirar los dados
dice.roll_die(10)





