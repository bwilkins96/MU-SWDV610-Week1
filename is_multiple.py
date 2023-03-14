# SWDV 610: Data Structures and Algorithms
# Function that takes two integers (n, m) and returns whether n is a multiple of m

def is_multiple(n, m):
    return n % m == 0 

if __name__ == '__main__':
    print(is_multiple(25, 5))      # -> True
    print('----------')
    print(is_multiple(100, 9))     # -> False