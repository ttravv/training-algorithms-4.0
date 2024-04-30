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

def main():
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))
    result = merge(arr1, arr2)
    print(*result)

if __name__ == "__main__":
    main()