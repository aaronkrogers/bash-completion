import pytest


class TestPdftotext:

    @pytest.mark.complete("pdftotext ")
    def test_1(self, completion):
        assert completion.list
