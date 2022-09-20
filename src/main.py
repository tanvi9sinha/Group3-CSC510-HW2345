from cgi import test
import sys
from cli import *
sys.path.append('../tests/')
from tests import *
the = cli_func(sys.argv[1:])
if the["eg"] != "nothing":
    test.runs(the["eg"], the)
