from tkinter import *
from tkinter import filedialog
root = Tk()
root.fileName = filedialog.askopenfilename()
from PIL import Image
from PIL import ImageFilter
#function necessary for determining the imagefile name from the path of the file.
def filepre(name):
    name1 = name.split(':')[1]
    name2 = name1.split('/')
    name3 = name2[len(name2) - 1]
    i = (".tiff", ".bmp", ".png", ".jpg")
    if (name3.endswith(i) == True):
        return(name3)

name=filepre(root.fileName)

my_array=[0,0,0,0,0,0,0,0,0,0,0,0,0]
#function for determining the size of image
def image_size(event):
    my_array[0]+=1
    img = Image.open(name)
    print(img)
    print(img.size)

#function for determining the format of image
def image_format(event):
    my_array[1]+= 1
    img = Image.open(name)
    print(img.format)

#function for displaying the image in the default image viewer.
def image_show(event):
    my_array[2] += 1
    img = Image.open(name)
    img.show()

#function for cropping the image.
def image_crop(event):
    my_array[3]+=1
    img = Image.open(name)
    x,y = img.size
    print(x,y)
    x1 = int(input("Enter the X1 coordinate :"))
    y1 = int(input("Enter the Y1 coordinate :"))
    x2 = int(input("Enter the X2 coordiante :"))
    y2 = int(input("Enter the Y2 coordinate :"))
    #if negative value is entered.
    if(x1<0 or y1<0 or x2<0 or y2<0):
        print("\nInvalid Input as one or more input is negative")
    #if all the values are positive.
    else:
        #area to be cropped.
        area =(x1,y1,x2,y2)
        cropped_img = img.crop(area)
        cropped_img.show()

#function for combining two different images.
#the second image choosen must have size more than the first image.
def image_combine(event):
    my_array[4]+=1
    img = Image.open(name)
    img.show()
    root.fileName = filedialog.askopenfilename()
    name1 = filepre(root.fileName)
    moon = Image.open(name1)
    moon.show()
    x,y=img.size
    if(img.size <= moon.size):
        area = (0,0,x,y)
        moon.paste(img,area)
        moon.show()
    else:
        print("Invalid Input as size of second  image is less than that of first image ")

#function to display the red, green and blue channels of any image.
def image_channels(event):
    my_array[5] += 1
    img = Image.open(name)
    img.show()
    r,g,b=img.split()
    r.show()
    g.show()
    b.show()

#function to display after mergining different channels(red,green,blue) of any image.
def image_merge(event):
    my_array[6] += 1
    img = Image.open(name)
    img.show()
    r, g, b = img.split()
    new_img = Image.merge("RGB",(b,r,g))
    new_img0 = Image.merge("RGB", (b, g, r))
    new_img1 = Image.merge("RGB", (g, b, r))
    new_img10 = Image.merge("RGB", (g, r, b))
    new_img2 = Image.merge("RGB", (r, b, g))
    new_img.show()
    new_img0.show()
    new_img1.show()
    new_img10.show()
    new_img2.show()

#unction to display after mergining different channels(red,green,blue) of any 2 random images.
#there can be 120 different combinations can be made as each image has rgb content.
#so we have rgb from first image and rgb from second image.
#we have to fill 3 places.
#first place can be filled with 6 choices.
#second place can be filled with 5 choices.
#third place can be filled with 4 choices.
#6*5*4 = 120 different images.
def image_diffmerge(event):
    my_array[7] += 1
    root.fileName = filedialog.askopenfilename()
    name2 = filepre(root.fileName)
    img = Image.open(name2)
    root.fileName = filedialog.askopenfilename()
    name3 = filepre(root.fileName)
    img1 = Image.open(name3)
    if(img.size == img1.size):
        r,g,b = img.split()
        r1,g1,b1 = img1.split()
        #here we are just showing only 9 combinations from 120 combinations
        new_img = Image.merge("RGB",(r,g,b1))
        new_img1 = Image.merge("RGB", (r, g1, b))
        new_img2 = Image.merge("RGB", (r1, g, b))
        new_img3 = Image.merge("RGB", (r, g1, b1))
        new_img4 = Image.merge("RGB", (r1, g, b1))
        new_img5 = Image.merge("RGB", (r1, g1, b))
        new_img6= Image.merge("RGB",(r,g,g1))
        img.show()
        new_img6.show()
        img1.show()
        new_img.show()
        new_img1.show()
        new_img2.show()
        new_img3.show()
        new_img4.show()
        new_img5.show()
    else:
        print("Invalid Input as images selected have different sizes ")

