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

Dilation and Erosion operations are achieved by using dilate and erode functions of OpenCV. Structuring element is used to perform dilation and erosion operations. 
Structuring elements ( a.k.a Kernels ) are used to modify the shape of the blobs. These are used to scan the image and modify the pixels on the basis of some rule/algorithm ( which governs whether you are doing Erosion or Dilation or something else. 

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

There are 3 types of structuring elements supported by OpenCV. For creating structuring elements, OpenCV provides the function [**`cv::getStructuringElement`**](https://docs.opencv.org/4.1.0/d4/d86/group__imgproc__filter.html#gac342a1bb6eabf6f55c803b09268e36dc). You can also create any other structuring element using numpy arrays. It is simply a matrix.

1. Ellipse/Circular shaped
1. Rectangular shaped
1. Cross shaped

```cpp
kSize = 3;
Mat imageDilated1;
// element = cv::getStructuringElement(elementType, kernelSize, anchor)
Mat kernel = getStructuringElement(cv::MORPH_ELLIPSE,  cv::Size(kSize, kSize));
dilate(image, imageDilated1, kernel, Point(-1,-1), 1);
erode(image, imageEroded, kernel);
```

###  Opening and Closing 
If we want to remove small white spots, we should perform erosion followed by dilation so that the smaller white spots are removed, whereas the bigger white blobs are unchanged. Similarly you can remove black spots using dilation followed by erosion.
These operations are also given some names : Opening and Closing.

**Opening** refers Erosion followed by Dilation and these operations is used for clearing white blobs and

**Closing** refers Dilation followed by Erosion and are used for clearing black holes

Opening and Closing operations can be performed by combining erosion and dilation. It can also be done using special OpenCV functions

In OpenCV, the opening and closing operations are implemented using **MorphologyEx** function.

To specify between the opening and closing operation to be performed we specify an argument in the function [**`MorphologyEx`**](https://docs.opencv.org/4.1.0/d4/d86/group__imgproc__filter.html?fbclid=IwAR1GtoDsIv4Fi8o7vrZ8SGb3bb1uiU_Nyt94fc9J2sHKF7FlbDNT1fq-kI0#ga67493776e3ad1a3df63883829375201f) definition. The argument for opening operation and closing operations are [**`MORPH_OPEN`**] and [**`MORPH_CLOSE`**] respectively.

```cpp
void morphologyEx(Mat srcImage,         //Source image. The number of channels can be arbitrary. The depth should  CV_8U, CV_16U, CV_16S, CV_32F or CV_64F
                Mat imageMorphOpened,   //Destination image of the same size and type as source image
                MORPH_OPEN,             //Type of a morphological operation (MORPH_OPEN, MORPH_CLOSE ...)
                Mat structuringElement  //Structuring element. It can be created using getStructuringElement.
                Point  	anchor = Point(-1,-1),          // Anchor position with the kernel. Negative values mean that the anchor is at the kernel center.
                int  	iterations = 1,                 // Number of times erosion and dilation are applied.
                int  	borderType = BORDER_CONSTANT,   // Pixel extrapolation method.
                const Scalar &  	borderValue = morphologyDefaultBorderValue() //	Border value in case of a constant border. The default value has a special meaning.
                )
```
### Connected Component Analysis 
Connected Component Analysis (CCA) is a fancy name for labeling blobs in a binary image. So, it can also be used to count the number of blobs ( also called connected components ) in a binary image. Blobs are defined as group of pixels connected to each other. CCA will create a mask where all pixels corresponding to the background are 0, all pixels corresponding to the first blob, are 1, those corresponding to the second blob are 2 and so on and so forth.
### Contour Analysis 
### Blob Detection
### Coin Detection
