Plugin
======

Transformations can be user-created an added to PolyRename. To do this, place a
.py file in the polyrename/transformation/ package, and modify
polyrename/transformation/__init__.py such that your newly created
transformation is imported.

Transformations must do the following to be considered valid:

* Define a class which inherits from *Transformation*
* Define a static variable *schema* which conforms to the defined specification
* Define a **__init__** method which takes an argument for each option defined in
  the schema in the same order as the schema defines it
* Define a **resolve** method which takes a file sequence as an argument, and
  returns a file sequence
* Define a **__repr__** method. This will be used to display the configured
  transformation in the Pipeline Editor

See the existing transformations for reference when creating your own.
