def bigSorting(unsorted):
    # Write your code here


    return sorted(unsorted, key=lambda x:(x, len(x)))
unsorted = ['31415926535897932384626433832795', '1', '3', '10', '3', '5']
print(bigSorting(unsorted))