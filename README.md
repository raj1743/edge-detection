# edge-detection

<p>Implemented the edge-detection using various alogorithms available from Open-CV and Pillow Libraries.</p>

# OpenCV

We can detect an edge froma image with Gradient-Magnitude and Gradient-Direction for which we require a kernel in both Horizontal and Vertical direction which is Gx and Gy respectively. 

![image](https://github.com/raj1743/edge-detection/assets/127628708/981e7f48-88d1-47a5-bbc5-6c0eb16d9345)

All the diffrent kernels are as follows:

## Soble Operator:
  
![image](https://github.com/raj1743/edge-detection/assets/127628708/eec012b5-edea-4078-bc16-2585faa11bdf)

## Scharr Operator

![image](https://github.com/raj1743/edge-detection/assets/127628708/eeadc2a6-733b-4e3e-8552-f3cb4a5dc9c9)

## Laplacian of Gaussian (LoG)

The Laplacian of an image with pixel intensity values:

![Screenshot from 2023-10-02 23-39-25](https://github.com/raj1743/edge-detection/assets/127628708/09e123c4-ba28-4ce6-8cb6-920975e697ff)

The input image is represented as a set of discrete pixels, we have to find a discrete convolution kernel that can approximate the second derivatives in the definition of the Laplacian. Two commonly used small kernels are:

![image](https://github.com/raj1743/edge-detection/assets/127628708/70726771-3fa7-4d13-95d6-9d57c0e44bf6)

# Pillow

 With the Pillow library we can detect the edge with "ImageFilter.FIND_EDGES" or by passing the kernel to ImageFilter.
