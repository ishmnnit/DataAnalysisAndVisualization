f=open("wb",'r+')
line=f.read()
#print line
#line=json.load
start=0
end=0
output_map={}
while 1:
	start=line.find('[',start)+1
        end=line.find(']',end)+1
        if start==0:
		break;
        w=line[start+1:end-2]
        z=line[(line.find(':',end))+1:(line.find('.',end))]
	if not w.isdigit():
	        output_map[w]=z

stopword = open("stopword", 'r+')
for s1 in stopword:
	s=s1.strip()
	if s in output_map:
		output_map.pop(s)

for key, value in output_map.iteritems() :
	print ("%s,%s"%(key,value))
