from src.collecting import sum_nums


class TestCollecting(object):
    def test_sum_nums(self):
        assert sum_nums(5, 2) == 7
