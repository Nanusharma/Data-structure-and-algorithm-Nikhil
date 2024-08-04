# https://leetcode.com/problems/find-the-number-of-winning-players/
from collections import defaultdict
from typing import List
# from typing import Dict
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        player_dict = defaultdict(dict)
        
        for player in range(n):
            player_dict[player] = defaultdict(int)

        for x, y in pick:
            player_dict[x][y] += 1
        
        wins = 0
   
        for player in range(n):
            for color in player_dict[player]:
                if player_dict[player][color] > player:
                    wins += 1
                    break  
        
        return wins
obj = Solution()
n = 4
pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
print(obj.winningPlayerCount(n, pick))