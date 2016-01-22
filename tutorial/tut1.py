houses = [{
    'num_of_bedrooms': 3, 
    'sqft': 2000, 
    'neighborhood' : 1,
    'sale_price' : 250000
},{
    'num_of_bedrooms': 2, 
    'sqft': 800, 
    'neighborhood' : 2,
    'sale_price' : 300000
},{
    'num_of_bedrooms': 2, 
    'sqft': 850, 
    'neighborhood' : 1,
    'sale_price' : 150000
},{
    'num_of_bedrooms': 1, 
    'sqft': 550, 
    'neighborhood' : 1,
    'sale_price' : 78000
},{
    'num_of_bedrooms': 4, 
    'sqft': 2000, 
    'neighborhood' : 0,
    'sale_price' : 150000
}
]

N = len(houses)
lha = []
lya = []
lx1a = []
lx2a = []
lx3a = []

for house in houses:
    lx1a.append(house['num_of_bedrooms'])
    lx2a.append(house['sqft'])
    lx3a.append(house['neighborhood'])
    lya.append(house['sale_price'])
    
w0 = w1 = w2 = w3 = 1.0
def h(x1, x2, x3):
    return w0 + w1*x1 + w2*x2 + w3*x3 

def J(ha, ya):
    acc = 0
    for i in range(0,N):
        acc += (ha[i] - ya[i])*(ha[i] - ya[i])
    return acc / (2*N)
    
def dJ_dw0(ha, ya):
    acc = 0
    for i in range(0,N):
        acc += (ha[i] - ya[i])
    return acc / N
    
def dJ_dw1(ha, ya, x1):
    acc = 0
    for i in range(0,N):
        acc += (ha[i] - ya[i])*x1[i]
    return acc / N

def dJ_dw2(ha, ya, x2):
    acc = 0
    for i in range(0,N):
        acc += (ha[i] - ya[i])*x2[i]
    return acc / N
    
def dJ_dw3(ha, ya, x3):
    acc = 0
    for i in range(0,N):
        acc += (ha[i] - ya[i])*x3[i]
    return acc / N

avg_err = 0

lr = 0.1
for i in range(0,10):
    lha[:] = []
    for j in range(0,N):
        p = h(lx1a[j], lx2a[j], lx3a[j])
        lha.append(p)
        print 'Sale price = ' + str(lya[j]) + ' - My guess = ' + str(p)
    print 'Cost = ' + str(J(lha, lya))
    # caluclate tangent for linear regression
    t0 = dJ_dw0(lha, lya)
    t1 = dJ_dw1(lha, lya, lx1a)
    t2 = dJ_dw2(lha, lya, lx2a)
    t3 = dJ_dw3(lha, lya, lx3a)
    # update weigths
    w0 = w0 - lr*t0
    w0 = w1 - lr*t1
    w0 = w2 - lr*t2
    w0 = w3 - lr*t3
