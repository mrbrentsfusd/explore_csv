minecraft_materials = [
    "Oak Plank",
    "Stick"
]

def print_materials_list():
    print("\nMinecraft Materials")
    print("-------------------")
    for i, item in enumerate(minecraft_materials, 1):
        print(i, item)
    print()

print_materials_list()

print("Add 3 of your favorite Minecraft materials to this list, one per line.")


for _ in range(3):
    text = input("Add your material: ")
    minecraft_materials.append(text.title())
        # adding .title() after the variable name changes the text to have
        # the first letter of each word Capitalized

print_materials_list()
exit()
