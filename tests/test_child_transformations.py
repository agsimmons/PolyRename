import datetime
from pathlib import Path

from polyrename.transformation import prefix, suffix, date_time, sequence, current_datetime, insert, remove_range, replace_extension, replace, regex_replace
from tests import TEST_SEQUENCE_01


def test_prefix():
    """Verify that prefix tranformation behaves as expected"""

    transformation = prefix.PrefixTransformation('HelloWorld')
    assert transformation.resolve(TEST_SEQUENCE_01) == [Path('/home/test/HelloWorldexample.py'), Path('HelloWorldfile_without_extension'), Path('HelloWorldrelative.jpg'), Path('relative/path/HelloWorldextreme_extreme04.tar.gz')]


def test_suffix():
    """Verify that suffix tranformation behaves as expected"""

    # TODO: Determine how we want to handle things like 'example.tar.gz'
    transformation = suffix.SuffixTransformation('HelloWorld')
    assert transformation.resolve(TEST_SEQUENCE_01) == [Path('/home/test/exampleHelloWorld.py'), Path('file_without_extensionHelloWorld'), Path('relativeHelloWorld.jpg'), Path('relative/path/extreme_extreme04.tarHelloWorld.gz')]


def test_date_time():
    """Verify that date transformation behaves as expected"""

    transformation = date_time.DateTimeTransformation(2012, 1, 3, 0, 0, 0, 0, ' (%Y-%m-%d)')
    assert transformation.resolve(TEST_SEQUENCE_01) == [Path('/home/test/example (2012-01-03).py'), Path('file_without_extension (2012-01-03)'), Path('relative (2012-01-03).jpg'), Path('relative/path/extreme_extreme04.tar (2012-01-03).gz')]


def test_sequence():
    """Verify that sequence transformation behaves as expected"""

    transformation = sequence.SequenceTransformation(10, 22, 'a', 4)
    assert transformation.resolve(TEST_SEQUENCE_01) == [Path('/home/test/exampleaa10.py'), Path('file_without_extensionaa32'), Path('relativeaa54.jpg'), Path('relative/path/extreme_extreme04.taraa76.gz')]


def test_current_datetime():
    """Verify that current datetime transformation behaves as expected"""

    format_string = '%Y-%m-%d %H:%M:%S'

    transformation = current_datetime.CurrentDateTimeTransformation(format_string)
    resolved = transformation.resolve(TEST_SEQUENCE_01)

    now = datetime.datetime.now()

    # Make sure that all datetimes are the same
    datetime_portions = [x.stem[-19:] for x in resolved]
    assert len(set(datetime_portions)) == 1

    then = datetime.datetime.strptime(datetime_portions[0], format_string)

    elapsed = now - then

    assert elapsed.seconds < 240


def test_insert():
    """Verify that insert transformation behaves as expected"""

    transformation = insert.InsertTransformation('hello', 7)
    assert transformation.resolve(TEST_SEQUENCE_01) == [Path('/home/test/examplehello.py'), Path('file_wihellothout_extension'), Path('relativhelloe.jpg'), Path('relative/path/extremehello_extreme04.tar.gz')]


def test_remove_range():
    """Verify that remove range transformation behaves as expected"""

    transformation = remove_range.RemoveRangeTransformation(-4, 0)
    assert transformation.resolve(TEST_SEQUENCE_01) == [Path('/home/test/example.py'), Path('file_without_extension'), Path('relative.jpg'), Path('relative/path/extreme_extreme04.tar.gz')]

    transformation = remove_range.RemoveRangeTransformation(0, 2)
    assert transformation.resolve(TEST_SEQUENCE_01) == [Path('/home/test/ample.py'), Path('le_without_extension'), Path('lative.jpg'), Path('relative/path/treme_extreme04.tar.gz')]

    transformation = remove_range.RemoveRangeTransformation(0, 100)
    assert transformation.resolve(TEST_SEQUENCE_01) == [Path('/home/test/.py'), Path(''), Path('.jpg'), Path('relative/path/.gz')]

    transformation = remove_range.RemoveRangeTransformation(5, 32)
    assert transformation.resolve(TEST_SEQUENCE_01) == [Path('/home/test/examp.py'), Path('file_'), Path('relat.jpg'), Path('relative/path/extre.gz')]

    transformation = remove_range.RemoveRangeTransformation(100, 500)
    assert transformation.resolve(TEST_SEQUENCE_01) == [Path('/home/test/example.py'), Path('file_without_extension'), Path('relative.jpg'), Path('relative/path/extreme_extreme04.tar.gz')]


def test_replace_extension():
    """Verify that replace extension transformation behaves as expected"""

    transformation = replace_extension.ReplaceExtensionTransformation('.txt')
    assert transformation.resolve(TEST_SEQUENCE_01) == [Path('/home/test/example.txt'), Path('file_without_extension.txt'), Path('relative.txt'), Path('relative/path/extreme_extreme04.tar.txt')]


def test_replace():
    """Verify that replace transformation behaves as expected"""

    transformation = replace.ReplaceTransformation('ex', 'HELLO')
    assert transformation.resolve(TEST_SEQUENCE_01) == [Path('/home/test/HELLOample.py'), Path('file_without_HELLOtension'), Path('relative.jpg'), Path('relative/path/HELLOtreme_HELLOtreme04.tar.gz')]


def test_regex_replace():
    """Verify that regex replace transformation behaves as expected"""

    transformation = regex_replace.RegexReplaceTransformation('[_w]', 'HelloWorld')
    assert transformation.resolve(TEST_SEQUENCE_01) == [Path('/home/test/example.py'), Path('fileHelloWorldHelloWorldithoutHelloWorldextension'), Path('relative.jpg'), Path('relative/path/extremeHelloWorldextreme04.tar.gz')]
