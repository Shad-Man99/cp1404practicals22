"""
emails
Estimate: 60 minutes
Actual:   90 minutes
"""

store_email_name = {}
email = str(input("Email: "))
while email != "":
    email_parts = [str(parts) for parts in email.split("@")]
    whole_name = " ".join(email_parts[0].split(".")).title()
    print(whole_name)
    check_name = str(input(f"Is your name {whole_name}? (Y/n) "))
    if check_name == 'n':
        whole_name = str(input("Name: "))
    store_email_name[whole_name] = email
    email = str(input("Email: "))
for key, value in store_email_name.items():
    print(f"{key} ({value})")
