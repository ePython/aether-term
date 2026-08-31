# Security Policy

## Supported Versions

| Version  | Supported |
| -------- | --------- |
| Latest   | ✅        |
| < Latest | ❌        |

Only the most recent released version receives security fixes.

## Reporting a Vulnerability

**Please do not open a public GitHub issue for security vulnerabilities.**

To report a security issue:

1. Email <!-- TODO: replace with a real security contact --> `security@example.com`
   with the subject line `[SECURITY] aetherterm - <brief description>`.
2. Include:
   - A description of the vulnerability and its potential impact.
   - Steps to reproduce or a proof-of-concept (if available).
   - Any suggested mitigations.
3. You will receive an acknowledgement within **3 business days**.
4. We aim to release a fix within **30 days** of a confirmed vulnerability.

We follow [coordinated disclosure](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure):
please give us reasonable time to address the issue before public disclosure.

## Security Considerations

This application is a terminal client for serial, socket, telnet, and SSH
connections, and will eventually launch automation scripts against network
and serial devices. Once that functionality lands, pay particular attention
to:

- Credential handling for SSH/telnet sessions (never log or persist secrets
  in plaintext).
- Validation of automation-script inputs before they reach a live device.
- Safe defaults for any serial/socket/telnet transport (e.g. not trusting
  unauthenticated telnet by default).

Until then, the current scaffold makes no network connections and handles no
credentials.

## Dependencies

Keep dependencies up to date with `uv sync --upgrade`. `uv run poe audit`
runs `pip-audit` against the locked dependency set — review its output before
releasing, and check changelogs for any dependency that processes external
input (files, network, serial devices).
