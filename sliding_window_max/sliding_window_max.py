'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''



def sliding_window_max(nums, k):

    max_value = [0] * (len(nums) - k + 1)

    for i in range(len(max_value)):
        curr = nums[i]
        
        for j in range(1, k):
            if nums[i+j] > curr:
                curr = nums[i + j]

        max_value[i] = curr

    return max_value
    



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
