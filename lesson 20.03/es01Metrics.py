'''
Created on 20/mar/2014

@author: Baleani
'''
import os
#to not exe the module in the class

def print_sys_metrics(): #can be used imported in other module
        
    uname = os.uname
    
    print uname
    print "OS Type: %s\nHost: %s\nKernel: %s %s\nArchitecture: %s"%(uname)
    #need 5 %s for all the fields because kernel has 2 parametres
    
    load_avg = os.getloadavg()
    
    print "Load Average: \n %s(1min)\n %s(5min)\n %s(15min)"%(load)
    
    #memory=os.open("cat /proc/meminfo") #solo così non vedo risultato                                                 
    memory=os.open("cat /proc/meminfo").read()
    
    #to split strings amongs lines
    memory_array = memory.split("\n")
    
    #to select only values (elements) I want to see
    print "Total Memory: %s"%memory_array[0].split(":")[1].strip()    
    print "Free Memory: %s"%memory_array[1].split(":")[1].strip()
    
    print memory_array
    
if __name__ == '__main__':

    print_sys_metrics() #I have to call something in main
    
    