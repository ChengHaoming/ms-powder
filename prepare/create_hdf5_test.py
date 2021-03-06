import h5py
import numpy as np
import cv2

from pathlib import Path

if __name__ == '__main__':
    data_path = Path('../data/test/')
    real_path = Path('../real/')
    n_scenes = 32
    height = 160
    width = 280
    n_channels = 965
    h5f = h5py.File(str(Path(real_path / ('test.hdf5'))), 'w')
    dset_im = h5f.create_dataset('im', (n_scenes, height, width, n_channels), dtype='float32')
    dset_label = h5f.create_dataset('label', (n_scenes, height, width), dtype='uint8')
    for i in range(n_scenes):
        idx = str(i).zfill(2)
        im_npz = np.load(data_path / 'scene' / (idx + '_scene.npz'))
        im = np.concatenate((im_npz['rgbn'].astype(np.float32), im_npz['swir'].astype(np.float32)), axis=2)
        label = cv2.imread(str(data_path / 'label' / (idx + '_label.png')), cv2.IMREAD_GRAYSCALE)
        dset_im[i, :, :, :] = im
        dset_label[i, :, :] = label
    h5f.close()




