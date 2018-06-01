import os
path = '/home/ubuntu/ttr/TicketToRide'
imagePath=os.path.join(path,'Just3')
files = os.listdir(imagePath)
print('total files: ' + str(len(files))) 
i = 1

labelFile = open(os.path.join(path, 'threeTestSegment.txt'),'w')

for file in files:

	print(i)
#Segment 1
	if i>=1 and i<=12:
		labelFile.write('0\n')
	if i>=13 and i<=20:
		labelFile.write('0\n')
	if i>=21 and i<=30:
		labelFile.write('0\n')
	if i>=31 and i<=39:
		labelFile.write('0\n')
	if i>=40 and i<=48:
		labelFile.write('0\n')
		
	#Segment 2
	if i>=49 and i<=57:
		labelFile.write('1\n')
	if i>=58 and i<=66:
		labelFile.write('1\n')
	if i>=67 and i<=75:
		labelFile.write('1\n')
	if i>=76 and i<=84:
		labelFile.write('1\n')
	if i>=85 and i<=93:
		labelFile.write('1\n')
		
		
	#Segment 3
	if i>=94 and i<=102:
		labelFile.write('2\n')
	if i>=103 and i<=111:
		labelFile.write('2\n')
	if i>=112 and i<=120:
		labelFile.write('2\n')
	if i>=121 and i<=129:
		labelFile.write('2\n')
	if i>=130 and i<139:
		labelFile.write('2\n')
	if i==139:
		labelFile.write('2')
		
	i = i+1
	
labelFile.close()
