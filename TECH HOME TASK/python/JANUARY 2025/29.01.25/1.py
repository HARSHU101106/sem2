def findMaxLength(nums): 
    prefix_sum = {0: -1}   
    max_length = 0 
    balance = 0 
 
    for i, num in enumerate(nums): 
        balance += 1 if num == 1 else -1   
        
        if balance in prefix_sum: 
            max_length = max(max_length, i - prefix_sum[balance]) 
        else: 
            prefix_sum[balance] = i   
 
    return max_length 
 
nums1 = [0, 1, 0, 1, 1, 0, 1, 0] 
nums2 = [0, 1, 1, 1, 0, 0, 1, 0] 
nums3 = [0, 0, 1, 1, 0] 
 
print(findMaxLength(nums1))   
print(findMaxLength(nums2))   
print(findMaxLength(nums3)) 
