
import numpy as np
from skimage import io
import matplotlib.pyplot as plt

def print_hi(name):
    print(f'Hi, {name}') 


if __name__ == '__main__':
    print_hi('Rozgrzewka')
    a = np.array([1, 3, 5, 7])
    # array([1, 3, 5, 7])
    b = np.arange(4)
    # array([0, 1, 2, 3])
    np.arange(2, 10, 1)
    # array([2, 3, 4, 5, 6, 7, 8, 9])
    np.linspace(0, 10, 6)
    # array([ 0.,  2.,  4.,  6.,  8., 10.])

    c = np.array([[1, 2, 3], [4, 5, 6]])

    d = np.zeros((2, 3))

    d = np.ones((2, 3))

    np.random.random((2, 3))

a[2:]
# array([5, 7])
c[:1]
# array([[1, 2, 3]])
c[:1,1:]
# array([[2, 3]])
for x in c:
    print (x)
    for y in x:
        print(y)

for x in c.flat:
    print(x)

[x for x in c if x[1] < 3]

print_hi('Przetwarzanie obrazu w NumPY')
# wgranie pliku z obrazem
pic = np.array(io.imread('http://analityk.edu.pl/wp-content/uploads/2020/01/fire.jpeg'))
# wyswietlamy obraz
plt.imshow(pic)
plt.show()

# obracamy obraz
plt.imshow(pic[::-1])
plt.show()

# odbicie lustrzane
plt.imshow(pic[:,::-1])
plt.show()

#  zblizenie samochodu
plt.imshow(pic[300:450,150:600])
plt.show()

# psujemy obraz
plt.imshow(pic+100)
plt.show()

# wyodrebniamy ogien
pic = np.array(io.imread('http://analityk.edu.pl/wp-content/uploads/2020/01/fire.jpeg'))
mask = pic[:,:,0] < 200
pic[mask] = 255
plt.imshow(pic)
plt.show()