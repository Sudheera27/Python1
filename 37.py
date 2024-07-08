cities=["New York","Chicago","Denver","Los Angeles"]
lat=[40.7128,41.8781,39.7392,34.0522]
long=[74.0060,87.6298,104.9903,118.2347]
distance=[]
latp=28.5383
longp=81.3792
for i in range(0,4,1):
    d1_squared=(latp-lat[i])**2+(longp-long[i])**2
    d1=d1_squared**0.5
    distance.append(d1)
min_distance=min(distance)
pos=distance.index(min_distance)
print("Please take the patient to "+cities[pos])
