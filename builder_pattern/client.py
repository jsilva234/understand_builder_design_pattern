from builder_pattern.builders import (
    ConcreteHouseBuilder,
    HTTPRequestBuilder,
    WoodenHouseBuilder,
)
from builder_pattern.directors import HouseDirector

if __name__ == "__main__":

    print("Wooden houses:")
    wooden_builder = WoodenHouseBuilder()
    director = HouseDirector(wooden_builder)

    director.construct_full_house()
    wooden_house = wooden_builder.get_result()
    print("Full Wooden House:", wooden_house)

    director.construct_minimal_house()
    minimal_wooden_house = wooden_builder.get_result()
    print("Minimal Wooden House:", minimal_wooden_house)

    print("\n\nConcrete houses:")
    concrete_builder = ConcreteHouseBuilder()
    director = HouseDirector(concrete_builder)

    director.construct_full_house()
    concrete_house = concrete_builder.get_result()
    print("Full Concrete House:", concrete_house)

    director.construct_minimal_house()
    minimal_concrete_house = concrete_builder.get_result()
    print("Minimal Concrete House:", minimal_concrete_house)

    # simpler example
    # builder pattern can also be used without a director
    print("\n\nSimpler HTTPRequest example:")
    builder = HTTPRequestBuilder()

    request = (
        builder.set_method("POST")
        .set_url("https://api.example.com/data")
        .add_header("Authorization", "Bearer token")
        .add_header("Content-Type", "application/json")
        .set_body('{"key": "value"}')
        .build()
    )

    print(request)
