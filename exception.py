# The below function currenty throws an exception when called.
# Write code that calls the function but catches
# the exception and prints "Missing Data"

class MissingData(Exception):
    pass

def get_data():
    raise MissingData

try:
    get_data()
except MissingData:
    print("Missing Data")
