import pytest


class TestLdd:
    @pytest.mark.complete("ldd ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ldd -", require_cmd=True)
    def test_options(self, completion):
        assert completion
