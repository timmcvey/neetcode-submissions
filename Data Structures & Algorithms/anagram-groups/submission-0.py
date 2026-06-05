class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = {}

        for i,v in enumerate(strs):
            if not "".join(sorted(v)) in groupedAnagrams:
                groupedAnagrams["".join(sorted(v))] = [v]
            else:
                groupedAnagrams["".join(sorted(v))].append(v)
        
        solvedList = []
        for k,v in groupedAnagrams.items():
            solvedList.append(v)

        return solvedList