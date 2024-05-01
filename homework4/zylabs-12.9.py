# Prabhu Roka
# 1986444
# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    # FIXME: The following line will throw ValueError exception.
    #        Insert try/except blocks to catch the exception.
    try:
        # Try to convert age to an integer
        age = int(parts[1]) + 1
    except ValueError:
        # If conversion fails, set age to 0
        age = 0
    print(f'{name} {age}')

    # Get next line
    parts = input().split()
    name = parts[0]
