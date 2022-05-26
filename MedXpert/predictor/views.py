import base64
import io
import math
from io import BytesIO
from PIL import Image
import imghdr
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.shortcuts import render
from json.encoder import JSONEncoder
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from keras.models import load_model
from keras_preprocessing import image
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.views import APIView
import json
from django.core.files.storage import default_storage
import numpy as np
from tensorflow import Graph
import tensorflow as tf
import time

img_height, img_width=224,224
with open('imagenet_classes.json','r') as f:
    labelInfo=f.read()
labelInfo=json.loads(labelInfo)

img_height, img_width=224,224
with open('imagenet_classes2.json','r') as f:
    labelInfo1=f.read()
labelInfo1=json.loads(labelInfo1)

img_height, img_width=224,224
with open('imagenet_classes1.json','r') as f:
    labelInfo2=f.read()
labelInfo2=json.loads(labelInfo2)

model_graph=Graph()
with model_graph.as_default():
    gpuoptions = tf.compat.v1.GPUOptions(allow_growth=True)
    tf_session = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpuoptions))
    with tf_session.as_default():
        model=load_model('best_model.h5')

model_graph1=Graph()
with model_graph1.as_default():
    gpuoptions1 = tf.compat.v1.GPUOptions(allow_growth=True)
    tf_session1 = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpuoptions1))
    with tf_session1.as_default():
        model1=load_model('best_model1.h5')

model_graph2=Graph()
with model_graph2.as_default():
    gpuoptions2 = tf.compat.v1.GPUOptions(allow_growth=True)
    tf_session2 = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpuoptions2))
    with tf_session2.as_default():
        model2=load_model('best_model2.h5')

@csrf_exempt
def covid(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        data = body['imageFile']
        data=data.split(',')[-1]
        im = Image.open(BytesIO(base64.b64decode(data)))
        ts = time.time()
        path='media/'+str(ts)+'.jpeg'
        file=im.save(path, 'JPEG')
        file_url=default_storage.path(str(ts)+'.jpeg')
        img=image.load_img(file_url,target_size=(img_height,img_width))
        x=image.img_to_array(img)
        x=x/255
        x=x.reshape(1,img_height,img_width,3)
        with model_graph.as_default():
            with tf_session.as_default():
                predi=model.predict(x)
        predictedLabel=labelInfo[str(np.argmax(predi[0]))]  
    return JsonResponse({"data":predictedLabel})

@csrf_exempt
def malaria(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        data = body['imageFile']
        data=data.split(',')[-1]
        im = Image.open(BytesIO(base64.b64decode(data)))
        ts = time.time()
        path='media/'+str(ts)+'.jpeg'
        file=im.save(path, 'JPEG')
        file_url=default_storage.path(str(ts)+'.jpeg')
        img=image.load_img(file_url,target_size=(img_height,img_width))
        x=image.img_to_array(img)
        x=x/255
        x=x.reshape(1,img_height,img_width,3)
        with model_graph1.as_default():
            with tf_session1.as_default():
                predi=model1.predict(x)
        predictedLabel=labelInfo1[str(np.argmax(predi[0]))]  
    return JsonResponse({"data":predictedLabel})

@csrf_exempt
def pneumonia(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        data = body['imageFile']
        data=data.split(',')[-1]
        im = Image.open(BytesIO(base64.b64decode(data)))
        ts = time.time()
        path='media/'+str(ts)+'.jpeg'
        file=im.save(path, 'JPEG')
        file_url=default_storage.path(str(ts)+'.jpeg')
        img=image.load_img(file_url,target_size=(img_height,img_width))
        x=image.img_to_array(img)
        x=x/255
        x=x.reshape(1,img_height,img_width,3)
        with model_graph2.as_default():
            with tf_session2.as_default():
                predi=model2.predict(x)
        predictedLabel=labelInfo2[str(np.argmax(predi[0]))]  
    return JsonResponse({"data":predictedLabel})