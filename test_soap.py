import pytest
import logging
from soap import get_correction_variants


class TestSOAP:
    def test_check_test(self, incorrect_word, correct_word):
        logging.info("Start SOAP-test \"test_check_test\".")
        assert correct_word in get_correction_variants(incorrect_word)


if __name__ == '__main__':
    pytest.main(["-v"])
