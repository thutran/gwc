# Rock-Paper-Scissors Championship

## How the simulation works:
1. Assign random numbers to players.
2. Decide on how to assign players into pairs (i.e. who competes with whom).
3. Rock-paper-scissors until the champion is found.

## Options for grouping people:
1. Simulate_Simple(): the first (order of adding to the championship) player competes with the second, the winner of this first match will then play against the third player and so on. The last match will be between whoever has won previous match and the player who was last added to the championship. This is a very unfair way to decide who plays against whom.
2. Simulate_Quicksort_Like(): recursively use pivot values to divide players into two teams then four and so on until pairs of players are finalized (similar to quicksort).
