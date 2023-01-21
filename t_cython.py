#from third_party.cython.build.libwin-amd64-3.8 import connectivity

import sys
sys.path.append('./third_party/cython/build/lib.win-amd64-3.8')
from connectivity import enforce_connectivity
import connectivity