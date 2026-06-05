class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = defaultdict(list)

        for i,v in enumerate(strs):
            groupedAnagrams["".join(sorted(v))].append(v)

        return list(groupedAnagrams.values())
        
        # solvedList = []
        # for k,v in groupedAnagrams.items():
        #     solvedList.append(v)

        # return solvedList