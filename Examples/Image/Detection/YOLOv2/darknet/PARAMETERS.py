# ==============================================================================
# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# ==============================================================================

import os.path

# Set to the DataSet you want to train
par_dataset_name = "ImageNet2012"


par_trainset_label_file = "train_map.txt"
par_testset_label_file = "val_map.txt"
par_abs_path = os.path.dirname(os.path.abspath(__file__))
par_max_epochs = 50

if(par_dataset_name == "ImageNet2012"):
    par_image_height = 224  # Darknet19 scales input image down over all by a factor of 32. \\
    par_image_width = 224   # It needs at least a 3x3 shape for the last conv layer. So 32*3 is required at least.
    par_num_channels = 3  # RGB
    par_input_bias = 114
    par_num_classes = 1000
    par_data_path = os.path.join(par_abs_path, "..", "..", "DataSets", "CIFAR-10")

    par_minibatch_size = 128


