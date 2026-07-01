#!/usr/bin/env python3
"""Lightweight locked-reference validator.

Checks only the essentials needed to avoid semantic fallback:
- registry exists
- every reference has a project-local local_file
- file exists
- SHA-256 matches
- confirmation is present when --require-confirmed is used

This intentionally avoids heavy render, Node, or runtime-evidence checks.
"""
import argparse, hashlib, json, sys
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def fail(msgs):
    for m in msgs:
        print(f"ERROR: {m}", file=sys.stderr)
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--project', required=True)
    ap.add_argument('--registry', default='phase1/locked_reference_registry.json')
    ap.add_argument('--require-confirmed', action='store_true')
    args = ap.parse_args()
    project = Path(args.project).resolve()
    reg = Path(args.registry)
    if not reg.is_absolute():
        reg = project / reg
    errors = []
    if not reg.is_file():
        return fail([f'missing registry: {reg}'])
    try:
        data = json.loads(reg.read_text(encoding='utf-8'))
    except Exception as e:
        return fail([f'cannot read registry: {e}'])
    refs = data.get('references') or data.get('locked_references') or []
    if not isinstance(refs, list) or not refs:
        return fail(['registry has no references'])
    for i, r in enumerate(refs):
        label = r.get('id') or r.get('slide') or f'reference[{i}]'
        local = r.get('local_file') or r.get('path')
        if not local or not isinstance(local, str):
            errors.append(f'{label}: local_file is null or missing')
            continue
        if '://' in local:
            errors.append(f'{label}: local_file cannot be URI/ephemeral URL: {local}')
            continue
        p = (project / local).resolve()
        try:
            p.relative_to(project)
        except ValueError:
            errors.append(f'{label}: local_file must stay inside project: {local}')
            continue
        if not p.is_file():
            errors.append(f'{label}: file does not exist: {local}')
            continue
        recorded = r.get('sha256') or r.get('hash')
        if recorded:
            actual = sha256_file(p)
            if recorded != actual:
                errors.append(f'{label}: SHA-256 mismatch')
        else:
            errors.append(f'{label}: missing SHA-256')
        if args.require_confirmed:
            confirmed = r.get('confirmed') is True or r.get('state') == 'LOCKED'
            if not confirmed:
                errors.append(f'{label}: not confirmed/LOCKED')
    if errors:
        return fail(errors)
    print(f'Light lock check PASSED: {len(refs)} reference(s)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
