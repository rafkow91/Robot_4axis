# Libs
from math import cos, sin, radians, degrees
import csv

# Global variables

l_AB = 10
l_BC = 10
l_CD = 10
l_DE = 10

coordinates = []
angles = []
with open('coordinates.csv', mode='w') as output:
    for z1 in range(1, 180):
        for z2 in range(1, 180):
            for z3 in range(1, 180):
                for z4 in range(1, 180):

                    z_1 = radians(z1)
                    z_2 = radians(z2)
                    z_3 = radians(z3)
                    z_4 = radians(z4)

                    x = cos(z_1) + l_DE * cos(z_4) * (cos(z_3) * (cos(z_1) * cos(z_2) - (4967757600021511 * sin(z_1) * sin(z_2)) / 81129638414606681695789005144064) - sin(z_3) * (cos(z_1) * sin(z_2) + (4967757600021511 * cos(z_2) * sin(z_1)) / 81129638414606681695789005144064)) - l_DE * sin(z_4) * (cos(z_3) * (cos(z_1) * sin(z_2) + (4967757600021511 * cos(z_2) * sin(z_1)) / 81129638414606681695789005144064) + sin(z_3) * (cos(z_1) * cos(z_2) - (4967757600021511 * sin(z_1) * sin(z_2)) / 81129638414606681695789005144064)) + l_BC * cos(z_1) * cos(z_2) + l_CD * cos(z_3) * (cos(z_1) * cos(z_2) - (4967757600021511 * sin(z_1) * sin(z_2)) / 81129638414606681695789005144064) - l_CD * sin(z_3) * (cos(z_1) * sin(z_2) + (4967757600021511 * cos(z_2) * sin(z_1)) / 81129638414606681695789005144064) - (4967757600021511 * l_BC * sin(z_1) * sin(z_2)) / 81129638414606681695789005144064
                    y = sin(z_1) + l_DE * cos(z_4) * (cos(z_3) * ((4967757600021511 * cos(z_1) * sin(z_2)) / 81129638414606681695789005144064 + cos(z_2) * sin(z_1)) + sin(z_3) * ((4967757600021511 * cos(z_1) * cos(z_2)) / 81129638414606681695789005144064 - sin(z_1) * sin(z_2))) + l_DE * sin(z_4) * (cos(z_3) * ((4967757600021511 * cos(z_1) * cos(z_2)) / 81129638414606681695789005144064 - sin(z_1) * sin(z_2)) - sin(z_3) * ((4967757600021511 * cos(z_1) * sin(z_2)) / 81129638414606681695789005144064 + cos(z_2) * sin(z_1))) + l_CD * cos(z_3) * ((4967757600021511 * cos(z_1) * sin(z_2)) / 81129638414606681695789005144064 + cos(z_2) * sin(z_1)) + (4967757600021511 * l_BC * cos(z_1) * sin(z_2)) / 81129638414606681695789005144064 + l_BC * cos(z_2) * sin(z_1) + l_CD * sin(z_3) * ((4967757600021511 * cos(z_1) * cos(z_2)) / 81129638414606681695789005144064 - sin(z_1) * sin(z_2))
                    z = l_AB + l_BC * sin(z_2) + l_DE * cos(z_4) * (cos(z_2) * sin(z_3) + cos(z_3) * sin(z_2)) + l_DE * sin(z_4) * (cos(z_2) * cos(z_3) - sin(z_2) * sin(z_3)) + l_CD * cos(z_2) * sin(z_3) + l_CD * cos(z_3) * sin(z_2)

                    line = str([round(x, 2),round(y, 2),round(z, 2),z1,z2,z3,z4])
                    line = line.replace('[', '').replace(']', '\n')
                    output.write(line)

print('Done!!')