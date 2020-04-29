fhand = open()
for line in fhand:
    line = line.rstip()
    if not line.startswith ('From ') : continue
    words = line.split()
    print(words[2])
