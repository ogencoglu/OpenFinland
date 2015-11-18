'''
Author         : Oguzhan Gencoglu
Contact        : oguzhan.gencoglu@tut.fi
Created        : 26.09.2015
Latest Version : 18.11.2015
'''

import numpy as np
import matplotlib.pyplot as plt
import lasagne
from lasagne.layers import InputLayer, DenseLayer, DropoutLayer
from lasagne.layers.dnn import Conv2DDNNLayer as ConvLayer
from lasagne.layers import MaxPool2DLayer as PoolLayer
from lasagne.layers import LocalResponseNormalization2DLayer as NormLayer
from lasagne.utils import floatX
import pickle
import skimage.transform
import cv2
from datetime import datetime
from copy import deepcopy

def load_model(pretrained_file):
    
    net = {}
    net['input'] = InputLayer((None, 3, 224, 224))
    net['conv1'] = ConvLayer(net['input'], num_filters=96, filter_size=7, stride=2)
    net['norm1'] = NormLayer(net['conv1'], alpha=0.0001) # caffe has alpha = alpha * pool_size
    net['pool1'] = PoolLayer(net['norm1'], pool_size=3, stride=3, ignore_border=False)
    net['conv2'] = ConvLayer(net['pool1'], num_filters=256, filter_size=5)
    net['pool2'] = PoolLayer(net['conv2'], pool_size=2, stride=2, ignore_border=False)
    net['conv3'] = ConvLayer(net['pool2'], num_filters=512, filter_size=3, pad=1)
    net['conv4'] = ConvLayer(net['conv3'], num_filters=512, filter_size=3, pad=1)
    net['conv5'] = ConvLayer(net['conv4'], num_filters=512, filter_size=3, pad=1)
    net['pool5'] = PoolLayer(net['conv5'], pool_size=3, stride=3, ignore_border=False)
    net['fc6'] = DenseLayer(net['pool5'], num_units=4096)
    net['drop6'] = DropoutLayer(net['fc6'], p=0.5)
    net['fc7'] = DenseLayer(net['drop6'], num_units=4096)
    net['drop7'] = DropoutLayer(net['fc7'], p=0.5)
    net['fc8'] = DenseLayer(net['drop7'], num_units=1000, nonlinearity=lasagne.nonlinearities.softmax)
    output_layer = net['fc8']

    model = pickle.load(open(pretrained_file, 'rb'))
    classes = model['synset words']
    mean = model['mean image']
    lasagne.layers.set_all_param_values(output_layer, model['values'])
    
    return model, classes, mean, output_layer
    
def prep_image(im, mean):
    
    # Resize so smallest dim = 256, preserving aspect ratio
    h, w, _ = im.shape
    if h < w:
        im = skimage.transform.resize(im, (256, w*256/h), preserve_range=True)
    else:
        im = skimage.transform.resize(im, (h*256/w, 256), preserve_range=True)

    # Central crop to 224x224
    h, w, _ = im.shape
    im = im[h//2-112:h//2+112, w//2-112:w//2+112]
    
    # rawim = np.copy(im).astype('uint8')
    
    # Shuffle axes to c01
    im = np.swapaxes(np.swapaxes(im, 1, 2), 0, 1)
    
    # Convert to BGR
    im = im[::-1, :, :]
    
    im = im - mean
    
    return floatX(im[np.newaxis])
    
def bgr2rgb(im):
    
    b,g,r = cv2.split(im)       # get b,g,r
    
    return cv2.merge([r,g,b])  
    
if __name__ == "__main__":  
    
    # Load pretrained model
    model, classes, mean, output_layer = load_model('vgg_cnn_s.pkl')
    
    start = datetime.now()
    # Prepare image for test
    im = cv2.imread('image_name.jpg')
    swap = True
    if swap:
        im = bgr2rgb(im)
    original = deepcopy(im)
    im = prep_image(im, mean)
    
    # Get probabilities
    prob = np.array(lasagne.layers.get_output(output_layer, im, deterministic=True).eval())
    top5 = np.argsort(prob[0])[-1:-6:-1]
    text =''
    print("\n")
    for i in range(5):
        print(i+1,'- '+ classes[top5[i]])
        text = text + str(i+1) + ' - '+ classes[top5[i]] + '\n'
    stop = datetime.now()
    print("\n\n\t\tScript Running Time: %s"%str(stop - start))
    
    if not swap:
        original = bgr2rgb(original)
    fig = plt.figure(figsize=(17, 14), facecolor='w')
    plt.imshow(original)
    #fig.text(.1,0.4,text)
    fig.text(.2,-0.01,text)
    


