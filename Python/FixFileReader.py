from __future__ import print_function
import re

c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []
c8 = []
c9 = []

param1 = re.compile("([^,]*)?")
param2 = re.compile("([^,])([,])(.*)")

with open('NoCommentsFixFiles/newgeneric.ebook.txt') as file:
    for line in file:
        c1.append(line[0])
        c2.append(line[2:7])
        c3.append(line[8:10])
        c4.append(line[11])
        c5.append(line[13:16])
        c6.append(line[17:20])
        c7.append(line[21:26])
        c8.append(line[26:57])
        c9.append(line[58:])
    

    length = len(c1)
    count = length - length
    while count < length:
        print("Field: " + c2[count].rstrip(), end=" ")
        if (not(c5[count].isspace())):
            print(" Position: " + c5[count], end = "  ")
        else:
            print ("", end = "")
        print("Operation: " + c8[count].rstrip(), end=" ")
        if (len(c9[count])> 1):
            m=param1.search(c9[count])
            n=param2.search(c9[count])
            if m:
                print(" " + m.group(1).rstrip(), end = ";")
            else:
                print()
            if n:    
                print(" " + n.group(3).rstrip())
            else:
                print()
        else: print(" " + c9[count].rstrip())
        count += 1
    
     
##string replacer

##if c8 = ADD-FIELD, FIXED-FIELD-EXTEND, REPLACE-STRING-GENERAL
##        print c2, c8, c9.regex split (non-greedy) p1,p2,p3
##        
##        = DELETE-FIELD, SORT-FIELDS, STOP-SCRIPT
##        print c8, c2
##        
##        =CHANGE-FIELD, DELETE-SUBFIELD,DELETE-SUBFIELD-DELIMITER
##        print c2,c8,c9
##        
##        =CHANGE-FIRST-IND
##        CHANGE-SECOND-IND
##        CHANGE-SUBFIELD
##        CONCATENATE-FIELDS
##        COPY-FIELD
##        DELETE-FIELD-COND
##        EDIT-SUBFIELD-HYPHEN
##        FIXED-CHANGE-VAL
##        FIXED-CHANGE-VAL-RANGE
##        REPLACE-STRING
##        print c2, c8 c9 p1 with p2
##
##        =CHANGE-FIRST-IND-MATCH,CHANGE-SECOND-IND-MATCH
##        print c2, c8 c9 p1 with p2 if p3
##
##        =COPY-SYSTEM-NUMBER
##        print 'c8 c2 'to' c9 params (4)
##
##        =FIXED-RANGE-OP
##        print c2, c8, 'on range' c5, c6
##
##        =COND-LOAD-VAL-POS
##        DELETE-FIXED-COND
##        load yes or no based on 2 params, column 5
