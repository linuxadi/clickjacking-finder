# Clickjacking Finder

Clickjacking Finder is a powerful tool designed to enhance web security by identifying clickjacking vulnerabilities across multiple domains simultaneously.

![Clickjacking Finder Logo](https://github.com/linuxadi/clickjacking-finder/blob/main/clcikjacking.png)

## Features

- Quickly scan multiple domains for clickjacking vulnerabilities.
- Detect vulnerable sites and provide detailed vulnerability information.
- Customize output options to display relevant details.


## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/linuxadi/clickjacking-finder.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python3 CjFinder.py domains.txt 
```

Replace `domains.txt` with the name of your input file containing the list of domains to scan.

## Demo: Using Clickjacking Finder without Any Flags

<div style="text-align: center;">
  <p>Here's a demo of using Clickjacking Finder without any flags. </p>
  <a href="https://github.com/linuxadi/linuxadi/blob/main/imports/without-any-flag.gif">
    <img src="https://github.com/linuxadi/linuxadi/raw/main/imports/without-any-flag.gif" alt="Clickjacking Finder Demo" width="75%">
  </a>
</div>



## Options

- `--all`: Scan for all vulnerabilities (equivalent to `--vulnerable`, `--show-title`, and `--status-code`).
- `--vulnerable`: Show vulnerable sites.
- `--show-title`: Display webpage titles.
- `--status-code`: Show HTTP status codes.

## Contributions

Contributions are welcome! If you find a bug or have an enhancement in mind, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
Designed with ❤️ by Aditya singh 
