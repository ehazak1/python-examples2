class suppress:
    def __init__(self, exctype):
        self.exctype =  exctype
    def __enter__(self):
        return self
    def __exit__(self, exctype, excinst, exctb):
        if exctype == self.exctype:
            return True
