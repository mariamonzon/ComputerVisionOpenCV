# Introduction to Computor Vision  OpenCV
##  1. Getting Started with OpenCV 
### Introduction to computer vision 
The difference between Image processing aand computer vision is that in image processing the input is an image
and the output is also typically an image. Sometimes the output image is an
improved version of the input image and sometimes it is just a processed version
of the input image. 
Similarly we can also think of edge detection as image processing
because the input is an image and the output is a processed version of the
image. 
On the other hand in computer vision the input is an image
and the output is usually some information. 
For example, in face  recognition the input is an image and the output is the identity of the person.
Similarly in object detection, the input is an image and the output is the
location and labels of objects in image. 
The main problems trated in computer vision can be rechognised as:

-  Image Processing: 
    - image denoising, restoration and enhancement
    - video compresion
    - image binarization and processing: edge detection corner detection 
-  3D reconstruction from 2D images
    - Stereo Vision: two images of the scene are taken from two different viewpoints using calibrated cameras. The depth at each pixel is estimated by finding which point in one               
    image corresponds to which point in the other image and this is followed by triangulation. This approach is extended to structure from motion technique.
    - Visual slam:  stands for simultaneous localization and mapping. This is a robotics application where a camera mounted on a robot is used to build a 3D structure of the   
    scene around it. 
    - Geometric CV: Instead of using one image if we use three images of an object lit from three different directions we can uniquely recover the shape of the object 
    up to a scale. This technique is called photometric stereo unlike stereo algorithms here the light is moved instead of the camera.
    -  Image alignement: calibrate a camera automatically you show it a checkerboard pattern from multiple viewpoints.  Feature matching and detection is also used in image 
    alignment.  Image alignment is one of those fundamental building blocks in computer vision. 
    that you get to use in
    - Motion estimation:  ind how each pixel in one frame has moved in the other frame as in videos the motion between the frames is small.  Motion estimation
    has many applications like video compression and video stabilization.
 - Recognition: The goal of image classification is to label an input image with the class that describes the image .  If there are multiple objects we need to first find a 
     bounding box around them before classifying them and these algorithms are called object detection algorithms. Given an input image they return an array of bounding boxes and 
    class label for every bounding box. 

### Basic image operations 
### Mathematical operations on images 
###  Sunglass filter : A simple application
###  Bitwise operations 
### Image Annotation 
###  QR code detection 

## 2. Video IO and GUI 
### Video IO using HighGUI 
### Keyboard as input device 
### Using the mouse for image annotation 
### Adding trackbar controller to your OpenCV application

## 3. Binary Image Processing 
### Thresholding 
In many computer vision tasks, we need to process a binary image.
A binary image consists of pixels that are either completely black ( pixel value 0 ) or completely white ( pixel value 255 ). 
It is easier to come up with algorithms which work on binary images. 
One of the easiest ways of creating Binary images from grayscale images is using Thresholding. Thresholding is one such example where we can simply use an OpenCV function and not worry about the implementation correctness and efficiency.
```cpp
    double cv::threshold    (   
    InputArray  src,     # src is the input array ot image (multiple-channel, 8-bit or 32-bit floating point).
    OutputArray     dst, # dst is the output array or image of the same size and type and the same number of channels as src.
    double  thresh,      # thresh is the threshold value.
    double  maxval,      # maxval is the maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.
    int     type         # type is thethresholding type ( THRESH_BINARY, THRESH_BINARY_INV, etc )
    )
```
### Erosion / Dilation 
- **Dilation** is used to merge or expand white regions which may be close to each other and
- **Erosion** is used to separate or shrink white regions
Dilation and Erosion operations are achieved by using dilate and erode functions of OpenCV

```cpp
    void cv::dilate    (    InputArray     src,
    OutputArray     dst,
    InputArray     kernel,
    Point     anchor = Point(-1,-1),
    int     iterations = 1,
    int     borderType = BORDER_CONSTANT,
    const Scalar &     borderValue = morphologyDefaultBorderValue() 
    )
        
    void cv::erode    (    InputArray     src,
    OutputArray     dst,
    InputArray     kernel,
    Point     anchor = Point(-1,-1),
    int     iterations = 1,
    int     borderType = BORDER_CONSTANT,
    const Scalar &     borderValue = morphologyDefaultBorderValue() 
    )
```
        // Parameters

        src input image; the number of channels can be arbitrary, but depth should be CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
        dst output image of the same size and type as src.
        kernel structuring element used for dilation; if elemenat=Mat(), a 3 x 3 rectangular structuring element is used.
        anchor position of the anchor within the element; default value (-1, -1) means that the anchor is at the element center.
        iterations number of times dilation is applied.
        borderType pixel extrapolation method.
        borderValue border value in case of a constant border

###  Implementing morphological operations from scratch 
###  Opening and Closing 
### Connected Component Analysis 
### Contour Analysis 
### Blob Detection
### Coin Detection
