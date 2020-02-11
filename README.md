# Product-Addition Match
Simple usage of conditionals to implement rock-paper-scissors game rules: 

1. Each player chooses an integer (input). 
2. Player 1 will play the `player1_number * player2_number % 3`-th element in the choices array. Player 2 will play the `(player1_number + player2_number) % 3`-th element in the choices array.
3. Use conditionals to decide the result of the match

A player can easily choose an integer which helps them win the match if they know their opponent's number and the order of elements in the choices array.


# Rock-Paper-Scissors Championship

## How the simulation works:
1. Assign random numbers to players.
2. Decide on how to assign players into pairs (i.e. who competes with whom).
3. Rock-paper-scissors until the champion is found.

## Options for grouping people:
1. `Simulate_Simple()`: the first (order of adding to the championship) player competes with the second, the winner of this first match will then play against the third player and so on. The last match will be between whoever has won previous match and the player who was last added to the championship. This is a very unfair way to decide who plays against whom.
2. `Simulate_Quicksort_Like()`: recursively use pivot values to divide players into two teams then four and so on until pairs of players are finalized (similar to quicksort).

