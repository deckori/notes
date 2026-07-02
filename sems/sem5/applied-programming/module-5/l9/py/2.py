tuple1 = ("DOH", "DXB", "MCT")
tuple2 = "RUH", "CAI", "AMM"
tuple3 = "BEY", "BGW", "KWI"

# Generate tuple4 by combining a given tuple with a new tuple
tuple4 = tuple1 + ("Qatar", "UAE", "Oman")

# Generate tuple5 by replication
tuple5 = tuple2 * 2

# Generate tuple6 by reassigning
tuple6 = tuple3

print(len(tuple4))  # Output: 6
print(tuple4)  # Output:('DOH','DXB','MCT','Qatar','UAE','Oman')
print(tuple5)  # Output:('RUH','CAI','AMM','RUH','CAI','AMM')
print(tuple6)  # Output:('BEY','BGW','KWI')
