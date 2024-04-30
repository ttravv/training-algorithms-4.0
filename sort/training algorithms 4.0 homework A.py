number_elements = int(input())
celie_chisla = [int(i) for i in input().split()]
opornii_elem = int(input())
counter = 0
for i in celie_chisla:
    if i < opornii_elem:
        counter += 1
print(counter)
print(number_elements - counter)