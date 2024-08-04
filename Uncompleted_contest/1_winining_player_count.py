# https://leetcode.com/contest/biweekly-contest-136/problems/find-the-number-of-winning-players/description/
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

