# Prabhu Roka
# 1986444
def get_age():
    age1 = int(input())
    # TODO: Raise exception for invalid ages
    if age1 < 18 or age1 > 75:
        raise ValueError("Invalid age.")
    return age1

# TODO: Complete fat_burning_heart_rate() function


def fat_burning_heart_rate(age1):
    heart_rate1 = 0.70 * (220 - age1)
    return heart_rate1


if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate} bpm")
    except ValueError as ve:
        print("Invalid age.")
        print(f"Could not calculate heart rate info.\n")
