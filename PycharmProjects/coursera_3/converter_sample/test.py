import requests
from decimal import Decimal
from currency import convert


correct = Decimal('3754.8057')
result = convert(10 ** 3, 'RUR', 'USD', "26/01/2016", requests)
print(result)
if result == correct:
    print("Correct")
else:
    print("Incorrect: %s != %s" % (result, correct))
