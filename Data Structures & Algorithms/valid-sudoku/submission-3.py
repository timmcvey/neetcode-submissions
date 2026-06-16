class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check sub-boxes
        subBoxBuckets = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        for i_row,v_row in enumerate(board):
            for i_column,v_column in enumerate(v_row):
                if i_row < 3:
                    if i_column < 3:
                        subBoxBuckets[1].append(v_column)
                    if i_column >2 and i_column <6:
                        subBoxBuckets[2].append(v_column)
                    if i_column > 5:
                        subBoxBuckets[3].append(v_column)
                if i_row > 2 and i_row < 6:
                    if i_column < 3:
                        subBoxBuckets[4].append(v_column)
                    if i_column >2 and i_column <6:
                        subBoxBuckets[5].append(v_column)
                    if i_column > 5:
                        subBoxBuckets[6].append(v_column)
                if i_row > 5:
                    if i_column < 3:
                        subBoxBuckets[7].append(v_column)
                    if i_column >2 and i_column <6:
                        subBoxBuckets[8].append(v_column)
                    if i_column > 5:
                        subBoxBuckets[9].append(v_column)        
        for subBox in subBoxBuckets.values():
            subBoxNums = [x for x in subBox if x != '.']
            if len(subBoxNums) != len(set(subBoxNums)):
                return False

        # check rows
        for row in board:
            rowNums = [x for x in row if x != '.']
            print(rowNums)
            if len(rowNums) != len(set(rowNums)):
                return False

        # check columns
        for i in range(len(board)):
            colNums = [x[i] for x in board if x[i] != '.']
            print(colNums)
            if len(colNums) != len(set(colNums)):
                return False

        return True