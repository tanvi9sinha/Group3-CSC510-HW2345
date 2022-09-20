import sys
from cli import *
sys.path.append("../Group3-CSC510-HW2345/")
# import tests
from tests import test_engine
the = cli_func(sys.argv[1:])
if the["eg"] != "nothing":
    test_engine.runs(the["eg"], the)

