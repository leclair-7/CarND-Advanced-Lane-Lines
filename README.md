## Advanced Lane Finding

A project in the Udacity Self Driving Car Engineer Nanodegree. This is a less schoolish version of the project writeup that was submitted for grading.

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)


[//]: # (Image References)

[image1]: ./output-images/original-undistorted.png "Undistorted"
[image2]: ./output-images/road-original-undistorted.png "Undistorted Road"
[image3]: ./output-images/threshold-binary.png "Threshold Binary"
[image4]: ./output-images/Transformed.png "Region"
[image5]: ./output-images/Lines.png "Transformed Mask"
[image6]: ./output-images/result.png "Brightness Changed"


---

### Goals / Steps:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

### Dependencies
Found in the requirements.txt file

### Build Instructions
1 python -m venv laneline_envinstall</br>
2 source laneline_envinstall/bin/activate
2 pip install -r requirements.txt
3 Start jupyter notebook in the repo directory
4 In Juyter notebooks: Restart and Run All

#### 1 Camera Calibration
###### Computing the camera matrix and distortion coefficients (with example)

This is done on box 3-5 of Advanced–Lane–Finding.ipynb. To find the distortion coefficient, the number of rows and columns to find on the chessboard, six and nine were inputted in the open CV find chessboard corners function, this runs an edge detection algorithm, lastly, cv2.calibrateCamera camera uses all of the image points to create a distortion coefficient matrix.

![Undistorted][image1]

![Undistorted-also][image2]

#### 2 Color Processing and Transforms
The code for this can be found at box number 10 of Advanced–Lane–Finding.ipynb. To find the parameters and explore functions to isolate the lane lines, I created a file, Function and Parameter Testing.ipynb
, that checks every combination of thresholds for each channel (increments of 10) of the following color representations,: RGB, HSV, HLS, and Sobel thresholds ('x' and 'y' direction). After trial and error, I ended up using following: V channel HSV, H channel HLS, B of RGB, and R of RGB.

![Color Transformed][image3]

#### 3 Perspective Transform
This can be found on box 7 of Advanced–Lane–Finding.ipynb file. To carry out the perspective transform, points were found on the original image which bound the lane (and not irrelevant parts of the image); we'll call these source points. Then destination points of where the source points would be on the new image were derived. Lastly, cv2.getPerspectiveTransform is called, and the below images show before and after.

![Warped Perspective][image4]

#### 4 Identifying Lane Line Pixels and Outputting lines

This can be found in box 12 of Advanced–Lane–Finding.ipynb. The following is the method used to find the pixels relevant for lanes and fit their positions with a polynomial. First a histogram was made from the bottom half of the binary thresholded, perspective transformed image. All the non-zero points of each image were obtained. We then define a region (the 'window') x_min, x_max, y_min,y_max. For each window the number of indices with nonzero points was obtained (that reside in the window). The next window centers itself on the average of the previous windows nonzero indices. This allows for a continuous curve. A line approximation (np.polyfit) is then calculated from the nonzero values in the windows.

![lines][image5]

#### 5 Radius of Curvature

To find the radius of curvature I passed the same point values that were used to create the original polyfit, then each point used in the polyfit was scaled (meter/pixel), which indicates the number of meters per pixel on each axis. Then I obtained the curve radius (average of left and right). The offset from center was obtained by calculating the midpoint of the image, and the mid point of the left and right curves from the polyfit. Then we subtracted center_of_lane - midpoint of image and scaled it. This can be found on box 12 in the "fitted_curve_to_mask_on_screen" function towards.

#### 6 Result
Below is a sample image of the outputted image, the rectified image was warped back on the screen.

![Pipeline output][image6]
##### Output video
[Results](https://github.com/leclair-7/CarND-Advanced-Lane-Lines/blob/master/results.mp4)


#### 7 Discussion - Problems Faced and Improvements to Be Made
Two important challenges: 1- figuring out the combination of thresholds. 2- Making the pipeline handle bad (or error) classifications. For image processing I began using sobel-x and then a combination of the direction threshold and magnitude threshold. These were confusing. I then created a jupyter notebook, "Function and Parameter Testing.ipynb", which prints all possible thresholds in increments of 10 which led me to finding the parameters used. To handle bad classifications I created a handler class LaneWatcher (box 12) which uses the previous good lane detection when an outlier is detected or is a misclassification occurred.

##### Problems with the pipeline:
I think if only 1 lane line showed, then the pipeline would fail. I also think that a different coloration of the road may present issues on highlighting the lane region.

##### Improvements
To improve this I think the LaneWatcher class can be tested and refactored to give up and start over after a certain number of missclassifications. Also simplifying the binary thresholding would make the image processing more resilient to poor conditions since it may give too much information.
