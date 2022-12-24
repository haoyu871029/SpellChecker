import re
from collections import Counter

def words(text): 
  return re.findall(r'\w+', text.lower())

word_count = Counter(words(open('big.txt').read()))

N = sum(word_count.values())
def percent(word): return word_count[word] / N # float

letters  = 'abcdefghijklmnopqrstuvwxyz'
def edits1(word):
    # 單字分屍
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]

    # 使用者可能少打一個字，故修正:
    deletes    = [L + R[1:]               for L, R in splits if R]
    # 使用者可能其中兩個字母打相反，故修正:
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    # 使用者可能某個字母打錯，故修正:
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    # 使用者可能在字母之間的空隙多打一個字母，故修正:
    inserts    = [L + c + R               for L, R in splits for c in letters]
    # 使用者可能某個字母不小心打了兩次，故修正:
    doubles    = [L + R[0] + R         for L, R in splits if R]
    # 使用者可能某連續字母少打了一個，故修正:
    one = [L + R[1:] for L, R in splits if len(R)>1 and R[0]==R[1]]
    return set(deletes + transposes + replaces + inserts + doubles + one)

def correction(word): 
    return max(candidates(word), key=percent)

def candidates(word): 
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    return set(w for w in words if w in word_count)

def edits2(word): 
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
    
# app

import streamlit as st
# command in termianl: 'streamlit run 111062692.py'
# change somewhere in 111062692.py, then you can see the "always rerun" at the top-right of your screen
# choose "always rerun" to automatically update your app every time you change its source code.

st.title("Spellchecker")

choice = open('output.txt').read()
choice = choice.split('\n')

option_a = st.selectbox('Choose a word or ... ',choice)
option_b = st.text_input('or type your own!!')

result = st.sidebar.checkbox('Show original word') 
# result = 是否勾選

def run(original_word):
  if result == True:
    st.write('Original word: *%s*'%original_word)
  cw = correction(original_word)

  if original_word == cw:
    st.success("--- *%s* --- is the correct spelling!"%original_word)
  else:
    st.error("Correction: *%s*"%cw)

if option_b != '' and option_a != ' ':
  original_word = option_b
  run(original_word)

if option_b != '' and option_a == ' ':
  original_word = option_b
  run(original_word)

if option_b == '' and option_a != ' ':
  original_word = option_a
  run(original_word)