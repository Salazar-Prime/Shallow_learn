# Assignment 2

## You are required to do this assignment on google cloud. Please use Python 3.6 or above. Your personal computers can be either in Windows 10 or Ubuntu or OSX.

## Download the dataset
1. Download assignmen2.zip from Blackboard.
2. Upload the assignment2.zip to the google cloud. Use the 'upload' button on jupyter notebook.
3. Unzip assignment2.zip. Copy paste the following command in the google cloud terminal. Make sure to modify ```path_to_gcloud``` appropriately in the following command.
```
unzip path_to_gcloud/assignment2.zip
```
4. Navigate to the 'assignment2' folder
```
cd path_to_gcloud/assignment2/
```
5. Download the CIFAR-10 dataset
```
cd ie590/datasets
bash ./get_datasets.sh
```

## IPython
After you have the CIFAR-10 data, you should start the IPython notebook server from the assignment2 directory, with the ``` jupyter notebook``` command. 

## Questions
### 1. Fully-connected Neural Network (20 points)

The IPython notebook `FullyConnectedNets.ipynb` will introduce you to the modular layer design of neural networks, and then you will use those layers to implement fully-connected networks with an arbitrary number of hidden layers. To optimize these models, you will implement several popular update rules (Adam and RMSProp).

### 2. Batch Normalization (30 points)

In the IPython notebook `BatchNormalization.ipynb`, you will implement batch normalization, and use it to train deep fully-connected networks.

### 3. Dropout (10 points)

The IPython notebook `Dropout.ipynb` will help you implement Dropout and explore its effects on model generalization especially to prevent overfitting.

### 4. Convolutional Networks (30 points)

In the IPython Notebook `ConvolutionalNetworks.ipynb` you will implement several new layers that are commonly used in convolutional networks.

### 5. PyTorch / TensorFlow on CIFAR-10 (10 points)

For this last part, you will be working in either TensorFlow or PyTorch, two popular and powerful deep learning frameworks. **You only need to complete ONE of these two notebooks.** No extra credit will be given to students who do both. 
Open up either `PyTorch.ipynb` or `TensorFlow.ipynb`. In there, you will learn how these frameworks work. Next, you will train a conv-net of your own design on CIFAR-10 dataset to get the best performance you can. When you created instances on google cloud, pytorch or tensorflow is already installed in your virtual machine. 

## General guidelines
1. You can work on this assignment in one of the three platforms:
	1. Locally on your personal computer (it does not need to have a GPU)
	2. Purdue Scholar cluster (requires manual setup of pytorch/tensorflow with GPU)
	3. Google cloud
2. You MUST program in Python 3.6 or above

## Working on google cloud
* Follow the [instructions](https://github.com/cs231n/gcloud/) here to setup the google cloud.
* Install requirements.txt on the command line
```
pip3 install --user -r requirements.txt
```

## Submission instructions
* Create the PDF reports of the following ipython notebooks on jupyter: `FullyConnectedNets.ipynb`, `BatchNormalization.ipynb`, `Dropout.ipynb`, `ConvolutionalNetworks.ipynb` and `PyTorch.ipynb` or `TensorFlow.ipynb`. 
* Save the PDF reports in `assignment2/ie590` folder. 
* Run the following on the terminal to create a zip file of your solutions. 
```
zip -r assignment2_firstname_lastname.zip . -x "*.git*" "*ie590/datasets*" ".env/*"
```
* Submit the `assignment2_firstname_lastname.zip` on the Blackboard. 