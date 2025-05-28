class Logger:
    def __init__(self):
        print("Message Before: Logger object constructed!...")

    def __del__(self):
        print("Message After: Logger object destructed.")

log = Logger()
del log
