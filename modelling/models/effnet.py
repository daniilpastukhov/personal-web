import torch
from torch.nn import functional as F
from torchvision.models import efficientnet_b0
import pytorch_lightning as pl


class LitEffNet(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.model = efficientnet_b0()

    def forward(self, x):
        return self.model(x)

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=0.001)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.cross_entropy(y_hat, y)
        return {'loss': loss}

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.cross_entropy(y_hat, y)
        return {'val_loss': loss}
