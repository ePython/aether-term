# aetherterm.spec — reproducible single-file, windowed GUI build.
#
# Build:  uv run poe build-exe
#     or  uv run pyinstaller aetherterm.spec --noconfirm --clean
#
# Output: dist/aetherterm.exe (Windows) / dist/aetherterm (Linux)

a = Analysis(
    ["src/aetherterm/__main__.py"],
    pathex=["src"],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="aetherterm",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,          # windowed GUI app (no console window)
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
