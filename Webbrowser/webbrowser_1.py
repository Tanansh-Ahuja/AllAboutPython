import webbrowser , sys, pyperclip
#all of this which is commented shows if you can send data from commandline
#sys.argv
#check if command line argument were passed
#if(len(sys.argv)>1):
#    address=' '.join(sys.argv[1:])
#else:
#    address = pyperclip.paste()
address=input("Enter address:  ")
webbrowser.open('https://www.google.com/maps/place/'+address)
    
