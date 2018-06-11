## Advanced Lane Finding
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)


[//]: # (Image References)

[image1]: ./output-images/original-undistorted.png "Undistorted"
[image2]: ./output-images/road-original-undistorted.png "Undistorted Road"
[image3]: ./output-images/threshold-binary.png "Threshold Binary"
[image4]: ./output-images/region-to-transform.png "Region"
[image5]: ./output-images/transformed-image.png "Transformed Mask"
[image6]: ./output-images/brightness-original.png "Brightness Changed"

The Project
---

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

The images for camera calibration are stored in the folder called `camera_cal`.  The images in `test_images` are for testing your pipeline on single frames.  If you want to extract more test images from the videos, you can simply use an image writing method like `cv2.imwrite()`, i.e., you can read the video in frame by frame as usual, and for frames you want to save for later you can write to an image file.  

To help the reviewer examine your work, please save examples of the output from each stage of your pipeline in the folder called `output_images`, and include a description in your writeup for the project of what each image shows. The video called `project_video.mp4` is the video your pipeline should work well on.  

The `challenge_video.mp4` video is an extra (and optional) challenge for you if you want to test your pipeline under somewhat trickier conditions.  The `harder_challenge.mp4` video is another optional challenge and is brutal!

If you're feeling ambitious (again, totally optional though), don't stop there!  We encourage you to go out and take video of your own, calibrate your camera and show us how you would implement this project from scratch!

## How to write a README
A well written README file can enhance your project and portfolio.  Develop your abilities to create professional README files by completing [this free course](https://www.udacity.com/course/writing-readmes--ud777).


Camera Calibration
Computing the camera matrix and distortion coefficients (with example)

To find the distortion coefficient, the number of rows and columns to find on the chessboard, six and nine were inputted in the open CV find chessboard corners function, this runs an edge detection algorithm, afterwords open Seabees calibrate camera uses all of the image points to create a distortion coefficient in matrix two

![alt text][image1]





2
And the code this can be found at box number 34. To find the parameters and explore functions to isolate the lane lines, I created a file that checks every combination of thresholds for each channel of the following color representations,: RGB, HSV, HLS, and so Sobel thresholds in the x and y directions. After trial and error, I ended up using the beat channel using the following: V channel HSV, HSV channel HLS, B of RGB, and read of RGB
3 this can be found on box 14 of the events – Lane – finding file
To fine to carry out the perspective, Points were found on the original image, these were found by trial and error to make a rectangle that would show abounding reason for where lane lines are most likely to appear, destination points of where this response would be on the new image, and a Matrix was calculated via the Seaview to don’t get perspective transform function, work perspective is called, and they are below image shows before and after.
This can be found in box 34 of the advanced nine finding code. The following is the method used to find the mainline pixels and fit their positions with a polynomial. First the binary threshold warped perspective transformed image was taken in the bottom half of the image in a histogram was made of the bottom half of the image, The number of windows was chosen, all the non-zero points of the each window were obtained. For each window the number of indices was obtained, and is it exceeded a threshold then the average horizontal axis index was obtained to put a new window. After the sleep was finished, hey Paul if it was a team with a number five function
To find the radius of curvature I passed the same point values that were used to create the original Polly fit, then I multiply each point used in the poly fit by scaling number, which indicates the number of meters per pixel on each axis. Then I obtain the curve radio by the formula then I obtained the radius of curvature for the left and the right by using the formula present it in the lectures.
