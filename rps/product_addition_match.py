def main():
    choices = ["rock", "paper", "scissors"]
    p1_number = input("Player 1 chooses an integer: ")
    p2_number = input("Player 2 chooses an integer: ")

    p1_choice = choices[int(p1_number) * int(p2_number) % len(choices)] # modulo with a negative number is a bit tricky but should be allowed
    p2_choice = choices[(int(p2_number) + int(p1_number)) % len(choices)]
    print("Player 1 plays", p1_choice)
    print("Player 2 plays", p2_choice)

    p1_win_msg = "Player 1 wins"
    p2_win_msg = "Player 2 wins"
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