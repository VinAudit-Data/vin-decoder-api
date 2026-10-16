# VinAudit VIN Decoder API Python Example

This repository contains the companion Python example for [Make Your First VinAudit VIN Decoder API Call in Python](https://data.vinaudit.com/blog/vin-decoder-api-python).

The example calls the documented VinAudit V3 specifications endpoint, reads the API key from an environment variable, applies request timeouts, checks both HTTP and API-level results, and prints a shortened response without exposing the API key.

## Requirements

- Python 3
- An active VinAudit VIN Decoder API key

## Install the dependency

```bash
python -m pip install -r requirements.txt
```

Use `python3` or `py` instead of `python` if that is how Python is installed on your system.

## Set the API key

Set `VINAUDIT_API_KEY` in the terminal where you will run the script.

### Windows PowerShell

```powershell
$env:VINAUDIT_API_KEY='YOUR_API_KEY'
```

### Windows Command Prompt

```bat
set VINAUDIT_API_KEY=YOUR_API_KEY
```

### macOS or Linux using bash or zsh

```bash
export VINAUDIT_API_KEY='YOUR_API_KEY'
```

Keep real API keys out of source code, screenshots, logs, and commits.

## Run the example

```bash
python vin_decoder_example.py
```

The script uses the test VIN `JN1BJ1CR6KW331514` from the companion article and prints only the following response fields:

- `year`
- `make`
- `model`
- `trim`
- `success`
- `error`

The complete API response is intentionally not printed because its `input` object may repeat the API key.

## Documentation

- [VIN Decoder API documentation](https://data.vinaudit.com/docs/api/vin/decoder)
- [VIN Decoder API product page](https://data.vinaudit.com/vin-decoder-api)
