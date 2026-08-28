---
name: "rar-cowork-cookbook-audit-scrap-an-asset"
description: "Audits scrap an asset records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_scrap_an_asset", "rar_sha256": "4c65e9e1a2b9de45144929a1cd24acbdf66613aab9b65bc4375d20db4b9ceec1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_scrap_an_asset`. The original RAPP
agent is preserved byte-for-byte in `audit_scrap_an_asset_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Scrap an asset Completeness Audit — Audits scrap an asset records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-scrap-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_scrap_an_asset_agent.py` and embedded as the fenced Python below (sha256 4c65e9e1a2b9de45…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_scrap_an_asset_agent.py` first:

```bash
python3 audit_scrap_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_scrap_an_asset_agent.py   # or on stdin
python3 audit_scrap_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap an asset Completeness Audit — Audits scrap an asset records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-scrap-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_scrap_an_asset',
    "version": '2.0.0',
    "display_name": 'Scrap an asset Completeness Audit',
    "description": 'Audits scrap an asset records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-scrap-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-scrap-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '333b1209737f1d37',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/scrap-an-asset'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-scrap-an-asset', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditScrapAnAsset(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditScrapAnAsset'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(AuditScrapAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6adOjVrLmX9G894PtS1UhARKoOjpiQICExCIWAcLVUUbs+y4WX//3OUh6q+zbds/tiBnVooVzcnky88k8SL++2V0bFvXb5zfVs/PF3k7TKPTqhZ27i13RF3UCnorkBv4tnCJv6+jWtUXdvH14c73GqaOyjYocbCc7N2qbBfjILsHuhd00XruoPaeo3WbhFzXYnpWp13q51zQP+WWRRs74/Dyyc8db2IEd5Q3Y1qXex5vdeO7CCT0naT4Bfd5gzwKat88//+PDWwRev33+9c1JgaZ3/eqsnczJWTfYkdp5AC6VI3AxB+9LrwaGZOAj1/MXr3c/Nl7qf1j8538mvV0HzU+fv+SL1+PL2/xH6fJFG3qLtrCbdrbILu1blEbt+GlBpr09NsDNtqtz4NWiAQjlwafnzu+SinLx9/naj08lnwKv/fHLWwFMsGf8vrz9tAAIfXmru/n1p1lK+eNPn9Ki9+off/oup+lusee0szBg9aevr/cvsWDh96WR/9D6dyD1Gamb9+Xtd87Nj6fds59g59unuIjyH5+Cy7q4e/kclB9/+iuxj9CkUdP+j+T+/BQcerYLfHoZ/tOHB8j/WEAvh77J/Gu1JQjrv+MJWP6u7sPiBdRfyX7g/99EpxHI2G+I/6m4P9sA/X3x81/69q82fFj4X95oL43uIDtuqfd58etX9czsfv7B/f7hD//4DYj+v4pRi652HhK+ZnYe+V7Tfv368w/N4+Mf/vHzD10Jcs2zs69dnf6ZzD/D9aHnDwi+Vv34x71A/yVP8qLPF98yffFrUf6v+rdPC91OI/f7583nxe/rZX5Ai9mJd6VPCH5XMw2w9Xc4/vT2GyAFQB515zwugyr/j/9YCJFTF03htwvVKbqZWfI2yrzZeC2MmgX4O9d27QFcmwgA+1oH8n+O8Gxx4S9++d/Ogws/Oi8uhO2Zbr4+2O6rnX99sN0vnxYakFXUURDldrpQyPP5S24HXt7Oesraa7z6DhjkNrbeR8A9H+cXiyhf/PJn4r4+dn4qx18ebBk9WUjZcTMDNYAhP81eGKGXv2x2AO16g+d0QGhaOMACPwJ8+QF41xTpHTDY7HGTRGm6cCNAzYDIx4dsgMrnWdgvv/wCWDf8kj8pE108Gb6BwYJv5iw+fgSu+GkUhO2X3HPCYvHDr7/9sPivxb/a9RA+6zgD516YAwuPqiQuQA11GVgGwgECCAjigfmvv70ABWJy0JJAhCI/8p6bQQ4mnvuOrnogPyLrzeLmAVQBollZ1C3g4UXUflpw/uKbvUDpfGlm6rAAjcb1Si93vRy0oTa0gTvfkMyLdtGARGv88cOia7yH1l9u9aNBeRkoZrv9ZSHszqAvFCn4bzbzsQhsLvIIwP8t9s/PgZD6h2ZBvYv4tBDnrFuUNoh6WNsvHb79jAvoB+/bgXB7kXv9l3zuet4M1aMEnvCARQAZ5xXSj3PM554K6t1t3nU/1thz99IeXaz+kjev9LZr79GmgSnjIugidyb9v71SqgmLLnUf+AFLZ0mvKLivqDxyUP1j09/9vtE/+vLiS4csV9ji//OQMNtC7vcKsyc1hl4woqZcnxjNo8uM5XPaAa37oexRD9/b+TsZvHPilzyNQMDr8W/PlQ9kX2uePNPVQLlCKg/5wCqA0Sz3kXVzFtX1nK/2l/ydfD+AQD6YBgAPShSk8Jw57wrnq++WhqAO5/ffG/ELpxkVkFmLsrsBZBa+57k320mAVfVcOS+kQQp6cxX1YeSEf/BqAaSDSAP5C2DEHA5A0A/oxAK4CYrGr4vs+/JoHm+AFW7nAGvBbOh9Whgg+ecEaEDFgRllXgNQ+OEhapF5AGNg4jeEm9Aun8bM4+TLQHvm3Mjrf4//69L3ZH1YMhsPZNqu3QIk+5kwXW94xvWbla9IAaHZnB2PTX8M9svTxe97xN++5A8Lv3E0qNp0bq+/g2YBqiV75uJMOg0gjsx7pQ/Ig0cn/fRshs9u+82Wz/80Qf/47w3Zj/Z2+WPcPi/Cti2bzzD8bEnvHekTqBAYZEhUes2zO318lNlHO//4KLM/yHpC83nx79nzBxGvNP68WH1aflrOl/jI8eY8fT2A+7uP1PUjNl/9kive97gC9UUGKGyGewTt8FvHeF8C2kZQe8G8+NlBmrnx9KDXPSgTIP8l/xb7V10ARs6Dud01xe/q9dE6Z855xuad2cGlvAW63XmgCrz5fJHO5jfe2+e8S9MPb7mdeX9xrpgZG2QkAGA+gYDaADNJG3mPd8ARcCGy59d/PCFJjxd2+szcpgWW2fWj/l+V8CK2D/NAmgPumIf/uS09KRwcWewubWdL27GcTXueNea559tQ9M9aH6UKdLjF57liPyzmAfbD4tss+mHxfjp4nLHyDhyPfp7n4NlPsBQ8fVv77dB3897+8SdmvMbivzAimtli5penu577nQoekSrtFjDeReGBSYXzGAjmJtiMj2b5z24DhbVXdaDrubPJ3zH4blrxtOe3hyvt8+z369s7mbyC95rzwHJQtaBoQN+DQU4DheD9M/vAtf/RBPjaAwgPTCNgE+Zs1t7WW9nIbet62HqFYVtka68cF8Fs5+b6m81mhdr2bXvbrG8OhuJrF1m6N+y2dTzPWQF5z7z9Ojf0aLYDsW2HcPAV5m5xe+N46PKGOt4KWbk46i3XW9QnCA8DkHzbmgC+fDn3dGZG7tswOoPw8vHXt9sGAysPWMORz8cO3ur2BuVvYniD6o1POjnM3SLzpGq3tuZ5r/K6DeKMS9uxju1WHER1YOTQiqJM5oSiNrB1AilHqNdw3pdkCkug0xKBkLPVDvax2NEOjEqhXO2uZ3nks0to7exEsAt1DWeZyhqpkBmCdGo085r6/r22/JjfbWnPPDU4P3ChbhYV5q2oLFLjURccHFpNPM9aOzPp3L0y1pdJd9VKUBl7q/v7827pxc3GPfPRxs3rcQMxlH82VyvogJWmjZn0Xg0Nub3pUrRdtZ5UV/UF4UqbNaXqknf7+668132qpknZKlXppfzBPeOCrWul6QfBamWKl/RWY0SHaOOVyXSNtczCDI3ApCw7uFhK2Fkb6zKuLgpH6LaudJ6lns8YVYFo8Jmkx4hvI7mxPbjKOtvqQ3K8HSx2r+Shx2+YS6NzleHUGBWPlNxw9nQ/CpHZp23WuDV6H3csIKylcgtIZpRxXCx4Ppc8ja8bo5pov7WS0D61o7+iD5h5atXQO+GtqrbW8troVnm3ZZg5TELY6Af5ph0rdn83mnrnrKWL2IwWRdgrA9ng0sZPVjGLnnat0+8IeYqElNHz0zJ0NpPCI5ObjSD5r1Qvo2uyhMv91j8eiVAb2VDu8mS8Nngietn1ZkGZE2RTey/kVC3Q1Z1VcxcYA4phzBMeP+KmZY+BMLIe0Xj7REuIPLhsJ1i6HX1MU0ZCP5z7sm5p+ZAKzi1ipxQtLR1Nyzg5TAi+SdfZ0dWvhjUh1+GATW6n7AaBE+ANc7IyW+Wy/EhqxgVZX+kqqY92dr37Q4KYQX62OjOQ80LOjXN6GrDSWd4ReiP52oRDPhwgfLG860YomuuhtWydn7RoQNmzvamESbhhebI1jbLO0mlgrsP1tqfXCGela36vYCib+/DBXqfuaZKok1aGqsf1dRrFA83zRFJc+f1FrxNsObIofQv2pB0q7DnaxepxPCEDc2SUkByZ694ZWDJZkWmjSfQgHJg6c8cCJzdwM9nXrhKv8lJuZCbKLnoT8Ay+ZpXDetioxH2alCNohbc7x8DLwKOvh9Q1Qg4uDv0mg1d+IQtwdbsLkV9D6qr3slq4nNZhvEITJ9eyQr5qhIIZSivijE5mQwRvlAS6FdXpnCT1OcaZG1K6VRWfuNXRv4XydqUkbM0Uy1yIYV9GfadWtYOuNtdB2EKdMpRCGd0PZDO4IZxbDs5U5VRmh7WmLo/55ng6DVcnbeW6Vk6wGdXZkMiVt+wiXiloVi6x1DFIPy88n7l1IifarjFszwfqBoOGIEqBF4WEu2UEpDv4Kw7ubT/FjKMV1+Wo52jkOEeY2ihITxtBxJtVUSEIzdCuUGaDkZQXrJ0Mo11imsxj7FL3gii4Ctwk3rmGwmVqV3n3saxFIzfx85pbbo8YQ6ExbKLeuvckB6Fy07aXADIZp/ARKlLBSGGtu5w570yTIQStaaQ/J13PwIUoYWcpSyVaMyjQN+ixP+SZiWxdLOh6jlmfjkOOoSQDibJ/Ug1jWe3MmIJuOQYfOkqdQg+bhhCF4w1id3I0eL4c56J2FxrUQUNdDQenDtCxSMdgGWP0kqbWiJxxY3NbKzs1JzfehkVF8ZQtVRtCxDNtHTSdkZGqbvRTbAgVoL5LoLeHXRgDTw60wjOJfrXYwuJMaggR2ryK3N1Q6L1Ha+1VyhEzPye8mGbRNj9K96ZC/Jwltr4ZUscVHa2XFrXa4lvlqFS6f3RzyLDPfcAeuAqUSg5jSLBL8bja41eBBINurGCQQQ8bDz6jmrKGukMEmDQ3JCzAWNqmx9F09K6X+92hSq7kBTWJ+nJijru7Xpcds6lRM4LodVcq9G1Jhx51IsrrsSfgzMKIPF4TGt0g7sXcx5doR7fJrretdYf59smmEDWl6qvVy2e1nu70MR4DUhpsVz/fL8W9C5uSmYY8X05btLNrZAoyNwkYym009BSMwhn3RPzI7TctEl6ck4FItnNCEtGwY2jy/TheOq5FnjxrX47J4MeddL1uCQGyL5xgyx6RjyY/8rpRslulwrvmss1PIQf6YE0JwzlhyUqLJ2btL0/3suO8ZVhgXStCEWPvVtSAqGjGUoG154vs6laJC7kaG5phxfZVSl1vzibCq5184l1lwJLWzbLC7nG2Qf19pneGtNyTO+3MHu1VFisXvkzTA7OfDHQjN7Cx5I6rHYrQlexpOibJmc130TmwdGWNlSlnWShrL53zrVzGxSBvFD9Hm4I/OvFhOjqlcOdGSnQOzPYCht1t1xFrtUvIcG9KZOHYVWbXWotb1ikIiTKtj8xxSRrudJxy2YQmV63DJmbttXveo6th56urskLXVcj1siPVlrWvEvyu2KQaORPOR1JSYUvsyPlqNgrtyWc256mLj6qwh6OkJGITa3UvLu7NSGWDm0buyT/pKd2SfkZ7QWJHRqTuneJaCXGx5XSaky9nIyWhOnZVeFuoywC/0HethlGWaldnZFp3Is9LF0gn91XRZ4PVL8XUSq1qIx+yquYMCNr61mnrMcISS2x+oPCERjdKsZIY7w6th6XRTCmdOHBHZBpqyvh1bPdp5asb075Tg1nIHhOfTnuv3SIbjpfZ3Ugi9lFal5p+MpSyodeHRLhiYX814o1k8BEqVhJhjwqNZr0TIkOoNu3dRgqOIVGWSUGidDF9SXUiXXV5DNIVpTOdvpMks9Qguii13spPgsHvGLG6grHPLAapTiper2SzCPDcPkClOB2ES4ofKIKDFGoI8pPPnXbROe/0Koy7GCX70wEp4XXTU8vOtigKxzjMXq+Pm2t8G6JwRxLw1UI5wqYG+aIydLDnbVaUYiEWx/VVhCM3tFzCIum0GtdGzba7LpDdjkfAab7KcgVh4jUEk2kqlrrqL/2rXBYE0dcxKd92lrjRmxWdrnbdhaXzKUoktcV5Sb/XLkU5OGtWrmGkZbg/8LagiEaSGPwIXfAB5+zMcA13pxuGeL4EOcptR5jXUTXZmE53AnmDMrjl3gZxO3mjK++pbjSPNz65WMwtx6P9TeWXu3DP7cXt2PQ9m6wYZRqOttWshbvZi83A6nm7KrJ2ukpNZyPOKu32+2BNOwq6WkOiysK15lxoMsgbTFiJI5vu0eDgcs7u6mTH1NcOqFUrK4g21YIQzhkx8gV3z7QWQfAtXiHLeIxryrzqk59EUCjixq3js9V+t1XjPielE0umids53Z66GbCe8EfyyC2LnjUTbVuWK+rirThyZWU8I5O4LYNiFyprt7kNAkQQbhNe9Lxg4z5mFfmqM/aVGwy2qszT1uhFYdAZartOuIQ4hkdstyqFSMkjG5EdXLuuy2A4rkhUJemVNwE7NBOtlIt91C79gQkwGSal3cX0sPyO3poqqwNpeWuwZs+rGHmuuRW0W6ctB7N21sqXRkLZYZSXPjOsbuxU5cOJNXescaac1j30F066U01uwFTGs5UcDFSZUgTekhRyUaEpuRPLLigyercxx6rBRXniU51V3cgoBSWXXfGy3wQamPxOoGjT8NTYq9oTOlobdYmQr7Uldmc53HRpKCE5z0acwbJjwXGaexLyid63dsikGyuhoRVIkr7ixKqP3dg7nVC0Yesk7YtAn6r9UHbTEZKb3LWyk4ee6et67ONqZR1uxhrZaQ4XJI1PcAUxQK5kDCaZMivtnEQ+54D5IrqhWszfj3d+OMRwvPTbEcqWdwy+UwYjtsuU8GK+2vS4V8PdMfJ4Dt0MhYOfenGa9k1frk7LdRuKUndxslxKcUEJiByiO2Xq2G2qTMHW4THXRXDojEkrvteb0qEwBFENeeVMRSdFxyOsXQ7rXajlEArJt56PeTEZPNLeQgaKbXp2d7uQm4lAG3XimBveY9dhiXpMuelEubC95JCvWbQeNQM5DMjhfo16rb2jRCcpdi9CkJ/k8GnXqehB7WgYZmnIhQ7u3iHM7aRc26zLA1I0BREpD6YbKtjZjiCyXer5DmXFyItjIgQnCarY7Xv1MJx4wpD4Mxh9sC1JlLGw77UD52aTRNfd4SIQhJCv8yJTdlAxNpsu7h3Ba06ITon9BsCSH7zrNS+SoVvyQs0dYYvPsLXKE3ZBx9F0991Ig2nuhtbBEY527Na5Ohy2F1ETtGJWsrZZY6mRxqM627d0lvtmRg9jr/KQTrmthC51WkaQ1nFQG5qMOzJsazYKT1F/ES+OrAmB4tcBbvoUoVOom28PmixvfbtxL6x1AvHh9GG0YhtxU8XH1drE72Ti3HX2cOC7iceg7doQHabXHMk/lN6NlA9YV+sqzfCqEnGrPb5mgkYBnRpuTmg5Uv2VhDUQrrA7gXPu9qBfSB4C5xCoBGbXDa0LJ0o8SwGncRmDZmtLuw3n/IAG5yNd6g3Dn5KrU7mCvyklLexhWuDBhMsnzeXKiUa23fCMDsbCUItw4t4LHEVjXQgOtzB6BTOfkV7vfLzVCdbSOOHsl2wqQZ6E2zgjt9Nea7bDkdCaKdsNG7pMicnK6hVZXfHQvPfUwC8T0ISxzaa7J23uduhphe0OewkNMKSjMdYmHNqSlyIkNXXRHCjdpL17QeeykxGNHuApSU09OEhd3BYWe2fDm5m/1q8r3Nn19dLYF84ai6VDUXV+MXkcJcIOybKTKg58QZmXWtBGEotZIrbwutqxo09PG/lENxVUWHfFGpSbt8WUG0SKwDYEnMf5VQzr/pqArOt2Y2p3zyc8tBkIEsb9M1wkZ4lEO7SXBsQr7ga8cY6icFtey7AW7vVuIHE5N48mgis4MWVbN2TEDUpQjX+0oat6SJicPWTk8d6zYrWzGiU/d9Bw2d+RxBPKdJyEpda1hOGXyUAHl1Ta3PlIGeD2eNEqCunqjhG1FS8uVUJYVoNtb+vsyMHGLk8UDxcdKldqexWcC3pbqRwzllcvu1D15krcc4NdOxCK2nG6wfDtFXUuwfLEprACW7u1xF8YaQoJ/0g5Ceg0irTt1zJ1xcgpHItL1isjFDOVbhIJyk4G7XTXQNP5vrhprW5W8jLv6rSQRnBYj2uOuyMFW+7gyT2pNWmZzJ3y72kJJ3KGjFgc+rjAe5iJicJ9I9QtxBY7Dre0yw0cZKOmExD+vpaL6oy1lzWynIgVEdC560pUFRysqdnHK0q19ll2zShpWsIqfY0w7WIo8rqAWVQocISa4kMhw2F4V0vavsVLk6CiKk2AopIkyb+/fXibb5K+bkr/y6+L5zt//89uQD7vFb5/BfW4NezZ7ueHrs//2ox/fHirnQgY8byZ2qRd8LoN+d9upX78s68r5h3j85vW+RuxoX2/L9/awfwToLcIVGfT1uPXpki7xw3cD2+3rpl/m9DMP19xwPPbw/isnKU9lMzPzuOe8de2+OpGTVk03tv8w4H5Wx7Pjez2/W3wupv84c0dAeyR03xFN+uvXl3Onr2+/ZhvyM5ff7z99n8A86+atUolAAA= -->
