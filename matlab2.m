
%reads input from input.txt, converts the input into an array, converts it
%into a matrix with dimesions of 256 by 256, then displays the original
%images for either image tested
input = fileread('input.txt');
input_array = uint8(str2num(input));
input_matrix = reshape(input_array, 256, 256);
figure()
imshow(input_matrix);
title('Original Image');

%reads image and implements the c program to output black and white image
output_variable = fileread('c_output.txt');
output_array = uint8(str2num(output_variable));
resized_matrix = reshape(output_array, 256, 256);
figure()
imshow(resized_matrix);
title('Black & White Image from C');

%reads image and implements the haskell program to output color flipped
%image
output = fileread('haskell_output.txt');
output_a = uint8(str2num(output));
resized = reshape(output_a, 256, 256);
figure()
imshow(resized);
title('Color Flipped Image using Haskell Program');

%outputs rotated image using prolog code
variable = fileread('prolog_output.txt');
array = uint8(str2num(variable));
matrix = reshape(array, 256, 256);
figure()
imshow(matrix);
title('Rotated Image using Prolog Program');


%utilize subplot to bring together all four images into one image file 
figure()

subplot(1, 4, 1);
imshow(input_matrix, []);
title('Original Image');

subplot(1, 4, 2);
imshow(resized_matrix, []);
title('Black & White Image from C');

subplot(1, 4, 3);
imshow(resized, []);
title('Color Flipped Image using Haskell Program');

subplot(1, 4, 4);
imshow(matrix, []);
title('Rotated Image using Prolog Program');

saveas(gcf, '4_results_from_Pepper.png');



