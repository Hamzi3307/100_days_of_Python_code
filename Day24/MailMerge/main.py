PLACEHOLDER = "[name]"

with open("Day24\MailMerge\Input\Names\invited_names.txt",mode="r") as file:
    names = file.readlines()

with open("Day24\MailMerge\Input\Letters\starting_letter.txt",mode="r") as letterfile:
    letter = letterfile.read()
    for name in names:
        name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, name)
        with open(f"Day24\MailMerge\Output\ReadyToSend\letter_for_{name}.txt", mode="w") as invitation:
            invitation.write(new_letter)