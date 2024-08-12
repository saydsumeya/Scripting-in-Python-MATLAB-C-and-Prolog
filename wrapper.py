import subprocess

#runs a ccprog.c that adds one to each value
input_array = ["1", "2", "3", "4", "5"]
subprocess.run(["gcc", "ccprog.c", "-o", "ccprog"])
process = subprocess.run(["./ccprog"] + input_array, capture_output=True, text=True)
output_variable = process.stdout.strip()
print("C program (add 1) output:")
print(output_variable)

#runs haskell2.hs that 1 from 255 each time
input = ["1", "2", "3", "4", "5"]
subprocess.run(["ghc", "haskell2.hs", "-o", "haskell2"])
pro = subprocess.run(["./haskell2"] + input, capture_output=True, text=True)
output = pro.stdout.strip()
print("Haskell program (subtract 1) output:")
print(output)

#runs prolog.pl that reverses the input_array
array = ["1", "2", "3", "4", "5"]
prolog_input = "[" + ", ".join(map(str, array)) + "]."
result = subprocess.run(['swipl', '-g', 'reverse_list', '-t', 'halt', '-q', 'prolog.pl'], input=prolog_input,
                        capture_output=True, text=True)
print("Prolog program (reverse) output:")
prolog_output = result.stdout.strip().replace('[', '').replace(']', '').replace(',', ' ')
print(prolog_output)


#runs ccprog2.c that changes values based on threshold
subprocess.run(["gcc", "ccprog2.c", "-o", "ccprog2"])
process = subprocess.run(["./ccprog2"] + input_array, capture_output=True, text=True)
output_variable = process.stdout.strip()
print("C program (threshold) output:")
print(output_variable)

#runs matlab1.m file
matlab_executable = '/Users/sumeya/Desktop/MATLAB_R2023b.app/bin/matlab'
with open('matlab1.m', 'r') as file:
   matlabcode = file.read()

Matlab_process = subprocess.Popen([matlab_executable, '-nodisplay', '-nosplash', '-nodesktop'],
stdin=subprocess.PIPE, text=True)
Matlab_process.communicate(input=matlabcode)
print("Running MATLAB CODE 1")

#opens and reads input.txt file
with open('input.txt', 'r') as file:
    line = file.readline()
    input_array = [str(value) for value in line.split()]

#processes input.txt file using thresholding function
subprocess.run(["gcc", "ccprog2.c", "-o", "ccprog2"])
process = subprocess.run(["./ccprog2"] + input_array, capture_output=True, text=True)
output_variable = process.stdout.strip()
print("C program (threshold) output:")
print(output_variable)

#prints out output from previous command into new file, c_output.txt
with open('c_output.txt', 'w') as f:
  f.write(output_variable)



#reopens input.txt file to process haskell function to output new color flipped image 
with open('input.txt', 'r') as file:
    line = file.readline()
    input_array = [str(value) for value in line.split()]

subprocess.run(["ghc", "haskell2.hs", "-o", "haskell2"])
process = subprocess.run(["./haskell2"] + input_array, capture_output=True, text=True)
output = process.stdout.strip()
print("Haskell Program")
print(output)

with open('haskell_output.txt', 'w') as f:
  f.write(output)



#reopens file to implement prolog program to string to output a rotated image
with open('input.txt', 'r') as file:
    line = file.readline()
    input_array = [str(value) for value in line.split()]
prolog_input = "[" + ", ".join(map(str, input_array)) + "]."
r = subprocess.run(['swipl', '-g', 'reverse_list', '-t', 'halt', '-q', 'prolog.pl'], input=prolog_input,
                        capture_output=True, text=True)
print("Prolog program")
variable = r.stdout.strip().replace('[', '').replace(']', '').replace(',', ' ')
print(variable)

with open('prolog_output.txt', 'w') as f:
  f.write(variable)



#runs matlab2.m file to output all 4 images in one
matlab_executable = '/Users/sumeya/Desktop/MATLAB_R2023b.app/bin/matlab'
with open('matlab2.m', 'r') as file:
   matlabcode2 = file.read()

Matlab_process2 = subprocess.Popen([matlab_executable, '-nodisplay', '-nosplash', '-nodesktop'],
stdin=subprocess.PIPE, text=True)
Matlab_process2.communicate(input=matlabcode2)



