import pytorch_lightning as pl


class CIFARDataModule(pl.LightningDataModule):
    def __init__(self):
        super().__init__()
        self.train_dataset = None
        self.test_dataset = None

    def setup(self, stage=None):
        pass

    def prepare_data(self):
        pass

    def train_dataloader(self):
        pass

    def val_dataloader(self):
        pass

    def test_dataloader(self):
        pass
