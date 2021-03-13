# lines we are looking for have the form:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
print(len(x.split()))
# a list formed from the line has 7 elements
# the second member of the list should have an '@' sign in it

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) != 7: continue
    if words[0] != 'From': continue
    if not '@' in words[1]: continue
    print(words[2])