"""Security scan for RAR agent submissions.

ONE POLICY, ONE SOURCE OF TRUTH
-------------------------------
This used to carry its own pattern list and its own waiver, and both had
drifted from what the registry actually enforces:

  * It banned eval / exec / __import__ / subprocess. The registry deliberately
    ALLOWS all four — dynamic code moved to CAPABILITY_PATTERNS, where it is
    permitted for every agent and recorded in the registry entry under
    `_capabilities` so consumers can filter on it, and subprocess was removed
    outright because wrapping a CLI is an ordinary integration pattern. A
    scanner enforcing a retired rule is how the nightly health check came to
    fail 60 nights in a row.

  * TRUSTED_NAMESPACES waived EVERY pattern for six publisher namespaces —
    90 of the 320 agents on disk — including `hardcoded secret`. The docstring
    justified that waiver by subprocess and code generation, neither of which
    is banned for anyone any more, so in practice the only rule it still
    excused was committing a credential. That is exactly the rule that must
    never be waived on the basis of who published the agent.

The patterns are now IMPORTED rather than restated, and they apply to every
agent regardless of namespace. Verified when this changed: zero of the 320
agents on disk trip DANGEROUS_PATTERNS with no waiver of any kind, so
enforcing it universally cost nothing and closed the gap.

Capabilities are reported, never fatal — the registry's job is to surface what
an agent can do, not to forbid meta-programming.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_registry import (  # noqa: E402
    CAPABILITY_PATTERNS,
    DANGEROUS_PATTERNS,
    SECURITY_ALLOWLIST,
)

fails = []
capabilities = {}
scanned = 0

for f in sorted(Path("agents").rglob("*.py")):
    scanned += 1
    src = f.read_text(encoding="utf-8", errors="replace")

    # SECURITY_ALLOWLIST is deliberately empty; anything added to it must still
    # pass on its own merits (test_security_allowlist_waives_nothing_dangerous).
    if f.as_posix() not in SECURITY_ALLOWLIST:
        for pat, label in DANGEROUS_PATTERNS:
            if re.search(pat, src):
                fails.append(f"{f}: {label}")

    tags = sorted({t for pat, t in CAPABILITY_PATTERNS if re.search(pat, src)})
    if tags:
        capabilities[f.as_posix()] = tags

if fails:
    print("Security scan FAILED:")
    for x in fails:
        print(f"  {x}")
    sys.exit(1)

print(f"Security scan passed ({scanned} files)")
if capabilities:
    print(f"  {len(capabilities)} agent(s) use dynamic code "
          "— allowed, tagged as _capabilities:")
    for path, tags in sorted(capabilities.items())[:10]:
        print(f"    {path}: {', '.join(tags)}")
    if len(capabilities) > 10:
        print(f"    ... and {len(capabilities) - 10} more")
