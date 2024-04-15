import os
import shutil
from tqdm import tqdm

folder_path = './Dataset'    
destination_path = './nnUNet_Raw'

patients = os.listdir(folder_path)
view_ID = {'axial': '001', 'coronal': '002', 'sagittal': '003'}
abb = {'axial': 'ax', 'coronal': 'cor', 'sagittal': 'sag'}


def init_folders():
    ''' init the destination folder'''
    
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)
        
        for folder in ['Dataset001_axial', 'Dataset002_coronal', 'Dataset003_sagittal']:
            os.mkdir(os.path.join(destination_path, folder))
            
            os.mkdir(os.path.join(destination_path, folder, 'imagesTr'))
            os.mkdir(os.path.join(destination_path, folder, 'labelsTr'))
            
    print('Folder inited')


def move_images():
    '''
    move the images from Dataset folder to nnUnet_Raw folder
    the last met the requirements from nnUNet
    '''
    
    for patient in tqdm(patients):
        for view in ['axial', 'coronal', 'sagittal']:
        
            img_path = os.path.join(folder_path, patient, 'images', f'{view}', f'{patient}_{abb[view]}.nii')
            mask_path = os.path.join(folder_path, patient, 'masks', f'{view}', f'{patient}_{abb[view]}.nii')
        
            img_destination_path = os.path.join(destination_path, f'Dataset{view_ID[view]}_{view}/imagesTr/{patient}_0000.nii')
            mask_destination_path = os.path.join(destination_path, f'Dataset{view_ID[view]}_{view}/labelsTr/{patient}.nii')

            try:
                shutil.copy(img_path, img_destination_path)
                shutil.copy(mask_path, mask_destination_path)
            except:
            	# some patient dont have all the views
                print()
                print(f'No {view} for patient {patient}')
                continue

    print('All patients moved')
    

def count_img_mask():
    # sanity check
    # number of images per view must be the same as number of labels
    
    datasets = os.listdir(destination_path)
    for dataset in datasets:
        n_imgs = len(os.listdir(os.path.join(destination_path, dataset, 'imagesTr')))
        n_masks = len(os.listdir(os.path.join(destination_path, dataset, 'labelsTr')))
        
        print(f'Dataset {dataset}: {n_imgs} images, {n_masks} labels')

if __name__ == '__main__':
    init_folders()
    move_images()
    count_img_mask()
