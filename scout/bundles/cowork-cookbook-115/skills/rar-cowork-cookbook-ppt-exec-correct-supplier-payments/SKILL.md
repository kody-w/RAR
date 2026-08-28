---
name: "rar-cowork-cookbook-ppt-exec-correct-supplier-payments"
description: "Generates an executive-ready PowerPoint deck on correct supplier payments status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_correct_supplier_payments", "rar_sha256": "83c33726f3f832415c827ee7f8fbf3c621060b896c1bf97a1724f508301169df", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_correct_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_correct_supplier_payments_agent.py` and in the RCI capsule.

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

Correct supplier payments Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on correct supplier payments status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-correct-supplier-payments
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_correct_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 83c33726f3f83241…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_correct_supplier_payments_agent.py` first:

```bash
python3 ppt_exec_correct_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_correct_supplier_payments_agent.py   # or on stdin
python3 ppt_exec_correct_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct supplier payments Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on correct supplier payments status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-correct-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_correct_supplier_payments',
    "version": '2.0.0',
    "display_name": 'Correct supplier payments Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on correct supplier payments status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-correct-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-correct-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f15e0532d898b6e2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/correct-supplier-payments'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-correct-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecCorrectSupplierPayments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCorrectSupplierPayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(PptExecCorrectSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaabOjxnr+K+Tkg8fRzJEAAdLculUBhBBIgBAgCXlcMyyN2EHs4Pi/p5F0ztjxdW6cSlU4m6C73+V5127OLy9WXflZ8fL5RQNWivBWHAc+KBArdRE2a7Mign+yyIY/iJOlVRHYdZUV5cvHFxeUThHkVZClcDkPUlBYFSjhUgR0wKmroAGfCmC5PbLPWlDssyCtEBc4EZKlkFhRAKdCyjrP4wByzK0+AWlVImVlVXX5Ec5I8hhUAGmDykcc3yqq8i5XZcVRkF4/5XeCaQaZvkJ5QGeNC8qXzz/9/PElgJ9fPv/y4sRWCR+97POKg1KxD7bak+v+yRQuj630CuflPcQjhfc5KLysSOAjF3jI8+5DCWLvI/Jv/xa1VnEtf/z8JUWe15eX8etQp0jlA6TKrLICLuJYuWUHcVD1rwgdt1ZfIgWo6iKFqkBNC6jH62Pld0pZjvx9HPvwYPJ6BdWHLy9ZPuILwf7y8iOSFZBfUY+fX0cq+YcfX+MR5A8/fqdT1nY4QgyJQalfvz7vn2ThxO9TA+/O9e+Q6sOsNvjy8hvlxush96gnXPnyGkL0PzwI50XWgNRKHfDhxz8j6/jQ8HFQVv8juj89CPvQe6BOT8F//HgH+Wdk8lToneafs82hWf+KJnD6G7uPyBOoP6N9x/+/kI6DFIbAG+L/kNw/WjD5O/LTn+r23y34iHhfXlYghrFWWHYMPiO/fNX2HPvTD+73hz/8/Csk/U/JaFldOHcKXxMrDTxQVl+//vRDeX/8w88//VDn0NeAlXyti/gf0fxHuN75/A7B56wPv18L+RtplGZtirx7OvJLlv9L8esrcrTiwP3+vPyM/DZexmuCjEq8MX1A8JuYKaGsv8Hxx5dfYYZIoTa1cx+GUf6v/4pIgVNkZeZViOZkdYVAA1dBAkbhdT8oEfg9xnYBIK5lAIF9zoP+P1p4lDjzkG//7twT5yfnmTineV59HVPi12fS+/qW9L6+Jb1vr4gOKWdFcA1SK0YO9H7/JbWucGzkmhegBEUD84ndV+ATzESfxg9IkCLf/jnxr3c6r3n/7Z4+g0eGOrDCmJ3KOgavo4YnH6RPfZz3FA6QOHOgPF4AE+tHqHmZxQ3MbiMaZRTEMeIGI9Os6O+0IWKfR2Lfvn2zrdL/kj7SKY48SkU5hRPexUE+fYKKeXFw9asvKXD8DPnhl19/QP4D+e9W3YmPPPYwsT/tASUUNUVGYHzVjyIyGhcmj7s9fvn1CS8kA4sUAq0XeAF4LIb+GQH3DWttQ3/CCBKxAcQY4pvkWVHBHI0E1SsieMi7vJDpODRmcT8rx7KWg9QFqdNDqhZU5x1JWJ+QEjph6fUfkboEd67f7MK6i5jAQLeqb4jE7mHNyGL4axTzPgkuztIAwv/uCY/nkEjxQ4kwbyReEXn0SFhBCyv3C+vJw7MedoG14m05JG4hKWi/pGN5BCNU9/B4wHMdS3jgPE36abT5WIRhLnDLN97XZ5l3Ef1e4Yovafl0fasYTeHAUgCZXuvAHQvC354uVfpZHbt3/KCkI6WnFdynVe4+yP5pU8C9dRS/7SVWYy/xpcZm6Bz5f+4/Rulpnj9wPK1zK4ST9YP5QHXsmkb0H40WbAQQ6FqPCPreHLyllrcM+yWNA+giRf+3x8y7LZ5zHlmrLiB0B/pwpw8dAWow0r376eh3RTF6uPUlfUvlH6Hp73kLKg+DGjr96GtvDMfRN0l9GLnj/feyfrdr4Y7aQ19E8tqOoZ94ALi2BeGs/BHmN0tApwVj3LV+4Pi/0wqB1KFvQPqjBQIIJ0z3d+jkDKoJw8wrsuT79GBslqAUbu1AaWFbCl6REwyX0WVKGKOw4xnnQBR+uJNCEgAxhiK+I1z6Vv4QZuxknwJaoy2yBDrLby3wHPzu4HdZRvEhVcu1KohlO6ZcF3QPy77L+bQVFDYZQ/K+6PfmfuqK/Lbm/O1LepfxPcvDSI/Hcv0bcBAYYcnD68ZEVcJkk4CnA0FPuFfm10dxfVTvd1k+/6F9//DXOvx7uTR+b7nPiF9Vefl5On2UuLcK9wpjZQp9JMhBOVa7T2MAfnqG2Ke3EPv0FmK/o/wA6jPy16T7HYmnW39G0NfZ62wc2gUOGP32eUEw2E+M+Wk+jn5JD+C7lZ+uMKbZuIfl9b3mvE2BhedagOs4+VGDyrF0tbBa3pMutMOX9N0TnnECk0V6HQtmmf0mfu/Fd0wwD0u91QY4lFaQtzu2a1cwbmXiUfwSvHxO6zj++JJaCfifbGHGAgCdFaIx7nxg4MD2pwrA/e69FRpvfr91u4cUzAVu9nmMrI/I2LbC/PfWgX5E3vYE921WWsNN0U9j9zuyhFPhn/e57/tCG7zAXVjV56Pkj43O2HQ9m+E/CjEGFJTYAWNRz94jdOT4ByLww/UKij8SUe4frPiZJmAmH3N2UL0FdwnldGHD8xGBtoNBB+MIpscaLvgjG8inALca1kJ3VPc7ft/Vyh66/HqHoXrsFn95eUsXTxs8O0M4Hcblp3KshlPop5AhvH94FBz7X/SMTwowxcGOBZJY4A6OUxjp4d4Cx+Yo4SwwCgDKW3i2hzskhs7Imb1Ykg5qe0vKQils7hGzBT5DUXLpepDewzO/jkU/GKXCLMtZOBQ6d+F80gH4zMYdgGKoS+FgRiwhpwWYQ4Del8LC6D5Vfag24vjevo6QPDX+5cUm53DmZl4K9ONip8ujReI7u/PPk4H0zCxcZKJ2yBTqZM9iIw2CnkqzyA2BikUoNydp0Yz8mjkxvqnxJpqU8Yqg00Hc48o5pUNRb3J3VXT9ylrjOkot436yIGbra0+bqRX0ayFOjseZkRzUeDv1MQEX3dKV9sItQRvGLnUZExbRIJ530lko4HZqOswkvIydeN3vtIJ3enuB8lEOdkW1i/z86uQXp15MYmCRRWCZpRb1mXqionMhR6HRyGq8T4B9iZ3uPFsIwsAY2MoA4RwFzRAtvY29oDxnreDUnJoOREQtTVZNBflmDmdwQ7c32y1vBhSOEgNWW853K5n0q8VMrNx1bm3aS66LtaLHyyJxa1G7LNZSmxnE7GzejPQw8fjp2pnXB76QVR+QM79m25g/bWdzO3aCKN/zvHfObm20ysmcoG9FdbphGco3BJGfreltuZVPaL9JAEubw03fxtF82jbCfEhsNub4VDKNZCleS3s1UW/rWVthDmqJdQPA4RrFaK3pF+ssbRWyP/F91RZpj7rlycplpYvSnXrG9EnJgRux3ho7DL/kxbG6EN1pe7gdaus6UfahxmKczVRKkkknEiVM/XjI1ZmiN5czPz9s0Ek2K1PRj9As1vhamPfp2duoq9sE5BOeXmIgTFNaiuWBXbpG4zWA5E487jK2fB5mLi9T82DbNc2lS/ZzNzwJUb9zEnm1E/fE0TmfrEB2Gmk13IK5Tltl5ybcRM4KCTOj/jCgBzIo+DN+aYULvS4odu3vMalTOMNJr7lJBHFBz/1Ft1yeF/jlVNdBUi6T4JiY9cbwy2TLByK7vvGXdWYBw4qVs75WvMcPzqDRZVjWFQzhvBX0Lg0X8mauKZLHSrqqbW7TklbFpdI0xHTCmkroLDckmsZeVPH4Tib7LdysZVZ9Sbtdh1qZsSUyhz+4R9Ner0VeMhNitzzM8elZn9PcfnukOcK45UriMl2fT41TI7arDRqss2MXkp1mHrfUtVMZVZ7DLphkDp1AmZR5VbijLvI5dxzWsbq4bU0+PSbKhmtLIBF4G0hhMenTPIbWoykhFTeE3B7A2eVwHw3FhXCJbupCOO5JgkxgTe8agZqu7XYVHnKtlVPbnoowUE9VbBK0MUmPB1J2i+Z2ayepIJnb62G1rDMjjmW/6/bYKqi3GNMdjSNdtPp0NsgLnNEtb7OrM5gd9+y26lfnGb3Ngolh3ExtP520Ge8QO313bIOoL8h5leqaqK8BtKMWMtPcyaqNlQx5vJl7zkwke0Hml4ID1vM6N8IlYFOAUoJx1PTeGgozS9eeYDJLYIqsWk5WRX81LwPfXHhhEDeMPl2EShJnhzKdEKq/jbky8afzU6mKlnHQUtGlsMDc77PaiXpCaPUq40qwc88TKcNie7NyhYzTrPk1KRupz7oisQxDDmIlnynnw8LmDZlKYu84jSaX+fRGlp2lus5AHuSVCgj5MndR0hYorMV0ZdiFijWh2avru8Rkdjgeb8sMd9yDW0/7cDIlSZ2duHNJCVZDfRWCS8xw7XFpTjb5Dg85Z7LZgGVkCduWwqOm4D3djhZ+6Q8ZHq5OB9oXe68kJ4uLHPKXdBsanYTZ6GTJqoS8uOl27G2L3l5Vm45eb9ec4HHrdR2x5+nhtmkrdyLM3SLZt4RIm1F21o2MiCrMWJgV63ElnfQxZ5znOV+oUnwsA4Ca5SDtViKjCekwyCsp6y63oU3xMGyqE7febbpkdoz4Jr7yFTZL98VOIoz9VhmGgiC8845c1lvjIIjyzSiCQm48MT9G1p5giNNtELD1/iTz/gUnJhNeWjO7plB25p5jVL9fuPvOUtLz0ImwZuziKTcsHHUdxKUhr5nimFKqGGi0To01ajsDTjJoPrPt66MmpqekmuyJ3e2QbDbnE4O2XGGF5P4MsdkXGenpokHcuptuEDIp6K6knjTukOdpaabXLZ+3+mpd0yJJytpWU7eoatnLWKm2mwmNKjNn608oY8K2G5EmCSMJrES195ZiJhXmhW0THrNb2K8B7ajOrauxFvfN5LLMSJQ9tK13svym2Hp0Zqncda2gx7NUNpm680KGJbSE4nOBbyVjoScpj8b57JRuuu3hZMrzCKVAWER+L1mLclNz15wP+CTWKyMk/AFtZYzbw/wXEV5TmoNwihRxa2K72wU7XLrCtyWwXDSWXNOrg3gl4uaWYnJY21ewZVVqa5TbAZW5TXJKir45nGJHgUrMS30t2xlaSpYjbDnNQRtqsYGeQG+35tSl8cvWYHzGaK1rKUnSNVFatMcDV8TKdLW4nLYcWA8SvdjhmquVxyStcAmjT6xOOzpKWkTViEmh76xrINulyesXJVtwgMcGs12LRLE2YzIQtc20HmQ9gW7rzbRGajFRW1o1v/IwqR7y0NJy6xZdzvIqs2IjslIJ57PZ1eWpEx/5aL4bVnsidNbbwqD4inS5bn+47rrjKcSYG8yZFeM0kUrmlhsHFrXSdlvFYjyJRw/b7iKuI6eNk73PiLYQbwSd3CexOt2xroYvMy26Dqrc5M0SZ5iG3GPZpZd3OybrTleWJRqwXDMBFsMmY7cHdUA13WTqTB2GiXCt9lW1Ip2D68/C621/ZrkF2ZzIRedumyLWyNSlpJBxwhu6z+1do69W0qydXw+L7QSnHIMRhoBnfRojZV+20ZlongzToxhDPI7PAyXL6mHW7W8A+gsjpgOvnGyXy8/tlCtP4jxgTpy8UzOyiNr1hl80RzOsquXaJoYDWFhn4bZqznJ1lI7nmbi78ivhPJyn64ylsGuSCqSpxwlTs3bO9XILu9ygX3FTAz/eGGagvEixiOCwz70o2gd0ap8IXZ8tSJaq6ekuiZa8d5J4k7ydw9V2Ji9VazZYEXruuH4mH/S96oLLrbN81cilM5cF80TzDxN+uOCTRA2c3gr0HPAabnZbh++KQEHR8tJkAZ63Wh5PmMCYZvVaDvWNqx2DQA0DzE1vyZyrT2gE6+vRmQ9WtwcW21eUAGZi0za+slz1wkYdAqEduuZ8CVmHPHVS2l13p+4y73WAZesDOmWV26rD9/MtdtQr97SPCkmvCUNWUHuGDf0gz060A+O41WWJ4gVdi7Zi28p7Q9hsTzt0dUvYbH21hNmp21pSLOYZjFH0uppvrD1YYhdLbRKXV9JSGeqbkq7N+fy4Uaeqbi221ikRORYEgXUVZ6tCpGXu2nmak50xTiU030nOfngLTlLASRkwQI5q1rGqB1XEp4F5XEbHvBeoIXVWwvEgXay91ibahsWqjoENWJJeVrnKpTf9gnaUG+Y8Po95iSe1hZOsFzOU3bkXgtqrvko6t8BgfWHr9fFR8i3r1jqtqe8iDO2rech7kXRxJrsFA1Rle1bwtIjwY70kIHlTuMydBTrgurAru6MG6aG619EALQ+ucyx3jEyudJefruomZPQtdeM4XD1bRUKThp0f8S1PtBFW1WHkWEl9UAimX10lZqoqIX0kFFpeQ3i9UM0MCdNDXTkVQURSyWwmeWsmkQWWDJeXY82Z3GXmnfG4pI1hx/quf/V2FrpQNtqW2+pCuNvQcyDKOzsSh4s6z5cH1rbRxW1QXbkJqUyoN0y5cDC9zVgMKmjyKmBjbCcsLfUGdsDgNtRc3iy1xUzud5SFC6laOIVNhf7SsMMJWfQFWCY12qCH4hBNqXbOWyXAZRw7LJ3V2sN2pcCzQxW2uMGz7VkrQe6auh4eV3oexfSFaYGOH+JWtsU11tUO1llGR1mMVZhJA1u/A9dHVjTv9izPBvjCvonzdrVUE5c7Ahufu9W+tOw+oWl3dpqnngEOq97tT+jxxGxmyaRi0xKrqyo0cXca5xlVljarYi52rEiUPsbhpFzDTV/V83izNFczR9GpSb9YTOeqw20X+23f4GQ9DXPYDg51sr8cBy+LrVyxfZlo1J2VHWYkK3eOy9bMQDd6ddWwWt96s5UTtSZ7OU+VUox7etaS5YJZ6at+1UdyazOC409saa4obRXNasopqNCMmOoMLpi7OswxWikqQOcbvtjDzNNseUdNGG0QSF2SmiuscGxlOsqZJn2Ab9JJOp1XvEJSq30bXJf1Tmm1yelsn49O6MbLLrXU/jjfihtLTvGTu6xNns9Y3x4yO86wijtYeD+zhtQ6Tyx0Ik/JrpuHBH10T8yUlnxmvQxXOgV3mxnAy6lAXthdQ54hrjtFYLvYTKSu8pR+0bgZeiPw6KxsknBIN+WwJwiKhRt5oqbpZuCKfL5hp/AObflQxgMYwuKSL7TgGEhUHE+IpuJY+Tp0i0B3e54SdSompJto4pa6ylr8rOxo3xT9ek5jy8IfTHHgGoXv4yJslF1D15Z73ZnSMPcrBXYD+6Ulb3SC5MzTdWowmJBbPIEfKDOmnRPFrE9rwKoCX+BifJ3PeK5bMafQG4DvbQyb8wV8Oghzvb7ybdFiVYuWHQ7OtrSuOcxLc1EO3MRqTxttVaZJWkbypL/qPgqcAxWfN2boOgccs/G9fQrthvMPq3S+ydrWxTtz0rXmtvfpYeJidHvaZYq+zE+L2uZNuSMKuwXX84ox3YrFuhJj9cJzjlSE6udqgG1UcLU2yv5yYrJFBbIVWIHFzqFRBm4OllomegZlRgf6ou3n5nJLXIEcSfvVzHC0i+saxSRa+8FeczPX7gRlqk8vE3ydnjwqmtrEBRYxc1lL5LTGwGqyW+1dwlFkdZrtzI6YYNu6nBaeF/K4uNQwzAcLaL81nqhLuUUVfDJlvGm0DDd0RqE1LFJ9TKFtuwn2DbuW1NU5uG2rDfDtuDGVXr7FOGcpgdU4/WCT8lSG3QgjKiwqn9fDQNlb08/Qfe92FFUMyr70k0VxIeytLG8SMpuSSr9k13a5yCTF3x2W9HW51q4hGy7byLXqlRjDXiONBxJUjXyuirrfu2F5uKrrcpp5pe+m8Y3ZHNoJztb1TY28iAKeotInXTi27pbLpX2JCzDNBefMNkLlKuFVHGUbPD6hzazANCoxKrCY9rTkXphgatWL9jTZleeUZiGMkkbJwCciuSzriDzXA4sros92BbE51gSruitH6hsn2p7FZHcptGJiCKI6vciplGBwxyYxRKrvrkCiKXC4ztxsp2VthJuSWsoy7it0o9x0KVtcieHcD/OaDt1B22TONL3kizBBk002XdABTwm3s5HTNP33l48v40H08zj5L7w4Hs/3/s+OGR8ngm+vlu5HycByP995ff4rQv388aVwAijS4zi1jOvr8+jxvxymfvrnryTG9f3jfez4Fqyr3s7eK7g3GGUMUrcuq6L/WmZxfT/Q/fhi1+X43w3l1+fB9ctdsSQfT8HfFPl+NFplow4v4z8ejG91gBtYFXjeXp9nyx9f3B6aJ3DKrzhJfAVFPmr5fL8xHsiOLzhefv1PcvnriLclAAA= -->
