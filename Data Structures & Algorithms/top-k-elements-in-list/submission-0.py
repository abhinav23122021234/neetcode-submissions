class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        for num in nums:
            if num not in mp:
                mp[num]=0
            mp[num]+=1
        l=[]
        for num,freq in mp.items():
            l.append([freq,num])
        l=sorted(l,reverse=True)
        ans=[]
        for i in range(k):
            ans.append(l[i][1])
        return ans