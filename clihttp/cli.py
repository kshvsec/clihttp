import sys
import requests
import json

def parse_args():
    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage: clihttp METHOD URL [OPTIONS]")
        sys.exit(1)

    method = args[0].upper()
    url = args[1]
    headers = {}
    json_data = None
    form_data = None
    timeout = 10
    allow_redirects = True
    verbose = False

    i = 2
    while i < len(args):
        if args[i] == "-H" and i + 1 < len(args):
            key, value = args[i + 1].split(":", 1)
            headers[key.strip()] = value.strip()
            i += 2
        elif args[i] == "-d" and i + 1 < len(args):
            json_data = json.loads(args[i + 1])
            i += 2
        elif args[i] == "--form" and i + 1 < len(args):
            if form_data is None:
                form_data = {}
            key, value = args[i + 1].split("=", 1)
            form_data[key.strip()] = value.strip()
            i += 2
        elif args[i] == "--timeout" and i + 1 < len(args):
            timeout = int(args[i + 1])
            i += 2
        elif args[i] == "--no-redirect":
            allow_redirects = False
            i += 1
        elif args[i] == "-v":
            verbose = True
            i += 1
        else:
            print(f"Unknown argument: {args[i]}")
            sys.exit(1)

    return method, url, headers, json_data, form_data, timeout, allow_redirects, verbose

def make_request(method, url, headers, json_data, form_data, timeout, allow_redirects, verbose):
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=json_data if not form_data else None,
            data=form_data if form_data else None,
            timeout=timeout,
            allow_redirects=allow_redirects
        )

        if verbose:
            print(f"\n🔹 Response Info:")
            print(f"  ➤ Status Code: {response.status_code}")
            print(f"  ➤ Headers: {json.dumps(dict(response.headers), indent=2)}")
            print(f"  ➤ Content:\n{response.text}\n")
        else:
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    method, url, headers, json_data, form_data, timeout, allow_redirects, verbose = parse_args()
    make_request(method, url, headers, json_data, form_data, timeout, allow_redirects, verbose)

if __name__ == "__main__":
    main()
