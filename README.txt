# Temperature Converter
### Cognifyz Technologies — Task 4

A clean, interactive Python program that converts temperatures between
**Celsius** and **Fahrenheit** with input validation and unit tests.

---

## Files

| File | Description |
|------|-------------|
| `temperature_converter.py` | Main program — run this to use the converter |
| `test_temperature_converter.py` | Unit tests covering all conversion scenarios |
| `README.txt` | This documentation file |

---

## How to Run

### Requirements
- Python 3.6 or higher (no third-party libraries needed)

### Run the Converter
```bash
python temperature_converter.py
```

### Run the Tests
```bash
python -m unittest test_temperature_converter.py -v
```

---

## Features

- Convert **Celsius → Fahrenheit**
- Convert **Fahrenheit → Celsius**
- Input validation (rejects non-numeric values)
- Loop-based menu — convert multiple temperatures in one session
- Clean, formatted output

---

## Conversion Formulas

| Direction | Formula |
|-----------|---------|
| Celsius → Fahrenheit | F = (C × 9/5) + 32 |
| Fahrenheit → Celsius | C = (F − 32) × 5/9 |

---

## Sample Session

```
Welcome to the Temperature Converter!

=============================================
       TEMPERATURE CONVERTER
=============================================
  [1]  Celsius  →  Fahrenheit
  [2]  Fahrenheit  →  Celsius
  [3]  Exit
=============================================
Select an option (1 / 2 / 3): 1

Enter the temperature in Celsius (°C): 100

---------------------------------------------
  RESULT
---------------------------------------------
  100.00° Celsius  =  212.00° Fahrenheit
---------------------------------------------

  Convert another temperature? (yes / no): yes
```

---

## Test Coverage

| Test Case | Input | Expected Output |
|-----------|-------|----------------|
| Boiling point | 100°C | 212°F |
| Freezing point | 0°C | 32°F |
| Body temperature | 37°C | 98.6°F |
| Crossover point | −40°C | −40°F |
| Absolute zero | −273.15°C | −459.67°F |
| Round-trip C→F→C | 25°C | 25°C |
| Round-trip F→C→F | 77°F | 77°F |

---

## Author
Cognifyz Technologies Internship — Python Programming Task 4
