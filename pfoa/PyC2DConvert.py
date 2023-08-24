# PyC2DConvert
''' A Python script that converts the cartesian coordinates into direct (fractional) coordinates.'''
 
import numpy as np

# Function to convert Cartesian coordinates to fractional coordinates
def cartesian_to_fractional(cartesian_coords, lattice_matrix):
    # Calculate the inverse of the lattice matrix
    inverse_lattice = np.linalg.inv(lattice_matrix)
    
    # Convert Cartesian coordinates to fractional using matrix multiplication
    fractional_coords = np.dot(cartesian_coords, inverse_lattice)
    return fractional_coords

# Function to read Cartesian coordinates and lattice matrix from a POSCAR file
def read_poscar(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Read the scaling factor for the lattice
    lattice_scale = float(lines[1])
    
    # Read the lattice matrix from the POSCAR file
    lattice_matrix = [list(map(float, lines[i].split())) for i in range(2, 5)]
    
    # Read Cartesian coordinates from the POSCAR file
    cartesian_coords = [list(map(float, line.split()[:3])) for line in lines[8:]]
    
    return cartesian_coords, np.array(lattice_matrix)

def main():
    poscar_file = 'POSCAR'  # Update with your POSCAR file's name
    cartesian_coords, lattice_matrix = read_poscar(poscar_file)
    
    # Convert Cartesian coordinates to fractional coordinates
    fractional_coords = cartesian_to_fractional(cartesian_coords, lattice_matrix)

    print("Cartesian Coordinates:")
    for x, y, z in cartesian_coords:
        print(f"{x:.6f} {y:.6f} {z:.6f}")

    print("\nFractional (Direct) Coordinates:")
    for x, y, z in fractional_coords:
        print(f"{x:.6f} {y:.6f} {z:.6f}")

if __name__ == '__main__':
    main()

