# mlp for binary classification
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from pandas import read_csv, DataFrame
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import generate_data
# load the dataset
path = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/ionosphere.csv'
data = generate_data.get_generated()
df = DataFrame(data)
#df = read_csv(path, header=None)
#print(f"================= Raw Data {type(df)} =====================")
print(df)
# split into input and output columns
X, y = df.values[:, :-1], df.values[:, -1]
print(f"================= Jacobs Data =====================")



print("================= This is X =====================")
print(X)
print("================= This is y =====================")
print(y)
# ensure all data are floating point values
#X = X.astype('float32')
# encode strings to integer
#y = LabelEncoder().fit_transform(y)

# split into train and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
print("================= Training/test shapes =====================")
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
# determine the number of input features
n_features = X_train.shape[1]
print(f"Number of features: {n_features}")
# define model
model = Sequential()
model.add(Dense(10, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
model.add(Dense(8, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(1, activation='sigmoid'))
# compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# fit the model
model.fit(X_train, y_train, epochs=150, batch_size=32, verbose=0)
# evaluate the model
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print("================= Results =====================")
print('Test Accuracy: %.3f' % acc)
# make a prediction

t = 630
while t <= 1260:
    t += 10
    row = [t, 1]
    yhat = model.predict([row])
    print('Predicted at %d: %.1f' % (t, yhat))