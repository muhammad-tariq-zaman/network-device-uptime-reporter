# network-device-uptime-reporter

List network devices by uptime, longest first, flagging anything running over a year without a reboot for a firmware review.

## How to run

```sh
python3 main.py devices.csv
```

## Example output

```
SW-CORE-01: LONG UPTIME (412 days uptime)
AP-03: OK (90 days uptime)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
