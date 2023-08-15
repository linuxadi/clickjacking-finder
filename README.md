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
  <p>Here's a demo of using Clickjacking Finder without any flags:</p>
  <a href="https://github.com/linuxadi/linuxadi/raw/main/imports/without%20any%20flag.gif">
    <img src="https://github.com/linuxadi/linuxadi/raw/main/imports/without%20any%20flag.gif" alt="Clickjacking Finder Demo" width="50%">
  </a>
</div>

## Demo: Using Clickjacking Finder with All Flags or --vulnerable, --show-title, and --status-code 

<div style="text-align: center;">
  <p>Here's a demo of using Clickjacking Finder with <code>--vulnerable</code>, <code>--show-title</code>, and <code>--status-code</code> flags. </p>
  <a href="https://github.com/linuxadi/linuxadi/blob/main/imports/with-all-flags.gif">
    <img src="https://github.com/linuxadi/linuxadi/blob/main/imports/with-all-flags.gif" alt="Clickjacking Finder Demo with All Flags" width="50%">
  </a>
</div>


## Options

- `--all`: Scan for all vulnerabilities (equivalent to `--vulnerable`, `--show-title`, and `--status-code`).
- `--vulnerable`: Show vulnerable sites.
- `--show-title`: Display webpage titles.
- `--status-code`: Show HTTP status codes.

 ## clickjacking Testing Guidance with Clickjacking Finder
- If you want to test Clickjacking vulnerabilities using Clickjacking Finder,first enumerate the subdomain with httpx-toolkit :

 # Step
   ```bash
   subfinder -d example.com | httpx-toolkit | tee domain.txt
```

- Now after your domain list is ready, test it for clickjacking vulnerability with the clickjacking-finder tool.

```bash
python3 CjFinder.py domains.txt 
```
## You can set a custom flag
-   `--vulnerable` just to see the vulnerable site result from clickjacking
-  ` --show-title ` To see the title of the website page
-  `--status-code ` Current status code of the website so that we can know who is on running status and who is not If the website will be on 404 Delete or 403, or 401 Unauthorized, then we ignore it so that our time is not wasted.

-  After running the command, you'll receive an output indicating vulnerable URLs. This output will help you identify whether your Clickjacking PoC successfully exploited the vulnerability.

<div style="text-align: center;">
  <a href="https://github.com/linuxadi/linuxadi/blob/main/imports/final%20result.gif">
    <img src="https://github.com/linuxadi/linuxadi/blob/main/imports/final%20result.gif" alt="Clickjacking Vulnerability Test Demo" width="50%">
  </a>
</div>

## License

This project is licensed under the [MIT License](LICENSE).

---
Designed with ❤️ by Aditya singh 
