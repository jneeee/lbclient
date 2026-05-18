import pytest
from lbclient import TokenDeque


class TestTokenDeque:
    def test_init_with_list(self):
        tokens = ["192.168.1.1", "192.168.1.2"]
        td = TokenDeque(tokens)
        assert len(td) == 2
        assert td.get_token() == "192.168.1.1"

    def test_get_token_empty(self):
        td = TokenDeque([])
        with pytest.raises(IndexError):
            td.get_token()

    def test_produce_token_after_get(self):
        td = TokenDeque(["192.168.1.1"])
        td.get_token()
        assert len(td) == 0
        td.produce_token("192.168.1.1")
        assert len(td) == 1

    def test_produce_token_only_if_in_helpset(self):
        td = TokenDeque(["192.168.1.1"])
        td.produce_token("192.168.1.2")
        assert len(td) == 1
        assert td.deque[0] == "192.168.1.1"

    def test_update_token_add(self):
        td = TokenDeque(["192.168.1.1"])
        td.update_token(["192.168.1.1", "192.168.1.2"])
        assert len(td) == 2

    def test_update_token_does_not_remove(self):
        td = TokenDeque(["192.168.1.1", "192.168.1.2"])
        td.update_token(["192.168.1.1"])
        assert len(td) == 2

    def test_str_representation(self):
        td = TokenDeque(["192.168.1.1"])
        assert "192.168.1.1" in str(td)

    def test_len(self):
        td = TokenDeque(["192.168.1.1", "192.168.1.2"])
        assert len(td) == 2
        td.get_token()
        assert len(td) == 1