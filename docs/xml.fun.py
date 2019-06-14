Filename = open('C:\\Users\\omarh\Malmo-0.36.0-Windows-64bit_withBoost_Python3.6\\Python_Examples\\okkk.txt') 
x = 0
y =0      
input_xml = ""                
while True:
    c = Filename.read(1)
    if not c:
        break
    if c != '\n':
      y = y +1
    if c == 'W':
      input_xml+= "<DrawEntity x= "+str(x)+"  y=\"9\" z="+str(y+1)+" \"type=\"Zombie\" />\n"
    if c == 'P':
      input_xml += "<DrawBlock x= " + str(x)+ " y=\"6\" z= " + str(y+1) +" \"type=\"air\" />\n"
    else:
        y = 0
        x= x+1