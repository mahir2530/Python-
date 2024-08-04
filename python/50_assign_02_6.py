n = int(input("Enter Your Basic Salary : "))

hra = ( n * 10 ) / 100
da = ( n * 20 ) / 100
ta = ( n * 10 ) / 100
pf = ( n * 20 ) / 100
ns = hra + da + ta - pf

print("Basic Salary : ", n)
print("H.R.A. : ", hra)
print("D.A. : ", da)
print("T.A. : ", ta)
print("P.F. : ", pf)
print("Net Salary : ", ns)
