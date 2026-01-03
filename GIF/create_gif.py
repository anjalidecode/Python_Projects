import imageio.v3 as iio

filenames = ['/home/vinay/Documents/Code/Python_Projects/GIF/pic1.jpeg', '/home/vinay/Documents/Code/Python_Projects/GIF/pic2.jpeg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('/home/vinay/Documents/Code/Python_Projects/GIF/pic.gif', images, duration = 500, loop = 0)
