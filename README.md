# FoggySight: A Scheme for Facial Lookup Privacy

This repository contains source code release for the paper "FoggySight: A Scheme for Facial Lookup Privacy" (to appear in Issue 3 of PETS 2021 and available [on arXiv](https://arxiv.org/abs/2012.08588)).

This current version contains a release of the code for experiments in _Section 6.4 Privacy Protection Success When Protectors Do Not Have Access to the Face Recognition Model_. 
In particular, we implement an expectations-over-transformations (EOT) algorithm for generating the decoys against an ensemble of networks.
We use two networks: those from https://github.com/davidsandberg/facenet 

The implementation is available under `notebooks/Generate Robust Decoys with Ensemble.ipynb`.
The code is mostly self-contained. 
It requires two things:

1. The models themselves. We expect those to be found under `MODEL_BASE` and follow the folder structure as downloaded from the FaceNet repo. See the function `build_model` for more details.
2. Clean, pre-cropped facial images to size 224. Those should be organized in subfolders per identity. Modify the paths in `path_for_id_clean` to return the folder for each identity given the identity's name only. 

Evaluation code is forthcoming.