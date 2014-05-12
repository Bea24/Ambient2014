'''
Created on 20/mar/2014

@author: Baleani
'''
import psutil,es02Tts

def cpu_monitor(threshold, interval):
    while(True):
        percentage = psutil.cpu_percent()
        if (percentage > threshold):
            es02Tts.say ("Warning the CPU is over %f"%percentage); #I use a f from another module
        time.sleep(interval) 
    
if __name__ == '__main__':
    cpu_monitor(10.0, 1)