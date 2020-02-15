from numpy import random # rand_number for players, RandomState for Championship
from datetime import datetime # random seed for Championship

class Player:
    # initializer
    def __init__(self, champ, name, rand_no):
        self.championship = champ
        self.name = name
        self.rand_number = rand_no
        self.choice = None

    # choose among rock, paper, scissors
    def Play(self):
        self.choice = self.championship.rand_gen.randint(0, 100) % Championship.total_choices

    # string-equivalent for the player's choice
    def Get_Choice_Name(self):
        if self.choice is None :
            return "nothing"
        return Championship.choices[self.choice]
    
    # string representation of a player object
    def __str__(self):
        return "Player " + self.name + " was assigned " + str(self.rand_number) + " and played " + self.Get_Choice_Name()



class Championship:
    choices = ["rock", "paper", "scissors"]
    total_choices = len(choices)
    choices_ids = range(total_choices)
    
    # initializer
    def __init__(self, total_players, seed=None):
        self.total_players = total_players
        self.seed = seed if seed is not None else datetime.now().microsecond
        self.rand_gen = random.RandomState(self.seed)
        self.players = []
        self.champion = None

    def Add_Players(self):
        for i in range (total_players):
            name = input("Player " + str(i + 1) + " name: ")
            self.players.append(Player(self, name, self.rand_gen.uniform()*100.0) )
            

    # game rules
    # return the winner (player object) if any
    # return None if tied
    def Compete(self, player_a, player_b):
        if player_a is None and player_b is None:
            raise Exception("Championship.Compete(player_a, player_b) needs at least one player object as a parameter")
        
        if player_a is None or player_b is None:
            return player_a if player_b is None else player_b 

        if player_a == player_b:
            return player_a

        player_a.Play()
        player_b.Play()
        print("-")
        print(player_a)
        print(player_b)
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
            return None


    # simple championship
    # very unfair order of who plays against whom
    def Simulate_Simple(self):
        self.champion = self.players[0]
        for p in self.players :
            current_winner = None
            while current_winner is None :
                current_winner = self.Compete(self.champion, p)
            self.champion = current_winner


    # quicksort-like algorithm to assign players into pairs

    # partition the players list using pivot value
    # return the final index of the pivot in the list
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

    # sort player list, compete, and return the final winner
    def Arrange_Players(self, players, first, last):
        # case only 1 element
        if first == last:
            return players[first]
        # case 2 elements --> compete
        elif first == last - 1:
            winner = None
            while winner is None:
                winner = self.Compete(players[first], players[last])
            return winner
        # case > 2 players --> recursively call Arrange_Players
        elif first < last - 1:
            final_winner = None
            finalist = None
            mid = self.Partition(players, first, last)
            winner1 = self.Arrange_Players(players, first, mid - 1)
            winner2 = self.Arrange_Players(players, mid + 1, last)
            while finalist is None:
                if winner1 is None :
                    finalist = players[mid]
                else :
                    finalist = self.Compete(players[mid], winner1)
            while final_winner is None:
                if winner2 is None :
                    final_winner = finalist
                else :
                    final_winner = self.Compete(finalist, winner2)

            return final_winner
        # case first > last --> sorting completed
        else : 
            return None

    # quicksort-like algorithm to assign players into pairs
    def Simulate_Quicksort_Like(self):
        self.champion = self.Arrange_Players(self.players, 0, len(self.players) - 1)


    # print players, their assigned rand num, their choices
    def Print_All_Players(self):
        for p in self.players :
            print(p)

    # print final winner
    def Print_Champion(self):
        if self.champion is not None :
            print("Player", self.champion.name, "is the champion!")
        else :
            print("No champion is found yet.")




# MAIN simulation
if __name__ == "__main__":
    total_players = int(input("Total number of players: "))

    # create a championship instance
    # championship = Championship(total_players, 1111) # seed number 1111
    championship = Championship(total_players) # random seed

    championship.Add_Players()
    championship.Print_All_Players()
    # championship.Simulate_Simple() 
    championship.Simulate_Quicksort_Like()
    championship.Print_Champion()
