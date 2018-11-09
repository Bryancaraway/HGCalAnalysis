log_list =[]
fine_list=[]

with open("cell_uv_map.csv") as f:
    log_list.append(f.read())

for log in log_list:
    lines = log.splitlines()
    for idx,line in enumerate(lines):

#Layer #, Wafer U, Wafer V, Cell U, Cell V
        if idx == 0:
            continue
        if idx%(len(lines)/10) == 0:
            print "Working...."
        values = line.split(",")
        fine_wafer = values[0]+","+values[1]+","+values[2]
        if fine_wafer not in fine_list:
            fine_list.append(fine_wafer)
            #print fine_wafer

fine_list.sort()

with open("fine_wafers.csv","w+") as outPut:
    for wafer in fine_list:
        #print wafer
        outPut.write("%s\n" % wafer)
        
