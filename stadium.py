class Cricket:
    def __init__(self,player,score):
        self.__player = player
        self.__score = score
    def info(self):
        print(self.__player)
        print(self.__score)
    def play(self):
        print(self.__player, "is playing cricket")
    def set_score(self,score):
        if score >= 0:
            self.__score = score
        else:
            print("Invalid")

class Football:
    def __init__(self,player,score):
        self.__player = player
        self.__score = score
    def info(self):
        print(self.__player)
        print(self.__score)
    def play(self):
        print(self.__player, "is playing football")
    def set_score(self,score):
        if score >= 0:
            self.__score = score
        else:
            print("Invalid")

c1 = Cricket("Rohit", 100)
f1 = Football("Ronaldo", 3)
sports = [c1, f1]
for sport in sports:
    sport.info()
    sport.play()