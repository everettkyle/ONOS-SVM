import joblib
import scapy

# need to scale down the data and also reshape it
# need to figure out the dimensions of the data
# also looking for different features

x_test = 1.7
y_test = 1

filename = 'fin_model.sav'
loaded_model = joblib.load(filename)

result = loaded_model.score(x_test, y_test)
print(result)
