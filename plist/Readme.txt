This converts an NSKeyedArchive (NSKA) plist into a normal unserialized one, that can be easily read.

C:\> Deserializer.exe sample.plist

# For json output, use the -j option.
C:\> Deserializer.exe -j sample.plist

# To process all plist files in a folder, simply provide a folder path instead of a file path:
C:\> Deserializer.exe C:\Samples\