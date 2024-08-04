n = input('Enter The Name : ')
s = float(input('Enter The Sallary : '))

hra = (s * 10) / 100 
da = (s * 5) / 100
total = s + hra  + da
pf = (total * 6) / 100
fs = total - pf

print('H.R.A. : ',hra)
print('D.A. : ',da)
print('Total : ',total)
print('P.F. : ',pf)
print('F.S. : ',fs)