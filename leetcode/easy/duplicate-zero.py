
# Given a fixed-length integer array arr, 
# duplicate each occurrence of zero, 
# shifting the remaining elements to the right.

# Note:
# That elements beyond the length of the original 
# array are not written. Do the above modifications to 
# the input array in place and do not return anything.

# Example:

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]


arr = [0,4,1,0,0,8,0,0,3]
i = 0


while i < len(arr):
    if arr[i] == 0:
        arr.insert(i+1, 0)
        del arr[-1]
        i += 1

    i += 1


print(arr)
