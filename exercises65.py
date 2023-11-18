prev_x = None
prev_y = None

perimeter = 0

while True:
    try:
        x = float(input("Enter the x part of the coordinate: "))
        
        if x == "":
            break
        
        y = float(input("Enter the y part of the coordinate: "))
        
        if y == "":
            break
        
        if prev_x is not None and prev_y is not None:
            distance = ((x - prev_x)**2 + (y - prev_y)**2)**0.5
            perimeter += distance
        
        prev_x, prev_y = x, y
    except ValueError:
        print("Invalid input. Please enter valid coordinates.")

if prev_x is not None and prev_y is not None:
    distance_to_first = ((prev_x - 0)**2 + (prev_y - 0)**2)**0.5
    perimeter += distance_to_first

print("The perimeter of that polygon is ",perimeter)
