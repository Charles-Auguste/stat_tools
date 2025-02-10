import pytest


@pytest.fixture
def sampling_data():
    sampling_data = {
        "margin_error": 0.05,
        "estimated_prop": 0.5,
        "confidence": 0.95,
        "population_size": 600,
    }
    return sampling_data
