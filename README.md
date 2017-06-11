# Biryani-or-Not-Biryani
Biryani or Not Biryani is a Biryani classifier. It predict a image is Biryani or not. 
## Getting Started
This instruction is for windows 10 machine. If you are using linux or mac this is more esear than that.
### Prerequisites
* Anaconda
* Python 3.5
* Tensorflow
### Installing
First you have to create a anaconda enviorment and activate it.
```
(C:\Anaconda3) C:\> conda create -n biryani python 3.5.2
(C:\Anaconda3) C:\> activate biryani
```
If you are using machine without GPU like me install CPU-only version of Tensorflow
```
(biryani)C:> pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow-1.1.0-cp35-cp35m-win_amd64.whl 
```
Now it's time to train Biryani model
```
python retrain.py --bottleneck_dir=bottlenecks --model_dir=inception \
--summaries_dir=training_summaries/long --output_graph=retrained_graph.pb \
--output_labels=retrained_labels.txt --image_dir=images
```
This command download google inception model and create new 
## Running the tests
