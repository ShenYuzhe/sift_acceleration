1. running command

cd naive
python run.py <image_1> <image_2>

Note: 
Matching between pictures of different size is supported.
Size of image_1 should be larger or equal to image_2.

2. Acceleration
a) Detecting space maxima and minima
b) Assigning key point orientations.

3. Code Structure
siftdetector.py:
	detecting key points and generating key point descriptors.

siftmatch.py
	matching the key points between to images

cl/pyrlv.c
	kernel code for detecting space maxima and minima 

cl/keyopoint_orientation.c
	kernel code for assigning key point orientations

4. reference
original python algorithm is retrieved from:
	https://github.com/rmislam/PythonSIFT
We contribute our effort to accelerate this code and rewrite pieces of algorithms in C.


