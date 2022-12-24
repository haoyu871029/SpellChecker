from random import sample

source = open('spell-testset1.txt').read()
source = source.split('\n')
options = []
for line in source:
  words = line.split(' ')
  for word in words:
    # 尋找字串 word 中是否含有冒號‘：’，若找到則回傳冒號在字串中的索引位置，否則回傳 -1。
    index = word.find(':')
    if index != -1:
      word = word[:index]
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