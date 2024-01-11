# 導入函式庫
import numpy as np  
import tensorflow as tf
from matplotlib import pyplot as plt
import os
import datetime

# mse for loss, sgd for optimizer
use_mse = False
# 設定損失函數和優化器
loss_function = 'mse' if use_mse else 'sparse_categorical_crossentropy'
optimizer_function = 'SGD'

# 載入 MNIST 資料庫的訓練資料，並自動分為『訓練組』及『測試組』
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 將 training 的 input 資料轉為1維並正規化
x_train_norm = x_train.reshape(60000, 28*28).astype('float32') / 255.0
x_test_norm = x_test.reshape(10000, 28*28).astype('float32') / 255.0

# 將 training 的 label 進行 one-hot encoding，例如數字 7 經過 One-hot encoding 轉換後是 0000001000，即第7個值為 1
y_train_one_hot = tf.keras.utils.to_categorical(y_train) 
y_test_one_hot = tf.keras.utils.to_categorical(y_test) 

#tfboard lordir
log_dir = "logs2\\fit\\" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir, histogram_freq=1)

# 建立簡單的線性執行的模型
model = tf.keras.models.Sequential([
    # Add Input layer, 隱藏層(hidden layer) 有 512個輸出變數
    tf.keras.layers.Dense(units=512, input_dim=784,  kernel_initializer='normal',activation='relu', name='layers_dense'), 
    # Add output layer
    tf.keras.layers.Dense(units=10,  kernel_initializer='normal',activation='softmax', name='layers_dense_3')
])

# 編譯: 選擇損失函數、優化方法及成效衡量方式
model.compile(loss=loss_function, optimizer=optimizer_function, metrics=['accuracy']) 

# 進行訓練, 訓練過程會存在 train_history 變數中
if use_mse:
    train_history = model.fit(x=x_train_norm, y=y_train_one_hot, validation_split=0.2, epochs=5, batch_size=100, 
                              verbose=2,callbacks=[tensorboard_callback]) 
else:    
    train_history=model.fit(x=x_train_norm, y=y_train, epochs=25,  validation_data=(x_test_norm, y_test),batch_size=100, 
                            verbose=2,callbacks=[tensorboard_callback])

# 顯示訓練成果(分數)
scores = model.evaluate(x_test_norm, y_test_one_hot if use_mse else y_test)  
print("\t[Info] Accuracy of testing data = {:2.1f}%".format(scores[1]*100.0)) 

# 預測(prediction)
X = x_test_norm[0:1,:]
predictions = model.predict(X)
print(predictions)

# Create side-by-side plots
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(x_test[0])

#train_history.history.keys()
plt.subplot(1, 2, 2)
plt.plot(train_history.history['accuracy'])  
plt.plot(train_history.history['val_accuracy'])  
plt.plot(train_history.history['loss'])  
plt.plot(train_history.history['val_loss'])  

plt.title('Train History')  
plt.ylabel('acc')  
plt.xlabel('Epoch')  
plt.legend(['acc', 'val_acc','loss', 'val_loss'], loc='upper left')  
plt.show()
