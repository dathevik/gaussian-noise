# gaussian-noise
This is a script that is adding white gaussian random noise to a plot/spectrum using input data file (csv). It is using Signal to Noise Ratio to change the quality of the spectrum and noise spectrum and detect which SNR is better for noised spectrum.

Dependecies (python version > 3.6 , probably can work with lowers too)
  - matplotlib
  - numpy
  - pandas
  - os
  
What does the script do?
  1. Reads the input data csv file.
  2. Separates the columns to (wave and flux).
  3. Definea the signal as a DataFrame of wave and flux.
  4. Plots the signal/spectrum and normalized signal/spectrum
  4. Makes the gaussian randon noise.
  5. Defines Signal to Noise Ratio. 
  6. Adds noise to the signal/spectrum, degrading it 10 times.
  7. Plots every degraded noised signal/spectrum in the output folder

What do you need to do?
  1. Make sure you have all dependecies mentioned above
  2. Clone the reposity
  3. Run gaussian.py (there is no need to change anything)
  4. Enjoy results in the output file ;)
  Optional  
    1. You can add your csv data in input file and change the path
    2. Run the code have your own results 
    3. Play with std (standard deviation) to change the quantity/quality of noise
