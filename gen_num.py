import random
import sys

total = 20
rand_from = 0
rand_to = 100
filename = './random_int'

def main():
    try:
        with open(filename, 'w+') as file:
            for index in range(total):
                file.write(str(random.randint(rand_from, rand_to)) + ' ')
    except IOError:
        print "Error opening or writing file: ", filename
        sys.exit()

if __name__ == '__main__':
    import profile
    profile.run("main()")
