from dataclasses import dataclass
from datetime import datetime


@dataclass
class Vendite:
    data: datetime.date
    ricavo: float
    retailer: int
    product: int

    def __str__(self):
        return f'Data: {self.data}; Ricavo: {self.ricavo}; Retailer: {self.retailer}; Product: {self.product}'

    def __lt__(self, other):
        return self.ricavo < other.ricavo
