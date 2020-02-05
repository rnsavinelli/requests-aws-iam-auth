#!/bin/sh
echo "$TWINE_USERNAME"

python3 -m twine upload --skip-existing --non-interactive -u "$TWINE_USERNAME" -p "$TWINE_PASSWORD" ./dist/*