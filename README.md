# Development of Deep Learning-based Algorithm for Segmentation of Bowel Lesions in Crohn’s Disease Patients on MRE

For more details refer to the Thesis [Executive Summary](2024_04_Cazzolla_Executive_Summary.pdf)

## Introduction
Crohn’s disease (CD) is a type of inflammatory bowel disease characterized by transmural inflammation and skip lesions within the intestinal walls.

<p align="center">
  <img src="./images/Screenshot%20from%202024-01-22%2016-06-25.png" width="250" title="hover text">
</p>

Computed tomography enterography (CTE) and Magnetic Resonance Enterography (MRE), have emerged as the standards for assessing the
small intestine. 

While existing research has predominantly focused on applying deep learning to CTE images, there remains a notable gap in its application
to MRE segmentation for CD.

<p align="center">
  <img src="./images/aim.png" width="650" title="hover text">
</p>

The purpose of this work is to develop a deep learning automatic segmentation model for Crohn’s Disease detection from MRE images.


## Methods

### Dataset
Dataset consisted of 60 patients. Each had available an axial, coronal and sagittal 2D volumetric T2 weighted HASTE MRI image.

<p align="center">
  <img src="./images/mri.png" width="650" title="hover text">
</p>

### Labels
The target of the segmentation consist on the bowel wall of the disease-affected portions of the gastrointestinal tract.

<p align="center">
  <img src="./images/labels.png" width="650" title="hover text">
</p>

### nnU-Net
[nnU-Net](https://github.com/MIC-DKFZ/nnUNet) was used as segmentation model. Three model were trained, one for each dataset.

<p align="center">
  <img src="./images/axial_nnunet.jpg" width="650" title="hover text">
</p>

The model were trained on a Nvidia RTX 3090, with a total training time of 6 days.

## Results

<p align="center">
  <img src="./images/results.png" width="450" title="hover text">
</p>

<div align="center">

| Dataset           |  Dice Score      | Dilated Dice Score     |
|:----------------------:|:-------------------:|:-------------------:|
| Axial                        | 0.323 $\pm$ 0.286 | 0.413 $\pm$ 0.330 |
| Coronal                             | 0.279 $\pm$ 0.272 | 0.384 $\pm$ 0.339 |
| Sagittal                               | 0.295 $\pm$ 0.284 | 0.397 $\pm$ 0.364 |

</div>