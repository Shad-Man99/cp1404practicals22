"""
CP1404/CP5632 Practical
Hexadecimal colours in a dictionary
"""

hexadecimal_colour_code = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                           "Alizarin crimson": "#e32636",
                           "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite":
                               "#faebd7",
                           "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc"}
print(hexadecimal_colour_code)
lower_keys = {}
for key, value in hexadecimal_colour_code.items():
    lower_keys[key.lower()] = value
colour_name = input("Enter colour: ").lower()
while colour_name != "":
    try:
        print(colour_name, "is", lower_keys[colour_name])
    except KeyError:
        print("Invalid key")
    colour_name = input("Enter colour: ").lower()
print("Thank you")
