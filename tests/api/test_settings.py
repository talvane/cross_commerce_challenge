from api.settings import Settings


def test_settings():
    settings = Settings
    assert settings.__fields__.get('API_EXTRACT') is not None
