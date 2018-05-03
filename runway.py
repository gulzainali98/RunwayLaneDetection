import cv2 as cv
import numpy as np
import math

import sys

print str(sys.argv[1])
img= cv.imread( str(sys.argv[1]), 0);
img2= cv.imread(str(sys.argv[1]));

def find_lines(img):
    img = cv.GaussianBlur(img, (3, 3), 5.0)
    edges = cv.Canny(img, 150, 350, apertureSize=3)
    minLineLength = (np.array(img).shape[1] * .15)
    maxLineGap = 5
    lines = cv.HoughLinesP(edges, rho=1, theta=np.pi / 180, threshold=100, minLineLength=minLineLength,
                            maxLineGap=maxLineGap)
    return lines

def find_thresholdedLines(arrDistance, arrPoints):
	counter=0
	index1=0
	maxDistance1=0
	for i in arrDistance:
		if(i> maxDistance1):
			maxDistance1=i
			index1=counter
		counter= counter+1

	counter=0
	index2=0
	maxDistance2=0
	for i in arrDistance:
		if i> maxDistance2 and counter!=index1:
			maxDistance2=i
			index2=counter
		counter= counter+1
	line1= arrPoints[index1]
	line2= arrPoints[index2]
	return line1,line2





edges = cv.Canny(img,150,350)


(thresh, im_bw) = cv.threshold(edges, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

lines = cv.HoughLinesP(im_bw,1,3.14/180,200)

# print lines

# for images where we have to find lines.
# print find_lines(img)

arrDistance=[]
arrPoints=[]
for a in find_lines(img):
		for x1,y1,x2,y2 in a:
			# print [x1,y1,x2,y2]
			arrDistance.append(math.sqrt(( (x1-x2)*(x1-x2) ) + ( (y1-y2) * (y1-y2) )))
			arrPoints.append([x1,y1,x2,y2])


line1,line2=find_thresholdedLines(arrDistance,arrPoints)


cv.line(img2,(line1[0],line1[1]),(line1[2],line1[3]),(0,255,0),2)
cv.line(img2,(line2[0],line2[1]),(line2[2],line2[3]),(0,255,0),2)


cv.imwrite('houghlines'+str(sys.argv[1]),img2)




cv.imwrite("grey.png",im_bw);