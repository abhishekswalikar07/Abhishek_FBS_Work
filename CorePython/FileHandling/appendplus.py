fp=open("CorePython/FileHandling/Python_flow_chart.txt","a+")
print("Curser position:",fp.tell())

fp.write("\nFirstbit Solutions")

print("Curser position:",fp.tell())

fp.seek(0,0)
content=fp.read()
print(content)
fp.close()

