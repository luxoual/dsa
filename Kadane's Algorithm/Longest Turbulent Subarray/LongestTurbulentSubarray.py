# Original
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # Bruteforce is we try every subarray, check if its
        # turbulent, then we keep an ongoing result.
        # Note if we go from k+1, and check behind, even
        # if we start a new subarray from where we are,
        # it'll always have size of 2, and we'll also know
        # what we are expecting next.

        # Applying Kadane's algorithm and DP, we can add the current
        # number, if it is what we are expecting next

        result = 1
        curr = 1 # Length
        n = len(arr)

        if n == 1:
            return 1
        
        expect = 0 # 1 means we expect next to be greater, -1 means less

        for i in range(1, n):
            if arr[i] == arr[i-1]:
                curr = 1
                expect = 0
            elif expect == 0:
                curr+=1
                result = max(result, curr)
                if arr[i] > arr[i-1]:
                    expect = -1
                else:
                    expect = 1
            elif (expect == 1 and arr[i] > arr[i-1]) or (expect == -1 and arr[i] < arr[i-1]):
                curr+=1
                expect *= -1
                result = max(result, curr)
            elif (expect == 1 and arr[i] < arr[i-1]) or (expect == -1 and arr[i] > arr[i-1]):
                curr = 2
                result = max(result, curr)
            
        return result



# More cleaned up but same approach / correct approach
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        result = 1
        curr = 1 # Length
        n = len(arr)

        if n == 1:
            return 1
        
        prev = 0 # Instead of tracking what we expect next, we just need to keep track of the previous comparison

        for i in range(1, n):
            comp = 0
            if arr[i] > arr[i-1]: comp = 1
            elif arr[i] < arr[i-1]: comp = -1
            else: comp = 0
            
            # Check if it matches before
            if comp == 0: curr = 1
            #We can take both
            elif prev == 0: curr = 2
            elif comp != prev: curr+=1
            else: curr = 2
            
            prev = comp
            result = max(curr, result)
            
        return result

