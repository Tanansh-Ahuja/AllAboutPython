import webbrowser
google=input("Google search: ")
#webbrowser.open_new_tab("http://www.google.com/search?btnG=1&q=%s" %google)
#The above line of code can also be written. its not wrong.
webbrowser.open_new_tab("http://www.google.com/search?btnG=1&q=" +google)
