def merge(arr1, arr2):
    merged_arr = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
    merged_arr.extend(arr1[i:])
    merged_arr.extend(arr2[j:])
    return merged_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = merge_sort(arr)
    print(*sorted_arr)

if __name__ == "__main__":
    main()