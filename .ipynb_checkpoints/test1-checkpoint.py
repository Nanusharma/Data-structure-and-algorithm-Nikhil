from typing import List
from collections import defaultdict

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        # Dictionary to store count of balls of each color for each player
        player_picks = defaultdict(dict)
        
        # Initialize player picks dictionary
        for player in range(n):
            player_picks[player] = defaultdict(int)
        
        # Count the number of balls of each color picked by each player
        for x, y in pick:
            player_picks[x][y] += 1
        
        winning_count = 0
        
        # Check each player if they have picked more balls of any color than their player number
        for player in range(n):
            for color in player_picks[player]:
                if player_picks[player][color] > player:
                    winning_count += 1
                    break  # No need to check other colors for this player
        
        return winning_count

# Example usage
solution = Solution()
print(solution.winningPlayerCount(4, [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]))  # Output: 2
print(solution.winningPlayerCount(5, [[1,1],[1,2],[1,3],[1,4]]))  # Output: 0
print(solution.winningPlayerCount(5, [[1,1],[2,4],[2,4],[2,4]]))  # Output: 1
