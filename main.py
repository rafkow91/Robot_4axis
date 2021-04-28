# Libs


# Global variables
servo_angles = []
x = float(input('Podaj x:\t'))
y = float(input('Podaj y:\t'))
z = float(input('Podaj z:\t'))

coords_delta = 0.05
user_coord_up = [x + coords_delta, y + coords_delta, z + coords_delta]
user_coord_down = [x - coords_delta, y - coords_delta, z - coords_delta]

with open('coordinates.csv', mode='r') as input_file:
    for line in input_file:
        coordinates = map(float, line.strip().split(', '))
        coords = coordinates[0:3]
        angles = coordinates[3:]

        if user_coord_up > coords > user_coord_down:
            servo_angles = angles
            break

print(servo_angles)