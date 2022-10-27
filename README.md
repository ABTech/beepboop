Beep Boop Webserver
===================

Takes `BEEPBOOP_URL` as an environment variable

## Development
```bash
pip install -e .
python3 -m beepboop
```

## Deployment
```bash
pip install .[deploy]
gunicorn beepboop.server:app
```
