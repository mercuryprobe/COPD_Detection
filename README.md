# COPD Detection
Detection of COPDs from the [ICBHI 2017 Challenge dataset](https://bhichallenge.med.auth.gr/ICBHI_2017_Challenge).

Note: Detailed information regarding the dataset generation, preprocessing, augmentation and prediction pipeline can be found in [The Report](https://github.com/mercuryprobe/COPD_Detection/blob/main/Report.pdf).

**Motivation**
- Medical professionals typically demonstrate low accuracies at detecting the presence of COPDs using Auscultation sounds [Yoonjoo Kim et al., 2021](https://www.nature.com/articles/s41598-021-96724-7).
- Need for liteweight, accurate mechanism for detection.

**Aim**
- Develop an ML model to utilise demographic and audio data to predict presence and class of COPDs.
- Exceed peak human baseline of 81% (demonstrated by Fellows, as noted by the aforementioned paper).

**Methodology**
- Generate demographic data from within the ICBHI dataset by filling missing values.
- Add crackling/wheezing information to dataset by reading audio file descriptions.
- Find out how well classification can be performed with oracle data about crackling/wheezing within the audio.
- Generate audio datasets by performing data augmentations - noisy, pitchshift, timeshift, timestretch audio files. Dataset expanded to size 4600.
- Create Mel Frequency and Chroma Based features from the data:
  - Mel Frequency Spectrograms: Extract non musical, granular information about power distribution for each frequency at a given timestep for a given audio file, on the Mel scale. Useful for detecting short bursts of audio (like crackling).
  - Mel Frequency Cepstral Coefficients (MFCCs): Transformed version of the spectrogram. Useful for detecting phenomes.
  - Chromagrams: Capture the energy distribution of musical pitches across time. Useful for detecting musical sounds (like wheezing).
  - Chroma Energy Normalised Statistics (CENS): Transformed version of Chromagram. More robus to variations in loudness and instrumentation.
- Generate audio features' graphs as inputs for a CNN architecture, and simultaneously flatten features to form 1D arrays of the representations, which can be utilised via numerical models as features.
- Perform PCA for cumulative explained variance of 95% to reduce number of features significantly.

**Results**
- CNNs performed well on the base dataset, achieved 88% testing accuracy using MFCCs. Failed to generate results for augmented dataset due to computational restraints.
- SVMs perfomed almost equally well on augmented dataset.
- MFCCs appear to be best discriminator among audio features.

**Contributions**
- Aryaman Trivedi: Experiment design, data preprocessing, dataset generation, data augmentation, report
- Palaash Goel: Experiment design, CNN model, report
- Ieshaan Awasthy: Flattened data models, report
- Divyajeet Singh: Report compilation
