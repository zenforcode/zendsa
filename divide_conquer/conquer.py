def max_subarray(array):
    local_max = array[0]
    global_max = array[0]
    sliding_start = 0
    for idx in range(1, len(array)):
        local_max = local_max + array[idx]
        if local_max > global_max:
            global_max = local_max
        else:
            local_max = local_max - array[sliding_start]
            sliding_start = sliding_start + 1
    return global_max         

if __name__=="__main__":
    nums = [-1,20,-4,10,1,-1]
    print(max_subarray(nums))
