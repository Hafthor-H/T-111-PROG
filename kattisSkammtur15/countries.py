search = input()


with open("/src/countries.txt", "r") as skra_inn:
    counter = 0
    for country in skra_inn:
        country = country.strip()
        if country.endswith(search):
            print(country)
            counter += 1
print(f"{counter} countries with suffix {search} in total.")