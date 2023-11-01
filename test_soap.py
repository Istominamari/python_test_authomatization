import pytest
from soap import check_text

class TestSOAP:
    def test_checkTest(self, incorrect_word, correct_word):
        assert correct_word in check_text(incorrect_word)[0]["s"]

if __name__ == '__main__':
    pytest.main(["-v"])