"""
Module: comp110_lab08

Modules with some functions for Lab 08 practice problems.
"""
from cImage import *
import math

def double(oldimage):
    """ 
    Returns a new image that is a copy of
    oldImage, but twice the size.
    """
    oldw = oldimage.getWidth()    
    oldh = oldimage.getHeight()

    newim = EmptyImage(oldw*2,oldh*2)   

    for row in range(newim.getHeight()):
        for col in range(newim.getWidth()):
            originalCol = col//2
            originalRow = row//2
            
            oldpixel = oldimage.getPixel(originalCol, originalRow)

            newim.setPixel(col, row, oldpixel)
        
    return newim
    
def resize(imageFile):
    """ 
    Code to test the double function.
    """
    old_image = FileImage(imageFile)
    image_window = ImageWin("Image Processing", old_image.getWidth(), old_image.getHeight())
    old_image.draw(image_window)
    
    double_image = double(old_image)   
    double_image_window = ImageWin("Image Processing", 
        double_image.getWidth(), double_image.getHeight()) 
    double_image.draw(double_image_window)

    
    image_window.exitOnClick()
    double_image_window.exitOnClick()

def halve(oldimage):
    """ 
    Returns a new image that is a copy of
    oldImage, but half the size.
    """

    return oldimage # you will replace this line


def display_bird():
    """
    Displays image from image_file in an ImageWindow
    """
    image = FileImage("green-bird.gif")
    image_window = ImageWin("Green bird",
          image.getWidth(), image.getHeight())
    image.draw(image_window)
    image_window.exitOnClick()

def make_jailbird(image):
    """
    Returns a copy of image in which regions with 
    green pixels are replaced by alternating white
    and black lines
    """

    return image  # you will replace this line

def test_jailbird(imageFile):
    """ 
    Code to test the jailbird function.
    """
    image = FileImage(imageFile)
    image_window = ImageWin("Image Processing",image.getWidth(),
                    image.getHeight())
    image.draw(image_window)
    
    new_image = make_jailbird(image)
    new_image_window = ImageWin("Image Processing",new_image.getWidth(),
                    new_image.getHeight())
    new_image.draw(new_image_window)
    new_image_window.exitOnClick()
    image_window.exitOnClick()