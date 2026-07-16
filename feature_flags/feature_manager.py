from config_loader import ConfigLoader


class FeatureManager:
    features = {}

    @classmethod
    def load(cls):

        data = ConfigLoader.load_config("features.yaml")

        cls.features = data["features"]

    @classmethod
    def is_enabled(cls, feature_name):

        return cls.features.get(feature_name, False)

    @classmethod
    def get_all_features(cls):

        return cls.features
