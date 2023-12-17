# Timetable printer

## Prerequisites
- Python 3.11
- PIP 23.2

## Install
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt 
```

## Usage
Available options:
```bash
printer [-h] [-o OUTPUT_FILENAME] [-i TABLE_ID] [-t TEMPLATE] [-q] html_file
```

First download a timetable html file (example):
```bash
wget http://pei.prz.rzeszow.pl/as/Zima2023_teachers_days_horizontal.html -O timetable.html
```

Run script inside virtual environment:
```bash
python3 ./printer.py timetable.html -i table_78 -o timetable.pdf
```

## Development
PyCharm (probably every Jetbrains IDE):
- Choose or create a new Python 3.11 interpreter from virtual environment
- Select script *printer*. Click *run button* (Shift+F10)