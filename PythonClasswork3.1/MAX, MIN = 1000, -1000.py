MAX, MIN = 1000, -1000

# Returns the optimal value for the current player
# Initially called fpr the root and maximizing player
def minmax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Terminating condition: leaf node is reached
    if depth == 3:
        return values[nodeIndex]

    # If it is the maximizing player's turn
    if maximizingPlayer:
        best = MIN
        # Recur for the left and right children
        for i in range(0, 2):
            val = minmax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                break
                return best
            else:
                # If it is the minimizing player's turn
                best = MAX
                # Recur for the left and right children
                for i in range(0, 2):
                    val = minmax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
                    best = min(best, val)
                    beta = min(beta, best)

                    # Alpha-Beta pruning
                    if beta <= alpha:
                        break

                return best

# Driver Code 
if __name__ == "__main__":
    # Example values at the leaf nodes
    values = [3,5,6,9,1,0,-1]

    # Start the minmax algorithm with the root node (depth 0) and maximizing player.
    print("The optimal value is: ", minmax(0, 0, True, values, MIN, MAX))
            