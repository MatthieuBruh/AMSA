# ccl_abx
`ccl_abx` is a Python module for reading Android Binary XML (ABX) files and converting them back to XML for processing. The module can also be executed at the command line to convert ABX files there.
https://github.com/cclgroupltd/android-bits

## Command line usage
To convert an ABX file at the command line:

`ccl_abx.py file_path_here.xml`

The converted data will be outputted to `STDOUT`, so if you want to save the file you can redirect the output:

`ccl_abx.py file_path_here.xml > processed_file_path.xml`

If the file being converted has multiple roots (such as the `settings_secure.xml` file) you can add the `-mr` switch to account for these multple roots:

`ccl_abx.py file_path_here.xml -mr`


## Known issues
Our testing so far suggests that the module will round-trip an ABX created from a known XML file except for
* Ignorable whitespace (e.g layout whitespace around tags) will be discarded
* Elements with mixed content (text *and* child elements) will cause an exception to be raised - it doesn't appear that the methods that create ABX files in Android will create this structure though, so it appears to be a non-issue for now.
* If the code which *encodes* the ABX file attempts to convert numerical attributes to floating-point numbers then the usual caveats around floating-point accuracy apply

We have provided some test files so that you can confirm the behaviour of the module, and the `makeabx` Java application found in this repo can be used to generate further test files if needed.
