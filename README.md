# swift_localization

This is a primitive implementation of a locale string generator that parses an XCode project for NSLocalizedString instances, then extracts the keys and creating a dictionary based on the extracted key and uses its translation as a value

# Usage

```python script.py <project_path> <language_code> <output_file_path>```

### Example

To generate a Swedish locale translation

```python script.py <project_path> se ~/tmp/localization.txt```