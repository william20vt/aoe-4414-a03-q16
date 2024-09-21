# sez_to_ecef.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  sez= a 1x3 array of the components of sez
#  lat_deg=lattitude of the observers location
#  lon_deg=longitutde of the observers location
#  ...
# Output:
#  A description of the script output
#
# Written by William Sosnowski
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math
import numpy as np

# "constants"
R_E_KM=6378.1363
E_E     =0.081819221456
# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
sez=np.zeros(3)
lat_deg=float('nan')
lon_deg=float('nan')

# parse script arguments
if len(sys.argv)==6:
  sez = np.array([float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])])
  lat_deg = float(sys.argv[4])
  lon_deg = float(sys.argv[5])  #the float here converts it from a text string to a number
else:
    print(\
    'Usage: '\
    'python3 sez_to_ecef.py  sez lat_deg lon_deg'\
   )
    exit()

# write script below this line

lat_rad=np.radians(lat_deg)
lon_rad=np.radians(lon_deg)

rotation_matrix = np.array([
        [-np.sin(lat_rad) * np.cos(lon_rad), -np.sin(lon_rad), -np.cos(lat_rad) * np.cos(lon_rad)],
        [-np.sin(lat_rad) * np.sin(lon_rad),  np.cos(lon_rad), -np.cos(lat_rad) * np.sin(lon_rad)],
        [ np.cos(lat_rad),                    0,              -np.sin(lat_rad)]
    ])

ecef_vector = -rotation_matrix @ sez

print("ECEF Coordinates (meters):")
print(f"x: {ecef_vector[0]:.3f} km")
print(f"y: {ecef_vector[1]:.3f} km")
print(f"z: {ecef_vector[2]:.3f} km")

ecef_x_km=ecef_vector[0]
ecef_y_km=ecef_vector[1]
ecef_z_km=ecef_vector[2]
print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)