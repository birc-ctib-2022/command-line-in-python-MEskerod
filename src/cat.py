import sys
from tracemalloc import start


def split_args(args: list[str]) -> tuple[list[str], list[str]]:
    """
    Split argv and return the flags separated from the rest.

    >>> split_args(['-n', 'foo', 'bar'])
    (['-n'], ['foo', 'bar'])
    >>> split_args(['-n', 'foo', '-s', 'bar'])
    (['-n', '-s'], ['foo', 'bar'])
    """
    flags, rest = [], []
    for arg in args:
        if arg.startswith('-'):
            flags.append(arg)
        else:
            rest.append(arg)
    return flags, rest

flags, args = split_args(sys.argv[1:])

if not args:
    args.append('/dev/stdin')

start=''
if "-n" in flags:
    start=0
for arg in args:
        with open(arg) as f:
            while True:
                if "-n" in flags:
                    start +=1
                line = f.readline()
                if not line:
                    break
                print(start, ' ', line, sep='')
        

        
