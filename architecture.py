import os

l = ['mydata', 'mydata/tmp', 'mydata/augustus', 'mydata/gffread', 'mydata/gffread/cds', 'mydata/gffread/tr_cds', 'mydata/Orthofinder']

for test in l:
    if not os.path.exists(test):
        os.makedirs(test)