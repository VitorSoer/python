# Type: String
string = 'Hello World'
stringType: str = 'Some random text...'
print(string, stringType)

# Type: Number
integer = 10
integerType: int = 5
print(integer, integerType)

floatNumber = 12.5
floatType: float = 50.75
print(floatNumber, floatType)

# Type: Boolean
boolean = False
booleanType: bool = True

# Type: List
listType = ['List', "of", "items"]
print(listType)

# Convert types
print(
    type(int('10')),
    type(float('10.5')),
    type(str(10))
)
