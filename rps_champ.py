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
        # self.choice = self.championship.rand_gen.randint(0, Championship.total_choices)
        self.choice = self.championship.rand_gen.randint(0, 100) % Championship.total_choices

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
            self.players.append(Player(self, name, self.rand_gen.uniform()*100.0) )
            

    # game rule
    def Compete(self, player_a, player_b):
        player_a.Play()
        player_b.Play()
        print("-")
        self.Print_One_Player(player_a)
        self.Print_One_Player(player_b)
        print("---")
        
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
            self.winner = current_winner


    # quicksort-like algorithm to assign players into pairs
    # partition the players list using pivot value
    def Partition(self, players, first, last):
        pivot = players[last].rand_number
        swap_index = first 
        for i in range(first, last):
            # swap players so that players with small numbers are pushed to the first half of the list
            if players[i].rand_number < pivot :
                players[swap_index], players[i] = players[i], players[swap_index]
                swap_index += 1
        players[swap_index], players[last] = players[last], players[swap_index]
        return swap_index

    # sort player list and compete
    def Arrange_Players(self, players, first, last):
        # case only 2 elements --> compete
        if first == last - 1:
            winner = 0
            while winner == 0:
                winner = self.Compete(players[first], players[last])
            return winner
        # recursively call Arrange_Players
        elif first < last - 1:
            winner = 0
            mid = self.Partition(players, first, last)
            winner1 = self.Arrange_Players(players, first, mid - 1)
            winner2 = self.Arrange_Players(players, mid + 1, last)
            while winner == 0:
                winner = self.Compete(winner1, winner2)
            return winner
        # case only 1 element (first >= last)
        else :
            return players[first]

    # quicksort-like algorithm to assign players into pairs
    def Simulate_Quicksort_Like(self):
        self.winner = self.Arrange_Players(self.players, 0, len(self.players) - 1)


    # print players, their assigned rand num, their choices
    def Print_One_Player(self, p):
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
    championship.Print_All_Players()
    # championship.Simulate_Simple() 
    championship.Simulate_Quicksort_Like()
    championship.Print_Winner()
    # championship.Print_All_Players()