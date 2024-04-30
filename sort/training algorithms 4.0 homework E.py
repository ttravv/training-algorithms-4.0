def radix_sort(arr: list[str]) -> None:
    len_arr = len(arr)
    for i in range(len(arr[0])):
        buckets = [[] for _ in range(10)]
        print('**********')
        print('Phase', i + 1 )
        for num in arr:
            if len(num) > i:
                buckets[int(num[-i - 1])].append(num)
            else:
                buckets[0].append(num)
        
        #вывод buckets
        for j in range(0,10):
            if len(buckets[j]) == 0:
                print(f'Bucket {j}: empty')
            else:
                print(f'Bucket {j}:', ', '.join(buckets[j]))
        arr = sum(buckets, [])
    print('**********')
    print("Sorted array:")
    print(', '.join(arr)) 


n =  int(input())
arr = [input() for i in range(n)]
initial_array = ', '.join(arr)
print(f'Initial array:\n{initial_array}')
radix_sort(arr)
    
