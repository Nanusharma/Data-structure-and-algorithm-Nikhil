class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        count=0
        for i in range(len(colors)-1:
                if i+1 =len(colors) or i ==0:
                    if i == 0:
                        if colors[i]!=colors[i+1] and colors[i]!=colors[len(colors)-1]:
                            count+=1
                    if i == len(nums)-1:
                        if colors[i]!=colors[i-1] and colors[i]!=colors[0]:
                            count+=1
                
            else:
                if colors[i]!=colors[i+1] and colors[i] !=colors[i-1]:
                    count+=1
        return count
        