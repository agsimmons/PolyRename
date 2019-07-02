from pathlib import Path

from polyrename.transformation import prefix, suffix, date_time, sequence, current_datetime, insert, remove_range, replace_extension, replace


TEST_SEQUENCE_01 = [Path('/home/test/example.py'), Path('file_without_extension'), Path('relative.jpg')]


def test_prefix():
    """Verify that prefix tranformation behaves as expected"""

    transformation = prefix.PrefixTransformation(TEST_SEQUENCE_01, 'HelloWorld')
    assert transformation.resolve() == [Path('/home/test/HelloWorldexample.py'), Path('HelloWorldfile_without_extension'), Path('HelloWorldrelative.jpg')]


def test_suffix():
    """Verify that suffix tranformation behaves as expected"""

    # TODO: Determine how we want to handle things like 'example.tar.gz'
    transformation = suffix.SuffixTransformation(TEST_SEQUENCE_01, 'HelloWorld')
    assert transformation.resolve() == [Path('/home/test/exampleHelloWorld.py'), Path('file_without_extensionHelloWorld'), Path('relativeHelloWorld.jpg')]


def test_date_time():
    """Verify that date transformation behaves as expected"""

    transformation = date_time.DateTimeTransformation(TEST_SEQUENCE_01, 2012, 1, 3, 0, 0, 0, 0, ' (%Y-%m-%d)')
    assert transformation.resolve() == [Path('/home/test/example (2012-01-03).py'), Path('file_without_extension (2012-01-03)'), Path('relative (2012-01-03).jpg')]


def test_sequence():
    """Verify that sequence transformation behaves as expected"""

    transformation = sequence.SequenceTransformation(TEST_SEQUENCE_01, 10, 22, 'a', 4)
    assert transformation.resolve() == [Path('/home/test/exampleaa10.py'), Path('file_without_extensionaa32'), Path('relativeaa54.jpg')]


# TODO
# def test_current_datetime():


def test_insert():
    """Verify that insert transformation behaves as expected"""

    transformation = insert.InsertTransformation(TEST_SEQUENCE_01, 'hello', 7)
    assert transformation.resolve() == [Path('/home/test/examplehello.py'), Path('file_wihellothout_extension'), Path('relativhelloe.jpg')]


def test_remove_range():
    """Verify that remove range transformation behaves as expected"""

    transformation = remove_range.RemoveRangeTransformation(TEST_SEQUENCE_01, -4, 0)
    assert transformation.resolve() == [Path('/home/test/example.py'), Path('file_without_extension'), Path('relative.jpg')]

    transformation = remove_range.RemoveRangeTransformation(TEST_SEQUENCE_01, 0, 2)
    assert transformation.resolve() == [Path('/home/test/ample.py'), Path('le_without_extension'), Path('lative.jpg')]

    transformation = remove_range.RemoveRangeTransformation(TEST_SEQUENCE_01, 0, 100)
    assert transformation.resolve() == [Path('/home/test/.py'), Path(''), Path('.jpg')]

    transformation = remove_range.RemoveRangeTransformation(TEST_SEQUENCE_01, 5, 32)
    assert transformation.resolve() == [Path('/home/test/examp.py'), Path('file_'), Path('relat.jpg')]


def test_replace_extension():
    """Verify that replace extension transformation behaves as expected"""

    transformation = replace_extension.ReplaceExtensionTransformation(TEST_SEQUENCE_01, '.txt')
    assert transformation.resolve() == [Path('/home/test/example.txt'), Path('file_without_extension.txt'), Path('relative.txt')]


def test_replace():
    """Verify that replace transformation behaves as expected"""

    transformation = replace.ReplaceTransformation(TEST_SEQUENCE_01, 'ex', 'HELLO')
    assert transformation.resolve() == [Path('/home/test/HELLOample.py'), Path('file_without_HELLOtension'), Path('relative.jpg')]
