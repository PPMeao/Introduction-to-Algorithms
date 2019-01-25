import sys

file_read = 'random_int'
file_write = 'sorted_array'

def read_file(filename):
    msg = 'Error opening file: '
    try:
        with open(filename) as file:
            return file.readlines()
    except IOError:
        print msg, filename
        sys.exit()

def main():
    lines = read_file(file_read)
    print lines

if __name__ == '__main__':
    if sys.argv.count('--profile') > 0:
        import profile
        profile.run('main()')
    else:
        main()
