
"""
Created on Mon May  6 10:37:12 2023

@author: LoboM
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten

(X_train, Y_train), (X_test, Y_test) = keras.datasets.mnist.load_data()

X_train=X_train.reshape(len(X_train),28,28,1)
Y_train=Y_train.reshape(len(Y_train),1)
X_test=X_test.reshape(len(X_test),28,28,1)
Y_test=Y_test.reshape(len(Y_test),1)

X_train=X_train/255
X_test=X_test/255

print("Forma train de X: ", X_train.shape)
print("Forma train de Y: ", Y_train.shape)
print("Forma test de X: ", X_test.shape)
print("Forma test de Y: ", Y_test.shape)
idx=random.randint(0,len(X_train))
plt.imshow(X_train[idx,:])
plt.show()

model=Sequential([
    Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),
    MaxPooling2D((2,2)),
    Conv2D(32,(3,3),activation='relu'),
    MaxPooling2D((2,2)),
    
    Flatten(),
    Dense(64,activation='relu'),
    Dense(10,activation='softmax')
])


model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train,Y_train,epochs=5,batch_size=64,validation_split=0.1)

model.evaluate(X_test,Y_test)

idx2=random.randint(0,len(Y_test))
plt.imshow(X_test[idx2,:])
plt.show()

y_pred=model.predict(X_test[idx2,:].reshape(1,28,28,1)) 

print(np.max(y_pred))