input_filename = "country_info.txt"

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip("\n").split("|")
        country, capital, code, code3, dailing, timezone, currency = data
        # print(country,capital,code,code3,dailing,timezone,currency,sep='\n\t')
        country_dict = {
            "name": country,
            "capital": capital,
            "country_code": code,
            "cc3": code3,
            "dailaing_code": dailing,
            "timezone": timezone,
            "currency": currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        # code_lookup=(code.casefold()) = country
        countries[code.casefold()] = country_dict

# print(countries)
# print(countries(find_name)("capital")) # () means "go look up something inside this container."
# first loop up countries("india") then returns dict
# then ("capital") looks inside the dict and then print "New delhi"

while True:
    find_name = input("Enter the name of the country: ")
    if find_name.casefold() == "quit":
        break
    country_key = find_name.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        if country_data["capital"]:
            print(f"The capital of {find_name} is {country_data['capital']}")
        else:
            print("This country doesnt have any capital")
    else:
        print("You have entered invaid")
for country, data in countries.items():
    if not data["capital"]:
        print(f"{data["name"]}")
