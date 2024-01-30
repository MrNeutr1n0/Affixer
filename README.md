# Affixer
## The Affixer is designed to add specific text, strings, or characters both "Before" and "After" each line in a file. This is useful for modifying lists of domains, URLs, or any other list of data.
<br>

## Features
- **Prefixes**: Add text to the start of each line.
- **Suffixes**: Add text to the end of each line.
- **User-Friendly**: Simple to use with command-line arguments.
- **Safe**: Includes error checks for smooth operation.

## Prerequisites
Make sure you have Python 3.x installed on your system to use Affixer.

## Installation
Clone/Download the script to your computer. No extra setup needed.
```
https://github.com/MrNeutr1n0/Affixer.git
```

## How to Use
Run Affixer in the command line like this:
```
python affixer.py -i INPUT_FILE -o OUTPUT_FILE -b "PREFIX_TEXT" -a "SUFFIX_TEXT"
```
Replace INPUT_FILE with your source file, OUTPUT_FILE with the desired output file name, PREFIX_TEXT with the text to add before each line, and SUFFIX_TEXT with the text to add after each line.

python Affixer.py -i INPUT_FILE -o OUTPUT_FILE -b PREFIX_TEXT -a SUFFIX_TEXT
- `-i`, `--input` Input file containing lines to be modified.
- `-o`, `--output` Output file to save the modified lines.
- `-b`, `--before` Text to add before each line (optional).
- `-a`, `--after` Text to add after each line (optional).

<br>

## Examples

- **Adding "https://" before and "/admin/config.json" after each line in domains.txt:**
```
python affixer.py -i domains.txt -o updated_domains.txt -b "https://" -a "/admin/config.json"
```

- **Adding "https://" before each line in domains.txt:**
```
python affixer.py -i domains.txt -o updated_domains.txt -b "https://"
```

- **Adding "/db_backup.sql" after each line in list.txt:**
```
python affixer.py -i list.txt -o list2.txt -a "/db_backup.sql"
```
etc...

<br>

## Disclaimer
The Affixer is developed for educational and professional purposes. Please use Affixer responsibly. You are responsible for your actions. Misuse of this tool can lead to potential legal consequences. The developer assumes no liability and is not responsible for any misuse or damage caused by this program.


## License
The Affixer is distributed under the MIT License. See [MIT License](LICENSE) for more information.
