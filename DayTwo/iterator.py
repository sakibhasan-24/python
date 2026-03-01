#iterator is something that can be LOOP over

#list is iterable


#what is iterator???
#iterator is something that gives value one by one using next() function
letters=["a","b","c","d"]

for l in letters:
    print(l.upper())


print(list(map(str.upper,letters)))
# print(reversed(letters))