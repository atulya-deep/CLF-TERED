from detectron2.utils.visualizer import ColorMode
from detectron2.data import DatasetCatalog, MetadataCatalog, build_detection_test_loader
from detectron2.evaluation import COCOEvaluator, inference_on_dataset
evaluator = COCOEvaluator("training_dataset", cfg, False, output_dir="./output/")
val_loader = build_detection_test_loader(cfg, "training_dataset")
inference_on_dataset(trainer.model, val_loader, evaluator)
