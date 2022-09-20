from cgi import test
import sys
from cli import *
sys.path.append('../tests/')
import test_engine
# from tests import *
the = cli_func(sys.argv[1:])
if the["eg"] != "nothing":
    test_engine.runs(the["eg"], the)
