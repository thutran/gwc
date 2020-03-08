from random import randint
# from secrets import randbelow

def main():
    choices = ["rock", "paper", "scissors"]

    p1_choice = input("Please enter your choice ('rock' or 'paper' or 'scissors'): ")
    p2_choice = choices[randint(0, 99) % len(choices)]
    # p2_choice = choices[randbelow(100) % len(choices)]
    print("You play", p1_choice)
    print("Computer plays", p2_choice)

    p1_win_msg = "You win"
    p2_win_msg = "Computer wins"
    tied_msg = "The match is tied"

    if p1_choice=="rock" and p2_choice=="paper" :
        return p2_win_msg
    elif p2_choice=="rock" and p1_choice=="paper" :
        return p1_win_msg
    elif p1_choice=="paper" and p2_choice=="scissors" :
        return p2_win_msg
    elif p2_choice=="paper" and p1_choice=="scissors" :
        return p1_win_msg
    elif p1_choice=="scissors" and p2_choice=="rock" :
        return p2_win_msg
    elif p2_choice=="scissors" and p1_choice=="rock" :
        return p1_win_msg
    else :
        return tied_msg

if __name__ == "__main__":
    result = main()
    print(result)