"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject(data)


def display_subject(subjects):
    for subject in subjects:
        print(f"{subject[0]:<6} is taught by {subject[1]:<1} and has {subject[2]:>3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_entries = []
    input_file = open(FILENAME, "r")
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_entries.append(parts)
    input_file.close()
    return data_entries


main()
