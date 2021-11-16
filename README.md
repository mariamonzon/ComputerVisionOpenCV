# ComputerVisionOpenCV

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
