

# Enter your code here

#user inputs say ethanAlexanderFilmer, wanna make that into ethan_alexander_filmer
#str_name = str(name)

def to_snakecase(str_name):
    for one_char in str_name:
        if one_char.islower():
         print(one_char,end='')
        if one_char.isupper():
         print('_' + one_char.lower(),end='')

def main():
    name = input("What's your full name? ")

    to_snakecase(name)

main()    