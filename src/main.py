from cgi import test
import sys
from cli import *
sys.path.append('../')
from tests import *
the = cli_func(sys.argv[1:])
if the["eg"] != "nothing":
    runs(the["eg"], the)
