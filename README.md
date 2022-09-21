# The-Sound-of-Fourier-Transform
Exploring how Fourier transforms can help us understand human sounds through the Laurel/Yanny audio clip

### Motivation
Explore working with audio modalities. Explore how Fourier transforms can help humans better understand sound. 

### Context
In 2018, the Laurel/Yanny audio clip became really popular due to the different ways people processed the audio. 
While some people heard “Laurel,” others heard the clip as “Yanny”.

I process the said clip and process it in different ways to better understand how or why people here one word versus the other. 

### Methodology
We generate a “spectrogram” of the signal, chop the signal up into 500- sample long blocks, and compute the Fourier transform for each chunk.

Then we alter the signal to sound more like “Laurel” or, more like “Yanny”. To do so, we experiment with different
threshold frequencies *t*, nameliy zeroing out values below and about this threshold.

### Exploration Findings and Images

![audio_signal](https://user-images.githubusercontent.com/56423291/191400364-31143b55-8dbe-405b-82c0-65e743d0e6db.png)
![fourier_transform](https://user-images.githubusercontent.com/56423291/191400368-2170d28f-54e4-42d8-bffe-6fa7bb9cb9da.png)
![spectrogram](https://user-images.githubusercontent.com/56423291/191400390-3248e7c0-1a68-4edb-9cf6-20e5185f2bd1.png)
![3D_Square_Root](https://user-images.githubusercontent.com/56423291/191400375-38c58ee1-5acf-479b-842b-9cd8d05408ee.png)
