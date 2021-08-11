# print("hello world")
# stu="Hello World Variable"
# print(stu)
# def dumbfunction(stu, marco, steven):
#     s=stu
#     m=marco
#     steve=steven
#     print(s)
#     print(m)
#     print(steve)

# dumbfunction(stu="Keyword", marco="Drowyek", steven="bro")
# dumbfunction("Keyword","Drowyek","bro")

# def defaultingvalue(x="DefaultValue"):
#     print(x)
# defaultingvalue()
# defaultingvalue("New String")
# defaultingvalue(x="Hello World")
# def required_default(x, y=3.14):
#     print(x)
#     print(y)
# required_default()
# required_default("Requirement")
# required_default(x=0.0)
# required_default(x=4000, y=9000)
# def stupid(x, y=5):
#     print(x)
#     print(y)
#     return x*y    
# m=stupid(y=1, x=2)
# print(m)
# marco=True
# brad=False
# print(not marco)
# print(not brad)
# evens=[2,4,8]
# print(evens)
# def ProjectGoal(marco="Make a Screensaver"):
#     print(marco)
# ProjectGoal()
# def squared(x):
#     return x*x*x
# odds=[3,6,9,11,13,15,17,19,21,23,25,27,29,31,33]
# # for odd in odds:
# #     odds_squared=squared(odd)
# #     print(odds_squared)
# print(odds[0])
# print(odds[1])
# print(odds[-1])
# print(odds[-2])
# sides={
#     "triangle": 3,
#     "square": 4,
#     "pentagon": 5,
# }
# for kinder in sides:
#      print(f"{sides[kinder]}")
#      print(kinder)
# for key, value in sides.items():
#     print(f"this shape:{key} -> has {value} sides:")
# answer = input("Is your car a Honda?")
# honda = "y" in answer.lower()
# if honda:
#     print("It's a Honda!")
# else:
#     print("Its not a Honda.")


makes = ["Honda", "Ford", "Chevy", "Kia"]

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

# for i, brand in enumerate(makes:
#     if brand == "Honda":
#         print(f"{i} I'm a {brand}")
#     elif brand == "Chevy":       
#         print(f"{i} I'm a {brand}")
#     else:
#         print(f"{i} I'm a {brand}")
