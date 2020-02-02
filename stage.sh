#!/bin/sh

python3 -m twine upload --skip-existing --non-interactive -u "$TWINE_USERNAME" -p "$TWINE_PASSWORD" --repository-url "https://test.pypi.org/legacy/" dist/*