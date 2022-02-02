import datetime

print("---------------------------------------------------------")
mydt = datetime.datetime.now()
print("welcome to word counter")
print("it will count your words,characters,letters too!!")
print("Copyright (c) " + mydt.strftime("%Y") + " Suresh Pandiyan \n")

y_name = str(input("what is your name "))

y_filepath = str(input("enter your file path: "))
print("-----------------------------------------")
print("Hello "+y_name,",below your status about your file \n")

m = []

with open(y_filepath) as f:
	for mm in f:
		data = mm.rstrip().split(' ')
		m.append(data)


#print(m[0])

x = []
y = []

for xs in m:
	for kk in range(0,len(xs)):
		k = xs[kk][0].upper() + xs[kk][1:]
		#print(k)
		x.append(int(len(xs[kk])))
	y.append(len(xs))


ini = []

for pos in xs:
	for md in range(0,len(pos)):
		ti = ''.join(pos[md])
		ini.append(ti)

lop = ini


newy = []	
for kkm in ini:
	newy.append(kkm)

def inthechar(ss):
	if any(ss in newy for ney in newy):
		return ss+" typed |"
	else:
		return ss+" not-typed |"

_a = inthechar("a")
_b = inthechar("b")
_c = inthechar("c")
_d = inthechar("d")
_e = inthechar("e")
_f = inthechar("f")
_g = inthechar("g")
_h = inthechar("h")
_i = inthechar("i")
_j = inthechar("j")
_k = inthechar("k")
_l = inthechar("l")
_m = inthechar("m")
_n = inthechar("n")
_o = inthechar("o")	
_p = inthechar("p")
_q = inthechar("q")
_r = inthechar("r")
_s = inthechar("s")
_t = inthechar("t")
_u = inthechar("u")
_v = inthechar("v")
_w = inthechar("w")
_x = inthechar("x")
_y = inthechar("y")
_z = inthechar("z")


print("character ", sum(x))
print("words ", sum(y),"\n")

print("how many characters you are typed in fingers between a to z:  \n")
#ik = str(singlechar())			
print(_a, _b, _c, _d, _g, _h)
print(_i, _j, _k, _l, _l, _m)
print(_n, _o, _p, _q, _r, _s)
print(_t, _u, _v, _w, _x, _y, _z, " \n")
