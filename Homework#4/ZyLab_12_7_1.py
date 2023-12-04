# Name: Huzaifa Shoeb, ID: 1925670

def get_age():
    age_use = int(input())
    if age_use < 18 or age_use > 75:
        raise ValueError("Invalid age.")
    return age_use


def fat_burning_heart_rate(age_use):
    heart_rate_use = 0.7 * (220 - age_use)
    return heart_rate_use


if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate} bpm")
    except ValueError as ve:
        print(ve)
        print("Could not calculate heart rate info.\n")
