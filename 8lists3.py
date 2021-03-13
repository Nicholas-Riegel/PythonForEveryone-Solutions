fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 7 and words[0] == 'From' and '@' in words[1]:
        print(words[2])
        
