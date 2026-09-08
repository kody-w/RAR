---
name: "rar-cowork-cookbook-scheduled-brief-monitor-asset-inventory"
description: "Builds a morning brief on monitor asset inventory from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_asset_inventory", "rar_sha256": "f5f02dd1155bf73fc224b8e92cc3fb971f847b1e30ea35b5dd3f329312f7385a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_monitor_asset_inventory`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_monitor_asset_inventory_agent.py` and in the RCI capsule.

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

Monitor asset inventory Scheduled Email Brief — Builds a morning brief on monitor asset inventory from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-asset-inventory
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 F&SCM legal entity to query; recipe defaults to USMF.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run it, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_asset_inventory_agent.py` and embedded as the fenced Python below (sha256 f5f02dd1155bf73f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_asset_inventory_agent.py` first:

```bash
python3 scheduled_brief_monitor_asset_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_asset_inventory_agent.py   # or on stdin
python3 scheduled_brief_monitor_asset_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor asset inventory Scheduled Email Brief — Builds a morning brief on monitor asset inventory from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-asset-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_asset_inventory',
    "version": '3.0.3',
    "display_name": 'Monitor asset inventory Scheduled Email Brief',
    "description": 'Builds a morning brief on monitor asset inventory from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-monitor-asset-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-asset-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd221e78b1b399a85',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/monitor-asset-inventory'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-monitor-asset-inventory', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; recipe defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run it, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where monitor asset inventory stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on monitor asset inventory for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads monitor asset inventory, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on monitor asset inventory from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams', 'example_request': 'Draft my monitor asset inventory morning brief from USMF for the owner and set it for 7am weekdays.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; recipe defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run it, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly monitor asset inventory brief for the responsible owner, drafted as an email (not sent) with a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefMonitorAssetInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorAssetInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; recipe defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run it, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(ScheduledBriefMonitorAssetInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOj1pblX1HfimjbpczLPCgrKqIRAiQhBiEkBE5HmhnEPApw+b/3QVJm2u/5Vb/X0Z9adoYkOGfPe619Lvrtze7aqKjfPr2dfDtfCHaaxpFfL+zcW7DFvagT8FYkDvi3cIu8rWOna4u6efvw5vmNW8dlGxc52L7u4tRrFvYiK+o8zsOFU8d+sChycCGPwZaF3TR+u4jz3s/B13ER1EW22Iy5ncVus8BIYsFp6uLH1A/tdAHWxO24OJ8k/qdPi7YoF8Qibv2sWTjjIs5K220/ACOLzE5jv1n0zYL66Nnjoi6AA0C73fu1HfofHo7k/tAuwA5gafNh0UZ+vmjAgtlar7aDduFndpwCLfO9RXHPQQDKtJvv676dzc76g52Vqd+8ffr5lw9vwID07dNvb24KnJpj50a+16W+t56dlp4OM7O/u6/uAhmpnYdgcTmCiOfge+nXQVFn4JIHIvX69mPjp8GHxb//e3K367D56dPnfPF6fX6b/9O6/GFmW9hN63sL1y5tJ05BtN4XTHq3x2ZR+21X57P5DUhYHr4/d36XBML5n/O9H59K3kO//fHzWwFMsOcgfX77aQES9vmt7ubP77OU8sef3tPi7tc//vRdTtM5N99tZ2HA6vcvr+8vsWDh96VxsPhyUjn2pav23bj0gfA/+De/nqa/xL1C8uW5+Mei/LD4a8mzP/8J7H2WpAPk/rVYEAOw8+39VsT5jy8ddQEyZOeu/+NP/0gsyK6bpHHT/lNyf34KjnzbA9F6heSnD4/0/bJYvnz7JvMfqy1BwfwrnoDlX9V9C9Q/kv3I7N+IBo0DeuJrLv9S3F9tWP7n4ud/6Nt/t+HDIvj8tvHTeO5VJ/U/LX57lMjPP3jfL/7wy+9A9P9RzKnoavch4Utm53HgN+2XLz//0Dwu//DLzz90Jahi0Mxfujr9K5l/FdeHnj9F8LXqxz/vBfrPeZID4Fh866HFb0X5P+rf3xcXgFDe9+vNp8UfO3F+LRezE1+VPkPwh25sgK1/iONPb78DAMqBN90T0QB+/Nu/LaTYrYumAGB2couuXYAEt3Hmz8brUdwswP8zatQ+iGsTg8C+1oH6nzM8W1wEi1//l/sA/Y/uC/Sh5iu0fXkA+pcXmn95oPmXb2j+6/tCn7GzjsM4B/itMar6OQcInLez6rL2G7/uAVw5Y+t/BF39cf4A2GDx6z+p4ctD2Hs5/vrA9PiJghq7mxGwAfvfZ1+NGdyfnrmAz/zBdzugJy1cYFQQAwT/AGLQFGkPEHSOS5PEabrwYoAxD1aaZYPYfZqF/frrr47dRJ/zJ2RjiyfhNRBY8M2cxcePwLsgjcOo/Zz7blQsfvjt9x8W/7X473Y9hM86VODmKzPAwv1JkReg07oMLANJA2kGMPLIzG+/v2IMxMwEBfIYBzP3zZtBpSa+9zXgpy3zESXIheODQPszXRZ1O7Ni3L4vdsHim71A6XxrZoqoaNqF55d+7vm5OwKpNnDnWyTzogWc2cZNMH5YdI3/0PqrU9sPEzPQ8nb760JiVcBLxYNK6xdPgc0goSD838rheR0IqX9oFuuvIt4X8lybi9Ku7TKq7ZeOwH7mZR4gXtuBcBtw+v1zPvOwP4fq0SjP8IBFIDLuK6Uf55yDySUDqOA1X3U/1tgze+oPFq0/582rCex6ToULSAEoDbvYm6nhP14l1URFl3qP+AFLZ0mvLHivrDxqUPoHA8+3KWHBPeaNx7Cw+NyhMIIv/n+en+agMIKgcQKjc5sFJ+ua+UzWPFLOSX1OobPFoGKfjfl9rvmKXV8h/HOexqDy6vE/nisfKX6tecJiV4Mga4z2kA/qC9gzy32U/1zOdT07bX/Ov3IF8HPxAEYQb4AVoJdmb74qnO9+tTQCgDB//z43PMql9uZIgRJflJ2TgvILfN9zbDcBVtVzC7/SDHrBn9v5HsVu9Cev5pSBrAL5c9Jj0JQgkO/f8Pt596vpf9r4HI/mLY/RsQMdXD8EADv82cA5h/e4BUBmt88JHvj56SEEuJGV7ey7A3oo+/C66Nd+1cUNqJhnwkFc/RJA9sf5/enpfNUfStA2IFigOcoORPfRTnP9ZGD4ATYARAHdlcU5GAZAUF5BeAi0sxkbAPa+ptWnxMfll0P+owdnFvu6cXZk3jMPBs/6t/PxjxCi/1WZAHnZvOKh928r7Zu2WfYMow2AQqDx693nBPH+HAKeU8biq9xPf3dE+vFfO0U9aP385wL4tIjatmw+QdCTir8y8TsAMehpa/OdlT8+YOLjCyM+PjDi4zeM+JP4p+efFv+aiX8S8WqRTwvkHX6H51uHV4m9XiAi7Me1+RGf737ONf870gL1AG3amQnScUahr7T4dQngxrAG4AUWP2mymdn1DtDmwQsgGZ/zP9b83HOAdvJwrtGm+AMWPOYDUP/P3H2jL3Arb4Fub54tQ/99PpLN5jf+26e8S9MPbwBL/X/6ODcTVTaXdzMfBUEjgYGtjf3HtwdaDO388c/HZOXxwU7fFxsfIFPa/LEEX/Qy0+sfOuXpKnDRBRo+LDwQoGamQ+DqrHzuMrsBZQsqdnapHcvZh+fJb54VH4Tw5UkIf2/QnwiE/58nVlr8iUEADFadP2Pty0hwVrW7FEQX3Jnp5S91fhte/16hASaFea9XfJpJ88MLgsA7OHB8WHw7OwBPX6e5WYOfd+Cg/PN8bplD/9gyfwB7wNu3Td/+LOH4b7/8lV0zN/29TZrflIDbHmPxk77uYIwDDvtx/0LbB9GBMn5S3aPr/tLzr535V44D3nwNRjFwz38P3xd3309m3n2xPiCldkHNjOMBNY+pZ16Rjn+hCyh7oDTgujky30P+3fHicXqbzQKBap9/bPjtDRStDarIfpXta/wHywGofWzmQQcC/Q0Ugu/PTgT3/m8PBi8xTWSDiRTICYgARj0PQQjCCSgscFEUd2h/hbouFjgrCglonHIQH4N9GyMcwvOwAENXGIKC1TRhA3nPtv4yD3XxbNpsF4jIR4AM/vfb4JL38unpwxywb+eQ2feXa7+9OSQOVm7xZsc8Xyy0QhwI2DHU1+UVpgfiaHQlb8eOAvLvG2R8QFHmLiNmGykxytQwK4/7zfZwXQrHa9d0fBdtVkxO7VWXslCzSKo9isDECh2tO85jyrRPJmLpYVNxX01Dt5oOCj4mTdRe7Et8UDGxUXof4jJMzAo9PSZ5dR715qRLqenQ5hKCLjBd+VICJ6Ios8tJkTtRPkKpoOMSvKrO/qnyqZtiDRVnXKEJPUHbZnVqhpOnGftwP+FZ0fc5NNF9Cot2RXP8Uux4seS7bhXLMgsMkUZ2UC1tVx88oqa9M53krUYkKdvRPVaVmqNdpTixEzV1WVGRIFjnj1R6zGTW1cDuUt5rx6BsylJXTtfsVPKJd4Sh1NlfdivhRkEE0RuTM5BQEFhnVe1Rym+CQOUMiZboimaLZGsgI9zHHi5Pl7o1Y4Qx3AjOVwwKcV5Gwvx5b1dSci39EdvQMDd5Q9Hez7p421QxHmGtr14nmRA0adI2dheoQsx0wliu1cP5VE2+KMHjeRu26yrn4MS/ZgyidyJaINstAVPVNkD8dJOddwf5GF9E3tcyLeUc/FotdWV9dEpbRDYsxHBjxNUy3kwja92cmzv4QucOxIl3jnu00ptO3iXHLQ37SZdLqKIQND5S6/s1juzC2ki6p9llUvqb9dloEt/scLTAkvRyGbrORg5eInQMdDgV5IovDVevpi1ilEFV3ja6NBiFSV90PqCWASwPS02tCjU6FjXLZn1FisJZhrJz6iUSmUnxmtaqc3WxrYlfrqeRtDJTF/khO+nhdlOLK/FG2MUyvstrP2S3PAghlMXQFd4wTkdPKL2OC54Z06HQyUvI2+IZCw9BiyL+wJXCNuORunG7KdPyi5+SAkvtLvh9okUNO5dTfzj0h4m5Qjkv9MvDqDWpBHHyctdi3GbQKI6OGnS7JkjDDzsHu5pwP9hkxdaIe+D2viCXSFDGOUsrxTULr5JiupuliQrSnRCk0TFlNnMSEKI1tDX3Hbsy7bRToIBeriKCg4xSGaBEcixISlQagta4EiNoXOMZe9Lvsr0TZYb0WkQvZT4SNP9yrcMy9IbudD8WumSroGepQSOU0OCbU1KY7RF1r2zvjsZw4Kt8SptAd92beXPLcI9kxgXe30Sxu3vaaYOt7Wq1ZiUN3obBBt4NrDzI9n7js7p92ZYH3DJGUXGkKdzlq8zKtjv+Yl51ur1sVUwBo8teYTxtb+bHU5OQG230bqfG2yXnFCBMusQpRGhiWO8YKlC1pSFFRTjuatOB9uIUb7qxMWiScj2r49tgtDGB7OUh586II8ABuZkichP7cSCQSBJaRujukni7LDM6u7Z7VfWu+n5IYntvVpUqMvK+rLULdLsJYhhnotn17Yq9L+8drBk4w3HbKh4FkW7ccZs5JHdVUqLWXZXWKSMp19G5MXbaUdoM+9TWhKV7vMaFVyn31fZ6uKBcFiWsMM5CqBV1tdTTofW0wd5MWoOo0IkaKrhseqzN3YhS16zdYvSGwE0kO5sKju9cPthSO+wOF02jnWBDRtsrD/vH0EIziY4QlWFLkV8eMVm2ksEQljycGtAqvcDetO4h2XGO0VqmA6Q37Nw0JUjZZDtHUDXa39KryWnDqTAFy7Py4wCO6x7WaQm8DBOsPJBL3IRDr8QOFKKNtnK/IDZnNtNx25yKe9vuFeN0l9Y4zkyTwS6ZNakV5043p7Nzv2Qyh7dupk49s740hDLIahBtTI2bYL00M7ppd0xNH7s117obCQExUlEp8vv8VgtDVMCWcjryhKAKcit5bLPBmh2ZxRlMS8TmUpBoa2X74rpbn9acYW3ck3VCtBN3tI0DFhxvh6nac5kGHzvtovR0U96Q8y6D8XVfuEf8fNyk5soR21W8wmq5as1dgDQOpFn59iKb9V6m+xOTtOpNjyk5xyiC0FIhvzCRajFXSidlwE81sTsHjEru7uau0mpFZ6fAgxAmWgGAp0jONKTqVtxNlSKrPqj9Zd9DtxW1vPZ9raGW5hG6M2WpRldtzHByExu7kMX9E67Xp5geylbeyta+1ej+hsoDczsjqyhjREDbrgKtnWWA0Yq7nM63ms1l5Mh6RXI+o2hj0ph77RX/gOWKiI2aeJZ2uzGCD9tUWDd2GV2X3phG6aXexUbMQZIhleoeypcX9+KvFMVYiSuzyi5OKDUBrkgnaUMpVXAWFCQpy5vnXsGspsEMg3l3PNuJbiRjsLa/Zx5lgOBmF0LprPNeMo+TVakTzwpECaX2pcyPu3s22Zht3khIiDr6zorbQ7hP8jG8V9LRJQy7vQIA3Zy0GO9PObExARuxg+9Zd8FdWxVRKR4cQ8hIEOeUYw3ej8oEZFbkr6fjWsd5alBZApGPq+h2Ml2IP90gkY8t3Kpg+6p6R3TNABTgDyxslCUX35ZXBcn2Gn/uhmy4uSF8hMuAOUa4ygzGgR9FzdOc7rDB8GNBuZfmuMdV0akKKr6yd9fhC8YeD/YuqEypNQzE8ilV4e7rEBLWpXnSppSlcHf0AQpp13WrXwXbcVk/O1YNp051p0lycmwxuZYwOtubq5uYVXrC7GxeG8g2Sq6b08oIYabl0nq6IIWdJEbGCnch9S/dbh9cS+kKO9WRjI8yT2WWdAuI9jptxS1uXLL4IuxFLRK2a7fJzsmFgRn+HpjTaBpi5Rx3B4ng4oTgZf24mkh9aeOtJCHrGkYgITTwcE8lrjtGsTqO4nbTRNKWLRpcIfsDtC9UauWCyXIjUTA8QA5vottJC7WxrshlC1CdODh790zKEsKIWD2QXu7Mf/71yZgHZjmDb5ERrtRd6Bwp4oYLk1eniY3eTeuww80zezQq/rinl1Wq8wfRaPhhm+4u8Q0tBKMT8H1G3SEzJotw3R+4aLsfdNGBl0K6YTVZ32KXsesPTrGdoAMU5AeE25/3a1TQJicyz/RmExpFDCzwM2S8gNPQqRSJvQRLgIeM5Jb1Sy88FkXoCvvrzd42d/RaNjRjcVttvbcvoN5EcvRItsPW5p0k93Xc4A5uLaElVWKpWaJ6IcdNv9msrV5UNWo6IC1zbPNRKq7bnc6tinx53LDnc0E7m2sGdzmUT4oI4ZdxDSqQ1eLSQOiIy07yLlI4mSWNTrI8dHksT2TBK87ZFLjNdmnitbnPcbxK1+kS6TbD2rhdd2xmp6UGzkZrF4yBnDtxFwHlCWa9Ca0cbnU+6Us2QUbTGcmt44sRdHSa6iINOzoalS1U+BwjJS5zyxK7yDfOqVhX1/GAGONBsW5VrlvHMhj4wa66AwbGAkLbOYVubSXbi/oLqXFEvDr7BreJ1+c8A2zuYMhQeUce8U/oDt/g1x2Y40TaCj3W3yTwlNSIinoHgivyKyKnwtlCxAy6HhEp763LrnbBufUw6Yi6lxXLtCpet/jrhV2d73W3WeZMAaPn8Uitdm2XM/tNhtNSa133URIZp8N1HewMjbVUJ941TS/qZDix0wVMV0K92jW7Y5AwqHKB4EPtYZliHMJhpHi1VYoT0nD5UK+donUqfAuFZN7KRXw5aSMcdTDRdQFd3aKSk5AOOUE7rJRJClSFjWWTyl6nYRd2upIcity9la7a7K/o1pUm3tKpZIUJqcB5Z31jp3tFOYeJ6Jz5LkHLYc11a5pnBqQ4ndHCPhsBysqalNgELuM39iCU910YwWKc8TU4abUdIRm8V44pkl7P3oW0Kd3YDdcT1XmoWXHHjY/wU+A6ENeq9b61GM8d7hzMkqJoTFZ7cQ6bC7Od5OPVbAlaUlJYWZ9MhRP5w6q3vLsRx+IlZ7Mi4UYWzciRTQRxiXkHAd7obetCNXc7aAh3CzcXXNO7FN+eBcxbmlcVx3zh6l/P0jl16WV9rXpMClDFOrrbdm0Q5FGnY+awGba8yUdmXclycjcr21ifxQIKmNLQPXyVrJtjYCRKSsWtigN8uCYWjTpt1rJMqq7vLHN2KZ894Ec4Ia0Vcx9PNBcN8OG28e+8hDbTzTCsoYu25Mrg7fI4Irs8uTE6ziZLi4CNlkCWSoZyoi7I+n7yZbzn+j7lpeNlmWn2jo2rrWjLCe45BeS7YieqMe2JTHbcZ163lTckPPmhSuP9dCj3DRn6BlohBHWEpqwIz4UI6me956dyVTuUYN9YyuCOY7QZcjxBjLyBWcW287WFhFwhbKyaHFstXePkjdYV8tRpfkMTuub5dTqJ9aYDGOiPSV+hvk4agXGSPD9Ym5IjDH1Z2rwsHdDJRoUhuNCaHSLC3rt0gGG3RgthYrEML8IVQfvgrndsJBJtWIDDCILxaHujy0LmuzNzCfyMF6CuD27suCIV9WR6fc5U+XoSgbCNT+BbsTJvktBW9rWlDgx1XTtod5MgLNqpfFB1uDMEKD51dxlAf9VXvXKD194KnID2KyTCGizysXpS1Q4XK6jJpRXK96bQdT0+Voe650H4yFSwg1OGEoq7sgd56vzjeX1OLYNwsvpqJ75GbNWrUxGyqRYitfdXbodPa79a36ye9NDbtUfYTbRbp311uiu33j3bG4MRrTsgCMVh2/i8WiUeOHQiwfEYU2YBGX6W4Hxr5NfaosMWOqL9epzO1/IiBGvMFkWnZyv0gtw9rL7xK6k/U6G7x502uJSj6hwCbItBSzDIinlS7MF4P5FbSMh5zWpPB3cF79qDYRCIOA0n87A6+mNJ7QnSI2mswConLOt9DrJEc8vag5Ue0Z1MDxVmV55hydUgfT8yxD64kFh7zAPN1m3Ds/oNV6ewW8nhUp6UuFhRnE5hHkMjbKFYQdpLZ7ec1vG0G+6Nul0myjUee433qbTzzrBwDjellkPwsm879eDvmhVVCb2jjiTlbOT07p/rk8BWmhMt9/TKOK4EFENqXexlQAcjaa+6WLO3GnzY5LZKE9XqmiMmTkUjfvD3yT0ULCb2wQHRRiE7JVALG3b62ok7JLS59MIGcabzeZsXaFYS3mk4S/SyvMs7pzWJm5U7qok5xMZxhlHaqJNSpe0gQpzvOjoe1vkuvpRcxEeNVnnCgRCpIr4p5Sl0N8xWNK9XqI/jgr2VWuegaJfdSp2xBSTWze2wP4tOJ9OkxFGsKVs7vNWGW6jmx0Md+CK9a9IUDI+EjVE9hu+2/XJpbuPuWgvbWFOgjFdA59yVROaExnZt150UaGiUymF7NfDi+Mr0nTk1OLQayK23gbjbVMvyeX/wll68twlWXPp3wthnZe3ZrYmOvk5M0Ro6cIpz0YwtenFBh4Oh52qlrufZMkqx6q6hksBYsoF7WjdGqhpbmMci2FhFFph2VHCKQpfoJUEFUOvwjiFqypv/VBvaaxum4pE8rFecS0VX6lxpd2RT8+V2A1/zLbzv14wuY4wZVmus4jp09IS1xUDdDcqkwCpZbsxNonMt7XZ2sN2uv66ReJ9FY28y8ETR6n23nlY2ksNwl41Ga9Ec5twU9ehe1KC5Y/jyurrlGMkg8iRNdUEFFnYgYy1ssLua8mWdDz4d4Y3YY0QhaJ2KDnUObw92xGv4ktQvS1TDV7V1KQ8OlvFXxc+kY1vfZc9FkWBTW/4qRCxku+HsTrbJI6BiNYNCKtcNP3E8H4poLvEJfmgCMHh5TM7vx1gYw9MREWSAyZ4nh6lg5avSWpEkqAVa5ZFwncF1kW6HQxwfPH+J3Xb86Pu4KQ5BqJ9EIZ9KmhfWdXLaIbp088hThYn7KJAdmtP2KzGwHB5pgtW+85MsuXDDUgwvB67RUx9ui6LfQ7yH8VDnr5ahBB21AgvNbjih+0QuuESGL0tRWBJnVlLPxNYCpinnbTlQAcQIawKwfGttics5r+5wbaHp4Ab2tUlPcqrt6P1mv1rtaL8inUtL3C8338jy65COLb0KJLG63BrZXB22cnIdSMcwvBOKnjKYFGQw8652npzlaiVgiHLqPDJub3eQgiuBm8U5uvCHfRxEzr2nvILv/eMB3hQ1mClxmNH1I10ezz3riipbVmNbGVq0spXwpuJ7ZKN3/dgOANolymgB5KEQQvrxRlSV83J5JtITNBkOsyRWI7Q3fSU4o3bHgkHP2lkmC4eBdaTwaM+vScQJV73cq7IHZtCkxTSjyLdBx5ukgnlk5ZEeTGOmQ1HCsuEZIR+XNhUU2HnyOvtE6lS1MXno6CpJVtB0ikYF4miF3XDWUq3tpl2CUXtEsbTf3eQNPJLBeWVf+wAZVjDXj96+3DAyz1oHua59gdhRaDseVVdo9cYPlfEouU1/Y7kTGFDJfbGFb8FBYnCZ9Ua7vTUZSvnGubNZk7+u8nt7HtV6mZ9c2cI6WmCCsIRbvpF0E4px/FAd9J7udzVpdTuHWubRzSUjMhsht275gMCujBMQdAm1Fc4JkNZsqBq/C/J0t+SRPtEsHI/BCo3Jm4awd0P2YT71CNpuTl3fTbpyKOg1skSaM0kZtcH29zt6aTyvw7G6wagpPNRizwUwxaK+dGebCwQtw1hAvZ61+40FmjHtLI2iAnJV5VnCGZ7TxwO8Z0NmdeoCJEPZymQKdXPhkz2UpJhGuYof1xHWKzV7DH0Z5tSDtZELvmThQqlL6nzD17u2t3xr44qXAdaEJS55nezugiUWrDNmvMG8DLnSkkDiu1fmCV7JCEMaviTn2QU+0xV9wjUHO8eRaIik4LHn41K9uBdkaqGJogYh0LqjkkvX8gpd2Cum7xSmYatJX8p4pXfUPc7UojvfTo6q75bKgK22gxUxB0c5Hhnm7cPb/DT29Uz1X/2V1/wg5//ZM6Pno5+vP9h4PEf0be/TQ9enf9myXz681W4M7Ho+JWvSLnw9aPqbZ2Qf/8nH9LOQ8fkzqq/PjZ/Po1s7nH9x/BbnXte0wIamSB8/3gA7nK6Zf57YzL9gdcH7Hx+L/o1L4IrtPp4UfmmLL17clEUzPymL8/nHGb4X2+3Xr+HrGeKHN+/1YPgLRhJf/Lqc3X49/wfeYu/wO/b2+/8GhchtlkAuAAA= -->
