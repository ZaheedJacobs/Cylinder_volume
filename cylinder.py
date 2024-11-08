# Calculate the volume of a cylinder

import math             # For calculations

def circle_area(diameter: float)-> float:
    # Calculate the area of a circle
    return round((math.pow(diameter, 2) * math.pi) * 0.25, 2)

def cylinder_volume(diameter: float, height: float)-> float:
    # First calculate the area of the circle base
    base_area = circle_area(diameter)

    # Then multiply that area to the height of the cylinder
    return round(base_area * height, 2)

def main():
    # Ask user for diameter and height of cylinder
    # then calculate and print the volume
    diameter_in = eval(input("Enter the cylinder's diameter: "))
    height_in = eval(input("Enter the cylinder's height: "))
    result = cylinder_volume(diameter_in, height_in)
    print(f"The volume of the cylinder is {result:.2f}")

if __name__ == "__main__":
    main()