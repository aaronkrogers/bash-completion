import pytest


class TestAdb:

    @pytest.mark.complete("adb ")
    def test_1(self, completion):
        assert completion.list
