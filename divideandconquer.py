from datetime import datetime
import psutil
start=datetime.now()
with open("np gen file.txt", "r") as file:
    S = []
    for line_number, line in enumerate(file, start=1):
        line = line.strip()  
        parts = line.split()
        if len(parts) == 2:
            try:
                x, y = map(float, parts)
                S.append((x, y))
            except ValueError:
                print(f"Error: Invalid coordinates on line {line_number}")
        else:
            print(f"Error: Line {line_number} does not contain exactly two elements")

n = len(S)
if n == 1:
    print("Closest pair distance: ∞")
elif n == 2:
    p1, p2 = S[0], S[1]
    print("Closest pair distance:", ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) ** 0.5)
else:
    sorted_S = sorted(S)  

    m_idx = n // 2
    m = sorted_S[m_idx][0]
   
    S1 = sorted_S[:m_idx]
    S2 = sorted_S[m_idx:]

    delta1 = min(((S1[i+1][0] - S1[i][0])**2 + (S1[i+1][1] - S1[i][1])**2) ** 0.5 for i in range(len(S1) - 1))
    delta2 = min(((S2[i+1][0] - S2[i][0])**2 + (S2[i+1][1] - S2[i][1])**2) ** 0.5 for i in range(len(S2) - 1))
    delta12 = min((abs(S2[0][0] - S1[-1][0])**2 + 
                   abs(S2[0][1] - S1[-1][1])**2) ** 0.5, delta1, delta2)
    print("Closest pair distance:", min(delta1, delta2, delta12))

endtime=datetime.now()

totaltime=endtime-start
usage=psutil.Process().memory_info().rss

print("in seconds : ", totaltime)
print(usage)