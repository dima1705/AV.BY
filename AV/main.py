import os
import sys
from AV.parser.parser_brand_model_gen import auto_with_mileage


sys.path.insert(1, os.path.join(sys.path[0], '..'))


auto_with_mileage()

