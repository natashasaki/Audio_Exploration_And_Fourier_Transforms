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
