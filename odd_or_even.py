# SWDV 610: Data Structures and Algorithms
# Function that returns whether an inputted number is odd or even

def odd_or_even():
    num = int(input('Give me a number: '))

    if num % 2 == 0:
        print(num, 'is an even number')
    else:
        print(num, 'is an odd number')

if __name__ == '__main__':
    odd_or_even()
