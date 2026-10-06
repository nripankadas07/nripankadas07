# Contributing

Thanks for considering a contribution to `nripankadas07`. Keep changes small, tested, and aligned with the existing public API.

## Local checks

```bash
test -s README.md
test -s LICENSE
python -m pip wheel --no-deps --wheel-dir /tmp/profile-wheel .
python -m venv /tmp/profile-package-check
/tmp/profile-package-check/bin/python -m pip install /tmp/profile-wheel/*.whl
PATH="/tmp/profile-package-check/bin:$PATH" /tmp/profile-package-check/bin/python test_installed_cli.py
```

## Contribution rules

- Add or update tests for behavior changes.
- Keep README examples in sync with the implementation.
- Keep runtime dependencies minimal and intentional.
- Prefer explicit errors over surprising coercions.
