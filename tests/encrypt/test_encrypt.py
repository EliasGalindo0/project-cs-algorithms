import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("AABBCC", 3) == "BAA_CCB"
    assert encrypt_message("AABBCC", -1) == "CCBBAA"
    assert encrypt_message("ABBCCA", 4) == "AC_CBBA"
    with pytest.raises(TypeError) as exc_message:
        encrypt_message(15, 5)
    assert exc_message.value.args[0] == "tipo inválido para message"
    with pytest.raises(TypeError)as exc_key:
        encrypt_message("AABBCC", "4")

    assert exc_key.value.args[0] == "tipo inválido para key"
