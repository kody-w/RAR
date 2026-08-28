---
name: "rar-cowork-cookbook-demo-data-write-off-bad-debt"
description: "Generates and creates realistic demo records for write off bad debt in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_write_off_bad_debt", "rar_sha256": "d246bc66a729aa0fd8d868bc7a3702a922b2e94fcb2861a06ffdc1b2db1cb082", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_write_off_bad_debt`. The original RAPP
agent is preserved byte-for-byte in `demo_data_write_off_bad_debt_agent.py` and in the RCI capsule.

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

Write off bad debt Demo Data Generator — Generates and creates realistic demo records for write off bad debt in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-write-off-bad-debt
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_write_off_bad_debt_agent.py` and embedded as the fenced Python below (sha256 d246bc66a729aa0f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_write_off_bad_debt_agent.py` first:

```bash
python3 demo_data_write_off_bad_debt_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_write_off_bad_debt_agent.py   # or on stdin
python3 demo_data_write_off_bad_debt_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Write off bad debt Demo Data Generator — Generates and creates realistic demo records for write off bad debt in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-write-off-bad-debt
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_write_off_bad_debt',
    "version": '2.0.0',
    "display_name": 'Write off bad debt Demo Data Generator',
    "description": 'Generates and creates realistic demo records for write off bad debt in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'demo-data-write-off-bad-debt',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-write-off-bad-debt',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '132ad93d46ccbb0b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/write-off-bad-debt'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-write-off-bad-debt', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataWriteOffBadDebt(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataWriteOffBadDebt'
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
    print(DemoDataWriteOffBadDebt().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjSJbtX2FiPmTVKDMEYhFkW5s9doQQaAMhKsui2BexbxLU1H8fR1JEVk111+s2e2ZPuQQI9+t3Pee6E7++2F0bFfXL15eDb+eQaKdpHPk1ZOcexBbXor6AH8XFAf8gt8jbOna6tqibl88vnt+4dVy2cZGD6aKf+7Xd+s19qlv792vwI42bNnYhz88KcOsWtddAQVFD1zpufagIAsixPfDYaaE4h2yoAfOd4ga1fm7n7X1oW9txHufhXXQZp0ULNS54XMdF8wo08W92VqZ+8/L1p58/v8Tg+uXrry9uajfgqxcOrMzZrX2aFtSCgLE9DqwG5qV2HoIB5QBckIP70q/Bchn4yvMD6Hn3Q+OnwWfov/7rcrXrsPnx67ccen6+vUx/9l0OtZEPtYXdtD6w3S5tJ07jdniF6PRqD5Mb2q7Om8k64ME8fH3M/C6pKKG/T89+eCzyGvrtD99einJyKfDvt5cfIeCHby91N12/TlLKH358TYurX//w43c5TeckvttOwoDWr2/P+6dYMPD70Di4r/p3IPURScf/9vI746bPQ+/JTjDz5TUp4vyHh+CyLvopQK7/w4//TKwb+e5lCv+/JPenh+DItz1g01PxHz/fnfwzNHsa9CHzny9bgrD+O5aA4e/LfYaejvpnsu/+/1+i0zgHmf7u8X8o7h9NmP0d+umf2vZXEz5DwTeQ1Gncg+xwUv8r9OvbYcuzP33yvn/56effgOj/q5hD0dXuXcJbZudx4Dft29tPn5r7159+/ulTV4Jc8+3sravTfyTzH/n1vs4fPPgc9cMf54L19fySF9cc+sh06Nei/I/6t1fIAMDhff+++Qr9vl6mzwyajHhf9OGC39VMA3T9nR9/fPkNQEMOrOnc+2NQ5f/5n9AmduuiKYIWOrhF10IgwG2c+ZPyxyhuIPB3qu3aB35tYuDY5ziQ/1OEJ42LAPrl/7h3rPziPrFyPsHdmwdQ5+2Oc28A594Azr1NOPfLK3QEMos6DuPcTqE9vd1+y+3QB3AH1itrv/HrHiCJM7T+F4BBX6aLCR1/+Suxb3cJr+Xwyx0n4wcq7dnVhEhNl/qvk1WnyM+fNrgA8P2b73ZAeFq4QJMgBij6GVjbFGkPEG3yQHOJ0xTyYoDdAPiHu2zgpa+TsF9++cWxm+hb/oBQFHowQjMHAz7Ugb58ASYFaRxG7bfcd6MC+vTrb5+g/4b+atZd+LTGFqD4MwZAQ/mgqRCoqS4Dw0B4QEABYNxj8OtvT8cCMYCLIBCxOIj9x2SQkxffe/fyQaK/LHACcnzgXeDZrCzqdiKYuH2FVgH0oS9YdHo0IXdUNC2gqdLPPT93ByDVBuZ8eDKfSAkkXhMMn6Gu8e+r/uJMzAVUzEBx2+0v0IbdAp4oUvDfpOZ9EJhc5DFw/0cOPL4HQupPDcS8i3iF1CkLodKu7TKq7ecagf2IC+CH9+lAuA3l/vVbPnGhP7nqXhIP94QTU0+MfA/plynmgNozUP9e8752+GRzDzreWa3+ljfPdLdr/87jQJUBCrvYm0jgb8+UaqKiS727/4Cmk6RnFLxnVB45+Gfqn0gamlgaejYSE911CxjBoP9vncWkKi2Ke16kjzwH8epxf364cOqEJlc/mifA9A9hU7l8Z/937HiH0G95GoN8qIe/PUbeHf8c84ClrgZ+2tP7u3ygGHDhJPeelFOS1fWUzva3/B2rPwOr7sAE4gIqGGT4lFjvC05P3zWNQJlO9995++myyXKQeFDZOSlwZuD7nmO7F6BVPRXWMwYgQyePQtcodqM/WAUB6SARgHwIKBGDUgF4fnedWgAzgWuDusi+D4+n0AEtvM4F2oJW03+FTqA2pvxoQEGClmYaA7zw6S4KynzgY6Dih4ebyC4fykzd6VNBe4pFkYHU+H0Eng+/Z/Ndl0l9INWecPRbfp2Q1fNvj8h+6PmMFVA2m+rvPumP4X7aCv2eVP72Lb/r+AHmoKzTiY9/5xyQf3X2SOYJlRqALJn/TCCQCXfqfX2w54OeP3T5+qeW/Id/r2u/86H+x8h9haK2LZuv8/mDw94p7BVgwhzkSFz6zZ3Ovkz++nIvri+guL6A4voyFdcfZD5c9BX69/T6g4hnQn+FkFf4FZ4eKTGoSeCH5we4gf3CnL9g09Nv+d7/Ht9nEkxomg6APz+o5X0I4Jew9sNp8INqmomhroAU79gKIvAt/8iBZ4UA6M7DiReb4neVe+dYENFHwD4oADzKW7C2N3VioT9tT9JJ/cZ/+Zp3afr5Jbcz/y+3JRPAg/wEbpi2MaBWQEvTxv797qO9mW7+uAO7VxEof6/4OhXTZ2hqRT9DH13lZ+i9z7/vmfIObHR+mjraaUkwFPz4GPuxvXP8F7ClaodyUvmxeZkaqWeD+2clphoCGrv+RNrFR1FOK/5JCLgIQ7/+sxDtfmGnT2RoWnui4Lh9r+cG6OmBhuYzBIIG6gyUDkDEDkz48zJgndqvOsB13mTud/99N6t42PLb3Q3tYwf468s7Qjxj8Oz2wHBQil+aie3mIEHBguD+kUrg2b/VBz7nAjwDvci06VxghOMShL1cULYNBx7pkQTpuEsbXcILm1osnIVPYYHrLEgCsWEiCDwXcRaeg7gOTC6AvEcyvk10Hk/6LGzbJd0lgnnU0iZcH4Ud1PWRBeItUR/GKTQgSR8DrvmYegFg+DTyYdTkwY+WdHLG09ZfXxwCAyMlrFnRjw87pwx7eVo6+8ihasI/W+Z85cR6dXR6oa5lH5FE11nRGWeNjVDodcOrg8wjqmuEmq17tahFHEXnS1nqu9wXpbWaqh0SNmIdI6Oc4e7Mm+Xgmc7zu0TBSs8+8acDLiiCtq/q8DBSRzEW/eHSrYUh1cs1oq1NdEl0QaqcDtJosIcUa+ZYekodYndQGhvX40N6XOPW2VM2/WnmsWzRI4156delqfTaujQOKVL3GyMecNiKy4i/Duaija4qV1Kkr8TzjVl2czXH+hHpsLbfzYWu1vexW8RFtB7q1hX80+BVtY2sLFZIco8f54IRuSl6Zuuy25eZdkDSLl/G8gFflFZYZAifGulQGALhmgqD25WlCERc6MrQrJRLq8pR1FprwhzS8zHXIjs1bMcUd1nnKtVQHx34FCc4UttqgHipZttJiRXOgBHULtkSY8xJlrcuHWFTV/RRXu+bGTVeLD69NZQj+51L0qWiKO7lpPOMOZNOx+vi0HMuJoUDrjSzS2ajqzN1mdeMVHVgo8aSLmIb1bpxhzZOrYuTFdskQbLdgk3OarRAotqoT8dIPUq5UF2yoacuobgtTyUuGhye6GtdsHf4bcMbVSIiIXWkjCVOpqftjHTXSsYQFuJ4LVofscQYU/jaofBwbtFLXI0btCEH0dVuua7vHM0U9yciI4emRjI7CZSRJolzx19PNRuIp+3SXo+bk4XZmi+aGwMbqRslOLIJxglRvThjObf2j1e9ca+HRbZdBVrQLQk7Rg1DMM+zbDiRm61UX5t9YxXhyjyEy2Ix2Jcqy3LeOpYqr9vHQ6pqleKpthVTs8wwZixHEfiM25MCt2QHwbWrnevMJPJ69XKYcILjOPJYl7KesUQD1UqX69mq1WtH35+MfLT2qzq101MrXWIZSa6LtSJuzlc1NpUEqbcz+LZCEjlYHzvmgBbyAaDjfizmV4fCj2HMFM7IIlUmdoxJClduv08lvRTPerxXbxohcwxnWSvCZrtdtD7t90cj80X+6h5VfKkkrlLM+D6/LPJEkCx+vyJWC4bfS4wE/ufxc3c1/dv2MGu8y02z8Cpb7IcTqrNb8tqKiLleeDtlns+jeqZu46V+kM1AyEZ1dqk6RbCCpJRw1RtmiT3KdlL7PquI7glm2tYSw7XL97OLtc2IdZwQiFnRc5eXjX15kvmYrrYejZeOt1b18TBXFmztjIVHNxKx2Ys5it5wODZuZhKpenENFuZasRZlSzjGbOPZfFkKqWGRTnwsymZ5K+V0V0VUbR4KpwoGoIpVmAbAcqHzC8HZkTNGievSUgCgmGzBB10pYRfE4S7KrbdJQ7erPeOZKCvNLjsk02GRQJM83W5nArzLZey871e73mkQxR4GJG82Mhzz+KqO5TPhjkpyytwyPBk2kenGrDhG5mo7KIXgMsoRT7SgH9JS7RIe3VLrckPtNb5AUXzUy80udulxW28qTeYWTBYgAF/IKKPO9Wm7O1yYWzCb5VgQtry0D7wr1m78Y89eEoEztbKBfakNcxH44Li8hPujIBywNMUAzbiMrJ6dFYvYeHlYr+J6M5LB3gl12M3lWD/PTGNA3ajBZxmda0ZeFuSCxPaWz6yYjte2qdxdmHq+j4zikFTKxTIVPxoOYcTuu1O5r4icd0xjga5XETPQYDMbOonF286m0U/wKrVQLsJo5nAo9g3Y7KwbPoMtzExuCSrVB6B/m0ZCHiNkTiMa1d4IdtSO3JA0JDHz83Qx7+tWO1/4w1E+YcTooINvWMJx6N1ctS5zNjyzMQiqPfP5rVAzCIJuGyWOrpQ0Lk5raz4HTDJfNZfYV6VmR+r9EBW0ZZl9RWLyipEbdpMqyz2uJFrNMjXiVtlRC7XLGHg3Vd4A4kfpvcdUSkpw8Um+6EhwMehA3kZrBiFD/Oio9iDDrFu5fLdbqqwXJ3CZrJPqstvIzHY9qulKmMN4yrYLmWS3M4MeiXTDpxuOt13soiqmwC9GesiwM08dCH6nwsV8GXNcd6va9mrmB8O6Luxda9WntDBwTXJvc0Wxb0mNHk7wMe1u14t7TqykjsSdZVfnBA1m21S0NDRNOhIk62nvD8viQJosIoEMhauIrxPFd2bZ8raHM21NpuaGjNlFYKSZb7rpBbkG+v6yIK8pXbhncbOlAIAxCs86t+3WO2W1fV6v3O2Y3JDKOI0KyYjczpBn2D7XdL7paMle2N1Y8fmtXS/hEReLs13EF3LlJn7I0/yWvp1khFgfVQtvemfgV6RYuvz+UntGfioSK0TNbJWh8WpVZdu4GyQQj0V3hPfnw+m8U3v20HXubtYRWBelwk0o2YSPYNp3qyDbRXu6R9uW49VY7099wi6obNWRcH00FK1htDEgulKXZfym3ip1JR01+5ZXW2YLRIqRioF+Yy7qUokeLrjAmszB8FeGphjbArewBG23YxMeDQvONd5bsP65OVWANNf02qHnMNXEpXO9iEVrbU6AapZdcNiWxQ6mkcEKOnjb1gwJ90Zf4LySNwW96rih7nXHA3qUyrmLi5GwemWnzkks8APHgZeowMLojUELDV1wUcediWOT9955QDOlTBE3Q3W8t7pRGLRU99u+oyyM7Q9ezAgASz0/ZzFZrmgmCq+2dUKyOpW3zDxiy4NDb9LDxd2f5kEuU/tsFE/yOTLCQVWP8IAP+agU3gWHI+VUCXvmRun0xV1j2nW4GCxFEPgo1sZQJXIdDZVuG8seOJK/ihsZVWwSWTOKGqmbPUxwXSx2h20mMofRNXbnJZ7Z6VHI2bWkhvqBt4lGp4lSLuZVEKwOVuAg/Po4NkW7kshuHSyEzfW2lW9GX4q6zZaVox9n2Kqxdpq+lSX1ZvlcuBV9wHh2JguyJkiFMT8bVaD7lBgNWp1byjnfpAyM3OL1YsUN6jZLOI5kyxu2K3yviXNK041oR58WnmRF56pdK+Gt4BEfH+WbYK273qtXAVym1y5l1APMdSF61gLR9LXSJhTKj3TFPa2vQdaUO4eZD4skp3YH3ZTOyz0Cd5lWrS57tMmCuLKo8bAIxu1ocBt2Wa/CWacnfBkdOB7jfbEQOUYSiGi2WSqZ14D0zg6pF69KV7GuKsrKx9PMZpji4uunTb9BFW5mCWd0dpVndV4SINl36dnu2E2c1Q2yWZ9aQ6Sw41nyD7TDMWgW4idaG0wrYxvCTX029LSKJ1cx4pfpMUrT1sc0dC83dpTRqGA7GCDetFxd9VbkrKRL6xtjcdrZx+Rsv9oU7VIXTf6M9p3RC2t2p2K5hXdWwGwic4ctND/lWJ3oVHot6oW4NuBbeqOc8HhdZ2awUZnbMhHNfCdTgJ9oZLf0DV9I/FJDveXRDi/X83hdImVmHBKfzBCpoxhTm+t+YlsCV4qCaVY54fI8KXtIZuR7zorjGI4kdhltS24uizskdRVBlDFKcUG7zYBCOx+jECOZ8+XsjryQC/YGrvTNsEuO2rEeBs9LZktGi50xC2mFZtQyUFq6IbQgL3Nav5YsAPt9f2sIkuNL5MQbFznN64vKL/rGF7gNrK7IAlOaKva83uNUlpqvAwVxt6VZbpYsWhBENUtXFsOLIyqY/cHoUZPXc0m8EBgslew81YiMiZaRGQcR76PE1vQB+xvO0qu8XDWMc+0uV8utEutEOjNNEDGlONfeQFyYsF2eSRVJVuc1e4rQOtra7qGygRr5Ym0ylkSK+aonK/XWDhksDYutuVD2zoVwLZXhhcpKjwhPrIDEuWJE2z29NaT1tapHf855gyN2ZEFv1I6Zy0siua5mfXfokgpkX44ihc6JFOw1ijgf4BrvqwohVdbqLQM1de6USTgsaQTfYh2FnmhKyi+zedODHouXGLbnDl0/n/NbkpIVy6cW43LdOBRfLVJqz5vVjHYWsZSEq7lAwaAiNXaBO7RqBCRrIhwfDueZY27scMVrGrpid+RtvgvjhMyonUm7l2QGGmHNs8y6NJolatK3a+32bnLGRA71dnYFX/wUmSsV6LnHXDQFZZNY9DDMmH6tDOi4OvfMjCU7sceCeY2elaTfZOFpY6z6ZcRhvTZ0Nc7OQTpv4SisrrqxhYVr0NRL57oRd9weNLdOWiyaTLalBeyMuW3OfGTWzonbDU5S2vCkaA6qhhGojis9UrrBktUFDbWJhMXSTNpQWdczh+21UXVMtOmUwNbADh1WeuW2X45Rh3c4jrJEcJY7mu7HTW1hEjsX5U64irt2jPfa9eJH22J/uInUcJvD84MMPB9yTX/0CBGTd06K+5WMo+sdV9xyKucuO0zCFZtRA7VYbvglW+MnV/ax5ZjgVymOzsOMVje7a090h+WsFZMbNuc20i6o6CWfFWnbA0wEHQZLk3JDe+eVnVt9CPJE2jucLkrU7JobhuJG/FwaFWx7jEQsnLELxF4wy75udBYVHZ8DnLffjxtsKxTRTF8Gnbr1rKMcxr25B1UyNg3VqEgrdscFjiDYiN9W7g7vInxDSkEvco0vin1xpclcLTRhmLGNf91q6s0ZkWzrLXeszl4dJanrUyegOwK3UMPHNzCFukuj2p/tCD2SxtVTLkdCQ8PwyPQ0G2MFSwqw3EfL5rCiN7VE0n5CEupp2Eo3QnAPlkfpyiwXwizYOYXn3GiV7dBmHq22veK1VDrifTo3AnQcsDpPIyV0bpi1BOFEKqnlHN7E6mvrWR1CLjCvOdrpDvU2gVSPo3v0zkcnA33yfkmmCLVkV8HQF47jswh106WVKKVStpLB/kdNDNM18Xp+dTm2oiIxKU99twH1tBz6W0QI5UoO9VLBuqAfb+ZF4CPKcd1oIMYEZFp3PPk12EmUPU4UpN3BNr8OLHy3ojhtJGim0hJGFDKnCEdqjOEVoqr9CV1ZhtrPqFRZ4DA8N+KGKQ7p2TwG+BHf5i7tcxEZCGpwioTZ0cNDnGZsbJfHBMzY5yve7I0gpXsr1zkt2eys9ILxatqNUrnTc7Qpbc5CMxobBs6ikNYKA3J+aLVw08e7Xd4t4GBcHW3cY+CeyoSOdGjhZC63Rr5k4T3tkkTnwuuTepKEOk5mxko4zi9lqnUzb7FtWDdI8qu0Zh2JvRI+LMoX+6zwtLyYZSttzp8kRLrovh3c2tugLevO0HaEsxcxVJP40juOBEcZXLDoQV9I0y+fX6az5ueJ8b/08nc6yft/dqD4OPt7f2N0Py72be/rfa2v/5o6P39+qd0YKPM4LG3SLnweL/6vo9Ivf/WOYZo5PN6jTi+0bu37YXprh9Ov/bzEudc1bT28NUXa3Q9qP784XTP9JkLz9jyQfrkbk5WP0+2n8uC6qD2/fmuLN9duopfptwSmNzS+F9ut/7wNn4fGYOIAohG7zRtK4G9+XU4GPt9YTOet0yuLl9/+B+x3gi1XJQAA -->
