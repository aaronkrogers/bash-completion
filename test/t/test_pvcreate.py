import pytest


class TestPvcreate:

    @pytest.mark.complete("pvcreate --",
                          skipif="! pvcreate --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
