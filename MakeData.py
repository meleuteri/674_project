import MinkowskiEngine as ME
import torch
import numpy as np
import os

class MakeData(torch.utils.data.Dataset):
    def __init__(self, root_dir):
        self.scenes = []
        for filename in os.listdir(root_dir):
            if filename.endswith(".txt"):
                self.scenes.append(root_dir + filename)

    def __getitem__(self, idx):
        scene_name = self.scenes[idx]
        scene_data = np.loadtxt(scene_name)[0:1000]
        if scene_name[10:15] == "train":
            label_data = np.loadtxt(scene_name[:26] + ".labels")[0:1000]
        elif scene_name[10:14] == "test":
            label_data = np.loadtxt(scene_name[:25] + ".labels")[0:1000]        
        discrete_coords, feats, unique_labels = ME.utils.sparse_quantize(
            coordinates=scene_data,
            features = torch.ones(scene_data.shape),
            labels=label_data,
            quantization_size=0.1)
        #data_pt = {'scene': discrete_coords, 'label': unique_labels}
        #return data_pt
        return discrete_coords, feats, unique_labels
        
    def __len__(self):
        return len(self.scenes)

# example of creating the dataset
# if __name__ == "__main__":
#     md = MakeData('dales_txt/train/')
#     print(md[0]['scene'].shape)
#     print(md[4]['scene'].shape)
