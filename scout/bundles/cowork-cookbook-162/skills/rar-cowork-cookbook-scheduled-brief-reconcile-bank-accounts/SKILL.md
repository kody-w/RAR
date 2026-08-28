---
name: "rar-cowork-cookbook-scheduled-brief-reconcile-bank-accounts"
description: "Schedulable morning-brief email summarizing reconcile bank accounts for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_reconcile_bank_accounts", "rar_sha256": "f5fef67f7b740414caa7c47dd3f8ff0d464922e4e76d62fdfcdc8feeda3b100c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_reconcile_bank_accounts`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_reconcile_bank_accounts_agent.py` and in the RCI capsule.

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

Reconcile bank accounts Scheduled Email Brief — Schedulable morning-brief email summarizing reconcile bank accounts for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-reconcile-bank-accounts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_reconcile_bank_accounts_agent.py` and embedded as the fenced Python below (sha256 f5fef67f7b740414…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_reconcile_bank_accounts_agent.py` first:

```bash
python3 scheduled_brief_reconcile_bank_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_reconcile_bank_accounts_agent.py   # or on stdin
python3 scheduled_brief_reconcile_bank_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile bank accounts Scheduled Email Brief — Schedulable morning-brief email summarizing reconcile bank accounts for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-reconcile-bank-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_reconcile_bank_accounts',
    "version": '2.0.0',
    "display_name": 'Reconcile bank accounts Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing reconcile bank accounts for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-reconcile-bank-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-reconcile-bank-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '69aaaf1ea9272d26',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/reconcile-bank-accounts'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-reconcile-bank-accounts', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefReconcileBankAccounts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReconcileBankAccounts'
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
    print(ScheduledBriefReconcileBankAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjxrbnV+HV+6PbT93FLqG+4YhBIKENEAgBktvRZkkWsYodPP7uk0iqavv6+r3riYkYdVeUgJNnP79zMqlfX6y6CrLi5cvLEVgpIlhxHAagQKzURbiszYoI/soiG/4gTpZWRWjXVVaUL59eXFA6RZhXYZaOy50AuHVs2TFAkqxIw9T/bBch8BCQWGGMlHWSWEU4wPtIASArJ4SUtpVGiOU4WZ1WJeJlBVIFAD4v8ywtw5FX1qag+AcChYV+ClykypCiThEX8uwRSN8CEMX9K9QHdFaSx6B8+fLTz59eQvj95cuvL05sleV3/YC7GJVS3zRYQAXYp3zII7ZSHxLnPXRKCq9zUEClEnjLhZY8rz6WIPY+If/1X1FrFX75w5evKfL8fH0Z/6lQwdGOKrPKCursWLllh3FY9a8IG7dWX0ITq7pIS8RCSujT1H99rPzOKcuRH8dnHx9CXn1Qffz6kkEVrNHjX19+GK3/+gKdAb+/jlzyjz+8xlkLio8/fOdT1vYVONXIDGr9+u15/WQLCb+Tht5d6o+Q6yO2Nvj68jvjxs9D79FOuPLl9ZqF6ccH47zIGpBaqQM+/vBXbGEMnCgOy+rf4vvTg3EALBfa9FT8h093J/+MTJ4GvfP8a7E5DOvfsQSSv4n7hDwd9Ve87/7/J9ZxmILy3eP/kt2/WjD5EfnpL2377xZ8QryvLzyIwwZmByyaL8iv346HJffTB/f7zQ8//wZZ/49sjlldOHcO3xIrDT1QVt++/fShvN/+8PNPH+oc5hqwkm91Ef8rnv/Kr3c5f/Dgk+rjH9dC+ac0SmHNI++Zjvya5f9R/PaK6FYcut/vl1+Q39fL+JkgoxFvQh8u+F3NlFDX3/nxh5ffIEyk0JrauT+GVf6f/4mIoVNkZeZVyBHCQjWiTRUmYFReC8ISgf8fGAX9+oCoBx3M/zHCo8aZh/zyv5w7en52nuiJlm8A9O0Oi9/eQfDbCILf3kDwl1dEg+yzIvTD1IoRlT0cvqaWD9JqFJ1DbARFA0HF7ivwGcLR5/ELEqbIL/+mhG93Zq95/8sd5cMHVqncZsSpEq5/HW01ApA+LXNgYwAdcGooJ84cqJQHmZafRpzO4gbi3OiXMgrjGHFDKBU2iP7OG/ruy8jsl19+sa0y+Jo+gJVEHp2jRCHBuzrI58/QOi8O/aD6mgInyJAPv/72AfnfyH+36s58lHGAOP+MDNRwe5QlBFZanYCxs4xhhjByj8yvvz19DNnA3oLAOIZeCB6LYaZGwH1z+HHNfiboKWID6Gjo5CTPimrsYGH1imw85F1fKHR8NOJ5kJUVbFc5SF2QOj3kakFz3j2ZZhVSwnQsvf4TUpfgLvUXu7DuKiaw5K3qF0TkDrB7ZPFbuxuJ4OIsDaH739PhcR8yKT6UyOKNxSsijbmJ5FZh5UFhPWV41iMusGu8LYfMLSQF7dd07JZgdNW9UB7ugUTQM84zpJ/HmMMRAHbx1C3fZN9prLHHafdeV3xNy2cRWAW4N3qoSo/4deiOreEfz5Qqg6yO3bv/wKPnP6PgPqNyz0H1L+aE916OLO+zxb2lI19rAsMp5P/zIDLqzQqCuhRYbckjS0lTzw9/juPT6PfHxAWHgacYWDvfB4Q3eHlD2a9pHMLkKPp/PCjvUXjSPJCrLqAyKqve+cMUgP4c+d4zdMy4ohhz2/qavsH5Jxj0O3bBIMFyjh62vAkcn75pGsCaHa+/t/a7xwp3LG6YhUhe2zHMEA8A17acCGpVjFX2jARMVzBWXBuETvAHqxDIHWYF5I9AJULocejdu+ukDJoJI+MVWfKdPBwHJqiFWztQWzifglfEgIUyRqCE1QmnnpEGeuHDnRWSAOhjqOK7h8vAyh/KjCPtU0FrjEWWwPz9fQSeD7+n9l2XUX3I1XKtCvqyHRHXBd0jsu96PmMFlU3GYrwv+mO4n7Yiv+87//ia3nV8B3lY44/8/e4cBNZWUt5BdYSoEsJMAt7z9NGdXx8N9tHB33X58qc5/uPfG/XvLfP0x8h9QYKqyssvKPpoc29d7hUCBApzJMxB+b3jPerv83u1fR6r7fNbtf2B/cNbX5C/p+IfWDxz+wuCv2Kv2PhoHzpgTN7nB3qE+7w4f6bGpyPKfA/1Mx9GlIVVbffvLeeNBPYdvwD+SPxoQeXYuVrYLO+YC4PxNX1Ph2exQEhP/bFfltnvivjee2FwH7F7bw3wUVpB2e44t/lg3NjEo/olePmS1nH86SW1EvBvb2jGJgDTFrpk3AzBEoLDUBWC+9X7YDRe/HE3dy8uiApu9mWssU/IOMR+Qt7n0U/I2w7hvvNKa7hF+mmchUeRkBT+eqd93yra4AVuzKo+H9V/bHvGEew5Gv9ZibG0oMYOGBt79l6ro8Q/MYFffB8Uf2Yi379Y8RMwysoa23RYvZX5W5J+QmAAYfnBioJAWcMFfxYD5RTgVsN+6I7mfvffd7Oyhy2/3d1QPfaOv768AcczBs85EZLDCv1cjh0RhckKBcLrR1rBZ/+3E+STDUQ8OLpAPh7tAW8682b2jMIonHIsa+ZQM9clPcbzMJeaUnOCABSYTd0p4bme4zrMCOkWaeMY5kB+jxz9Nnb/cFSNsCyHcWY45c5n1tQBJGaTDsAJ3J2RAKPnkDMDGbrfl0YQLp/2Puwbnfk+zI5+eZr964s9pSDlmio37OPDoXPdQqmZLQX7CYmhCwwlA9K1jW0RFzx5qgNiShB4z+YhcSQX+sq6hSdVasr+trkdq4QKW3O6XJPcoYznYq/EhmkRR2WyVihJogJzS5mLiXcQJfoY7rblXL+UubjCblFZtEexrERjuBiN6BO7hNnH52ZfuMcVWHVFpe5QtOn2wnaZ40knmSDvD6c5rR9WIkFMybI6o5SdZGS/nV+MQrUXmmAb+u6GJUZ9pHVU56O+zvHQxOzN5Eas+Dia+Vpi9hWugyHsgcb0l0MaY6hs4vRkG05R75AyBB4yAReU+C7sl/a2km62MTh0k93IzYXTNdNlB3Rpz6pchxOBQUbYDo4GHcnPyeXKSG85seCSQa/4EwHSYZ4y+pZXOqtIcJ+xjxzVlUIVbeVqf9B3hHFO8nVYWbdK2ik3zbTjIZDxTJJDOjIvfIMDHFj4zjCsXaGbqZLb9EJE7UriLgaX6Pmwm/nRVIn24voYHziTq7rGXV8uNcOw+b5YO5FxWvI8VrA37WDFrZf6V1yvqgaP0r1qEPy8ESchfbKNXac5NnHh3eIU6GeLzvmMQi+nVXgjeNuTNhc8oSNaU7q5ahTbMp1cwtKWbGV6tVr9uvHSWpe5anOmEqcStBsdzLWtadNtKqME40zZiL1VmF3FZDEwgX6tyBYMBHVW8YioezGtUUdcWwamYLeKtsSrRux2k5LYhtU02x+TwpZXuzbp2GZCcEm/XADhSubBsDJ2zWQfBZddDDabSpKH9bJ0tV4WcC0RDCKnObpACc8+KcnUymfyvtzL8irRGfNCXGZBdlVie5tKyfHaz1Q6xt2hhwr0uzpwBZAFpo8uzs7RW7RNdyApM20PGxzNtJXgTK6TtitNhrG9oSE2iixtZsQGsNuyadR9pkm3CsfdcBA5Q52SRoVfFfqsoZdayoKUF0TNibZRT2281TYS8KSOL+RCpiQnB7Ki0eSekm+9tCFagctse4sX4arhY1VQ7HwTbU61pvLtUerEqbo8JqSTZxtra+mV4eBayoeWfBF6NNaTFTa5xQP8UDnqbtsrvZVzJqK3YjQZo2QGRXTz1xcRbQ8SIHa1UnNezaz6BankylC6qI+2g6ocS9O/DQpo9cCQ0E3lmDcdl1mFqlqCM40Vh7nONdOw2RFvBalY9otz0KC5oNH1jTpPrnbHX/E22p6Jxa3PNWZQ3WVwzExONNrJvAh2V28zRxd77Tb0OjNBw0B1Nd0F1akfVhMbRGAtTIdcP0y6+KwyR0vUhZYHeF9XzHUBbt3c5l0xuaWdpOIdcb21p2jByidzwKYredcX0snICVrfpAzOT/bFrNktz03j6fHWybDSsuk1CBfu9FYYtFjPl/VaZLa8xjvpNTCwgJsnuN7axeEGupZs5Yi4mEsWJ2U6zm9U7Ti8uZ5eivO209JNrpIcOIeZU5GH9fxSEYVxnaV0aFnB9Hjd5pk3KPlUZOvrZtifa0veuAyfOyu5h0m/dbFZTnZSfxVTejZF3eX8Js94jo9Rf3EEq+3CEAg3V7a7dRcflIQFk1Bfu2fr2l/WmriAMHU7y/luMe+Ik7LrHJNqBJLNq9ZNnIRug+m8UePhoOTxmq0ZUtJWRbk6+0zU9+xWEa63vbePt9hiR7FKqV7P8pJcbLiIXFptsCFosy+KduYE+/NCD8TtJLfOU2Vlagd9iERgAZRtg22bG8RlxRRCfDgExYEPXJnnpfMR23mNzJaksS4Hed9cGECfje2VuJY0PWc8LWTK0oxbmt4lIj4UxczTt1s1PHiJtC35XnHCIzadr5LzGp37vmGQLOPVSquvehF4Ry4257TJ0OLaW9fK4dBYCypwV2tv6PurIwXtUeFSK4o3ZyJlGm5XbveNXuQFR1ikqXbcbrpS5UhiLy67m95W845mDnuUxLxhoQ7qlRjsiNyosrhY2JvjCdfaCXtgHX9oE2UNfA0NAS6e/NMtcGSqtqTErCOznSYn/UTLflXvWqFj2kFE5a4CdoAFitZFlGKJPLYMiQi9zWM95bdzC27pK3ovBdlZXq3j9LRhW448XHY4dnJ3oW0pl0MCiNORup3bcJOn9IlmGQIVpaoyqJ1Vmzt8vSpI3MFPYuYmR0ZccVa+uQZ73eGSqz8fqqtUX+qlvNxGOLpf0/su2B69PY4Z4dlQ3PWR8bIeBPVuw59EaslIU7Ew1nW9EvxI4Dab/FAB3Abni1+xHQprTwfMRjZsNsVZAevOwmLqlJxKlEYRcuF2Xii5yk2M3e58O+ebnt+Y2UGF+AVbTwLCaEdcbLtjcpZbXI0b5uvU9Fwng31SL9SaSTfrE3sBkBKNPNmlG225so+CWktX9jjZh9pwpGeYqm0t4bBYCwVm6wp/8Icl6e2z/cRdzGWlFobrjlTTfX8xh0GVJKsSWtZwi4heUdeajJhoqQSAiau1fkLPi526mh6pZbGu5KtDZv3JYHrY+cPEWrFqg9LyaUM0066Yc0rZa0lozviM5bK1hmFH0yja+UIuwuDkBLsNOm35ebWd7z0i2Gm8xE7rBG0ZoV5ehxtgZtuO1Q9narFz1incC0+nJ8E9EvhFV2xsAkBoe/QUna8c4crltNHXG3m+KUB3kyjpWsQG4N3r1T2DJNV72Igs9EBs6i02TYnqSmYxIwyYvTQ2gu7NU2fv5+xlF/Hn2y5N51V5o41je8DUWgw7Xjy3aX+um30/ydZ0sRMKX2O4AmMux1o7tI61okIIPpIa65i5xQpZmrl1z8WLSthXGVtzsrpbuRor9TO9FhcTPgy5FoZdQGPLnzaqBmHghFXqxqK3k6xdFVV3WvBpsprakuGwtJPAulLTPPbNPBKaSS5R/hbH69O8OshhTfqHns4axRyuLJPqRyYuLo0vsiQeqUchcTLjvOc5nMHP0WWnrbr8XLvRRmfrWxreMs7S+Mg15B50W09WMVa/7vqN30tSqwbBhDc3k4w5yMRFm6S7TX9eMDO5KNubbuIWfVmSl3OZLvUon86JskaPyTFn89O2aK9Gs1fJSV9sB5sVBsc+8JpxvJkrQancfhole3vOAl0yFUaNyzS93NAlJzPRwOiaV+9kfHWZyGVErT13KUhDBMI9gfU+cfL8zVJwyOta5zuVl+Ld0YmJSrysi3QvL+RWuU12O7IIpfWUMVrXErVIWLuo7LUuf1BIAV/vj417yRd6QTTuabXxbfxkUrzsu/iZLaPlxbJh6NrETM7FkBOyvltQ0wxrQ/UyS3Q5N2R85u/dXdwVQnZ1dBqo7C0HMeySmC8lskweODw+0gGziC7L4eiT1n5vD13nHa0m5rjzfJJe6OPFS6LQDI7LwtP4xXDGhX7F9qdDvKvBqlHcbKnt06DvfKa7HvrsNEkHZlG28txckJETpV4wz3P1dN5cKCBI+21+bmRunxjToCC9G2/mIOzbkJuVywGVrzvANQJbD3lazlQXwOZdtT12Q6OryNkkr6qhe7BIOe79xW7Gs47I+60OtICtu4uoTwcuUIaLfOBiodrnAynu26Wc+6XFsnPWm8JRg9oN2cz0jHahcdFuF/OCV0Q+pcR4uAWBp8tLmrqGeJ5RYq60NaUm+mXloDVeBo0/u80yCvi9BQB9obDKPZtDeN2xt9Dk4NZQNxXcdLnY5dprO862bq4yDZZx7eGI7rG1eXS0ijYKAiVuaUJdQRMNqLVWaTdvuxrV0Zrv0fWuUWu4r9wviLUPd58qd65uc4Ga16mY5eaRstz0hMl0u8h7qRGgf525CAFKxQ2XNFbsUsypUCa5Fu5G3aXnrZrFRByWJ87x8VCfefb8zM9PHubIwnYxm/BzhWbo3uHCvOjYdZTSTaeFPQYwVUCbosr7Buez/ZXGaGOd2gviuJ8eAdwTTbN6frX5ua2Fhndr0FkvkjTbKLeyOszMA6MdNnthjg8k5JILK+K05k5TbO7fqACz8+1hO2COu6xvPZWdY4dgDA9brSLsHA4NfVkdJyyb0xhFaUKSYny0g607jOgrk7i4U9xIbYc6fWkswlaY2joxxZw0o1Q6tC+aSOkLcn9DaYVPhXO8F68Xtr9Nrs1O9MlhK3nX02IG1HIKB2MPM6+eriqGeN40dremGrkjblsO1deJnWurkz89TZRIQodDXrOwMqU4q7vaCq0zA0KHXge0dUVN83JrJpU3b7tznKqod97uWUm9sBPgBbV7TciU9lFRlUJ8Njtdu3BrtHs7HOSOmdkEc+CPt6RzHUrWpUXpdiLcxVKkTS+larmSWdNuTqGRZYfOqvStqEhaqcpZAyyzVHsmt2OTcuSlv5MHYUVPrmdDYo5ls2rnTAdbQ7buBi6XPc5vZ62BhV7NsxMxQgVbNMC26oZoOYTiyur0ueYMfEgWmGk2DZmJa0ftZzyurE8lsXTnvuuQkYKpq6Dyd/ZC0GcWtV9tOsKg8EWAnp3tyirsZGtSE4sJMZbWJW+QSdsg2PlkvoyqLiKj2YUST84gX2lzc44lrEhYUdAFZ1OQGKDcibhnUd61t01E13PXFQPnuF7KZjRP6oW3EPjSFY5lqRy81IVK36ZhiNLzQzWP9/ztMPcc4cRR1l5r8mRyqVuLO5AxoCUMR/OZ26hnK2gVzGjnQtGc+GaRTZZA4fwpH8+78wrYjZOqvqocyjMKExa4y62s9XBoOYbrPM139hAxCXmekRwLllIx3/Wtgwr8Bb06/KoiesqoY3kOVi5Kh6sFWk/A+liCs9pYRaAPKoPZJoqryUSfLgU3qkkPHSadi3cHoBqXOdpgJkpvzzS1l5mi3pAmFjhEsOxVl1LykD0zkm7jFaFNpl21ziaZImq3KX2b0bsmnCxN5pz4Fnc8rW/TyWa97tqTulYLyrOvxNJMgbms3Llld+ZmNlwAh8vKagknf5pd8nxNUuziJqbBfhnYUTJcBx/b0GJgZnYvGFnFHMocYCAwqVI/HrhlcHXdqXk49W7ri3KqMjouAYGkF3gKp6hVEXBgnyorugkSdWUCOHsl0lGcOriSCF5wJhQqORzh3G4N8XSV1hQfFtP9YZIW4hqt1/GWWcTAcpZznLh1amib+1yOKaetZoPthx165kqUMhTxWuv6EVyPqtVTomt4VsDdPKbiaBQf6i4IhoJ1ADtTNGpqNDbhd0tNuyj+QiYJkjtMQ2WS9Ud70Cab8rydzHuDFOEGT6ultImwusKYAHXjg7YvjxHLsj/++PLpZTyafh4w/93XyeNh3/+zM8fH8eDba6f74TKw3C93WV/+tmY/f3opnBDq9ThlLePafx5G/tMZ6+d/853FyKR/vK8d35V11dvhfGX54x8gvYSpW5dV0X8rs7i+H/Z+erHrcvw7iPLb81D75W5iko8n5P9k0niGe3958K3Kvj3eLb+Mf6wwvgUCbmhV4HnpP0+gP724PYxb6JTfyCn9DRT5aPTzVch4Yju+C3n57f8AYjhQ5PAlAAA= -->
