# ns-v-bm-decoding
### Description
All code necessary to reproduce the analyses run for a poster presented at INCF's Neuroinformatics 2018 meeting, entitled _Quantitative comparison of functional decoding approaches across meta-analytic frameworks_, comparing lexicons and functional decoding results from BrainMap.org and Neurosynth.org.
### Installation
No installation necessary, Python code was written in 2.7.13 because I'm stubborn and didn't want to update to Python 3. <br>Requires `numpy`, `pandas`, `scipy`, `seaborn`, and `neurosynth` to recreate python analyses and figures.<br>Regrettably, recreating BrainMap-style functional decoding depends on `MATLAB`.
### Usage
All files comparing terms from each database are located in `terms`, scripts required for performing BrainMap functional decoding are located in `/brainmap`, and scripts required for performing Neurosynth functional decoding are located in `/neurosynth`. Decoding input for both methods is a nifti file of a binary region/network mask and output is a series of files detailing feature weights for said region/network.
#### Neurosynth Decoding
1. ns-get-dataset.ipynb
2. ns-decoding.ipynb
#### BrainMap Decoding
1. BMA_ImageSearch.m
2. BMA_ForRevInf.m
