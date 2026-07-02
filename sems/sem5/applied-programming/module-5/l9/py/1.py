def liters_100km_to_miles_gallon(liters):
    miles = 235.2145 / liters
    return miles


def miles_gallon_to_liters_100km(miles):
    liters = 235.2145 / miles
    return liters


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
