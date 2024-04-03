import random
import math
import numpy as np

x_coords=np.random.permutation(100)[:200]
y_coords=np.random.permutation(100)[:200]

np.random.shuffle(x_coords)
np.random.shuffle(y_coords)

xypairs=np.column_stack((x_coords, y_coords))

with open("pointslist.txt", "w") as file:
    for xypairs in xypairs:
        file.write(f"{xypairs[0]} {xypairs[1]}\n")

# Function to calculate distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


points=[]
with open('pointslist.txt', 'r') as file:
    for line in file:
        x,y=map(int, line.strip().split()) 
        points.append((x,y))      
    

# Brute force search
min_distance = float('inf')
closest_pair = None
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = distance(points[i], points[j])
        if dist < min_distance:
            min_distance = dist
            closest_pair = (points[i], points[j])

print("Closest pair:", closest_pair)
print("Distance:", min_distance)



