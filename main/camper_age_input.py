"""
Program camper_age_input.py

Author: Greg Wilhelm

Last date modified: 1/26/2020

The purpose of this program is to prompt for the age of one infant (age 1-5 years) who is attending camp and
convert the years to months via a function call then print out a string showing the user the conversion of
the years they entered to months.

"""

MONTHS_IN_YEAR = 12


def convert_to_months(years):
    months = years * MONTHS_IN_YEAR
    return months


if __name__ == '__main__':
    while True:
        user_input = input("Please enter the age of your infant (1-5 years): ")

        try:
            age_in_years = int(user_input)
            if 1 <= age_in_years <= 5:
                age_in_months = convert_to_months(age_in_years)
                print(age_in_years, "years is", age_in_months, "months")
                break
            else:
                print("Invalid input.")
        except ValueError:
            print("Invalid input.")

#   Input   Expected Output         Actual Output
#   1       "1 years is 12 months"  "1 years is 12 months"
#   5       "5 years is 60 months"  "5 years is 60 months"
#   -1      "Invalid input."        "Invalid input."
#   0       "Invalid input."        "Invalid input."
#   60      "Invalid input."        "Invalid input."
#   .5      "Invalid input."        "Invalid input."
