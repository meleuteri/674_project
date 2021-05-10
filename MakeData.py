#import MinkowskiEngine
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
        scene_data = np.loadtxt(scene_name)
        if scene_name[10:15] == "train":
            label_data = np.loadtxt(scene_name[:26] + ".labels")
        elif scene_name[10:14] == "test":
            label_data = np.loadtxt(scene_name[:25] + ".labels")
        data_pt = {'scene': scene_data, 'label': label_data}
        return data_pt

    def __len__(self):
        return len(self.scenes)

# example of creating the dataset
# if __name__ == "__main__":
#     md = MakeData('dales_txt/train/')
#     print(md[0]['scene'])
#     print(md[0]['label'])
#     print(len(md))
#     md2 = MakeData('dales_txt/test/')
#     print(md2[0]['scene'])
#     print(md2[0]['label'])
#     print(len(md2))
