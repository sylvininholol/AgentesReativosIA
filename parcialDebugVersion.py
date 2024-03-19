import random

class Ambient:
    def __init__(self, interactions, roomsnumber, dirt_spawn_rate):
        self.award = 0
        self.rooms = [Room() for i in range(roomsnumber)]
        random_vacuum_position = (random.randint(0, roomsnumber - 1))
        self.vacuum = Vacuum(random_vacuum_position)
        self.rooms[self.vacuum.position].dirtyBool = 0
    
    def spawnDirt(self):
        cleanRooms = [i for i, room in enumerate(self.rooms) if room.dirtyBool == 0 and i != self.vacuum.position]
        if cleanRooms:  # Verifica se há salas limpas para sujar
            randomRoom = random.choice(cleanRooms)
            dirt = random.random() * 100 <= dirt_spawn_rate

            if dirt:
                self.rooms[randomRoom].dirty()

                
    def interaction(self):
        print("ESSE É O VETOR PRINCIPAL")
        self.show_without_A()
        print("AQUI COMEÇA ------------")
        for i in range(interactions):
            self.show()
            self.giveAwards()
            self.agentAct()
            self.spawnDirt()
            
            
    def agentAct(self):
        action = self.vacuum.act(self.rooms[self.vacuum.position].dirtyBool, roomsnumber)
        if(action == "Limpando..."):
            self.rooms[self.vacuum.position].dirtyBool = 0
            print("Limpando...")
        else:
            self.vacuum.move(random.choice([-1, 0, 1]), roomsnumber)

    def giveAwards(self):
        if(self.rooms[self.vacuum.position].dirtyBool == 1):
            self.award += 1
                
    def show(self):
        for i in range(roomsnumber):
            if i == self.vacuum.position:
                print("A ", end='')
            elif(self.rooms[i].dirtyBool == 1):
                print("S ", end='')
            else:
                print("_ ", end ='')
        print()
        
    def show_without_A(self):
        for i in range(roomsnumber):
            if(self.rooms[i].dirtyBool == 1):
                print("S ", end='')
            else:
                print("_ ", end ='')
        print()
                
    

        
class Room:

    def __init__(self):
        self.dirtyBool = random.choice([0, 1])

    ## sujo == 1, limpo == 0
    
    def clean(self):
        self.dirtyBool = 0
        
    def dirty(self):
        self.dirtyBool = 1
  
        
class Vacuum:
    def __init__(self, position):
        self.position = position
        self.needClean = 0
        
    def move(self, moveDirection, roomsnumber):
        if(moveDirection == -1):
            print("Indo para a esquerda")
        if(moveDirection == 0):
            print("Parado")
        if(moveDirection == 1):
            print("Indo para a direita")
            
        if(self.position + moveDirection >= 0 and self.position + moveDirection < roomsnumber):
            self.position = self.position + moveDirection
        else:
            print("O aspirador bateu de cara na parede!")

    def act(self, dirtyBool, roomsnumber):
        self.needClean = dirtyBool
        
        if(self.needClean == 1):
            return "Limpando..."
            
            
            

def main(interactions, roomsnumber, dirt_spawn_rate):
    ambiente = Ambient(interactions, roomsnumber, dirt_spawn_rate)
    media = 0
    for i in range(10):    
        ambiente.interaction()
        print("Recompensa recebida: ")
        print(ambiente.award)
        media += ambiente.award
        ambiente.award = 0
    total = media / 10
    print("Média rodando 10 vezes: {} / {}".format(total, interactions / 2))
if __name__ == '__main__':
    interactions = int(input("Digite o número de interações desejado: "))
    roomsnumber = int(input("Digite o número de salas desejado: "))
    dirt_spawn_rate = float(input("Digite a taxa de spawn de sujeira (entre 0 e 100), equivalente a porcentagem: "))
    main(interactions, roomsnumber, dirt_spawn_rate)
