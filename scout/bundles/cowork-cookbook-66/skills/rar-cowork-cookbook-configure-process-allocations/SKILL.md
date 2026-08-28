---
name: "rar-cowork-cookbook-configure-process-allocations"
description: "Applies a bulk configuration change to process allocations from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_allocations", "rar_sha256": "6bc6cf834f9590f021736e472f5b89db08f019f21251b64e450432515922246d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_process_allocations`. The original RAPP
agent is preserved byte-for-byte in `configure_process_allocations_agent.py` and in the RCI capsule.

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

Process allocations Configuration Bulk Setup — Applies a bulk configuration change to process allocations from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-allocations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_process_allocations_agent.py` and embedded as the fenced Python below (sha256 6bc6cf834f9590f0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_process_allocations_agent.py` first:

```bash
python3 configure_process_allocations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_process_allocations_agent.py   # or on stdin
python3 configure_process_allocations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process allocations Configuration Bulk Setup — Applies a bulk configuration change to process allocations from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-allocations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_process_allocations',
    "version": '2.0.1',
    "display_name": 'Process allocations Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to process allocations from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-process-allocations',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-process-allocations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd3389183098435b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/process-allocations'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-process-allocations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureProcessAllocations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureProcessAllocations'
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
    print(ConfigureProcessAllocations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjSJbtX2FiPmTVkBkgdrKtzR4CtCGExKKFyrIs9n0HIahX//05kiIyc6q6p9tszJ4yw0KA+/W7nnPdid9frK4Ni/rl84vmWTm0tNI0Cr0asnIX4ou+qBPwq0hs8AM5Rd7Wkd21Rd28fHxxvcapo7KNihxM58oyjbwGsiC7S+9j/Sjoamt6DDmhlQce1BZQWReO14BhaVo494cN5NdFBhaEorzsWki8OV4K+VHqfYT6qA2hq5VG7kPOpFVdpKltOQnUdGVZ1O0rUMW7WVmZes3L519+/fgSge8vn39/cVKrAbde+Kcu3v6xOPdtbTA3BaqBQeUA/JCD69Kr/aLOwC3X86Hn1U+Nl/ofof/6r6S36qD5+fOXHHp+vrxM/9Quh9pwMtFqWs+FHKu07CiN2uEV4tLeGhqo9tquzicPNcCNefD6mPlNUlFCf5+e/fRY5DXw2p++vBRAhbuyX15+hooarFd30/fXSUr508+vadF79U8/f5PTdHbsOe0kDGj9+vV5/RQLBn4bGvn3Vf8OpD7CaXtfXr4zbvo89J7sBDNfXuMiyn96CAbBvHq5lTveTz//I7FO6DlJGjXtvyT3l4fg0LNcYNNT8Z8/3p38KwQ/DXqX+Y+XLUFY/x1LwPC35T5CT0f9I9l3//830WmUg+R/8/hfivurCfDfoV/+oW3/bMJHyP/yInhpdAXZYafeZ+j3r9pe5H/54H67+eHXP4Do/1GMVnS1c5fwNbPyyPea9uvXXz4099sffv3lQ1eCXPOs7GtXp38l86/8el/nBw8+R/3041ywvpEnedHn0HumQ78X5X/Uf7xCx6n0v91vPkPf18v0gaHJiLdFHy74rmYaoOt3fvz55Q8ADzmwpnMe9f/55T//E5Ijpy6awm8hzSkABIEAt1HmTcrrYdRA4P9U27UH/NpEwLHPcSD/pwhPGhc+9Nv/ce6A+cl5AibyBoLe1yfsff0O9n57hXQgtKijIMqtFFK5/f5LbgVe3k4LlrXXePUVQIk9tN4nAEKfpi8AJKHf/qncr3cRr+Xw2x0uowcuqfx6wqSmS73Xya5T6OVPKxwAvd7NczogfZLyAN/mI7C3KdIrwLTJB00SpSnkRjUwuKiHBxR3+edJ2G+//WZbTfglf4AoDj2IoUHAgHd1oE+fgE1+GgVh+yX3nLCAPvz+xwfo/0L/bNZd+LTGHmD5MwpAw42m7CBQVV0GhoEAgZACyLhH4fc/np4FYnLAZCBmkT8x0zQZZGXiuW9u1lbcJ4ykINsD7gWuzSY+AcgMRe0rtPahd33BotOjCbvDomkh1yu93PVyZwBSLWDOuyfzooUaEIjGHz5CXePdV/3Nrq27ihkob6v9DZL5PWCKIp0YsX4yB5hc5BFw/3sSPO4DIfWHBpq/iXiFdlMeQqVVW2VYW881fOsRF8AQb9OBcAvKvf5LPjGiN7nqniIP94BBwDPOM6SfppgD1s4AArjN29r3MdbEZ/qd1+ovefNMeKueQuEAAgCLBh1gaEADf3umVBMWXere/Qc0nSQ9o+A+o3LPwf1f9AL8D33DfGolNIAbJfSlw9AZAf3/azMmjbnlUhWXnC4KkLjT1cvDk1NfNHn80UoByodAOj2q5lsb8AYib1j6JU8jkBb18LfHyLv/n2Me+ATq2wWooN7lg+ADT05y77k55Vpd3x3xJX8D7Y/AK3eEAiYAs0GiT654W3B6+qZpCKp1uv5G4PdY1u5kOsg/qOzsFOSG73nu3QltWE/19QwCSFRvqrU+jJzwB6sgIB3kA5APASUiUDEA2O+u2xXATFBa9yi8D4+mtgho4XYO0BY0nt4rdAIlMqVJA+oS9DbTGOCFD3dRUOYBHwMV3z3chFb5UGbqVZ8KWlMsigxk7vcReD78ltR3XSb1gVQLxB74sp8Q1vVuj8i+6/mMFVA2m8rwPunHcD9thb5nl799ye86voM6qO50IubvnAOBqsqae8pN4NQAgMm8ZwKBTLhz8OuDRh88/a7L5z816D/9ez38nRiNHyP3GQrbtmw+I8iDzN647BVAAwJyJCq95huvfXrW2afv6uwHoQ8ffYb+PcV+EPHM6M/Q7BV9RadH28jxppR9foAf+E/zyydievolV71vAX5mwYSq6QCI9J1i3oYAnglqL5gGPyinmZiqB+R4x1gQgi/5exI8S+SBMoAfm+K70r1zLQjpI2LvVAAe5S1Y2516ssCbNivppH7jvXzOuzT9+JJbmfc/blImsAdJClwxbWyA10GD00be/eq92ZkuftyU3UsJYIBbfJ4q6iM0NaYfofce8yP01vXfd1F5B7Y9v0z97bQkGAp+vY993/HZ3gvYZLVDOan92MpMbdWz3f2zElMhveHxREnPypxW/JMQ8CUIvPrPQpT7Fyt9wkPTWhMdR+1bUTdAT7ebwBwEDhQbqB8Aix2Y8OdlwDq1V3WA99zJ3G/++2ZW8bDlj7sb2sd+8PeXN5h4xuDZ+4HhoB4/NRPzISBJwYLg+pFO4Nm/1xU+JwNUA40JmE3ZDuX4DE74LMmiPorNaJzyCBrzSZthXRtlfHTG+tgMI2c2RXgEiRI4+E6yGIYRlAvkPTLy68Tt0aSQh/oezs4wx8UpjCQJdkZjFutaBG1ZLsowNEr7LgD+b1MTAIlPKx9WTS58b1AnbzyN/f0F6ABGrohmzT0+PMIeLYogbFW1YZryCvtMEvO838wXdmAvLnLPzJdByKWYcSyaTV3R9cbVt11NWZUXnR1UDJC5iKwTmJzpM9XD80O+sWoj4hu9q+JyRncOXd5mC9QLTfO4SWtzTtrptmz5rFEEf6FVSB3VsLSFa0arb4c6ohc0jcCbhpbk1pHmqMrzcD4JjiPa0MYiHvjd7GjaJr9I1mfTw8Wb1RrkSUqd0VB3bNnetmfZ9exy4Nd66uSjKpnnvjVTSyvwJYEr1ytNwc75bA7M9RoezvqMgRFMzM4ZYTTe3CAuWoM7poF1uDikOm/bh2Ol3dIi31FhxigZfNW6pN7QWnzWtFONawqSuGHRZnMhtyvKKFPCv1rOYLRuta43Vuzo+q1fH2/H+mJrx/BIlNRgH4btqdpuxX1isf1y6m6r/TFs4F07v1JCeHQrdH2qVOmoJdgxcYN4L8H6WXKj8qgvmbrZSUutQeS1oZXRsdvlhbuV87gXUivx0LkaH4Qr4iwWgmn0ezKqz2ffbswkvUgs5s74mMCrdD0y/myppKtjs1AiJ98J3iDAGZdt6suma2bL+rTt1NLzxePCl7NIZzNqhlYVOzulSS1xyF5mGNE5zAaxsk7FrS2uTmxIGAICzQYrgSdDr2JPvr1bDrponZjOqeerNWzu6iTf2nuUSftExrBUVBbHduu3Z7DTq6XRzCpCQvq9lNXpelEf8lsQw1jM94cFP1advjjzPqFvBsY479P6LC3DPXUhcHG9rPED3x51bCHoSHeC69ANiCNbL/wNPfS65mTUMVMId0Uttqan7nwrLCKrrbaVQO5qklp4QofBocazAy2GtLxqevcCG6CFq/sRWYvKWLk+Igjsct3FJFWM1sgzmxy/qtu1vqtmKOUNDKZut6xdahZbOA1+burdOI/spayh+axgbXStqsymFnVMOpwL7aCc3LXNB5eO7xTxdtyGzuqUHU7EjkPttS3JhJ2tx7g5gixqorUm2XY3N1BjI6bauJVseQwZXb1JzNmpul650s4SO1sn6TSq874RfaeRD1Qe9NSmF/0DUfg7Bh1tufToTlrBuyzDS2vJnIM9i8yYyA7jYZt4zHWD6zsAM+dF51zDPp67hx4ZKGxTISV+XYjxZm+tu5YfDZH3CmuPsVu1ZC8WK59pXbnJsdQvhS4zt1FsHC07dB0cb11H8Z0ZJq+Piu2PfU0iYhXVq4HhDFfST2VbqactOm5dBZlt1sMJHtBLK6r1rqP6zS47UEe4Op9SWxoki9x0mFldj2I4Uw9VjPr7wsG3nKdJrZ7PDHW5qj14Y55uZUZU7mEHb+T1IDg6zRn6ojsu7NiusSR0Q/IGkETharG1+OWB7UpndjGudhkqoqqXCyPc5ufO0ix8jOeb/NglR6uC96sDQcsKGw96O1+yJYHUUjWzVJtB2jg/pwvaOevwau6Lt17Ax2xoKHLA8nCPdL1vXQ86Rt88b2Z3mlWudJom+xg2mjWi0Z0hj/XI6nqWXpRuhka6v4Zb8UAhqKy2ibQ1eilMW1y5LdFUjZPVqOy3PjdfkTc/omBYXAViQEezpd5sXQb29DTe7nTjQtGmMdsnXX9mhHW86ZXlXK+KNuj2vsSlu+DkDOg1P4SkkIRXYXe7ps2J9O1Th6lqIB85MbWMUrOF/eZoNYV7UKur4y1GrgoNZ1dEA3lyjQuHN81mIEg6nUVzbYP1t4jSZkKc1n5N5ug50zJMVZqGQrzzBmZ8fREazFjaotV0tBdrterspaPkjFggr9V4kEKSwWHMYU6R13UmG7OtyHlJDABbSfMVTlOMvMhznGaYzT5pYK4gjoJhpgkMO9VNG7j6cGGMaydkEpnaqpOq9exC1Wc5aZ1juGnQFCBM7AhL4lREeS8dL5hrKfG80El4H0RGbEVCuevYKlHQs5YftxqrZW6EpZNT4yq4wBGKudnFbK4dAD+yvLk7h9mLc0zd0YZcwpQWmicvC4j9zZK1GUMRonpLkPMqYvbaoWu7I74VXe5UCC6rdQHarnQBDZOeE0OLalKHGtEswXBRYsi4zZbdcinKPm9cJdZNwL5slZAefuEZ0wptM442WEjEQacDoEAuFZIRgSDmJ1M8mvG6ClUbdebiqrCXM43wpE5SWlOxXXgeLE7KVVUO6/4iVS684YfuejQGH89VLHJ3Mc3EnlQvFwhrndyZO5BmCVoZmBZ7jlAxvW0ce6sd5ntiUd9SoHZGXdZiy2bIQqoBF5n2ZctgGz0pRRvn+dA29tZgdcutjNCeIdvboxY3kjRY69ASaQ7jjo6+PWzxCGxf07Ol2QeOCa2Uu2okKgg127uWtcsE52LzpFfKkY1qGhpbq90VRCKXqEOaL7xCVrlwNydnyCXT4mqZ2Rs+QvVuCVKwjZIFgttWtbbXpdlxi7RkZcemj+3u1OBrHs5AN6f1GrwFjaZxCbqOH1eVQOmVuErWumdk2mYLx+pSR03poK4oR8Ot5XEMTzYuEbIFSPdorU+XJHZFFxPUTTuXa+PgWCiPKwJ1k1JkfuC4IKHtIF+ZNHVg28wVFXYOwA9eRCcq8dwe7yxFc2+3NNHNCCQOutpa7FkyFo16PSaFB/aA/mUYeYcIMH290eZ4KYj7lTY4F4q55YhK0Zi2KkjWz049fjWzcXHa743bEfVY3uFHPWfmIneTfHct7g7kgduuBeuyXvFXmzwPu13grWO5jKvFZUTtW4Q5Z+CUZXwyFu0uSWZLs+g3kXeQ4j0dOmsNi4XK3IozM+MJHzvMh9WRYSmqWBn1cahy67IaC+fCEfyVW0WBTNedOrtVRHK2eWovlPpG7y1qDV8u6/p6OyrxFSMrXc6c9eWCbS5rNaMKfbMokUr11prJ2jtFDs7hCQkE00HP4Za+RYC7bx4vtxd8b5TmSJH6aS4pznFzaNCFiJ13nYyOxElQgrMm8lx4PGlHAxBXX65OYxE2/TkqLZu8LXT32pSGGqVwbJjRoVnsTqY511POLizRG3hydzke0XFjXc+hM7Bqpm/rntoRAsoYtFgdXTl3zsuOJ1nGdEVrV/hWt99Hu9hUr9V2o2UkCwyYMfVOWl3yFabbaG2ETXxBet0QK+x6cVkGsBUt1xsFkURri+ZFuB0OTn5IMZ0Y5tx+x4xSWBWzakgUZamdMTFOb9WVGxixkM0IFc7auq+a44nsshWrVSzCrlYmtrdp1vTn0mGQDbRLdyGogkQUjKq12A0Tu9aFAlfz7a1fJqKCS+m8Z7eeuaBcrrypixujaTFosizmsgzi8dLH17zRN/1xTpBatjN1dONHcmL3ceQm/YJTskKuTLM+YWORn2QX9wG2pBKXrAhpjI3Bm4mBH6AzeZ56fKKi3PLi8AsLFoeCajktWRy315BXOY+4pabM6Xrazz1KIE/z2coJFZrHx1OYBIdZX4M2ye5MT17pxd4MqpVdLWx+ox4GNcxnhMnmKsfF+rgbGsvQCmuxrS+GeEmMAAP8Zl4lWCXFNK1TXS35A7bk1EbYBEWTc4otMcRplLekoCQE2xsWetVWiXWulqsqn1sc187Lip3PD2fTpVWYk4JzGl0Oo1/T46Bp4vEydlpnzPuAECz4djNkqSzP6XLupucRu/SlszWoahAazXXNA57KRRWFhXYlNgrGxse4xMhE5kNEJml7pYH9y2nrbBk99vDAjmfkOT8huJU7I5NdS/1qnee0QiNpfHNy9qboA7mjRXulDK3gsLdjelir2wa3sPxcnWNtvlN6y9pviANxWQJaQqS4bJPr/sIiY3v09Juekn3YDM0gXHNVONx8xC4FVNWdMiv7E4PTpJtkbHUFcctXoMlYIdxY4xuEnGvHnlGk7az29XBAXVRdXdz5mbGF68IWDtgeMAc5EwCVwkxe2jKyuHpIq8DXUlKEAccRenFm5u1KclplVefw5rqleGF22FvXupyPmEoHBhqwQUkKGa5qqo4VWbfxxNtuhQ/6zUQOe0pXOWkx3oi4D9uFst+LZlvCHMln5o4oFRPT90ynojTYpcCmsuVA2zq45pE4uquAcOnsVMUmZwlenfDkiGfK3tEuOLXIFunCR+X5NTsavpCuUdC8lAGyRkJiR89mi1FbKZjc0IpA+B3cjAvxwtSsjKZRGaCND/ZZqQwjBJ8TZtMuenlmnO1VzJzqC6rsDB+nqM0JmV1pT1hkTaVv4CBBuZmUCCwJL0hUcT0fZ1lV7E5XH/CroWoR5zonFXML6rRKyWqhIfW4mBeCX0XeDqeba2wjCTdD9YRQfJjlN1YUICKpFRoRgs2uuSrSUxI06sCS12gsU0YMtB2dbSg4I1L7kErzuiREnfOrYb+U1wnFS6OgqKdCXyEXMYx0Bm5mNZGfoxVvK+v+WC90NC7ni/Xep27+VQgKgs0aMkcOKyNAD7ceptE+7R11pS0yjZqvDlv9PG8BBsu7geJr2R/hIOsKTOV3IYId0bRdJ0GK5DBqYSbdbhsVcK4L0iBobtdxZ22vrYLZNKMYHHw81DjWOCph4jLTzl0VaajORekdTAgLpiA2rCcI3nI235nKnCms5ZXfc+R13gNQx68zI+Cdc8SaEW4euFE8CZfBdSO296jVeQcPN7zqkszbtxYp6EY2c29KXTsOomLMJbJ3PaDmhELyisOpDS4yHC/d2Hyvhk6+NVc6yoo21x0PRwMpcqPlUJ9aTiR23ra0d7DnAkG3CBwGqErXV7ai2Nk49v36xnAIguyFItkr63M43vhB9iwYR6TCy6Wd1ttZfrphsICIei3aDgbj1h5prn7IDEt2SwmYHzSIaooDp97UMVngBZ/fqrLbhCa8PG+NqidGNbiekQV/DRXMhXd7bsfNZafdHBYsiyAUFxRJW5chvrqVZQ5fcAezuNMAo2Pc82V3atfZfn2YI4e+lR3BEjhKE4TteJiFZEgt2YyvKtvZdcuxsnXQGNj1StfhU8UtAksV3Bg9rQ0U7lPC3cfkprYYyaYAyAtJsD3zIn9eBttxv9ryUs0cbMKccWMwLpZWqcxj025V6giaTdRoVexEzmGlKSKYrk7WGd53sR5pZ9JGDUSG0UWzd0h5N7sKN9lhrvTOiVGPLqQlSi0He0lIUUS3c6K2E5xM+4qjUgTFyLzrjqjsgLiuuIOMLjElLTG4l9U1euNFMb6yAZdj62gxEx1/bu17Pdns6TJW8mawLhjaeDDNUSsfXY3oyM0RouQ47u8vH1+mw+nnEfO/9tp4Ovb7Xzt9fBwUvr1kuh8ue5b7+b7W539Rn18/vtROBLR5nK02aRc8DyP/28nqp3/6XmKaOjzewU5vwW7t2wF8awXTHw69RLnbNW09fG2KtLsf7H58sbtm+juG5k3Dl7s5WTmdhr+vNp3Z3l8NfG2Lr483xS/TnxlMb3Y8N7Ja73kZPM+ZP764A4hJ5DRfcYr86tXlZOTzRQewDXtFX2cvf/w/mhBQ6Z0lAAA= -->
