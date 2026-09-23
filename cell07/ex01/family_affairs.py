def find_the_redheads(family):
    return list(filter(lambda name: family[name] == "red", family))


dupont_family = {
    "Rin": "red",
    "Rose": "blond",
    "James": "brunette",
    "Khaow": "red",
    "Rod": "red"
}

print(find_the_redheads(dupont_family))