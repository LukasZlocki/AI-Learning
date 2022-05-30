
import numpy as np
from skimage import io
import matplotlib.pyplot as plt

def main():
 
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


# Call main function
if __name__ == "__main__":
    main()  