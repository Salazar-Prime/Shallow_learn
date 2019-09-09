# Assignment 1

## You are required to do this assignment on google cloud. Please use Python 3.6 or above. Your personal computers can be either in Windows 10 or Ubuntu or OSX.

## Download the dataset
1. Download assignmen1.zip from Blackboard.
2. Upload the assignment1.zip to the google cloud. Use the 'upload' button on jupyter notebook.
3. Unzip assignment1.zip. Copy paste the following command in the google cloud terminal. Make sure to modify ```path_to_gcloud``` appropriately in the following command.
```
unzip path_to_gcloud/assignment1.zip
```
4. Navigate to the 'assignment1' folder
```
cd path_to_gcloud/assignment1/
```
5. Download the CIFAR-10 dataset
```
cd ie590/datasets
bash ./get_datasets.sh
```

## IPython
After you have the CIFAR-10 data, you should start the IPython notebook server from the assignment1 directory, with the ``` jupyter notebook``` command. If you are unfamiliar with IPython, you can also refer to the [IPython tutorial](http://cs231n.github.io/ipython-tutorial/).

## Questions
1. k-Nearest Neighbor classifier (20 points)
	* The IPython Notebook knn.ipynb will walk you through the implementation of the kNN classifier.
2. Training a Support Vector Machines (25 points)
	* The IPython Notebook svm.ipynb will walk you through the implementation of the SVM classifier.
3. Implement a Softmax classifier (20 points)
	* The IPython Notebook softmax.ipynb will walk you through the implementation of the Softmax classifier.
4. Two-Layer Neural Network (25 points)
	* The IPython Notebook two_layer_net.ipynb will walk you through the implementation of a two-layer neural network classifier.
5. Higher Level Representations: Image Features (10 points)
	* The IPython Notebook features.ipynb will walk you through this exercise, in which you will examine the improvements obtained by using higher-level representations as opposed to using raw pixel intensity values.



## General guidelines
1. You can work on this assignment in one of the three platforms:
	1. Locally on your personal computer (it does not need to have a GPU)
	2. Purdue Scholar cluster
	3. Google cloud
2. You MUST program in Python 3.6 or above

## Working locally
1. Install python 3.6 or above
2. Install the dependencies
```
cd assignment1
pip3 install -r requirements.txt
# Use this command to install the required modules dependencies
# You can use anaconda to create virtual environment and maintain your python modules.
```

## Working on google cloud
* Follow the [instructions](https://github.com/cs231n/gcloud/) here to setup the google cloud.
* Install requirements.txt on the command line
```
pip3 install --user -r requirements.txt
```
