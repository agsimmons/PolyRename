from polyrename.transformation.child import text, sequence


def test_text():
    """Verify that text transformation returns the same value it was initialized with"""
    my_string = 'Hello World!'
    my_text = text.TextTransformation(my_string)
    assert my_text.resolve() == my_string


def test_sequence():
    """Verify that sequence transformation behaves as expected"""
    file_sequence = range(4)

    my_sequence = sequence.SequenceTransformation(file_sequence, initial=14, step=2, pad_character='a', pad_length=4)
    resolved_result = my_sequence.resolve()
    assert resolved_result == ['aa14', 'aa16', 'aa18', 'aa20']
