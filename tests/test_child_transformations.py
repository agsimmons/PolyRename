from pathlib import Path

from polyrename.transformation import prefix, suffix


def test_prefix():
    """Verify that prefix tranformation behaves as expected"""
    file_sequence = [Path('/home/test/example.py'), Path('file_without_extension'), Path('relative.jpg')]
    transformation = prefix.PrefixTransformation(file_sequence, 'HelloWorld')
    assert transformation.resolve() == [Path('/home/test/HelloWorldexample.py'), Path('HelloWorldfile_without_extension'), Path('HelloWorldrelative.jpg')]


def test_suffix():
    """Verify that suffix tranformation behaves as expected"""
    # TODO: Determine how we want to handle things like 'example.tar.gz'
    file_sequence = [Path('/home/test/example.py'), Path('file_without_extension'), Path('relative.jpg')]
    transformation = suffix.SuffixTransformation(file_sequence, 'HelloWorld')
    assert transformation.resolve() == [Path('/home/test/exampleHelloWorld.py'), Path('file_without_extensionHelloWorld'), Path('relativeHelloWorld.jpg')]
