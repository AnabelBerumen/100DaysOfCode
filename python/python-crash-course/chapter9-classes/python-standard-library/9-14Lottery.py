from random import choice

lotteryWins = [3,6,9,12,15,"a","x","l","k","z"]

def premioMayor(lotteryWins):
    
    ticket = []
    for i in range(4):
        
        rand = (choice(lotteryWins))
        ticket.append(rand)
    
    return ticket



def myTicket(lotteryWins):
    
    ticket = []
    for i in range(4):
        
        rand = (choice(lotteryWins))
        ticket.append(rand)
    return ticket


def evaluador(my_ticket,premio_mayor):
    if my_ticket != premio_mayor:
            return False
    


    return True

def ganador(ticket_ganador,tiradas_maximas):
    intentos= 0
    triunfo= False

    while not triunfo:
        mi_ticket = myTicket(lotteryWins)
        triunfo = evaluador(mi_ticket, ticket_ganador)

        intentos += 1
        if intentos >= tiradas_maximas:
            print("Excediste las tiradas")
            break

    if triunfo:
         print(f"\nTicket Ganador{ticket_ganador}\nTu ticket {mi_ticket}\ninteto numero {intentos}")   
    else:
        ("Sigue participando")

ticket_ganador = premioMayor(lotteryWins)
print(f"El ticket_ganador es {ticket_ganador}")

ganador(ticket_ganador,10000)





   




        
        









