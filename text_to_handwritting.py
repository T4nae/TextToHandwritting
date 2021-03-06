# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import random

# Custom font style and font size
myFont = ImageFont.truetype(r'./Fonts/HomemadeApple.ttf', 30)
imgpath= r"./pages/"
imgforpdf = []

def randpage():    
    pages = ['paper.jpeg', 'paper2.jpeg']
# Open an Image

    img = Image.open(imgpath +pages[random.randint(0,1)])
    return img
 
def randstring():
    random_string = ''
 
    for _ in range(10):
    # Considering only upper and lowercase letters
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
    # Convert to lowercase if the flip bit is on
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
    # Keep appending random characters using chr(x)
        random_string += (chr(random_integer))
 
    return random_string


#print(len(text)) 
#45 char per line #1125 char per page

def makeimg(chunks):
# Add Text to an image
# Call draw Method to add 2D graphics in an image
    size = 0
    newpage = 1125
    img = randpage()
    I1 = ImageDraw.Draw(img)
    p = 0
    for j in range(0,len(chunks)):
         chunk= chunks[j]
         I1.text((110, 100 + p*40), chunk, font=myFont,fill = 'Black')
         p = p + 1
         size = size + len(chunk)
         #print(size)         

# check if page is full and go to next page                                   
         if size == newpage:
            saveimg(img)
            img = randpage()
            I1 = ImageDraw.Draw(img)
            newpage = newpage + 1125
            p = 0
            #print(newpage)            
    return img            
 
# Display edited image
#img.show()
 
# Save the edited image
def saveimg(img):
    if os.path.exists(r"./temp"):
        pass
    else:
        os.mkdir(r"./temp")
    save = randstring() + 'save.jpeg'
    img.save(r"./temp/" + save)
    imgforpdf.append(save)
    #print(imgforpdf)
    
def savepdf():
    images = []
    for i in imgforpdf:
        im = Image.open(r"./temp/" + i)
        images.append(im)
    string = randstring()        
    images[0].save(string + 'save.pdf', save_all = True, append_images=images[1:] )
    
def deleteimg():
    for i in imgforpdf:
        os.remove(r'./temp/' + i)
    os.rmdir(r"./temp")

def main():
    print("Enter Text or File Path")
    text = input('> ')
    chunks=[]
    #dividing text into chunks of 45 char
    if os.path.exists(text):
        with open(text , 'r') as file:
            text = file.readlines()
            for j in text:
                if len(j) > 45:
                    temp= [j[i:i+45] for i in range(0, len(j), 45)]
                    for k in temp:
                        chunks.append(k)
                elif j == '\n':
                    chunks.append(' '*45)
                else:
                    chunks.append(j)
    else:
            chunksize = 45
            chunks = [text[i:i+chunksize] for i in range(0, len(text), chunksize)]                
            #print(text)
            
    #print(chunks)
    saveimg(makeimg(chunks))
    savepdf()
    deleteimg()
    
if __name__ == '__main__':
    main()
