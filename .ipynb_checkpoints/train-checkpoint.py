{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "20dafa72",
   "metadata": {},
   "outputs": [],
   "source": [
    "from keras.optimizers import RMSprop\n",
    "from keras.preprocessing.image import ImageDataGenerator\n",
    "import cv2\n",
    "from keras.models import Sequential\n",
    "from keras.layers import Conv2D, Input, ZeroPadding2D, BatchNormalization, Activation, MaxPooling2D, Flatten, Dense,Dropout\n",
    "from keras.models import Model, load_model\n",
    "from keras.callbacks import TensorBoard, ModelCheckpoint\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import f1_score\n",
    "from sklearn.utils import shuffle\n",
    "import imutils\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e533663",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = Sequential([\n",
    "    Conv2D(100, (3,3), activation='relu', input_shape=(150, 150, 3)),\n",
    "    MaxPooling2D(2,2),\n",
    "    \n",
    "    Conv2D(100, (3,3), activation='relu'),\n",
    "    MaxPooling2D(2,2),\n",
    "    \n",
    "    Flatten(),\n",
    "    Dropout(0.5),\n",
    "    Dense(50, activation='relu'),\n",
    "    Dense(2, activation='softmax')\n",
    "])\n",
    "model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8028ce7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "TRAINING_DIR = \"./train\"\n",
    "train_datagen = ImageDataGenerator(rescale=1.0/255,\n",
    "                                   rotation_range=40,\n",
    "                                   width_shift_range=0.2,\n",
    "                                   height_shift_range=0.2,\n",
    "                                   shear_range=0.2,\n",
    "                                   zoom_range=0.2,\n",
    "                                   horizontal_flip=True,\n",
    "                                   fill_mode='nearest')\n",
    "\n",
    "train_generator = train_datagen.flow_from_directory(TRAINING_DIR, \n",
    "                                                    batch_size=10, \n",
    "                                                    target_size=(150, 150))\n",
    "VALIDATION_DIR = \"./test\"\n",
    "validation_datagen = ImageDataGenerator(rescale=1.0/255)\n",
    "\n",
    "validation_generator = validation_datagen.flow_from_directory(VALIDATION_DIR, \n",
    "                                                         batch_size=10, \n",
    "                                                         target_size=(150, 150))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b1c7680",
   "metadata": {},
   "outputs": [],
   "source": [
    "checkpoint = ModelCheckpoint('model2-{epoch:03d}.model',monitor='val_loss',verbose=0,save_best_only=True,mode='auto')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6810c04",
   "metadata": {},
   "outputs": [],
   "source": [
    "history = model.fit_generator(train_generator,\n",
    "                              epochs=10,\n",
    "                              validation_data=validation_generator,\n",
    "                              callbacks=[checkpoint])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
