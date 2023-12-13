# Timetable printer

## Prerequisites
- Python 3.11

## Install
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt 
```

## Run

First (temporary) download source timetable, e.g.
```bash
wget http://pei.prz.rzeszow.pl/as/Zima2023_teachers_days_horizontal.html
```

Classic approach run:
```bash
python3 ./printer.py
```

JetBrains IDE approach run:

Click *run button* (Shift+F10) when script *printer* is selected.