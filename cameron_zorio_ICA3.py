# Question 1 ------------------------
def factorial(n):
    if n == 0: 
        return 1
    else:
        prod = n
        for i in range(1,n):
            prod *= i
        return prod
        

print(factorial(5))

# Question 2 -----------------------------------------------
def dot(u, v): # helper function for computing dot products
    sum = 0
    for i in range(0,len(u)):
        sum = sum + u[i]*v[i]
    return sum

r1 = [1, 2]
r2 = [3, 4]
r3 = [5, 6]

A = [r1, r2, r3] # 3x2 matrix
B = [r1, r2] # 2x2 matrix

C = [] # A*B ---> 3x2 matrix

print("Matrix product result:")
for i in range(0,len(A)): # iterate through each row of A
    c_row = []            
    for j in range(0,len(B[0])): # iterate through each col of B
        # compute the dot product of the ith row of A with the jth col of B
        row = A[i]
        col = []
        for rows in B:
            col.append(rows[j])

        # save results into the (i,j) index of C
        c_row.append(dot(A[i], col))    # entry C[i][j]   
    C.append(c_row)   
    print(c_row)

# Question 3 ---------------------------------
mass = [1.7, 4.2, 2.6, 5.4]
value = [2, 3, -1, 5]

zipped = zip(mass,value)

result = [m * v for m, v in zipped]

print(result)

