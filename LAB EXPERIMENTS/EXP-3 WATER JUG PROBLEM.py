# Water Jug Problem

jug1 = 4
jug2 = 3

x = 0
y = 0

print("Initial State:", x, y)

# Fill Jug 2
y = jug2
print("Fill Jug2:", x, y)

# Pour Jug2 into Jug1
x = y
y = 0
print("Pour Jug2 to Jug1:", x, y)

# Fill Jug2 again
y = jug2
print("Fill Jug2 Again:", x, y)

# Pour Jug2 into Jug1 until Jug1 is full
y = y - (jug1 - x)
x = jug1
print("Pour Again:", x, y)

# Empty Jug1
x = 0
print("Empty Jug1:", x, y)

# Pour remaining water to Jug1
x = y
y = 0
print("Pour Remaining:", x, y)

# Fill Jug2
y = jug2
print("Fill Jug2:", x, y)

# Pour Jug2 into Jug1
y = y - (jug1 - x)
x = 4
print("Final State:", x, y)
