#this is in order to get the idea behind the sort function
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=False)
print(cars)

names = ["yordanos", "abebe", "zelalem"]

def hey(e):
	return len(e)
   
names.sort(key=hey)
print(names)