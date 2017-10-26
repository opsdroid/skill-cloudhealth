# opsdroid skill cloudhealth

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to interact with cloudhealth.

## Requirements

None.

## Configuration

None.
```yaml
skills:
  - name: aws-billing
    room: "#monitoring"  # (Optional) room to send alert to
    chapi-key: ABCDEF123456789  # Cloud Health API key for billing alerts
    daily-billing-alerts: true
    monthly-billing-alerts: true
```

## Usage

#### `how much was our AWS bill yesterday?`

Checks how much your AWS bill was yesterday.

> user: how much was our AWS bill yesterday?
>
> opsdroid: Yesterday we spent £57.89 on AWS.

## License

GNU General Public License Version 3 (GPLv3)
