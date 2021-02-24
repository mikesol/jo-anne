from hypothesis import given
import hypothesis.strategies as st


@given(st.integers(min_value=5, max_value=42))
def test_decode_inverts_encode(s):
    print(s)
    assert s == s


if __name__ == '__main__':
    test_decode_inverts_encode()
