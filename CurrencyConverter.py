with open("currencyrates.txt") as f:
    a=f.readlines()




print(a)

currencydict={}
for line in a:
    parsed=line.split("\t")
    currencydict[parsed[0]]=parsed[1]
print(currencydict)