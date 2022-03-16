'''
zip() will return an iterator of tuples. We can convert that zip object to a dictionary using the dict() constructor.
'''
names = ["Raphael", "Tanya", "Miriam", "Leonard", "Owen", "Julie", "Haleema", "Mabel", "Stanley"]
#Key lest
c =[]
for x in names:
    c.append(x)
#Name length lsit
z = []
for i in names:
    z.append(len(i))
# Merge lists
f = zip(c,z)

k= []
l = []
#h,v are the keys and values
for h,v in f:
    #find the values that is smaller than 7 then append the keys and the values to 2 new list
    if v <7:
        k.append(h)
        l.append(v)
        continue
# Merge lists
q = zip(k,l)
#Converting zip object to dict using dict() contructor.
print(dict(q))

#Solution Two
r = zip(c,z)
o = dict(r)
u = {key:val for key, val in o.items() if val < 7}
print(u)
