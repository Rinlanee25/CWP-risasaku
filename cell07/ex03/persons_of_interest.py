def famous_births(people):
    sorted_people = sorted(
        people.values(),
        key=lambda person: person["date_of_birth"]
    )

    for person in sorted_people:
        print(f'{person["name"]} is a great scientist born in {person["date_of_birth"]}.')


people = {
    "Rin": {"name": "Rinlanee Sasakul", "date_of_birth": "1815"},
    "Opal": {"name": "Piyaphorn Pimpiw", "date_of_birth": "1900"},
    "Pang": {"name": "Kantawan Suwan", "date_of_birth": "1878"},
    "Park": {"name": "Wannasa Sang", "date_of_birth": "1907"},
    "Boat": {"name": "Wichada taochaly", "date_of_birth": "1906"}
}

famous_births(people)