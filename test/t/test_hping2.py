import pytest


class TestHping2:

    @pytest.mark.complete("hping2 ")
    def test_1(self, completion):
        assert completion.list
