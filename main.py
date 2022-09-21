# import scipy.io.wavfile as wavfile
# import numpy as np
# import matplotlib.pyplot as plt
# import math
#
#
# def multiply(x, y):
#     # pad with 0's (shorter one will also be padded w 0 to length N)
#     longer_2N = 2 * max(len(x), len(y))
#     while len(x) < longer_2N:
#         x.append(0)
#
#     while len(y) < longer_2N:
#         y.append(0)
#
#     # calculate discrete fourier transform for both padded x and y
#     x_tranformed = np.fft.fft(x)
#     y_tranformed = np.fft.fft(y)
#
#     # calculate convolution
#     multiplied = x_tranformed * y_tranformed
#     convolved = np.fft.ifft(multiplied)
#
#     carry = 0
#     final_answer = []
#     for c in convolved: # process each value
#         curr = int(round(c.real, 0)) + carry
#         carry = curr // 10 if curr >= 10 else 0  # must carry over a 1
#         curr %= 10  # in case we carried over, recalculate
#         final_answer.append(curr)
#
#     # remove trailing 0's to clean up
#     while final_answer[-1] == 0:
#         del final_answer[-1]
#
#     return final_answer
#
# x = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# q3c = multiply(x, y)
#
#
# #
# # # Question 3
# # with open(”laurel_yanny.wav”, ”rb”) as f:
# f = 'laurel_yanny.wav'
# sampleRate, data = wavfile.read(f)
#
# print("sample rate: ", sampleRate)
# print("shape of data: ", data.shape)
#
#
# # part b
# def plot_time_vs_speaker(data, output_filename):
#     time = data.shape[0]
#     x_axis = [x for x in range(time)]
#     plt.plot(x_axis, data)
#     plt.title("Time versus Physical Position, 3B")
#     plt.xlabel("Time")
#     plt.ylabel("Phsyical Position/Displacement")
#     plt.savefig(output_filename + '.png', format='png')
#     plt.close()
#
#
# plot_time_vs_speaker(data, "3b")
#
#
# # part c
#
# fourier_transformed_data = np.fft.fft(data)
# print("shape of transformed data: ", fourier_transformed_data.shape)
# print(fourier_transformed_data[0])
# x_axis = [x for x in range(fourier_transformed_data.shape[0])]
#
# plt.plot(x_axis, np.absolute(fourier_transformed_data))
# plt.title("Fourier Transform")
# plt.xlabel("Time")
# plt.ylabel("Fourier Transform Magnitude")
# plt.savefig("3c" + ".png", format = 'png')
# plt.close()
#
# # 3D
#
# size = 500  # 500 sample chunks
# n_chunks = data.shape[0] // size
# coeffs = np.zeros((n_chunks, 80))
#
# for i in range(n_chunks):
#     chunk = data[i * size: i * size + size]
#     transformed = np.abs(np.fft.fft(chunk))
#     coeffs[i] = np.log(transformed[:80]) # only get first 80 coeffs
#
#
# fig, ax1 = plt.subplots()
# plt.imshow(coeffs, cmap='hot')
# ax1.set_ylim(1, 80)  # set axis from 1 to 80
# plt.xlabel("Index")
# plt.ylabel("Frequency")
# plt.title("3d Spectrogram")
# plt.savefig('3d_spectrogram.png', format='png')
# plt.close()
#
#
#
# # 3E
#
# def save_wav_file(data, threshold, low=False):
#
#     data = (np.absolute(data) * 1.0 / np.max(np.absolute(data)) * 32767).astype(np.int16)
#     with open(str(threshold) + ".wav", "wb") as f:
#         sample_rate = sampleRate
#         if low:
#             sample_rate *= 1.3
#         sample_rate = int(sample_rate)
#         wavfile.write(f, sample_rate, data)
#
#
# # print(np.absolute(np.fft.fft(data)))
# def zero_out_frequencies(data, threshold):
#     f = 'laurel_yanny.wav'
#     sampleRate, data = wavfile.read(f)
#     data = np.fft.fft(data)
#     print("fourier: ", data)
#
#     data[:42200] = 0
#
#     data = np.fft.ifft(data).real
#     data = (np.absolute(data) * 1.0 / np.max(np.absolute(data)) * 32767).astype(np.int16)
#
#     with open("zero_above_" + str(42200) + ".wav", "wb") as f:
#         wavfile.write(f, sampleRate, data)
#
#     # inverse_fourier = np.absolute(inverse_fourier)
#    # save_wav_file(data, threshold)
#
#
# # high_thresholds = [5, 10, 15, 20, 30, 100, 200]
#
# # high_thresholds = [x for x in range(100000) if x % 1000 == 0]
#
# # high_thresholds = [10]
# # for threshold in high_thresholds:
# # high = 400000
# # ow = 42000
# # zero_out_frequencies(data, low, high)
# zero_out_frequencies(data, 42000)
#
# save_wav_file(data, "temp")
# transformed_data = np.fft.fft(data)
#
#
# # thresholds = [42000]
# # for threshold in thresholds:
# #     curr_high_transformed = transformed_data.copy()
# #     # curr_high_transformed10urr_high_transformed > threshold] = 0
# #     curr_high_transformed[:threshold] = 0
# #     curr_high_transformed[:43008 - threshold] = 0
# #     curr_low_transformed = transformed_data.copy()
# #     # curr_low_transformed[curr_low_transformed < threshold] = 0
# #     curr_low_transformed[threshold:] = 0
# #     curr_low_transformed[:43008 - threshold] = 0
# #     curr_high_transformed_reverted = np.fft.ifft(curr_high_transformed)
# #     curr_low_transformed_reverted = np.fft.ifft(curr_low_transformed)
# #     save_wav_file(curr_high_transformed_reverted, "zero_above_sym_" + str(threshold))
# #     save_wav_file(curr_low_transformed_reverted, "zero_below_sym_" + str(threshold), low=True)
# #
import sys
print(sys.maxsize)