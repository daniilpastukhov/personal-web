import os
from pathlib import Path

import torch
from flask import Blueprint, request
from skimage.io import imread

from flask_backend.controllers.classification import ClassificationController

classification_blueprint = Blueprint('classification', __name__)


@classification_blueprint.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    Path('tmp').mkdir(exist_ok=True)
    with open('tmp/image.png', 'wb') as f:
        f.write(file.read())

    image = imread('tmp/image.png')
    image = torch.tensor(image).unsqueeze(dim=0).permute(0, 3, 1, 2).float()
    output = ClassificationController.predict(image)
    os.remove('tmp/image.png')
    return output, 200
