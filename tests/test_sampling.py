from stat_tools import compute_sample_size


def test_cochran_finite(sampling_data):
    confidence = sampling_data["confidence"]
    margin_error = sampling_data["margin_error"]
    estimated_prop = sampling_data["estimated_prop"]
    population_size = sampling_data["population_size"]
    res = compute_sample_size(confidence, margin_error, estimated_prop, population_size)
    assert res == 235


def test_cochran_infinite(sampling_data):
    confidence = sampling_data["confidence"]
    margin_error = sampling_data["margin_error"]
    estimated_prop = sampling_data["estimated_prop"]
    res = compute_sample_size(confidence, margin_error, estimated_prop)
    assert res == 385


def test_yamana(sampling_data):
    confidence = sampling_data["confidence"]
    margin_error = sampling_data["margin_error"]
    estimated_prop = sampling_data["estimated_prop"]
    population_size = sampling_data["population_size"]
    res = compute_sample_size(
        confidence, margin_error, estimated_prop, population_size, how="yamane"
    )
    assert res == 240
