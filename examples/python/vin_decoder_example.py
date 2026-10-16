"""Make a basic VinAudit VIN Decoder API V3 request.

The script prints only a small, sanitized subset of the response. It does not
print the response ``input`` object, which may contain the API key.
"""

import json
import os

import requests


API_URL = "https://specifications.vinaudit.com/v3/specifications"
TEST_VIN = "JN1BJ1CR6KW331514"


def main() -> int:
    api_key = os.getenv("VINAUDIT_API_KEY", "").strip()

    if not api_key:
        print("VINAUDIT_API_KEY environment variable is missing or blank.")
        return 1

    params = {
        "vin": TEST_VIN,
        "key": api_key,
        "format": "json",
    }

    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=(5, 30),
        )
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.Timeout:
        print("The request timed out.")
        return 1
    except requests.exceptions.HTTPError as exc:
        status = exc.response.status_code if exc.response is not None else "unknown"
        print(f"The API returned HTTP status {status}.")
        return 1
    except requests.exceptions.RequestException:
        print("The HTTP request failed.")
        return 1
    except ValueError:
        print("The API returned invalid JSON.")
        return 1

    if not isinstance(data, dict):
        print("The API returned an unexpected response.")
        return 1

    if data.get("success") is not True:
        safe_error = {
            "success": data.get("success", False),
            "error": data.get("error", "unknown_error"),
        }
        print(json.dumps(safe_error, indent=2))
        return 1

    attributes = data.get("attributes")
    if not isinstance(attributes, dict):
        print("The response did not contain a valid attributes object.")
        return 1

    safe_output = {
        "attributes": {
            "year": attributes.get("year"),
            "make": attributes.get("make"),
            "model": attributes.get("model"),
            "trim": attributes.get("trim"),
        },
        "success": True,
        "error": data.get("error", ""),
    }

    print(json.dumps(safe_output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
