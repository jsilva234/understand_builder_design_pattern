from builder_pattern.builders import HouseBuilder


class HouseDirector:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct_minimal_house(self):
        self.builder.reset()
        self.builder.build_walls()
        self.builder.build_roof()

    def construct_full_house(self):
        self.builder.reset()
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_doors()
