---
name: "rar-cowork-cookbook-adaptive-card-manage-compensation-changes"
description: "Produces a reusable Adaptive Card JSON snapshot of manage compensation changes status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_compensation_changes", "rar_sha256": "5b06b331d26d3acc33aea212243859bda8efc5bf3afa0ca618e1f03b76419540", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_compensation_changes`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_compensation_changes_agent.py` and in the RCI capsule.

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

Manage compensation changes Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage compensation changes status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-compensation-changes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_compensation_changes_agent.py` and embedded as the fenced Python below (sha256 5b06b331d26d3acc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_compensation_changes_agent.py` first:

```bash
python3 adaptive_card_manage_compensation_changes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_compensation_changes_agent.py   # or on stdin
python3 adaptive_card_manage_compensation_changes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage compensation changes Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage compensation changes status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-compensation-changes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_compensation_changes',
    "version": '2.0.0',
    "display_name": 'Manage compensation changes Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage compensation changes status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-compensation-changes',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-compensation-changes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2049405bac09391a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/manage-compensation-changes'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-manage-compensation-changes', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardManageCompensationChanges(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageCompensationChanges'
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
    print(AdaptiveCardManageCompensationChanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166beiSLbvv+I790NWXU4myKRkr17rKQqIIAqISmWtLIZgkHkW6tb//gL1nMy81d2v66734ZmDQETsef/2jsDfX6ymDrLy5fOLBqx0wltxHAagnFipO2GzLisj+JVFNvw3cbK0LkO7qbOyenl9cUHllGFeh1kKl+/LzG0cUE2sSQmayrJjMFm4FhxuwYS1SnciaspuUqVWXgVZPcm8SWKllg8g2SQHaWWNhCZOYKU+pFLVVt1UEy8rJyCxgeuGqT8J04lrVYGdQXLVKxywwhh+wzk6sJLqExQK3Kwkj0H18vmXX19fQnj98vn3Fye2Kvjo5U2gUR75zp39jjn74A2pxPACTs97aJsU3ueghJIk8JELvMnz7qcKxN7r5D//M+qs0q9+/vwlnTw/X17GP2qTTuoATOrMqmrgThwrt+wwDuv+02QRd1ZfQVPVTZmORqugaVP/02PlN0pZPvn7OPbTg8knH9Q/fXnJoAh3kb+8/Dyq/+WlbMbrTyOV/KefP8VZB8qffv5Gp2rsK3DqkRiU+tPX5/2TLJz4bWro3bn+HVJ9uNgGX16+U278POQe9YQrXz5dszD96UE4L7MWpFbqgJ9+/mdknQA4URxW9b9F95cH4QBYLtTpKfjPr3cj/zpBngq90/znbHPo1r+iCZz+xu518jTUP6N9t/9/Ix2HKYzkN4v/Q3L/aAHy98kv/1S3f7XgdeJ9eVmBGAZ4Oebf58nvX7X9mv3lg/vt4Ydf/4Ck/69ktKwpnTuFrzBNQw9U9devv3yo7o8//PrLhyaHsQaz7mtTxv+I5j+y653PDxZ8zvrpx7WQ/zGN0qxLJ++RPvk9y/9X+ceniWHFofvtefV58n2+jB9kMirxxvRhgu9ypoKyfmfHn1/+gECRQm0a5z4Ms/w//mMih06ZVZlXTzQna+oJdHAdJmAUXg/CagL/jrldAmjXKhzR7jEPxv/o4VFiCHG//W/nDqIfnSeIotYTgr46EIO+PiDw6/cQ+PUJgb99muiQQVaGfpha8URd7PdfxtlpPTLPS1CBsoWwYvc1+AgB6eN4MWLkb/82j693cp/y/rc74IcPvFLZzYhVVRODT6O+pwCkT+0cWCPADTgN5BRnDhTLCyHavkI7VFkMkb4ebVNFYRxP3LCEhsjK/k4b2u/zSOy3336zIYZ/SR/gSkweRaRC4YR3cSYfP0L9vDj0g/pLCpwgm3z4/Y8Pk/+a/KtVd+Ijjz1E+6d3oIT3ugOzrUngNOg46GoIJXfv/P7H08qQTAqrHvRl6IXgsRhGawTcN5NrwuIjTtETG0BTQzMneVbW96JUf5psvMm7vJDpODRiepBV9cQF0OwuSJ0eUrWgOu+WTGEZHP1Ref3rpKnAnetvdmndRUxGJ9W/TWR2DytIFsP/RjHvk+DiLA2h+d8D4vEcEik/VJPlG4lPk90Yn5PcKq08KK0nD896+AVWjrflkLg1SUH3JR1rJhhNdY+Uh3ngJGgZ5+nSj6PPx7INI8ut3njf51hjndPv9a78klbPRLDK0RUOLAyQqd+E7lge/vYMKdgNNLF7tx+UdKT09IL79Mo9BuV/0Stoj17hx27jS4NjU3Ly/0NbMsq/4Hl1zS/09Wqy3unq5WHXsaMa7f9owmBjcKd8z6FvzcIb1Lwh7pc0DmGQlP3fHjPv3njOeaBYU0LjqQv1Th+GArTrSPceqWPkleUY49aX9A3aX6F57jgGVYVpDcN+jLY3huPom6QBVHS8/1bm756FdoSxAKNxkjd2DCPFA8C1LSeCUpVjtj3dAcMWjDbugtAJftBqAqnD6ID0J1CIEOYPhP+76XYZVBOa2Suz5Nv0cGye8od33QlsWcGnyQkmzBg0FcxS2AGNc6AVPtxJTRIAbQxFfLdwFVj5Q5ixy30KaI2+yBIYx9974Dn4LcTvsoziQ6oQbWtoy27EXhfcHp59l/PpKyhsMiblfdGP7n7qOvm+Bv3tS3qX8R3uYa7H9+D9ZpwJzLGkuoPrCFUVhJsEPAMIRsK9Un96FNtHNX+X5fOfWvuf/lr3fy+fxx8993kS1HVefUbRR8l7q3ifYCKhMEbCHFTv1e/jWJk+PjLt4/eZ9vGZaT8weNjr8+SvCfkDiWd0f55MP2GfsHFICh0whu/zA23CflxePpLj6JdUBd+c/YyIEW/jHpbb9+LzNgVWIL8E/jj5UYyqsYZ1sGze0Re640v6HhDPdHnq+Qod9V0a36swdO/De+9FAg6lNeTtjl2cD8aNTjyKX4GXz2kTx68vqZWAv7DBGQsCDF1olHF7BNMINkd1CO53743SePPjJu+eYBAZ3OzzmGevk7GpfZ2896evk7cdw30vljZwy/TL2BuPLOFU+PU+930HaYMXuFWr+3xU4LENGluyZ6v8ZyHG9IISQ1CvRlne8nXk+Cci8ML3QflnIsr9woqfoAFxfSzZYf2W6hWU04UNEITzdkxBmFUwWhu44M9sIJ8SFA2sje6o7jf7fVMre+jyx90M9WMv+fvLG3g8ffDsG+F0mKUfq7E6ojBcIUN4/wgsOPY/7yifhCDuwUYGUqJsjLYJYuritEtYjkMQFrDwKY6TxJxibNeaA8+hbI+wPAtzLHo6B1MPI+wZTU4ZihwFe8TpyC0JR+Fwy3LmzmxKuszMoh1AYDbhgCk+dWcEwCiG8OZzQEI7vS+NIGg+NX5oOJrzvbkdLfNU/PcXmybhTIGsNovHh0UZw6Jx0t7dbKSkPV9P0Y1dGCpWVazhWlJT0PpgieJiaGYqWG8rqjO1ZMPwEc0Lq9rqsIUHLXgRmbSNxL4Uk5l2O0h2tyXizTkmATvzkAMlHNSlfG5Zx+5UabolDw0w+SLv4hNFtQFvnYO83laMcuQwG7CCzfeUziCt3M64U46F5XIlU9vjKQImvuloBDkTs2mkNIAjwnI1FctaqAOhIYhTkaghR1ZY7CV8b/bxmWeuyzNHB/66kdGBT3dQIuJAJmaHAMK8oc2AMV5EzPZDTJOVd2hNWhvaSG00fu7klaGlO6LKpic6Nju/Aj3ZA1JDVr1xCvRDfIuwgRc1lNCZYV072hJdqnKxFPVYE2OOds7GtT83Wlif+Jhl6tvC4eKtXDnrG6XCBMTkvIzU3DKvZlhQt6S4Js00q3fmEGJ7jcBOuR3pyhzTF3mWsKtzAvSWnYdXxayk48Fyet1C/DXrkLvGyTjcM/EttatnQydHVcX0J/NwWJbzppoGVe5sKXJ3m9JnqzZ3NyzeHIfCyXEy1wJlmEk6qEpB2l1yPj9RxYrEkHojXfSKx2jr0Jf17NZB8Xq8KPneo4obSWSnfMrvfInv0P1xe+Ssw+22bwCvn6Y+o88Nm5rH/B6ZO9tN5Pfi1Eaa2VScqwXV05ezjpinHXZwbbZnzvQJPwa15GzlrQCs1QZj5km7q5Ms9aRhMaezYt3xpXw28/1gbaVdYlaRwxyRjL6laEVzUpeuiBUXSHh12wrH+TXIL7cgjjfeAbmgSElZVYHdAoNsuCx2k30w3Rhi4l/CQ+AupFm+q65ZIEG5UqrGnaRtHLrKiTwu+tVUuW3nnDDPN8wqQLjrsOrLY7dWrRJdEo0z2Chy8UhqGTrnLD3dVp0o1jUyAJnBjlXJ0usjI4KtrWsRvlslfVqLQXV0F5dbaEdBlejqlaz3izSV12h66mNI6Zy6e3+26oQ578vUwbTzYWk1l/WwwFdA3JTFfoOFbiU1YqptDqxrL7mwM9eCGOJiMzVS/yYL8hW4c3FY0LCVoCyOmhV7bqtytJhyICxjJyyhzzRUwkWe96LoXFJ0elQdmzjahB6Q4rDBHFJBKwYNUL+J7d1S2+XMSQhO2znhbZUbkmTbbOsf+H29KeguRK3LsMuwcnUaToq/tUiHhWAvXMvrCiuAA6s8a+SXUA6jPJhvEtCLnX+wDtraSNFWiylJR91uOPaYy6UeSobr5Hg7n5Ppuhq8QhD3SwRuPVwVORIc28nB5nKY7zuELoQ1WrCWQR6xtSBc0nlQ0YQVd+KSVje7+nAGATVXHZ4KpeQUOs2lW6NMKBe91K8DhAKtNF0XpL4fJPwAbeOcRFsvpwPtGRhTTUNeaKWFa8r8sj3nl7pIdgK4LHiKcw6DTuFVIW+pJF5Ky3zrOgkjxPHxJm2b4TZcXDbamzQqhdXNmnsOug6TAULAWazAUDS6qS6YzaCUcqGIK2RZuVOuTrEgnV7sU6t75DUqqZmDobyiCgwS+z0iK3UdiLzD425tFYtzHaW8vqnVYdAvubY6AV2mvam9YOtkLUWBe0I3urWJZ/LAtMf9SmwvzJo6WsU+u3n7cwYMzdVxYndGmnnSo+q+W55vB20B+oRguRzNsP4YyOstebGXXUaKm2N6KS+KVhNHxrJPCm1qx256SCL7WDrqZgnoJLxiy0SSEQcPA9a+httoPhzcFZeUezZkFIUbnMOxOp/ALe/qlsvq67UEZ0c1YYXHuOhMDCSqEAwFjmR4sJNjDMfR1hVFNeHb6YnCYdrym6hRWi1MAxTJF1zG3AiBaQTWKEwhJVAKseT2sMo8z0vNmESo1U1Dt/y1m9LU3MJvm8V26qtYXlp75WhOs4Mll9NTaBrLcmkLoVjdYp6jSVbKdietPWjtzQkbudGP4UpvQ7Y5XPNtsjv58+UNKnXBXDzYdyptaGqE5MflajOQuAWopedqpiqrEKduV0m56GC/tvxS5a4hCTQnMRhtvj5ODSNQIm1v6a0wWzT2/oSbVgxhmjfL1i3PM3/fLZwNJm3D1jRtVQNIwpp94sY7++L6RzUr6sU5xzoRDypvbxCmamvJtF4l7rpgjzmbn27chcA8xq+ZYY/7i0Bky5noRS3PxttEikhNpTNnNeMHbUbirh6gplgJc9ZfBaWkXwhchQWczcSyKrR+mmhgc3Adrt3G60bz/GTBIXSUXQz82hyTDTkX1ydt6ujz807yxY14xhh16A/xcqHnp4G1ugW9CiUplZSdkSY9s+e1xSGPCnNhNe4pKQy2wAs53fsxlvhbw6dKmMzkGdixwZ+IVSTpdhclAyPOJcctTjdyY23O1U1yV6vIJZgkSyqR2XkDfj1EUp3Sm5q49NS25KhtUpRGUAnItZgqqiKjjLnaLrEt7HDmghGhjiLhXG/QV63aojmmRUxyCYlQ82XQrenET7EsmhubvTWXdrx7WqfKGuCsedntCyMctqLo6xyH5esTHmS7A4M7uzRACAeJPNgj5MvGZ1A9c+xFudTcGtXDSwM2HbuVhdgGFU2vQ1c7Gwa3TKco0IIZyuBInXvCNCA1q9YOu9uGQDpbX6hCiSPANcor2CDxeYqX7gpBz4bfqhGdYnWLZ4Kb0CKmbpBlLDH1bBnZi9Xy6Nu7lY9PTYdFuOgkIJ3BGpcgzi56IUkG4qbTZbwDh0Qz8N2RcHd6GZcNxawGgY9E6xaomAAbl2ZJuh1YxUq+tqmz3ihmGRnrwZ72Be6VNLft2GW0J+022S05/JqcF/TlmsdLsLVyGak66WSH4UpA1zejUI3OSitD3O5rg9OA1tZiuzaUpu6TbbfSTrbPUfJ8msPGKigFXXMMuwyxeNmclWJzdtdr5zbEi/mShI1n2q+58HJzNFzMRIXrpDAjN4mMRxgtcHDbJ+tJnM2OqM7im5Ze7rfEnpV3bSczqbsLqZ11RMW+OvYyAENFHcu1QV16I2+cmKLCgeUJPI5Q/DBkOh1YV3tNbLxa2Ps9uucrNZXNoAI4lvJtMvTrAnckTaHDdK6FlnA92eoUaxKlIEm1oWSUOxKzobSu+/3urHWrFguWgUPxG9gf8Jh+BUdl4R/MAWzU4z5e52XOhnhs62uVa+10QTgbY7WNmWly9Q6xPCtVFr0a7l7FuoDnwoS89RuLyHXtuKgCDbvow4oLXVM0aoePKLBI+hN9Zc2oXm2MdWGuReqAZYxOw/TwXNzXGTTqgqusFj2Gdr4sSIa6sK09fktYm79x00sfEHFqrgog7k5Nn/kxbk+9Od8u2Z3KyFfLtFhGgoBJKb7L0DKbq6G42O61/CQbRzM9cEFl+jBamEDmrntW2SNAp5Z1x5kCxUSSMS3CmXu+ysXhcmKW9bUfNjps5meb3aJmXHXXhnZ1QC8sd9aLlD5dF8i85XSeyG7R7HA7xYygrQekd6iMvmyk0s4ogYcttgEO1HLKL6iLMixOlLKWDS6+uNKlOMr94aorhj1oLnNl7dPCOJuDtigyhDfakL8t+Snhby9RsG5uSzuoZthqRTH82syM6BydlHUfFbDZqy4nDQki48I5tYWY/E0mXI6aTgsFwgQpCvaRmAb6ZuPHxaVg8CFvCgpEZHZsvcyfb8541GCYDTtgZ++urzdG6vE0IlyDlmqAWlRL5plrtkTQ6YbFzOy2uCIkX8yqs9ntuNTmg6aqZD+LcoRynUG/GutVfok5E+br0N3ibi9IQsM1oLlZYU7T9Xh6sZUWi9APxKm5CUFkRhzKtL7Q8nDLi/va0FutGxw49AwwR5AWGuELiD9kMkdyS+10kxVxTwD+yveYh2+uHuae8LLF1ExaUYR5OqfeMtE4+ugJFw29nMEw9VGDJMuUKmfo/LpEDuWhK2sPHVYozO8T0boOQpY4qu6QWAkDRW0PNp7pR5qFVdhl6eWwaO3O1xrM3nrYWo66CxsTKFtt0nCBkbQzX670a7/qk11nL2UnQGyZVBqyjvCGcNLUv/jL1gBm465EEpeVqgSLXFBKhdLP7Zb3bslSHTa0LiutL4Xt1jUd87xAloBwAXPYl+eLdG2Vwj+fVNUjtH03s6VZGUkI1xhuXJkH1qBovzRhqc2bReeulNivA8QKLc1Jy72gwp4r86j4TKZoKRBAjpYuVpyxdY8tjrBkKG2HKMHMHOZDnWyaoQA4sT7JB7ncTivzaiFMTAFBLY3Bql1SMXZK5d5ktE0du577Ccay7WKoicwsd3464zNXFixhPUsIUTmEIr6ZAsfrDeK8Zxfrq0N3c6AivYKL53NBO8AkBdpZkn3fKx4bXGZ+nV3I+Ww5N8UZV91MMiYE4ByUtbOdXnNSBcMqHEqqOpcYvdvtu2GJCbSv3HZbjUhI1JarFYtZa/qwldelXqeH6LRK1cvquOfomtkVUkHD/ayYEnMjZU2MxwWvkeqkbpTZdmaGLpkQDiOKsu4Mpy1OH9xk7g4p3HCc2LlSDux+TpvC8VLmCqIDiqZp0yWj7cYhDkOiLFv0yuH71eqEbYRWxzueZbzlyavwsb2Uls2+1h3uyJIXaVUXOKImB8sdZkXrJIXF3EBtY454oOazbVdzhsSwNtxgdWW3zprtolV2rDTz7HW4WG1v6CIVPeWqVtfbHByIdXM+GDKa1xc7xXBaUOaH1aGsGZs8rYR+KL2e8XFtKNsoph2OYNp8viMrmdlPO3q66n0X9mnppWfwJkcdxwY5t9Abej/bty17c6fF3hZqvUbb7oxS3IXqtsp81shwtsWU8pK8zrpAXy+mZFGq2Wx+nseDy2dIdoCYTlPhDGfbK6hWc1k/7Jc5u5q6nnC9dvPtpi2miG9GM74cdlIbA4TYZclUsq35snDwUrWuYbRwMUXSrwvc705RdjCb4qQIinAYqt5wPTuJhxNjW3Zr667m4vvbSVyc+Jxn8H0zZw7iTFl1cysk89Cex+XtRvnLS7U8sxh5SrrNrVVjPd57JzznzYWJmXGUCUKfmjUWc+IMP9QZ7lK+olQ+jlrJHDshUntOD+x5epE1YgXyONpVThPRZ5VgCSUP2GlJCUZLsUd35ch962Dbs5hIZqqViLERD6i5S+UE92jkuHBmZdwJysJNt53VYJyoWVoZyRtciWeqtzgLhpQcgeaaJcM4norsBlu4mMRpOF9SqeIVEZ0vD3NOpe0oXywWf395fRmPo5+Hyn/9dfJ4vPf/7JTxcSD49rrpfqAMLPfzndfn/4Fsv76+lE4IJXucrVZx4z8PIP/byerHf/ttxUimf7yzHd+T3eq3Y/na8sefIr2EqdtUddl/rbK4uR/yvr7YTTX+HqL6+jzMfrmrmeTjyfgPasH7ICzB1zr7WoIaXr2MP1gY3/4AN7Tqt1v/eer8+uL20HOhU30laOorKPNR5ecLkPGMdnwD8vLH/wHw1IQr+yUAAA== -->
