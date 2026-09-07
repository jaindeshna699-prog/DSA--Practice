class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        low = 0
        high = cols - 1
        while(low <= high):
            mid= (low + high) // 2
            # find max element in current column
            max_row = 0             
            for i in range(rows):
                if(mat[i][mid] > mat[max_row][mid]):
                    max_row = i
                    # check left and right neighbours
            left = mat[max_row][mid-1] if mid>0 else -1
                    
            right = mat[max_row][mid + 1] if mid + 1< cols else -1
                    

            if(mat[max_row][mid] > left and mat[max_row][mid] > right):
                return [max_row, mid]
            elif(left > mat[max_row][mid]):
                high = mid-1
            else:
                low = mid + 1
        return [-1,-1]
        
        



        