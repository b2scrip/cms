with open("menu.text") as fd:
    for line in fd:
        print("<a href="+line.split( )[1]+">" + line.split( )[0]+"</a>")
