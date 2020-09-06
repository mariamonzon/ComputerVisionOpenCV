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


Imagine you have multiple objects but instead of an image, you have a video
sequence. You can do object detection on each frame but you also need to know
which bounding box in one frame corresponds to which one in the next
frame. The class of algorithms that track an object from one frame to the next are
called object tracking algorithms. In object detection, you are searching for
objects in the entire image. In tracking, you know the location of the object in
the previous frame and that information can be used to reduce the search space
and make tracking fast. Tracking algorithms often learn the appearance of
the object and some of them can re-identify the object if it disappears and then
reappears in the frame. The next important problem is called image
segmentation. Sometimes it is not enough to put a bounding box around the object
of interest. We want to find a group of pixels that belong to the object, not
just a bounding box around it. This grouping of pixels in two different
classes is called image segmentation. Another problem closely
related to segmentation is called natural image matting - where the goal is
to segment the image into two classes - background and foreground.
Unlike image segmentation where a pixel can belong to only one class, in natural
image matting boundary pixels belong partially to the background and
partially to the foreground. So at the boundary the pixel value that we observe
is a mixture of the background and the foreground and these things are very
common when we are looking at very fine structures like a strand of hair. And
then there are many types of domain-specific recognition algorithms. For
example, many recognition algorithms have been specifically developed for
biometrics. You may know about face recognition, fingerprint recognition, iris
recognition and even gait recognition - which means you can be identified in a
video based on how you walk. In document analysis, we use text recognition which
is used to convert an image of the document into text. Image recognition
techniques are also used in other places where we want to detect fraud or find
if a merchandise is fake or real. In addition sometimes we need more granular
information about a person or object in the scene. For example in addition to
detecting the faces we may want to locate the landmarks on the face or
estimate the head pose. In some other applications we may also want to
estimate the pose of the entire body. Until now we have focused on problems
where we are trying to extract information from the image or a group of
images. For example, we discussed 3D reconstruction where a bunch of images
were taken and 3D information was extracted. Then we looked at recognition
problems like image classification, object detection, etc where we tried to
figure out what is inside the images. Now let me go over a third category of
problems where we are not necessarily trying to extract information from the
images but we are trying to expand the capabilities of a camera.
This class of problems fall under computational photography. The goal of
computational photography is to computationally bypass the limitations
of the camera. For example, you can take multiple images of a scene with
different exposure settings, merge the images together and produce a high
dynamic range photo that would not have been possible using a standard camera.
You could also take a video of a scene and create a super high resolution
picture whose resolution is much higher than the frames of the video or you
could convert a grayscale image to color. Sometimes additional hardware optics is
used to create a new kind of camera. A fine example of this was the light field
camera that uses a special lens to not only capture the intensity of light but
also the direction of light. With the light field camera you can change the
focus of an image even after it has been acquired. One of the crowning
achievements of computational photography was the recent imaging of a
black hole. Imaging a black hole would have required a telescope as large as
the earth itself. Instead the event horizon telescope project used a network
of eight different telescopes from around the globe these images were time
stamped using atomic clocks. The image recorded on a single telescope is
extremely low resolution but together the eight telescopes acted like one
giant telescope to bring us the first high-resolution image of a black hole.
You can clearly see how Computer Vision is having such a huge impact across
multiple domains. I hope this video has given you a good idea of a vast number
of problem domains in Computer Vision. This is an exciting field for
researchers and engineers. 

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
### Erosion / Dilation 
###  Implementing morphological operations from scratch. 
###  Opening and Closing 
### Connected Component Analysis 
### Contour Analysis 
### Blob Detection
### Coin Detection
