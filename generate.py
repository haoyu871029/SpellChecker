from random import sample

source = open('spell-testset1.txt').read()
source = source.split('\n')
options = []
for line in source:
  words = line.split(' ')
  for word in words:
    if word.find(':') != -1:
      word = word[:word.find(':')]
    options.append(word)
options = [" "]+sample(options,len(options))

# write into txt file
with open('output.txt', 'w') as f:
  for i in options:
    f.write("%s\n"%i)

# test
choice = open('output.txt').read()
choice = choice.split('\n')
choice