import numpy as np
import pandas as pd
from keras import Sequential
from keras.layers import Dense

sudoku_dataset = pd.read_csv("sudoku.csv")

unsolved = sudoku_dataset["puzzle"]
solved = sudoku_dataset["solution"]

solved = np.array([list(map(int, x)) for x in unsolved]) / 9.0
unsolved = np.array([list(map(int, x)) for x in unsolved]) / 9.0


model = Sequential([
    Dense(128, activation='relu', input_shape=(81,)),
    Dense(128, activation='relu'),
    Dense(81, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer="adam", metrics='accuracy')

model.fit(unsolved, solved, epochs=10, batch_size=10)

#print(model.predict([unsolved[:1]]))
