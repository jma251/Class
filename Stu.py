makes = ["Honda", "Ford", "Chevy", "Kia", "Saab"]

def get_selection() -> int:
    combo_string = ""

    for i, make in enumerate(makes):
        i += 1
        new_string = f"- {i}: {make}\n"
        combo_string += new_string 
    prompt = f"Choose Make\n{combo_string}\nSelection: "
    capture = input(prompt)
    selection = int(capture) - 1
    return selection

def get_confirmation() -> bool:
    prompt = "Is this correct? Y or N?"
    confirm = input(prompt)
    return "Y" in confirm.upper()

confirmed = False

while not confirmed:
    selection = get_selection()
    capture = makes[selection]
    selected_make = makes[selection]
    print(f"You have selected - {selection + 1}: {selected_make}")  # You have selected - 4: Kia /n Is this correct? Y or N 
    confirmed = get_confirmation()
