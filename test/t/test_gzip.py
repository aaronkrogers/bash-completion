import pytest


class TestGzip:

    @pytest.mark.complete("gzip ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("gzip ~")
    def test_2(self, completion):
        assert completion.list
