#! /usr/bin/env python

#pgm_id = pasta.py
#import sys

#f=sys.argv[1])
#in_pos=int(sys.argv[2]);

s_cnt=0
in_pos= int(input('n을 입력하세요.'))
in_list = []

with open('059.fasta','r') as f:
    for line_value in f:
        str_len=len(line_value)
        str_val=line_value
        for i in range(0,len(str_val)-1):
            i_str=""
            for j in range(0,in_pos):
                i_str+=str_val[i:i+1]
            
            search_str=str_val[i:i+in_pos]
            #print("-->",i_str,search_str)   
            if i_str == search_str:
                in_list.append(search_str)
                #print("search_str = ",search_str)    
                s_cnt += 1                
                #print("count= ",s_cnt)

print(in_list)
print("") 
print("###############") 
print("## 작업결과 ##")                                             
print("## 검색수 = ",s_cnt) 


