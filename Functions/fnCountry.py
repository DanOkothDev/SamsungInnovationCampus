def display_country(country: str = "Kenya"):
  print("The person is from ", country)

countryOne = input("\nEnter the country for person one: ")
countryTwo = input("Enter the country for person two: ")

print("\nOutput for person one")
print("---------------------------------")
display_country(countryOne)

print("\nOutput for person two")
print("---------------------------------")
display_country(countryTwo)

print("\nOutput for person three")
print("---------------------------------")
display_country()



