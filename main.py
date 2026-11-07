"""Network devices by uptime, longest first.

Usage: python3 main.py devices.csv
CSV columns: device,uptime_days.
LONG UPTIME over 365 days (firmware review due), otherwise OK.
"""
import argparse, csv, sys

def report(rows):
    out = []
    for row in rows:
        days = int(row["uptime_days"])
        verdict = "LONG UPTIME" if days > 365 else "OK"
        out.append((row["device"], days, verdict))
    return sorted(out, key=lambda r: -r[1])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for device, days, verdict in report(list(csv.DictReader(f))):
            print(f"{device}: {verdict} ({days} days uptime)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
