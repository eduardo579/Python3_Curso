import webbrowser, sys

direccion = ' '.join(sys.argv[1:])
webbrowser.open('https://www.google.com/maps/place/' + direccion)