from enum import Enum

class ProductCategory(str, Enum):
    FOOD = "food",
    CAR = "car",
    E_BOOK = "e_book"