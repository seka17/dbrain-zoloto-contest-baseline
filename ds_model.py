import json
import os
from collections import defaultdict
import numpy as np
from PIL import Image


MODEL_REL_FILENAME = 'class.txt'


class DSModel:
    def __init__(self, path_to_assets_dir: str = ''):
        # load assets into a newly created model here
        pass

    def train(self, path_to_training_data: str, path_to_model_dir: str):
        """Take data, produce a model and save its weights in the designated directory
        Baseline implementation:
        Choose the most popular class and save its name
        """

        markup_filename = os.path.join(path_to_training_data, 'markup.json')
        with open(markup_filename) as f:
            markup = json.load(f)

        # # This is how you iterate over training images:
        # for filename in markup.keys():
        #     full_path = os.path.join(path_to_training_data, filename)
        #     img = np.asarray(Image.open(full_path))
        #     # do something with the image here

        class_occurences = defaultdict(int)
        for filename, img_data in markup.items():
            class_ = self.get_class(img_data)
            class_occurences[class_] += 1
        best_class = max(class_occurences.keys(), key=(
            lambda key: class_occurences[key]))

        class_filename = os.path.join(path_to_model_dir, MODEL_REL_FILENAME)
        with open(class_filename, 'w') as f:
            f.write(best_class)

    def load_model(self, path_to_model_dir: str):
        """Load previously saved weights into a newly created model
        Baseline implementation:
        Load name of the most popular class
        """

        class_filename = os.path.join(path_to_model_dir, MODEL_REL_FILENAME)
        with open(class_filename, 'r') as f:
            self.best_class = f.read()

    def predict(self, batch: [bytes]) -> list:
        """Make a prediction for every element of data in the list
        Prediction format: [{'image_label': label1}, {'image_label': label2}, ...]
        Baseline implementation:
        Predict the most popular class for all objects
        """

        # # This is how you iterate over batch of test images:
        # for cur_data in batch:
        #     bytesio = BytesIO(cur_data)
        #     img = np.asarray(Image.open(bytesio))
        #     # do something with the image here

        best_img_data = self.get_img_data(self.best_class)
        predictions = [best_img_data] * len(batch)
        return predictions

    @staticmethod
    def get_class(img_data):
        # classes_info = img_data['aabb']
        return img_data['image_label']
        # for class_, class_bboxes in classes_info.items():
        #     if len(class_bboxes) > 0:
        #         return class_
        # raise Exception

    @staticmethod
    def get_img_data(class_):
        return {'image_label': class_}


if __name__ == '__main__':
    # This baseline don't require any assets so pass
    ds_model = DSModel()
    # Untar preview dataset, for example it in ./preview
    # Also create directory for artifacts to be saved
    ds_model.train('./preview', './artifacts')
