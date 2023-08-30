### Modules ###

import math
import my_module
from math import pi as PI_VALUE
from my_module import printValue, sumValues

result = my_module.sumValues(5, 3, 1)
my_module.printValue(result)

result = sumValues(1, 2, 3)
printValue(result)

print(math.pi)
print(math.pow(2, 4))

print(PI_VALUE)