#function to resize the image
#it is different from cropping the image.
def image_resize(event):
    my_array[8] += 1
    img = Image.open(name)
    print(img.size)
    x1 = int(input("Enter the resize length :"))
    y1 = int(input("Enter the resize width :"))
    if(x1<=0 or y1<=0):
        print("Invalid Input as one of the input is negative or zero")
    else:
        img1 = img.resize((x1,y1))
        img.show()
        img1.show()

#function to display the flipped image.
def image_flip(event):
    my_array[9] += 1
    img = Image.open(name)
    flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    flip_img1 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img.show()
    flip_img.show()
    flip_img1.show()

#function to rotate the image.
def image_spin(event):
    my_array[10] += 1
    img = Image.open(name)
    flip_img = img.transpose(Image.ROTATE_90)
    flip_img1 = img.transpose(Image.ROTATE_180)
    flip_img2 = img.transpose(Image.ROTATE_270)
    img.show()
    flip_img.show()
    flip_img1.show()
    flip_img2.show()

#function to change the mode of image
def image_modes(event):
    my_array[11] += 1
    img = Image.open(name)
    #this is CMPK mode.
    CMYK = img.convert("CMYK")
    img.show()
    CMYK.show()
    #this is black and white mode
    black_white = img.convert("L")
    black_white.show()

#function to add filter to the image
#it can add blur, detail and edge filters
def image_filter(event):
    my_array[12] += 1
    img = Image.open(name)
    blur = img.filter(ImageFilter.BLUR)
    details = img.filter(ImageFilter.DETAIL)
    Edges = img.filter(ImageFilter.FIND_EDGES)
    img.show()
    blur.show()
    details.show()
    Edges.show()

#function to determine which function of the program was used most number of time.
def max_used(event):
    z=max(my_array)
    if my_array[0]==z:
        print("Image Size is used most")
    elif my_array[1]==z:
        print("Image Format is used most")
    elif my_array[2] == z:
        print("Image Show is used most")
    elif my_array[3] == z:
        print("Crop Image is used most")
    elif my_array[4] == z:
        print("Combine Image is used most")
    elif my_array[5] == z:
        print("Image Channels is used most")
    elif my_array[6] == z:
        print("Merge Channels is used most")
    elif my_array[7] == z:
        print("Merge different channels is used most")
    elif my_array[8] == z:
        print("Resize Image is used most")
    elif my_array[9] == z:
        print("Flip image is used most")
    elif my_array[10] == z:
        print("Spin image is used most")
    elif my_array[11] == z:
        print("Image Mode is used most")
    elif my_array[12] == z:
        print("Filter image is used most")

#code for GUI buttons
button_1= Button(root,bg="black",fg="white",text="Determine Size")
button_1.bind("<Button-1>",image_size)
button_1.pack(fill=X)
button_2= Button(root,bg="black",fg="white",text="Determine Format")
button_2.bind("<Button-1>",image_format)
button_2.pack(fill=X)
button_3= Button(root,bg="black",fg="white",text="Show Image")
button_3.bind("<Button-1>",image_show)
button_3.pack(fill=X)
button_4= Button(root,bg="black",fg="white",text="Crop Image")
button_4.bind("<Button-1>",image_crop)
button_4.pack(fill=X)
button_5= Button(root,bg="black",fg="white",text="Combine Image")
button_5.bind("<Button-1>",image_combine)
button_5.pack(fill=X)
button_6= Button(root,bg="black",fg="white",text="Image Channels")
button_6.bind("<Button-1>",image_channels)
button_6.pack(fill=X)
button_7= Button(root,bg="black",fg="white",text="Merge Channels")
button_7.bind("<Button-1>",image_merge)
button_7.pack(fill=X)
button_8= Button(root,bg="black",fg="white",text="Merge Different Channels")
button_8.bind("<Button-1>",image_diffmerge)
button_8.pack(fill=X)
button_9= Button(root,bg="black",fg="white",text="Resize Image")
button_9.bind("<Button-1>",image_resize)
button_9.pack(fill=X)
button_10= Button(root,bg="black",fg="white",text="Flip Image")
button_10.bind("<Button-1>",image_flip)
button_10.pack(fill=X)
button_11= Button(root,bg="black",fg="white",text="Spin Image")
button_11.bind("<Button-1>",image_spin)
button_11.pack(fill=X)
button_12= Button(root,bg="black",fg="white",text="Image Modes")
button_12.bind("<Button-1>",image_modes)
button_12.pack(fill=X)
button_13= Button(root,bg="black",fg="white",text="Image Filter")
button_13.bind("<Button-1>",image_filter)
button_13.pack(fill=X)
button_14= Button(root,bg="black",fg="white",text="Most Used")
button_14.bind("<Button-1>",max_used)
button_14.pack(fill=X)
#never miss the next line.
root.mainloop()