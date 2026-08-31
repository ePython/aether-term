# Architecture overview

This directory is the home for architecture decision records (ADRs) and
design notes as aetherterm grows beyond its current scaffold.

Nothing has been written yet. Anticipated future topics:

- Terminal I/O backends (serial, raw socket, Telnet, SSH) and how they share a
  common transport interface.
- The GUI shell: main terminal view plus the configurable paged button-grid
  frame beneath it.
- The automation scripting engine invoked by button presses, and how it
  addresses the active session/device.
