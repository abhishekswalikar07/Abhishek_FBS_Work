fp=open("CorePython/FileHandling/Python_flow_chart.txt","w+")
print("Curser position:",fp.tell())

fp.write("Core Python")

print("Cursor position:",fp.tell())

fp.seek(0,0)
print("Cursor position:",fp.tell())

content=fp.read()
print(content)
fp.close()