import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class IGNDataset(CustomDataset):
    """IGN dataset.

    In segmentation map annotation for IGN, 0 represents zones without
    information so ``reduce_zero_label`` is fixed to True.
    The ``img_suffix`` is fixed to '.png' and ``seg_map_suffix`` is fixed to
    '.png'.
    """

    CLASSES = ('Dense forest', 'Sparse forest', 'Moor', 'Herbaceous formation', 'Building', 'Road')

    PALETTE = [[128, 0, 0], [0, 128, 0], [128, 128, 0], [128, 0, 128], [0, 0, 128], [200, 200, 200]]

    def __init__(self, **kwargs):
        super(IGNDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='.png',
            reduce_zero_label=True,
            **kwargs)
        assert osp.exists(self.img_dir)
