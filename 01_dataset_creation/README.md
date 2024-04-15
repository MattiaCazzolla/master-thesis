# Dataset conversion
Dataset folder structure is converted in the format requiered by nnU-Net

## Original dataset structure

```text 
.
├── patient_id_01
|   ├── images
|   |   ├── axial
|   |   |   └── patient_id_ax.nii
|   |   ├── coronal
|   |   |   └── patient_id_cor.nii
|   |   └── sagittal
|   |       └── patient_id_sag.nii
|   |
|   └── masks
|       ├── axial
|       |   └── patient_id_ax.nii
|       ├── coronal
|       |   └── patient_id_cor.nii
|       └── sagittal
|           └── patient_id_sag.nii
|
├── patient_id_02
├── ...
└── patient_id_N    
```

## Converted dataset structure
```text 
nnUNet_raw/
    ├── Dataset001_axial
    |   ├── imagesTr
    |   |   ├── patient_id_01_0000.nii
    |   |   ├── patient_id_02_0000.nii
    |   |   ├── ...
    |   |   └── patient_id_N_0000.nii
    |   |
    |   └── labelsTr
    |       ├── patient_id_01.nii
    |       ├── patient_id_02.nii
    |       ├── ...
    |       └── patient_id_N.nii
    |
    ├── Dataset002_coronal
    └── Dataset003_sagittal
```
