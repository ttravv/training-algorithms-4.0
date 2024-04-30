def compute_prefix_function(s):
    prefix_function = [0] * len(s)
    border = 0
    for i in range(1, len(s)):
        while border > 0 and s[i] != s[border]:
            border = prefix_function[border - 1]
        if s[i] == s[border]:
            border += 1
        else:
            border = 0
        prefix_function[i] = border
    return prefix_function

def main():
    s = input().strip()
    prefix_function = compute_prefix_function(s)
    max_prefix_suffix_length = prefix_function[-1]
    min_length = len(s) - max_prefix_suffix_length
    print(min_length)

if __name__ == "__main__":
    main()