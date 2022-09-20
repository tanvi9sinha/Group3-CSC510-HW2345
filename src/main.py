from cgi import test
import sys
from cli import *
sys.path.append('../../Group3-CSC510-HW2345/')
from tests import *
the = cli_func(sys.argv[1:])
if the["eg"] != "nothing":
    runs(the["eg"], the)
