img = imread('car.jpeg'); %reads pepper.pgm and mickey.png images and stores it into img

img_1d = reshape(img, 1, []); %reshapes the previously created 2D image matrix, img, into a vector 

dlmwrite('input.txt', img_1d, 'delimiter', ' '); %writes the vector into the input.txt file


