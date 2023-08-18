class Water:
    def __init__(self,has_gills,has_lays_eggs) -> None:
        self.__has_gills=has_gills
        self.__has_lays_eggs=has_lays_eggs

    def has_lays_eggs(self) -> bool:
        return self.__has_lays_eggs
    
    def has_gills(self) -> bool:
        return self.__has_gills