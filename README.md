# PyC2DConvert
# Cartesian Coordinates (XYZ) to Direct (Fractional) Converter

A Python script (with an example file) is provided to convert the **Cartesian** coordinates into **Direct (Fractional)** coordinates. 

**General Theory and Mathematics:**

The **transformation** from **Cartesian** to **fractional** coordinates involves **matrix operations** using the **inverse of the lattice matrix**. 

  **The transformation from Cartesian coordinates to fractional (also known as fractional or direct lattice) coordinates is a fundamental concept in solid-state physics and crystallography.**
  **It involves converting coordinates from a Cartesian coordinate system, which uses three orthogonal axes, to fractional coordinates that are defined with respect to the lattice vectors of the crystal.**

In a **crystal lattice**, there are usually **three basis vectors (a, b, c)** that define the unit cell. These basis vectors represent the **edges** of the unit cell and provide a reference for describing the **positions** of atoms within the crystal.

The **process** of **transforming Cartesian** coordinates (x, y, z) to **fractional** coordinates (frac_x, frac_y, frac_z) involves using the **inverse of the lattice matrix**. 
Here's the general formula:

| frac_x |   | inv_a11 inv_a12 inv_a13 |   | x |

| frac_y | = | inv_a21 inv_a22 inv_a23 | * | y |

| frac_z |   | inv_a31 inv_a32 inv_a33 |   | z |

In this formula, the matrix on the left represents the fractional coordinates, the matrix in the middle represents the inverse of the lattice matrix, and the matrix on the right represents the Cartesian coordinates.

The lattice matrix is constructed using the lattice vectors a, b, and c:

| a11 a12 a13 |

| a21 a22 a23 |

| a31 a32 a33 |

**A step-by-step explanation of how this transformation works:**

Start with the Cartesian coordinates (x, y, z) of a point. Multiply the Cartesian coordinates by the inverse of the lattice matrix.
The resulting values (frac_x, frac_y, frac_z) are the fractional coordinates of the point within the unit cell.

The reason why this transformation works is because the lattice vectors define the basis of the crystal lattice, and their inverse matrix allows us to convert coordinates from the Cartesian system to the fractional system. Fractional coordinates are useful for crystallography because they provide a way to describe the position of atoms within the unit cell in a way that is independent of the size and shape of the unit cell itself.

In summary, the transformation from Cartesian to fractional coordinates involves matrix operations using the inverse of the lattice matrix. This transformation is crucial for understanding the positions of atoms within a crystal lattice and is a fundamental concept in crystallography and solid-state physics.

