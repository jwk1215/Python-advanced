#! /usr/bin/env python

f = 'read_sample.csv'

def read_csv(f):
    ret = []
    with open(f,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(",")
                print(header)
                print()
                continue
            splitted = line.strip().split(',')
            print(splitted)
            d = dict(zip(header, splitted))
            print(d)
            ret.append(d)
    return ret  
         
ret = read_csv(f)
print(ret)






