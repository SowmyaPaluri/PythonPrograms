file = open('txt.txt','w')
file.write("A girl is playing\n")
file.write("She is in a playground\n")
file.write("The sky above is pink\n")
file.write("A balloon is in the sky\n")
file.write("The balloon is blue\n")
file.close()
f2 = open('result.txt','w')
articles = 0
the = ''
with open('txt.txt','r') as file:
    for line in file:
        articles += line.count('the')
        articles += line.count('a')
        articles += line.count('an')
f2.write(f"The number of articles in txt.txt file are {articles}\n")
with open('txt.txt','r') as file:
    for line in file:
        if 'the' in line or 'The' in line:
            f2.write(line)
            print()
f2.close()
    

