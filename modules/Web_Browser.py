import webbrowser

# webbrowser.open("www.google.com")
# help(webbrowser)

#https://docs.python.org/3/library/webbrowser.html?highlight=web%20browser#module-webbrowser

WindowsDefault = webbrowser.get(using='windows-default')
WindowsDefault.open_new("https://www.google.com")