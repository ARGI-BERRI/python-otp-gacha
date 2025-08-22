# python-otp-gacha

This app will find the date that the OTP number becomes 777777.

You can see the _X-Days_ that 777777 will appear in your OTP Generator by running the main script:

```log
2025-08-22 20:07:53.205 | INFO     | __main__:main:17 - key=b'OONADH5PAMWBY2SSQPFDL2RHAGDHUV24'
2025-08-22 20:07:53.526 | INFO     | __main__:main:23 - now.isoformat()='2025-10-10T05:28:23.206424+09:00'
2025-08-22 20:07:54.293 | INFO     | __main__:main:23 - now.isoformat()='2026-02-04T12:26:23.206424+09:00'
2025-08-22 20:07:55.319 | INFO     | __main__:main:23 - now.isoformat()='2026-07-11T06:05:53.206424+09:00'
```

Please note that the secret is generated in runtime randomly.

## Run and test codes

Please run `make run` to invoke the main script, and run `make test` to run pytest for this app.

## License

Apache License 2.0
