import cv2
import glob

violet = (164, 73, 163)

i = 0
for imPath in glob.glob("brick*/*.png"):
  i = i + 1
  im = cv2.imread(imPath)

  mask = cv2.inRange(im, violet, violet)
  centers = cv2.findNonZero(mask)

  txtPath = imPath[:-3] + 'txt'
  with open(txtPath, "w") as out:
    for center in centers:
      dx = 70
      dy = 45
      p = center[0]
      cv2.rectangle(im, (p[0]-dx, p[1]-dy), (p[0]+dx, p[1]+dy), violet, 3)
      out.write("pleurotes %d %d %d %d\n" % (p[0]-dx, p[1]-dy, 2*dx, 2*dy))

  cv2.imshow("im", im)
  cv2.waitKey()
