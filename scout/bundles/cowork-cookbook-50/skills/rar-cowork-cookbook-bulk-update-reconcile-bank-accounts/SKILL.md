---
name: "rar-cowork-cookbook-bulk-update-reconcile-bank-accounts"
description: "Applies a bulk field update across reconcile bank accounts records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reconcile_bank_accounts", "rar_sha256": "7d2c64110d35c1c0e150615ce4c124e7596afe4553f3db79610ac49e23cf4531", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_reconcile_bank_accounts`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_reconcile_bank_accounts_agent.py` and in the RCI capsule.

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

Reconcile bank accounts Bulk Field Update — Applies a bulk field update across reconcile bank accounts records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reconcile-bank-accounts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reconcile_bank_accounts_agent.py` and embedded as the fenced Python below (sha256 7d2c64110d35c1c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reconcile_bank_accounts_agent.py` first:

```bash
python3 bulk_update_reconcile_bank_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_reconcile_bank_accounts_agent.py   # or on stdin
python3 bulk_update_reconcile_bank_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile bank accounts Bulk Field Update — Applies a bulk field update across reconcile bank accounts records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reconcile-bank-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_reconcile_bank_accounts',
    "version": '2.0.1',
    "display_name": 'Reconcile bank accounts Bulk Field Update',
    "description": 'Applies a bulk field update across reconcile bank accounts records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-reconcile-bank-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-reconcile-bank-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '57a634f9d84a6185',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/reconcile-bank-accounts'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-reconcile-bank-accounts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateReconcileBankAccounts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReconcileBankAccounts'
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
    print(BulkUpdateReconcileBankAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjxrrmX2Hqfmj7Ul1oAQn6xIkYEGIVWlgkkNvRZkkWsW8C5PF/n0RSVdvXx3eOJyZi1EsJyHzzXZ/nzaR+fbHbJsyrly8vGrAzhLeTJApBhdiZh6zyLq9i+COPHfgPcfOsqSKnbfKqfnl98UDtVlHRRHkGp9NFkUSgRmzEaZMY8SOQeEhbeHYDENut8rpGKgAluFECEMfOYnjXzdusedyvvBrxqzyFCyNRVrQNkkR184p0URMiXjV8rtoMKSpwjUCHOMDPKwD1SdOoeYOqgN5OiwTUL19++vn1JYLfX778+uImdg1vvTBQIeOuifquAQMVoJ/rw/mJnQVwYDFAX2TwugAVXCGFtzzgI8+rH2qQ+K/If/5n3NlVUP/45WuGPD9fX8Y/KlSxCQHS5HbdAA9x7cJ2oiRqhjeETjp7GE1t2iobvVRDV2bB22Pmd0l5gfxzfPbDY5G3ADQ/fH3JoQr26OivLz8ieQXXg+6A399GKcUPP74leQeqH378LqdunQtwm1EY1Prt2/P6KRYO/D408u+r/hNKfYTUAV9ffmfc+HnoPdoJZ768XfIo++EhuKjyK8jszAU//PhXYt0QuPEYz39L7k8PwSGwPWjTU/EfX+9O/hlBnwZ9yPzrZQsY1r9jCRz+vtwr8nTUX8m++/+/iE6iDBbAu8f/pbh/NQH9J/LTX9r23014RfyvLyxIoivMDicBX5Bfv2n79eqnT973m59+/g2K/j+K0fK2cu8SvqV2Fvmgbr59++lTfb/96eefPrUFzDVgp9/aKvlXMv+VX+/r/MGDz1E//HEuXN/I4izvMuQj05Ff8+J/VL+9IUc7ibzv9+svyO/rZfygyGjE+6IPF/yuZmqo6+/8+OPLbxAiMmhN694fwyr/j/9AlGgEqdxvEA3CQoPAADdRCkbl9TCqEfh3rG2IQKCqI+jY5ziY/2OER41zH/nlf7p30PzsPkETG9Hw2wMHv30A4LcRAL+9A+Avb4gORedVFESZnSAqvd9/zewAZM24LES9GlRXCCjO0IDPEIo+j18gTCK//BvSv90FvRXDL3dQjx4Ypa7EEZ/qNgFvo42nEGRPi1wIwaAHbgvXSHIXKuRDofUrtL3OkyvEt9EfdRwlCeJFcFXIB8NdNvTZl1HYL7/84th1+DV7AOoceRBFjcEBH+ognz9Dy/wkCsLmawbcMEc+/frbJ+R/If/drLvwcY09xPZnRKCGkrbbIrDC2hSMjDKGF8LHPSK//vb0LxSTQWaD8Yv8kanGyTBDY+C9O1sT6M8zYvHOL5BH8qqBKI1AlkFEH/nQFy46PhpxPMzrBvFAATIPZO4ApdrQnA9PZnmD1DANa394Rdoa3Ff9xansu4opLHW7+QVRVnvIGnkC/xvVvA+Ck/Msgu7/SIXHfSik+lQjzLuIN2Q75iRS2JVdhJX9XMO3H3GBbPE+HQq3kQx0X7ORIcHoqnuBPNwDB0HPuM+Qfh5jfmdYGNj6fe37GHvkNv3OcdXXrH4mv12BO5FDVQYkaCNvpIR/PFOqDvMWtgOj/6Cmo6RnFLxnVO45qP5FfzDyN8LdG4oHjSNf29lkiiP//3qOUV2a59U1T+trFllvddV6uHFskkZ3P/oqyP0InPcome/9wDuavIPq1yyJYE5Uwz8eI+/Of455AFVbQV+ptHqXDyMP3TjKvSfmmGhVdXfE1+wdvV+hV+5QBWMDqxhm+Zhc7wuOT981DWGpjtffmfzpnbGmYfIhReskMDF8ADzHdmOoVTUW1zMIMEvBWGhdGLnhH6xCoHSYDFA+ApWIoNchwt9dt82hmbCu7t7/GB6NYYFaeK0LtYVdKHhDTrA+xhypYQBgkzOOgV74dBeFpAD6GKr44eE6tIuHMmPj+lTQHmORp2NS/C4Cz4ffM/quy6g+lGrDFIK+7EaQ9UD/iOyHns9YQWXTsQbvk/4Y7qetyO9p5h9fs7uOH7gOSzsZGfp3zkFgSaX1HUtHZKohuqTgmUAwE+5k/Pbg0wdhf+jy5U/d+g9/r6G/M6Txx8h9QcKmKeovGPZgtXdSe4NVgMEciQpQ3wnu86PoPn9U2+ex2j6/V9sfRD889QX5e+r9QcQzr78g07fJ22R8tIlcMCbu8wO9sfrMWJ/x8ekILN/D/MyFEViTATLqB8u8D4FUE1QgGAc/WKceyaqD/HiHWRiIr9lHKjwLBaJ4FowUWee/K+A73cLAPuL2wQbwUdbAtb2xRQvAuH9JRvVr8PIla5Pk9SWzU/Bv7VtGzIfpCt0x7ndg6cCep4nA/eqj/xkv/rhXuxcVRAMv/zLW1isy9qqvyEfb+Yq8bwTum6ushTuhn8aWd1wSDoU/PsZ+bAQd8AL3Xs1QjKo/djdjp/XsgP+sxFhSUGMXjDyef9TouOKfhMAvQQCqPwvZ3b/YyRMo6sYeWTlq3su7hnp6sMd5RWDwYNnBSoIA2cIJf14GrlOBsoX0543mfvffd7Pyhy2/3d3QPLaIv768A8YzBs92EA6Hlfm5HgkQg4kKF4TXj5SCz/5vGsWnCIhysEuBMpbezF3g0+nEmxPu1J2AKTFZTAkX4O50hoMlQS1sH+AEMffnnrOkFtOJ7eIUmM1dHyfmUyjvkZvfHrQGRYKJD+bUdOZ688WMIHBqupzZlGfjS9v2JiS5nCx9DxLB96kxhMinrQ/bRkd+9KyjT54m//riLHA4UsBrkX58Vhh1tBf40tmGDrpc+EF5IckJVmnU5uydZ746mJrGeqv4cJZaw+i2yVnK06VRl6U4uWRud2DQSKeCbAZI1wj9DdxFaP1po4r8tCb91WEv+Vdf9IY1rbHJkM9Odq9LmnyurJNiTbdJoZ72ZXZohLQ9Sq283Et8sq4wDC1q/IZtDXlo44gPyQ7sjjzh9ZbdHXt1Ii/MVD1t1vlt7Yj6LqirSanaSbvrOduUibXRzjn1rInX6eZ4OvV8EWqpESnTNCevkiWwKKFkm2Hws2pAMa7w9+YSIy1NAtUswOXp8bRK0qM83edu5HYacagcw6jdPisSaRmeuiyUKy/JgZrGuzKPFbPN1a074RfUitbKVu7kxIpMYqDOV087y0nQUBEPkoRxOX7gOuOcglLIV5zklqRUxnhm9PxV2cSzmyDOT+i0l9rF5gpOfHvU7NtJyDbdypFoBa3k7ak/raKjykrAmmCHeMP2CqEUlnqOWmrT2y1J0kW5EUB8mokrvnEns4BMAU9019OtdLakbGeiMI2Hit8noDSYfY8Z5Ylu7LkiNGUTaSzeUefYC/IZa523oj2ViXSZncPodmz1s4Decp3NT9KUT4KK77D92rGkGWsa2lpThNM0oDTq4BBkkvoUTsx2B77IvHZmgut+4NLd3GeWeycM9m6azNSEyhb2EEQ7R5tEWnKsN0xs2zO1kqfnNJ8PZLffpXIqcmWX9dGFnPFEKq3IrXDVmVQAa8z1JVm0NN+i4y26FPhrEBDXLa3euI1loBfSaShTWa7LgbpBqNpZEnlG54He7+PjesHdzrJmnmeyabZKWinAPLbKoqrSc1ZICX4lp9OtH1hZHgsxTmbCbB/z/aSKEgFjCBvnWWxh+d2ZCdZeZe4o9HY8+xqIMofpc3+v6WmrGquFGR5LzVUCtC62ZDhleYWxEqYbbHpPS2ubiptEnTEKNSELbXfAiMkyl52aHIwuFXN5yU3ykmtXusvTG4/ht9aZz51I33bKglkxl6MrVic6DeJNip6juUKepIBYOzdU5S1TxxNzv2331hYdthMsCBwf1+PLkp31FFuRkhVvzxidBFhJ4OkMaMXccub8Dt1e8wlNTOZVgt2odXXx4zxfzsiM6I8keSU8KaIa43Di6JDO7HB7Sjiih7XHrsrNjjVn4YrmwNYHub1Pl/0kx6fsQq6XxjGwwcqdM9Y1v2wkIHnVZrJ3E7HZVPrc6UKRaNBdbGY4KAfRu10XE4uMG325C4NMz7ZNhhaSyLknvuLCAVRHJgVTWubQ0tRCRw6Hcgkrec8HTrxa1OtLVJOevz6qO3EWTx1uc3FXGz9iwJY7RmK2HCRNVbYbOcLoFFWz3AC2IKXmNem2WSjarhnXRjWb0GadpleCOTZsuuNINTqvbTQ8tZWxsLryYtGrMLI5s6SVttNhAPapaciEwl8GnqR8jjDs5rTd7RtNUigVGMFkT4DKXazN/dpNS22ddUJ0afSyatZUOTk1MumRrJlje//a9ktxf1E5veq6I+tyRi7Fi9nNEOe8Sp6lsLOAsOeEIMgVhlDYcGlMDO6wFTQmJLqpf7B61xRDYd8FdRfFXoofLgSV6dN+l2rC6UwkIrpN0kU6COlB1mhOtePCCwLDX2z5RDD9o3XROne9W2mctJMnbKw7ya5NQ7ZeGRdFVKQjzwHeoE8VJzWkOplzM67Dw1w+0jTvSWU7rONqgspYN1/uw+tKOx57YXELNqtEXbJFfyb8YsqVeZR6nl9tJ/h1QyzIVgB63Kel6/m+0EjyzqjwPvVi12YD7TiHG19tgqFevOp5fHlpZsJKLA83jCyv2GVSk6YfRyQWT0kS3Us3YQhRo2GCTU2RxlwSYboE6qRIljtIRPIkyrfaJrQWFUfT891EPx7lzXoarE0rcW+k2k84beeUkZaFlX7LLWp9YIPBkLYGTTIXer+y6G3A7HmOOjERi8msjTNMY0plr2JnQsW7cuDWBVjVbJ4Tl3i3LEwQzz3cYC11f0pZzO3xcyhPhdatF1oTHKby+bpx4yPLEA0udQMtQmqbOcedcauUm77iLbJPB+nIsjwvRQqFo9r5VOoN6ri7Kl1w8bq+zUJpyiaitfZsP6bjo3NtsLgZtn2ubHSBs1fa1YB4vc/5TU5Hm+QQhme0GvoNN5fUaSYs6POWcmVaO/PS5YIZfXHQWHqyXmNDUu8sXDXFxRSbyoUVA1Gh5XbKG5A4VkqgKpp+406348B0FNmIxqn0BW7teqKxODJxs6Az+oCy+7zMxOJ45EqU3Ofa7ODOJe9QANQu63U6Xze8NRjYWhailo0BtvK3ADfPqZEUjKitbsHWXPcSUTlewatxdNK3hzjq3eXsvLDacJfZLWttS6sxr604oyB7UOtBL7nUoK/nK9WWM43WU+9CW4ddqhC3YkEM4TycHcSrLeSciOUTPaZ4LVofk4V8RgPFwE1A6lykLON6dT0YlRITeTHpbJzOjEOthmE1kbp+X61z02VWMioHzKKBqHhdHAbxEB+UqsjIPcO0wn4GMVQRWMboy4A93kBTlBTbyOcpZ0OO3gnXK5ahp6u/vGxrib/0OSDEDK2dQ6ALZkEuF5U2TA6Efp2Wzpn1gd6km9xrdPw0XU52tUxtSnF9XtUEOqOCFbvuVTuotuDgok2dwMDNGDJSdD7N3XDLtBBICdecKqRyPgj8ERbD3Nrq1UVW3UWIR4623hrlEdb1NG8Z3JuBVbIr1hsiQLe+N+RHqbzGrWknHS7gEP54WpwTJ3LaMkCi00xcWHqs7VrNb0VOW7iyKLpkmRbr5NzpyZS9pBrkUzk+LDZEPC/ZTNAIXZssl8eUWAF9z9gnzBXPoetV0TGzFvx1JUpnfj8JE/kcsUlXAG5lKTHDAHvGns8rTpPlIpFLI407Qjje4qTpL8Nlmco9x3p0fYkv7IZcz9SlarlerWXULlbbLgpnnnm+iLBxs7fHlLrxerlZyQ52KjN0iVNrSs/KFp+2cnhMD1s/1U+7QrO3be+1TLRPFvm6JhTnyCYNt1+0eLFT+tmlaryVd+y76EqsKc5qqEEdEt3vjTW5ImQrFds1TJgeMGLOJQK+Ypj5Bs+ObHEgvVC0XI2rcTpIuiaj566Y7MKzPZ0KoLBvZkRBdrnA+snOZJ6JE36JavMIXUq39cYi8a15WB6ODuCqMpbWa0imDsQ89rajT+ugrzSPozViQw474OldT6i6oCqpcVoCqTjcjtcaiPLckJSyX0i4WEO8plhJZ5TlYm93vLAP4xINPNoSLkqEl3vsWMSlJO4FG/Yc9sqSYEtHbKurmESCej6dQMEOC/zqHUTRyHdy6qqcJjnBuZNSweGSocEvvB8bBAVMfL8LFPfKXuWF3trn06xZq4ciDRXPVKJJhodHv2EPuu9PdYdi9VN6OJ68IPEl0dUPCWaeI1vy5ozs5LJnaMxpullo9SLXLG2zvxTEUYqmQ1oerNwPg43BihMD6DWvcUCZOzgXhengpmlfLBxNgLhKXzNVplGaW3DocTk5dl6lt6BXYtMK6J0mtzTIdp3V7BuGoaI4pxQwZLOG7nP8whQZwcP+xjQohvVIU5/TBkVfXJKi9K6QZ/NrHvCH46pyzSM15fQ1GpWZ456XqimspjNJ0OZ2pgr+hsToBu3r3bKsnO28OV4d4mjPtT2Ve0tutvfSZVthLkf4qAMux/BqpaDe41hvROtw6RFb9bLdnc9GuzrMljsm8LSaPQ+Sr5lAdxuFpjxuatQ3lcjS9dE48xZvmH20CjqswWjUuBiWsmTKpVSS82VnLhVa7UUr3daDu1l5gLyuctitG2Gfo+XuiJPhqpl49VLG1HWFl/Zwc73ZOSPSiRMz5lqf4BmYCa2VkthpTQpZJWBY015RupaTEaePGMYJ5FIDM2qZwS4wb9ohs7UUvTR8FglhG8fkZpOfOxnFSmNfXeeRjgY1XrLC3KaSU7juOj7O9Gu8xiPvAIwKUsFGX/nxbX/LvHRhmU7r1J1i0LNFJc53UUDN6X11PMtStsp3hO+Dk3e7KPxE0b1VOo3X/sQNrymP+luDXWBJM9fWMdZdFothsQKheKGw7hS4mO5UtUMWbupNY/vQmdYijBcovz95XY3zmw3jb605h6deZmW8ioNTjh2nxzLDKhNzFc0aivm1go0HX9YB2Ai4k+3PDYEeludoU8+uvr0+KSo/Yxz3ZM2u1zPIQtKeutlxc2UXTDG/7JSMIpfhcV+LA30w8fBcUyvUiWCrOF2JGt5ZGdwlqe2kbC0WXVhYuWklWQgi+lZNlq7uGjtlaK9HkcSanJlYt9kt6kV3BbdAdDq/HHY6s+tSFM9WZrur8dBl8OIkXgNGX+8qtKp7tLpcbhhxZuVzS1MGM2y26sZ3JHNLrJW1etYtIerUY3vbM1I1oW77Nuyu16uUqN7cL5VeaXzGpj3YjRNXJ6lcvUXbXrq56na5I4HHCTutM2+Adat06uYMOiRRuHXRC8Zc9ztbwPXKashsO6/6MFkGB7zoXarTSVXHeD278ovLtZtbydZBxajlL/7g77y+vPUnocECZcJdT3Hm+HtX310mE6xxnHiuz9t5cyK4sBR2em8yk0b18xtYqYpMMrIQSvvpLkgovYnUNQNbaT3D5zs9zJNiAdhm0OXcTsEkqZXbAibTBYgMrs7QWS4zN9RqrtTMp87KYokPbeYBDBCA2m3YvY66s4YiDjIVoYyhmPNLg2EDt5yC3PXmh422wsw5NzcPKNF72RxgjI+FzGXS+PONd+NdNBG4icQP7HXFwW41C8tq1tQD1u+UfMpNIwa2T+be9PWENPEcY40J29mHgDLNvuvI/SoSF41fnXAq4oh5ukj0a3U7ycQFOJvDqers0Ej36IERDssGpWn7Ilmazsk3yV26uLfa6Vtz2kS26Tnz5hyRjTd15hYhlOuzbU/8mYXq/XR1qXFfKAzzqOjz0rnuBIXeCCuOFLRQ1lmBG3YlmS+X52Sj57et4J1l5kKYzaxUha03l075AhDqYgc3NajTkssTyl7NXFyZOwei5goLiWpau2mymDPoStjf0GEuopd2RgZi5pusMg3TUOt3PV47sT8kdLnHE4OYTW7orA4hTrgtTRxWtXvjmqWlKqyuuiGzu034QcCjblHUN3ait4p/kgZyeXZSjxMzb7M/pEbbTEgOo7dmQ+bbXD7Q9Mvry3gU/TxQ/jtvi8cDvv9n54yPI8H310v3w2Rge1/ua335W1r9/PpSuRHU6XGiWidt8Dx8/C/nqZ//jfcSo4Dh8Rp2fBfWN+8H8I0djL9L9BJlXls31fCtzpP2fqj7Cp1Yj7/WUH97Hl6/3E1Li+b+7MOU8az2/nLgW5N/e7wufhl/72B8wwO86DFivAyep8yvLx5kmzRy62/zBfENVMVo7PNVB7Rx9jZ5g5783/Q8roCyJQAA -->
