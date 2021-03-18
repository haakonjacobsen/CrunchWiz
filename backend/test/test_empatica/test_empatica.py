from backend.crunch.empatica.measurement_functions import compute_emotional_regulation, compute_entertainment


class TestCrunch:

    def test_compute_emotional_regulation(self):
        list_of_ibis = [0.515649, 0.500023, 0.468771, 0.515649, 0.515649, 0.515649, 0.531274,
                        0.531274, 0.500023, 0.515649, 0.500023, 0.500023, 0.515649, 0.468771]
        assert 0 < compute_emotional_regulation(list_of_ibis) < 1

    def test_compute_entertainment(self):
        list_of_ibis = [0.515649, 0.500023, 0.468771, 0.515649, 0.515649, 0.515649, 0.531274,
                        0.531274, 0.500023, 0.515649, 0.500023, 0.500023, 0.515649, 0.468771]
        assert 0 < compute_entertainment(list_of_ibis) < 1
