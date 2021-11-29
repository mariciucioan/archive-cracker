from gui import GUI

import sys

if __name__ == "__main__":
    if len(sys.argv) > 0: # run in terminal
        pass
    else:
        GUI().run()
