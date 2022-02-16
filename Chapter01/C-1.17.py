# Had we implemented the scale function (page 25) as follows, does it work
# properly?
# 	def scale(data, factor):
# 		for val in data:
# 			val *= factor
# Explain why or why not.

# It doesn't work as expected. the val was calculated but never been assigned to data.
# Parameter data remains old values.

# Doesn't work
def scale1(data, factor):
    for val in data:
        val *= factor


# Does work
def scale2(data, factor):
    for i in range(len(data)):
        data[i] *= factor


data = list(range(10))

scale1(data, 2)
print(data)


scale2(data, 2)
print(data)
