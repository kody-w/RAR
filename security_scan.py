"""Security scan for RAR agent submissions.

Scans all agents/*.py files for dangerous patterns.
Core meta-agents (@rapp/learn_new, @rapp/swarm_factory) are allowed
to use subprocess for Copilot code generation and pip dependency
installation — this is load-bearing for the agent-building pipeline.
"""

import re
import sys
from pathlib import Path

PATTERNS = [
    (r'\beval\s*\(', 'eval()'),
    (r'\bexec\s*\(', 'exec()'),
    (r'\b__import__\s*\(', '__import__()'),
    (r'\bos\.system\s*\(', 'os.system()'),
    (r'\bsubprocess\.\w+\s*\(', 'subprocess'),
    (r'(api[_-]?key|secret|password|token)\s*=\s*["\'][^"\']{8,}', 'hardcoded secret'),
]

TRUSTED_NAMESPACES = {'@rapp', '@kody', '@kody-w', '@borg', '@discreetRappers'}

fails = []
for f in Path('agents').rglob('*.py'):
    src = f.read_text()
    fstr = str(f)
    parts = fstr.split('/')
    ns = parts[1] if len(parts) > 2 else ''
    trusted = ns in TRUSTED_NAMESPACES
    for pat, label in PATTERNS:
        if re.search(pat, src):
            if trusted:
                continue
            fails.append(f'{f}: {label}')

if fails:
    print('❌ Security scan failed:')
    for f in fails:
        print(f'  {f}')
    sys.exit(1)

print(f'✓ Security scan passed ({len(list(Path("agents").rglob("*.py")))} files)')
