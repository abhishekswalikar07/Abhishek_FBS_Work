fp=open("CorePython/FileHandling/Python_flow_chart.txt","r+")
print("Curser position:",fp.tell())

content=fp.read()
print(content)

print("Cursor position:",fp.tell())

fp.write("This is new line")

fp.seek(0,0) # Changes cursor position

content=fp.read()
print(content)
fp.close()
