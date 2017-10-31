# opsdroid skill cloudhealth

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to interact with [CloudHealth](https://www.cloudhealthtech.com/).

## Requirements

A CloudHealth account and an [api key](https://github.com/CloudHealth/cht_api_guide#getting-an-api-key).

## Configuration

None.
```yaml
skills:
  - name: aws-billing
    # Required
    chapi-key: ABCDEF123456789  # Cloud Health API key for billing alerts
    # Optional
    room: "#monitoring"  # Room to send alert to
    daily-billing-alerts: true  # Announce the previous day's bill each morning
    monthly-billing-alerts: true  # Announce the previous month's bill each month
```

## Usage

#### `how much was our AWS bill yesterday?`

Checks how much your AWS bill was yesterday.

> user: how much was our AWS bill yesterday?
>
> opsdroid: Yesterday we spent £57.89 on AWS.
