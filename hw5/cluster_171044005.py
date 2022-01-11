def max_cluster(clusters):
    size=len(clusters)
    max_current = clusters[0]
    max_finish_flag = 0
    
    for i in range(0, size):
        max_finish_flag = max_finish_flag + clusters[i]
        
        if max_finish_flag < 0:
            max_finish_flag = 0
        elif (max_current < max_finish_flag):
            max_current = max_finish_flag
            
    return max_current

a = [3,-5, 2, 11, -8, 9, -5]
print(max_cluster(a))