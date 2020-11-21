import sys

class redirect_stdout:

    def __init__(self, target):
        self.target = target

    def __enter__(self):
        self.oldout = sys.stdout
        sys.stdout = self.target

    def __exit__(self, exctype, excinst, exctb):
        sys.stdout = self.oldout

if __name__ == '__main__':

    def show_family(lastname, firstnames):
        print lastname
        for name in firstnames:
             print name


    with redirect_stdout(sys.stderr):
        show_family('Hettinger', ['Raymond', 'Rachel', 'Matthew', 'TBD'])


    with open('str_help.txt', 'w') as f:
        with redirect_stdout(f):
            help(str)
