import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
import math


with open(”laurel_yanny.wav”, ”rb”) as f:
    f = 'laurel_yanny.wav'
    sampleRate, data = wavfile.read(f)

    print("sample rate: ", sampleRate)
    print("shape of data: ", data.shape)


def plot_time_vs_speaker(data, output_filename):
     time = data.shape[0]
     x_axis = [x for x in range(time)]
     plt.plot(x_axis, data)
     plt.title("Time versus Physical Position")
     plt.xlabel("Time")
     plt.ylabel("Phsyical Position/Displacement")
     plt.savefig(output_filename + '.png', format='png')
     plt.close()


 plot_time_vs_speaker(data, "audio_signal")



def generateFourierTransform(data):
    fourier_transformed_data = np.fft.fft(data)
    print("shape of transformed data: ", fourier_transformed_data.shape)
    print(fourier_transformed_data[0])
    x_axis = [x for x in range(fourier_transformed_data.shape[0])]

    plt.plot(x_axis, np.absolute(fourier_transformed_data))
    plt.title("Fourier Transform")
    plt.xlabel("Time")
    plt.ylabel("Fourier Transform Magnitude")
    plt.savefig("fourier_transofrm" + ".png", format = 'png')
    plt.close()

def getSpectogram(data):
    size = 500  # 500 sample chunks
    n_chunks = data.shape[0] // size
    coeffs = np.zeros((n_chunks, 80))

    for i in range(n_chunks):
         chunk = data[i * size: i * size + size]
         transformed = np.abs(np.fft.fft(chunk))
         coeffs[i] = np.log(transformed[:80]) # only get first 80 coeffs


    fig, ax1 = plt.subplots()
    plt.imshow(coeffs, cmap='hot')
    ax1.set_ylim(1, 80)  # set axis from 1 to 80
    plt.xlabel("Index")
    plt.ylabel("Frequency")
    plt.title("Spectrogram")
    plt.savefig('spectrogram.png', format='png')
    plt.close()


 # 3E

 def save_wav_file(data, threshold, low=False):

     data = (np.absolute(data) * 1.0 / np.max(np.absolute(data)) * 32767).astype(np.int16)
     with open(str(threshold) + ".wav", "wb") as f:
         sample_rate = sampleRate
         if low:
             sample_rate *= 1.3
         sample_rate = int(sample_rate)
         wavfile.write(f, sample_rate, data)

 def zero_out_frequencies(data, threshold):
     f = 'laurel_yanny.wav'
     sampleRate, data = wavfile.read(f)
     data = np.fft.fft(data)
     print("fourier: ", data)

     data[:42200] = 0

     data = np.fft.ifft(data).real
     data = (np.absolute(data) * 1.0 / np.max(np.absolute(data)) * 32767).astype(np.int16)

     with open("zero_above_" + str(42200) + ".wav", "wb") as f:
         wavfile.write(f, sampleRate, data)

     # inverse_fourier = np.absolute(inverse_fourier)
    # save_wav_file(data, threshold)


 # high_thresholds = [5, 10, 15, 20, 30, 100, 200]

 # high_thresholds = [x for x in range(100000) if x % 1000 == 0]

 # high_thresholds = [10]
 # for threshold in high_thresholds:
 # high = 400000
 # ow = 42000
 # zero_out_frequencies(data, low, high)
 zero_out_frequencies(data, 42000)

 save_wav_file(data, "temp")
 transformed_data = np.fft.fft(data)
