from detectron2.engine import DefaultTrainer
from detectron2.config import get_cfg
import os

cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
cfg.DATASETS.TRAIN = ("training_dataset",)
cfg.DATASETS.TEST = ("test_dataset",)   # no metrics implemented for this dataset
cfg.DATALOADER.NUM_WORKERS = 4
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")# initialize from model zoo
cfg.SOLVER.IMS_PER_BATCH = 2
cfg.SOLVER.BASE_LR = 0.02
cfg.SOLVER.MAX_ITER = 23000   
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 900   
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 12  
cfg.TEST.EVAL_PERIOD = 1000
cfg.MODEL.ROI_HEADS.LOSS_FUNC = 'SupConLoss'
