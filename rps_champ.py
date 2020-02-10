from numpy import random
from enum import Enum 
from datetime import datetime

class Choice(Enum):
    ROCK, PAPER, SCISSORS, SIZE = range(4)
    
    # convert int value to key name
    
    
class Player:
    # initializer
    def __init__(self, champ, name, rand_no):
        self.championship = champ
        self.name = name
        self.rand_number = rand_no
        self.choice = 0

    # choose among rock, paper, scissors
    def Play(self):
        self.choice = self.championship.rand_gen.randint(0, Championship.total_choices)

    # string-equivalent for the player's choice
    def Get_Choice_Name(self):
        return Championship.choices[self.choice]



class Championship:
    # seed = 1111
    choices = ["rock", "paper", "scissors"]
    total_choices = len(choices)
    choices_ids = range(total_choices)
    
    # initializer
    def __init__(self, total_players):
        self.total_players = total_players
        self.rand_gen = random.RandomState(datetime.now().microsecond)
        self.players = []
        self.winner = 0

    def Add_Players(self):
        for i in range (total_players):
            name = input("Player " + str(i + 1) + " name: ")
            self.players.append(Player(self, name, self.rand_gen.uniform()*10.0) )
            

    # game rule
    def Compete(self, player_a, player_b):
        player_a.Play()
        player_b.Play()

        # if player_a.choice==0 and player_b.choice==Championship.total_choices - 1 :
        #     return player_a
        # elif player_b.choice==0 and player_a.choice==Championship.total_choices - 1 :
        #     return player_b
        # elif player_a.choice > player_b.choice :
        #     return player_a
        # elif player_b.choice > player_a.choice :
        #     return player_b
        # else :
        #     return 0
        
        if player_a.Get_Choice_Name()=="rock" and player_b.Get_Choice_Name()=="paper" :
            return player_b
        elif player_b.Get_Choice_Name()=="rock" and player_a.Get_Choice_Name()=="paper" :
            return player_a
        elif player_a.Get_Choice_Name()=="paper" and player_b.Get_Choice_Name()=="scissors" :
            return player_b
        elif player_b.Get_Choice_Name()=="paper" and player_a.Get_Choice_Name()=="scissors" :
            return player_a
        elif player_a.Get_Choice_Name()=="scissors" and player_b.Get_Choice_Name()=="rock" :
            return player_b
        elif player_b.Get_Choice_Name()=="scissors" and player_a.Get_Choice_Name()=="rock" :
            return player_a
        else :
            return 0

        # if player_a.choice==Choice.ROCK and player_b.choice==Choice.PAPER :
        #     return player_b
        # elif player_b.choice==Choice.ROCK and player_a.choice==Choice.PAPER :
        #     return player_a
        # elif player_a.choice==Choice.PAPER and player_b.choice==Choice.SCISSORS :
        #     return player_b
        # elif player_b.choice==Choice.PAPER and player_a.choice==Choice.SCISSORS :
        #     return player_a
        # elif player_a.choice==Choice.SCISSORS and player_b.choice==Choice.ROCK :
        #     return player_b
        # elif player_b.choice==Choice.SCISSORS and player_a.choice==Choice.ROCK :
        #     return player_a
        # else :
        #     return 0


    # simple championship, very unfair order of who plays against whom
    def Simulate_Simple(self):
        self.winner = self.players[0]
        for i in range(len(self.players)): 
            current_winner = 0
            while current_winner==0 :
                if self.winner == self.players[i] : 
                    current_winner = self.winner
                else :
                    current_winner = self.Compete(self.players[i], self.winner)
                    # print("-")
                    # self.Print_One_Player(self.players[i])
                    # self.Print_One_Player(self.winner)
                    # print("---")
            self.winner = current_winner
    
    # quicksort-like algorithm to assign players into pairs
    def Simulate_Quicksort_Like(self):
        pass

    # print players, their assigned rand num, their choices
    def Print_One_Player(self, p):
        # print("Player", p.name, "was assigned", str(p.rand_number), "and played", str(Championship.choices[p.choice]))
        print("Player", p.name, "was assigned", str(p.rand_number), "and played", p.Get_Choice_Name())
    def Print_All_Players(self):
        for p in self.players :
            self.Print_One_Player(p)

    # print final winner
    def Print_Winner(self):
        if self.winner != 0 :
            print("Player", self.winner.name, "is the champion!")
        else :
            print("No champion is found yet.")




# MAIN simulation
if __name__ == "__main__":
    total_players = int(input("Total number of players: "))

    championship = Championship(total_players)
    championship.Add_Players()
    # championship.Print_All_Players()
    championship.Simulate_Simple() 
    championship.Print_Winner()
    championship.Print_All_Players()