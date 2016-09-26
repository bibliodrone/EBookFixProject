import re

#form = re.compile("^\d\s.{5}.\s{6|[\d\s]{3)\s[\d\s]{3}\s.+\w+\s+[\w\d],?[\w\d].+$")
#splitter = re.compile("(\b)")
splitter = re.compile("^\d|\s\s+|,|\n")
fRange = re.compile("\d")
func = re.compile("[A-Z]+-+")
empty = re.compile("      ")
rng = " range "


with open('cleansprgr.txt', 'rt') as f:

    for line in f:
        strOut = "start "
        startField=line[2:8]
        rangeVal=line[13:20]
        function=line[27:47]
        pred=line[21:26]
        params = line[58:]

#Starting with field, pred range if present
        if re.match(fRange,rangeVal):              
            strOut=strOut + startField.rstrip() + " in range "+ rangeVal
            
        else:
            strOut = strOut + startField.rstrip()

        if re.search(empty,pred):
            continue
        elif not re.search(empty,pred):
            strOut = strOut + " " + pred.title().rstrip() + " "
    
        strOut = strOut + function.title() + " "
        print (strOut, end="")

        if len(params)>0:
            params = re.sub(",$",",_",params)
            
            params = str(params).split(",",1)
            params = " --> ".join(params)
        else: params = str(params)

        print(params)
        #for item in params:
        #    print(item, end = "")
        print()
        
        """
        if re.search(func, line):
        
        if re.search(fRange, line[2]):
            strOut = strOut + line[1] + rng + line[2]
            line[2] =""
        else: strOut = strOut + line[1]

        print (strOut, " ..do function ", line[2:])
        strOut = "Start from "
        
        print ("Start from",line[1], line[2:], ">>", len(line))
    """
