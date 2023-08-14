from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import sys
from bs4 import BeautifulSoup

GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'

def check(url):
    try:
        if "http" not in url:
            url = "http://" + url

        data = urlopen(url)
        headers = data.info()

        if not "X-Frame-Options" in headers:
            return True, data.getcode() 

    except HTTPError as e:
        return False, e.code 

    except URLError:
        return False, None  

    return False, None

def get_page_title(url):
    try:
        if "http" not in url:
            url = "http://" + url

        data = urlopen(url)
        soup = BeautifulSoup(data, 'html.parser')
        title = soup.title.string
        return title.strip() if title else None

    except Exception:
        return None

def main():
    try:
        if len(sys.argv) < 2:
            print("[*] Usage: python(3) clickjacking_tester.py <file_name> [--vulnerable] [--show-title] [--status-code]")
            sys.exit(1)

        file_name = sys.argv[1]
        sites = [line.strip() for line in open(file_name, 'r')]

        show_vulnerable_only = False
        show_title = False
        show_status_code = False

        valid_flags = {'--vulnerable', '--show-title', '--status-code'}
        user_flags = set(sys.argv[2:])

        if '--help' in user_flags:
            print("Usage: python(3) clickjacking_tester.py <file_name> [options]")
            sys.exit(0)

        invalid_flags = user_flags - valid_flags
        if invalid_flags:
            print("Invalid option(s). Use python(3) clickjacking_tester.py --help for more information.")
            sys.exit(1)

        if '--vulnerable' in user_flags:
            show_vulnerable_only = True
        if '--show-title' in user_flags:
            show_title = True
        if '--status-code' in user_flags:
            show_status_code = True

        for site in sites:
            is_vulnerable, status_code = check(site)
            title = get_page_title(site) if show_title else None

            if is_vulnerable and show_vulnerable_only:
                print(f" [{RED}+ Vulnerable: {site}{ENDC}]")
                if show_status_code and status_code:
                    print(f"   Status Code: {status_code}")
                if show_title and title:
                    print(f"   Title: {title}")
            elif is_vulnerable:
                print(f" [{RED}+ Vulnerable: {site}{ENDC}]")
                if show_status_code and status_code:
                    print(f"   Status Code: {status_code}")
                if show_title and title:
                    print(f"   Title: {title}")
            elif not is_vulnerable and not show_vulnerable_only:
                print(f" [{GREEN}- Not vulnerable: {site}{ENDC}]")
                if show_status_code and status_code:
                    print(f"   Status Code: {status_code}")
                if show_title and title:
                    print(f"   Title: {title}")
                print(f" [*] URL: {site}")

    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)

if __name__ == '__main__':
    main()
