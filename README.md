# ns-v-bm-decoding
### Description
All code necessary to reproduce the analyses run for a poster presented at INCF's Neuroinformatics 2018 meeting, entitled _Quantitative comparison of functional decoding approaches across meta-analytic frameworks_, comparing lexicons and functional decoding results from [BrainMap.org](http://http://brainmap.org/ "BrainMap")[^1][^2] and [Neurosynth.org](http://neurosynth.org)[^3].
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
<br>
Run `decoding_comparison.ipynb` to compare results of decoding. Due to the format of BrainMap's decoding output, significant CogPO terms must be typed in manually.
<br>
### References
[^1]: Fox PT, Lancaster JL. (2002) Mapping context and content: The BrainMap model. Nature Rev Neurosci 3, 319-321. [pdf](http://brainmap.org/pubs/FoxNRN02.pdf)
[^2]: Laird AR, Lancaster JL, Fox PT. (2005). BrainMap: The social evolution of a functional neuroimaging database. Neuroinformatics 3, 65-78. [pdf](http://brainmap.org/pubs/LairdNI05.pdf)
[^3]: Yarkoni T, Poldrack RA, Nichols TE, van Essen DC, Wager TD. (2011). Large-scale automated synthesis of human functional neuroimaging data. Nature Methods 8, 665–670. [link](https://www.nature.com/articles/nmeth.1635)
