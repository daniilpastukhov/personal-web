import numpy as np
import torch
from torchvision import transforms
from torchvision.models import mobilenet_v3_large, MobileNet_V3_Large_Weights
import imagenet_stubs.imagenet_2012_labels as labels


class ClassificationController:
    mobile_net = mobilenet_v3_large(weights=MobileNet_V3_Large_Weights.DEFAULT)

    @staticmethod
    def predict(image: list):
        image = torch.tensor(image)
        transform = transforms.Compose([
            transforms.Resize(224),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        image = transform(image)

        logits = ClassificationController.mobile_net(image)

        label_idx = logits.argmax(dim=1).item()
        label = labels.label_to_name(label_idx)

        probs = torch.nn.functional.softmax(logits, dim=1)
        prob = probs[0][label_idx].item()

        return {'label': label, 'prob': prob}
