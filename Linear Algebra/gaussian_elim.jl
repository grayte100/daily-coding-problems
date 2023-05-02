#solve system of equations of the form Ax = b
# x + 2y + z = 2
# 3x + 8y + z = 12
#     4y + z = 2

#Define Matrix A and b
A = [1 2 1; 3 8 1; 0 4 1]

b = [2; 12; 2]

#Augument the matrix

Ab = [A b]

#Get the size of the Matrix
m, n = size(Ab)

#Form a upper triangular matrix 

#Start with first pivot (1,1)
#First, eliminate first element of the second row i.e (2,1) step
Ab[2, :] = Ab[2, :] - Ab[2, 1]/Ab[1, 1] * Ab[1, :]

#Second, eliminate first element of the third row i.e (3,1) step
Ab[3, :] = Ab[3, :] - Ab[3, 1]/Ab[1, 1] * Ab[1, :]


#Move to the second pivot (2,2)

#Thirdly, eliminate second element of third row

Ab[3, :] = Ab[3, :] - Ab[3, 2]/Ab[2, 2] * Ab[2, :]
U = Ab[:, setdiff(1:size(Ab, 2), 4)]
c = Ab[:, 4]

# Solve the system using back substitution
x = zeros(n-1)
x[end] = Ab[end,end] / Ab[end,end-1]
