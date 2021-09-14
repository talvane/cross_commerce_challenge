from api.logconfig import LogConfig


def test_logconfig():
    logconfig = LogConfig
    assert logconfig.__fields__.get('LOGGER_NAME') is not None
    assert logconfig.__fields__.get('LOG_FORMAT') is not None
    assert logconfig.__fields__.get('LOG_LEVEL') is not None
