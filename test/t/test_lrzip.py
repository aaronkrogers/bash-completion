import pytest


class TestLrzip:

    @pytest.mark.complete("lrzip ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("lrzip ~")
    def test_2(self, completion):
        assert completion.list
