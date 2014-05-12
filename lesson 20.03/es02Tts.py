'''
Created on 20/mar/2014

@author: Baleani
'''
def say(text):
    
    wget_line = 'wget -q -U Chrome -O test.mp3 "http://translate.google.com/translate_tts?ie=UTF-8&tl=en&q='+text+"\""
    
    os.system(wget_line)
    
    os.system("mplayer -quiet -nolirc -msglevel all=-l test.mp3")
    
if __name__ == '__main__':
    string = ""
    while(string != "exit"):
        string = raw_input("Insert some word:\n>")
        if (string == "exit"):
            say ("Goodbye!")
        else:
            say(string)
    