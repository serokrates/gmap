import pandas
import numpy
from collections import Counter
import math
import cmath
from decimal import Decimal
from collections import Counter
name = []
cd = []
coordinates = []
coordinates1 = []
xx = []
latitude = []
longitude = []
fl = []
fln = []
w=0
def checking(fl,fln,name,latitude,longitude,cd,q,w):
    
    x = Decimal(latitude[q])
    y = Decimal(longitude[q])

    wsp = str(cd[w])
    s = wsp.split(",")
    
    r = 0.00005
    first = Decimal(s[0])
    second = Decimal(s[1])

    iff = (x - first)
    if2 = (y - second)

    if3 = abs(iff+if2)

    if if3 <= r:

        fln.append(name[w])
        


datatxt = open('bike_data.txt','r') 

df = pandas.read_excel('stacje2.xlsx')
v = numpy.asmatrix(df)

total_rows=len(df.axes[0])
total_cols=len(df.axes[1])

rows = df.shape[0]
b = int(rows)

for i in range(total_rows): 
    name.append(v[i,1])


for i in range(total_rows): 
    cd.append(v[i,3])


dane = str(datatxt.readlines())
s = dane.split(" ")
length = len(s)

for j in range(length):
    if 'lat=' in s[j] or 'lon=' in s[j]:

         coordinates.append(s[j])
            
p = 1

k = str(coordinates).split('"')
lengthk = len(k)

for t in range(lengthk):
    if '1'in k[t] or'2'in k[t] or'3'in k[t] or'4'in k[t] or'5'in k[t] or'6'in k[t] or'7'in k[t] or'8'in k[t] or'9'in k[t] or'0' in k[t]:
        coordinates1.append(k[t])

distance = len(coordinates1)
for o in range(distance):
    if p%2==0:
        latitude.append(str(coordinates1[o]))
    if p%2!=0:
        longitude.append(str(coordinates1[o])) 
    p=p+1


for q in range(int(len(latitude))):
    w=0

    while (w <int(len(cd))):
        checking(fl,fln,name,latitude,longitude,cd,q,w)
        
        w=w+1

counted = Counter(fln)
print(counted)
