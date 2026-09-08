---
name: "rar-cowork-cookbook-teams-update-process-customer-returns-and-exchanges"
description: "Summarizes customer returns and exchanges status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_customer_returns_and_exchanges", "rar_sha256": "3cea613cb2031c5442470857d5e9dd7ab66650429396c82dbdefae1e93b833c7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_process_customer_returns_and_exchanges`. The original RAPP
agent is preserved byte-for-byte in `teams_update_process_customer_returns_and_exchanges_agent.py` and in the RCI capsule.

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

Process customer returns and exchanges Teams Channel Update — Summarizes customer returns and exchanges status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-customer-returns-and-exchanges
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
    "as_of_date": {
      "description": "Date used in the update and card filename, e.g. 2026-05-24.",
      "type": "string"
    },
    "card_filename": {
      "description": "Output Adaptive Card JSON filename; defaults to teams-update-process-customer-returns-and-exchanges-<date>-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_customer_returns_and_exchanges_agent.py` and embedded as the fenced Python below (sha256 3cea613cb2031c54…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_customer_returns_and_exchanges_agent.py` first:

```bash
python3 teams_update_process_customer_returns_and_exchanges_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_process_customer_returns_and_exchanges_agent.py   # or on stdin
python3 teams_update_process_customer_returns_and_exchanges_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer returns and exchanges Teams Channel Update — Summarizes customer returns and exchanges status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-customer-returns-and-exchanges
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_process_customer_returns_and_exchanges',
    "version": '3.0.3',
    "display_name": 'Process customer returns and exchanges Teams Channel Update',
    "description": 'Summarizes customer returns and exchanges status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-process-customer-returns-and-exchanges',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-process-customer-returns-and-exchanges',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6cd8ed83e01be9bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/process-customer-returns-and-exchanges'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-process-customer-returns-and-exchanges', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used in the update and card filename, e.g. 2026-05-24.', 'card_filename': 'Output Adaptive Card JSON filename; defaults to teams-update-process-customer-returns-and-exchanges-<date>-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of process customer returns and exchanges. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-process-customer-returns-and-exchanges-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads process customer returns and exchanges, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes customer returns and exchanges status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.', 'example_request': "Draft a Teams update on customer returns and exchanges for USMF as of 2026-05-24, with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used in the update and card filename, e.g. 2026-05-24.', 'name': 'as_of_date'}, {'description': 'Output Adaptive Card JSON filename; defaults to teams-update-process-customer-returns-and-exchanges-<date>-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on customer returns/exchanges status with an Adaptive Card of KPIs and quick-action buttons.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateProcessCustomerReturnsAndExchanges(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProcessCustomerReturnsAndExchanges'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used in the update and card filename, e.g. 2026-05-24.', 'type': 'string'}, 'card_filename': {'description': 'Output Adaptive Card JSON filename; defaults to teams-update-process-customer-returns-and-exchanges-<date>-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateProcessCustomerReturnsAndExchanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adejVpLmX9G8/cF2K/NlBylras4gQAghkACBkJw+afZ9ETt4/N/nIinTdpWre6q6P41yEcu9sccTEYJf3qy2CYvq7dOb5ln5grfSNAq9amHl7oIp+qJKwFeR2ODfwinyporstimq+u3Dm+vVThWVTVTk8/Y2y6wqmrx64bR1U2SASOU1bZXXD2Le4IRWHoDbdWM1bb3wqyJbNKG3YMfcyiKnXmAkseDU06JM2yDKF34BxFgEUefli9QLrHTh5U3UjA9y30gvANfELfp8cfasDDAHXHIvXZRF3cyU5iW11XnugnYtIGznLRirchd77Sgv/Cj1/rLIiyaM8mAR1Y9dnvsOtPMGKytTr3779ONPH94icPz26Zc3J7VqcOntwUsvXavxTlXheHXNvJRWn4LRuct91RhQS8EB2FaOwNg5OC+9CqiXgUuu5y9eZ9/XXup/WPz7vye9VQX1D58+54vX5/Pb/Edt84fFmsKaxVw4VmnZUQps8r6g094a69/ZpQa+yoP3587fKBXl4q/zve+fTN4Dr/n+81sBRLBmT35++2EB7P75rWrn4/eZSvn9D+9p0XvV9z/8Rqdu7dhzmpkYkPr9y+v8RRYs/G1p5C++aCeOefGqPCcqPUD8d/rNn6foL3Ivk3x5Lv6+KD8s/pzyrM9fgbzPaLQB3T8nC2wAdr69x0WUf//iURUgtqzc8b7/4R+RdULPSdKobv6f6P74JBx6lgus9TLJDx8e7vtpsXzp9o3mP2ZbgoD5ZzQBy7+y+2aof0T74dm/IZ1GOcjMr778U3J/tmH518WP/1C3/2jDh4X/+Y31UpCOlWWn3qfFL48Q+fE797eL3/30KyD9n5LRirZyHhS+ZFYe+V7dfPny43f14/J3P/34XVuCKAYJ+6Wt0j+j+Wd2ffD5gwVfq77/417AX8+TfMafbzm0+KUo/0f16/vCsNLI/e16/Wnx+0ycP8vFrMRXpk8T/C4bayDr7+z4w9uvAIpyoE3rPG4D/Pi3f1tIkVMVdeE3C80p2mYBHNxEmTcLfw4BqIG/M2pUHrBrHQHDvtaB+J89PEtc+Iuf/7fzwPuPzgvvoWYGuS/tA+XmZJlh7stXcP/yQpovAI2/fAP3n98XZ8CqqCKA4ACxVfp0+pxbAUDuB7xWXu1VMxjbY+N9BBn+cT5YALT/+V/g9uVB+L0cf37UhOiJjiojzMhYt6n3PtvgEoIC8tTYASXOGzynBTzTwgECzhWg/gBsUxcpKA3NbK86idJ04UYAe0Cpe9WbNv80E/v5559tqw4/508oxxbPGlhDYME3cRYfPwJN/TQKwuZz7jlhsfjul1+/W/yfxX+060F85nECNeblMSDho1CBDGwzsAw4E7gfwMvDY7/8+rI3IJODegv8G/mR99wMIjjx3K/G13b0R5QgF7YHjA4MnpVF1TyKXvO+EPzFN3kB0/nWXEHCuYS6Xunlrpc7I6BqAXW+WRKUTVBZm6j2xw+LtvYeXH+2K+shYgagwGp+XkjMCdSrIgX/zWI+FoHNRR4B838Ljed1QKT6rl5svpJ4X8hzzC5Kq7LKsLJePHzr6Ze5P3htB8StRe71n/O5UnuzqR4J9DQPWAQs47xc+nH2OWhmQL+Su/VX3o811lxVz4/qWn3O61dyWNXsCgcUC8A0aCN3Lhl/eYVUHRZt6j7sBySdKb284L688ojBV5Pwn7VGzxaGebUwz/5i8blFYQRf/H/VYM02oXle5Xj6zLELTj6r16ev5iZz9umzL52lmcV85OVv7c5XSPuK7J/zNAKBV41/ea58ePi15omWbQUEVGn1QR+EFzDeTPcR/XM0V9WcN9bn/GsJ+QDUeuAlCAAAFSCV5gj+ynC++1XSEODBfP5bO/GIFmACYEcQ4YuytVMQfb7nubblJECqas7gl19BKnhzNvdh5IR/0Gp2B4g4QH8BhIhATgIvvH+D9efdr6L/YeOza5q3PDrKFiRw9SAA5PBmAWcP91EDcMxqnj090PPTgwhQIyubWXcbpBDQ9HnRq7x7G9VRM8Pl065eCdD74/z91HS+6g0lyBpgLJAbZQus+8im2fkZ6ImADABQQHJlUQ56BGCUlxEeBK1shgYAva/Ye1J8XH4p5D1ScC5uXzfOisx75n7hGfFWPv4eQc5/FiaAXjavePD920j7xm2mPaNoDZAQcPx699lYvD97g2fzsfhK99PfDU3f/3Nz1aPa638MgE+LsGnK+hMEPSv01wL9DjAMespaP4v1x2f5/Pgqnx+/AsXHl0U/AvYfvwHFH1g9rfBp8c+J+wcSr3T5tEDe4Xd4vnV4hdvrA6zDfNxcP+Lz3c+56v0GuoB9kYF4m305gu7gW4X8ugSUyaACIAUWPytmPRfaHtT2R4kAjvmc/z7+5/x76fkBuOx3uPBoFUAuPP34rZKBW3kDeLtz+xl48wz4yJbae/uUt2n64Q2gqPcvzH5z9crmoK/nCRK4BnR3TeQ9zqz6S+F/mUnNZ3+cqNkZ/EFJ/NbYPJ37Cnmg3qzNLNOHhfcevC9QGCU/wsRHFJ9lb8ZyFvY5Bc5947zly9ctf8/t+MjXf4Th856/gNT1rTYFpgNI+C/E28f/OS/+Xx9nSd7jGlTnP5VzhtWh+RMJHwdW+r5gPQDhaf37XH2V4bkN+R2kPOMA+N8BRv+wmNnXc9sAVJr9McORVYP8Bqn9p7I8quKXZ1X8EwfN9fQPhRPYpf5apl9e0TVp+6e0vzX5f0/4AjqnmZZbfJqbiA8vTAbfYDD7sPg2YwGNXlPv4xeLvM3ePv04z3dz1D22zAdgD/j6tunbLze29/bT38kFBHsAPSiXM63fhPxtafGYC2cVAOnm+TPGL28gwi1gX+sV46/BAiwHuPixnlslCMACYA7OnwkM7v13jBwvknVogf4W0MQczyIRzLFRGEMcAsdRnIJXBOUS3tp1KcsmSZKAcXSNrUlnhbr2HNUe4q0xe4VhDgXoPZHhy9wiRrOYs4zAOh8BuHi/3QaX3Jd+T31m432bcB7Z/VTzlzebxMHKHV4L9PPDQGvEhrCDPe53yxxeDSGiuONV4Trzhoqwv7vbegrmFAI9tmO37yw9jXtuE2kXgaPdwOqn7bEUg6W6X41nTHbW9EDTip6h9ri0XeBoroxL0st8E/Kkk7SyO/l2uwu9er1koi22MCwWhXu5c2fmGJ4Kxc4s0uAuSwPblEOQLUutVjFPUw57nyLW2FJYYSKVnqvlDtNzxjgJRaxGpX1sRPYm5kdCa68IKwzEem3puAfJFsFlRJweh7HSlGuIQgaZCsi2yJS7sTWP49XkEOsqmwfx0Ii7SxteR+x05njdEiKVQvQkT67jAd7IORe40Xnp+1AjVsc9d1JvpZFNkcsgUU/JOkGv+DMFEUSN3WQY8vMSFWvE7TBoCiLKDWRn0uikFy6qZZ83UjcwanZF0NuIXhyYlVcFhhqtlsDepkhWxv7QmU29WYsWotKSyMn1Rh7Xnn/nR6fGQ08T7O2E44m+6dNqx+1rxwYiV4RS7ptY80gDyMv1FzPao7pxOcBuJ044BmdT4ZH4pG35rLgegj6Y7LDvd94Wb5Mp0EXyEpVK3/WqVKjidJK51hi3dmSFx122vi01GiFVStnyQnCADqUo2CLWsB1VtSIhK3A1UFnEaOXtrGs3Nakm98AEEWtqJGI4Nm2N4k5bHeimdiQc7k8r9IDGZw3JOVTcr++HM3m/DrLJBJPj7/WlqRHZet9hkbA2Nutxq4uVELWHTlAVDLW1rXjuq+so7Aa+VEAtyKUbvjsd2uwWO0orjZpWxvxaPWHGVeflYi/xqhuconxlCnvWlokRU/I8y4otPTSVkiKVIsLAdHS6nCzDhrVEp6K1LArseaz8rB31whHr0I9ydilGbenkvGpmNsVVy2GM/HXkikQiVvjGhzg+iDwR07aJHE34eV8P1o4ykS50bKGIZOh0Oxy1fXHr8nCdorcwQWpcXDnbcrzu40y+h9IdD3r3JjrXzih3Km+JSLKfJHMnuW2Cs0N8qKh+BwWn1fHaTdXknOA4u52qOlzm3co89OodNiAO1bwLW9p0Nwmh2Q47IT+LcdyxzGQlQYCgrawI582Sjm48C/m9vuv5otWU4CZfRwdzptZRtpJMkX6THLf22tlmeqEEV5++H+wNHDJMiiBMFVLBihEOIoXL9GmzM+n1nbutBJmSLJuBocMJAMNxOtXovruu+6hksuXORBrjrDXuxYc5I15uYHitkJrbL4OcvhpsdVuGxbFONFT3FMo63T1Vs097niq21SQh+/3Z2N9wu0v91NyX7j2WTdPDEufmTRco4VsWVX32KMDB9gAfzvtbD2+G47Db3PhM0UjZLrM9dZO4u5+lNxpD+QrekepG48ZNjAp6f9+LoFbTp/syDCWcLLmz1TPDJqnyHjdisT7jrnXDGhHj831V5nC5P56F4lobtrqMrymYCQxawku+SenysizXcGMVnbA973k+Ejt4d+qs6bBCDdE6Hs4eecjCbuA7EjvnEea02/6msqe6wBKukTaaa2EbLBPpIFz5NexvTiraHy7l4PFValMriTfK8Ihfp3Cvx4fjgYNTgCfqXvGEAe2YBiIOh5rKDs7SFtCAjVIcSi3TqvbQbeXsnIuyRfxDjHs8PnYw2TTSVDcKyI8+zWInN3yQK9txR+QIEx2XqTs5dk5sdS91a5Vlj2yNbGJOlNILYwi7yuNwBN/6fslMDMMKtH4SB76HMIPb7sjYweLtmWHZG+pEvAMxTB8BBIwbBxaTWhCCkVVpbhszIzpGAtYR1xbrisuBzfSSuaqZetZhNmrktmMEYcsZh22Dg0gzNquWrMQLfbibIcul7T4/lzBdclkVIrvVKYLHECS+ydmF6dqUyNCQ2LrxzleWY6HSJ4QduruJnhCnTu8yHu2swTneRqepiaBJ0J4QVgq8XLWHhJJNAnX0uFIZW4DV3c7z1dJgi25USjdHA048XRxBIqzeoqB1wW3kjs9tJY7DRN8ut7C61teCuyNrztQgwx+JyyRO/v7eS/gEDUpN6yHO8eh2k9OTebzxnDHICNng1UbiGCgPYY4MbuV92U80Yowruph2GQqySogCreyxUU4TTdTuAUtslf0aVEy/DBp+M91ZQbjo1jk8nYWyGbM0gIeUHo9hz6iW3mf3TJUEuOyANB5UdUFniENo6NrFvDJnioVumygljr5s7B3K14gDa8N3UOP2uK7r7EUBXZeU4BrqTSgs4ZZzP2w4IxpuTOSg1dUwVuGJ3SZM35Jt6mPcOmX43GgEztgogabwtKSJw4UCWHB2zgC499k2Xop2dhiCvR42N/IgLzcbQ1pd6sbQ1ZywqUihPaUKRBEt7yv8wCj04cQM3oaodHhgL+JVZs9LQ9xnhbIvFCk/gG7TjHhmM2j17nA/pHLTRQRaB8xKHAu8hsl97GwEU9oWx/NgkZt8pQtJnUxsbEm7bhUpECTgtNUvD6uimGqt7lNlclQ8WkWchrqHS+rtzWycwoS+dUMgHrnEWSldTsH5WN44HrfhZMhGbEPdkuCmxMvJVjT2xh3kkaIQaB9Np+tY3ne3e7YJLt32ftGU3j1LV5bbwFMuN4dLUsWBHXA+h06YEuYNH5eQmtDbxtAYuqvJUEJEMHLs8fCwX5fxTRRFI91SjC+RZGDcb7pAN2daZGW+SYRcYTn1giqIdI8HP5rWxcgtY30jK9XqaCLXs2SxZMQhN5xMxrEiKincUVowIsjaMy+2Zps1cu0Fzq1aFPX9rd5uei0wBiNaQzdPjCfsGPTd6lqKtJlXq/XxEPcUtq1X+27q+P06E5X7tA5LoddPre8yxVm1iHvYZ5E5euLAJOsgh0nraBmgZ0o7PSqinrMQxYD32r1fCRnVL6/MWMFhKrAGYm0mz8BaJmLPalObkztCh8ElpwmaoOM5hUXeFPIhrPJNIp3YYIeWFumGK07rzo5KjJcsNwPRCRuZl0+EzQyNIhbSWSJXGEEUsHtZMaIgM4zWV8VVvBAFJPHynR2WA3K+sVa/Q87rbo2VSHq161wxr5Z3udGjB3quDsaMu3Jt8pWUmzvB0GGDXgW8U0AabqKV4LomdEI9fWPuDeOMJvsjk7odv9X27CVKetBRRRFelNj9MmTJprpF6lGSAUYwcWxfdS8v2TgReHvPxyl25bFKM9qscld3f4kewn7l+bGxBh6FcW95k4ZCM7ijkDenNPHuhhqj2cgwmyPdI/x5FVowBWnCCZLFC8Jrze0cTdpVBc3i3tsfYLwJeBztAjrSEFVDdwc3peSUrzclw21Pmy2/49Eq4tkdo3PyKUsalmyttD0M2HhTU0203XuXDZIhI/x+Crq4gZbumHfbgti1LSNiVoUYtjwl90pcUpgUJS4peHdBE8G8764QXkB48iIWXn0nhICbEg+UHFdvMOGQqKa43LcRf9SJche0YsoF4Vops0S46oD1XtwtD0rtoeONkYRAyOU6k3RND+OGxwaTZMmJgILOLbm7MEhiQ94Yt0R2Un3qIcmNXc7FLx7sbaEKmELObTQJx8nB3CbOVEqf0G2tc326r7Qm4e521OXNstK82/nQS5aa0Z520zZFANclqh5aisoQMb6bAlz1WIHL1+qepDSBZGNHDjvF6EVhf7YHrzwFPsp50ZrXtJpc1ie6HPw1vANRo182QpUj21WHdci4xE+tye90urIVwpPzLS5pFnXLgsO5qJl2uMZOui3IrrmaSmq7phyN97RLqP0YUuwZxvu+LPUdiW9Q+nywdzrrqNG1WtJrhCLHgWT23lVFj/wqLrYbDfaKlYHyKO7zNosjF4d3s3HHpwK2Jpq9MN4qFyAQ6FkDA7lYNZ0oELXHOsbiOOrAKjnc2bIP8Rg83feWaBzqVmdoHEm7jDt6TecKxtq3/Vo86QIsp9dIzMQ+shKubWnvqqVaKYDu9KjgkgVNJ/ZCotSxIBQPplGWFdHTspeEw/V0Ra9euK2H4w2l0dsW8ihlJUf0sh9DpqEL12GH5C5RAJZv90t2SVGbJOzN8qxtS0vq7m0lraCTgYA+bjmiKAhClikvh7VnuXon8J7pJOEmiYc4wM5qFOmJCwfXI+p6xz2jpe4pFek4ki+EuR17YqWUsby7ipUTQwIkDMxGv95uF4B6YgN36AreaI2Os55/aVbRkj2HBgSGQ0wZSXmZCGlnEPTpgt0pWKrXJ5KL4wsxjchej0LmJpVGpSBEZ+Zpe9xJbDUmGLwJVPVcx/0NJVerzAwk+dhOEs63y2FFHdFzRkNApDrKzFMveptr6hwTw8rlnmAxS/XqTAV5tHWVprac1b1G3ZIK43Zg8ip2TQOeFPJOKQgaO4y5MztPpQrUoNhSpDTMAN3IZn1xT8X6VIJep7qqfIayt7oJllteYgN/dww6s7IJ1vWGWzWpZbckHYO1TkYEWYfBdzMLZkeH4oaqa08ilZC7+wa02hRyXJad6J4xYUKoBD6qA8Mb9r0fENL1OhY6dqoxKbadXzYdtQdeJHocldzaNHSv7pLJIJI1tlPEabWW/Ak+IALKn9oSKnVcZzj7lgtEve9aVnDVO4dw2I6iMQS790uGaxoCspo2Gj1ZjqeWWMlLYcJ2BWva63I6TLclRu5x6zhgeNEhNWY7F27lHDHbh6iYggKVJ8ykZE/U2oWictjKpk70Zzc/iGRuluHWEM+ycw9hApLC6Yrz1Em6uWtph+JdcibbSiEndWyNdqPR9zTWhmG3kncCm2Qe5K1qHSInzo+RSsVvF//IImptuhEYsBSvaQ7cJqJZpjIpB/SH2VFyNGG6ySASsBA6n7eTrWZwftGIduTYcSOZh5ya2jZqu6xWSwfj2HC5LWUY5c1TgO+zbAXXsXlenbdFApEAg2oP871rgxvbHqFWyVk/xnd9J8J+SZqk5xtxs9wdcobQY4a+JcyeWJ1o216PRq5iPreRtkFlXzxQlnRmKd2ki3fxOssy00HcKlSVipticgtb8o72EdpVnUAdjkc1uEFX1JS74FyN11bfO1fYrW+Cfnci7QLa2jPvBFxpWIHOnnjxamJQHGUlkxdDZxfYJYsbdu/wUHIWuI2YiPZSFIerN3I21tw0dbKnbBdQEseLyxXohAjQr+f+GDinXUzBvrteFkcGiuWTsIuwBHFxTkCsLkRid8V22XVH7kLYNI19DJWJbNwt4bBxMZxZrkuNBuMuezLyrIbdnRNuW4F0d8KRH4lMxe4H1ZUKcqqhDbU5hxPTyZk6GRh3CZdXEkR00sZGh0qasN1teWqqWYyGz92mwULZMPATPNx4Pxrj7oZNZlaQN6Kyd+tE5a+rqTqrXX1OsJLBByYFI4cnn1oWq676UemRONaJ3RaF2QOyRC+nzFCYKCjklqtXNhgstwkLkSf0Nhzv930seexxmFJ9q3RwEq4d5iKZHmetA/aMNctbX19PZWV0XU1VloNSGuUf70tyiApijR69nU61joedN3vUziaH2zpLEtEJb8cvkVXqKp5yJjJSri4ehlGaO6zxdegSoa0vraNNulq0ojq4laOsNZXw4oTpuiRi5t5vztMxXoNJz51QAiELMPpfZWQo8jbmXOl0dYgEt9wVRzWUd8Lv8V2q890eSsTAUPf3ZJ+c9OwukwMmoTjCcLf0NF0mKofVQVudtlOwQfEqzHY9ot52qOI3ISdfzfxuMJKPC3obFStKohUcdkjvvjmBMsXdzcpktTUNO45mLo+Dc5MDGBLPtren+PsZ9+DlhS/s1EX2N/UCphWX2po+teTpE6aoxWGkjoOK7hOpzMYjbkFbZmoYn9/dr/FxVbqExcI41ULXMvb5C2JnBoivYH1Ea6qtuz4GFmPTXVOpdgDJ1EbrDkSJptZFIm6Y0dzR2qouS6O7p7IwXo6OF8fZeMAhuWIvhXU+xI4LMf1x4+VoMp1jLB8JIqlyrzjo3baxqetudYkkvhIIJl7ZF9aXO9ZQ4U1XIYFD6quzQsNNDOcbj7TpghTbQ6dDidyS8EFkVvTkHT0FZsvMThyvoXZj5eAHr7Jcqqj7EtJgw3W7fLm9diyVYuxSDvFpmU9imU0qr14ugiwANxw9+mwElozjGrWmoBFKipz1FczKNYIaSv2QFjsu8G07ooyjy5D+bKW16hyjiB0IH3EaJK6N1mw497JG2Jqh7lWunXXmolBgxpAF+HSJmCU/NWYGieatQBrdrM/ZZrQq97q2zK7lRx/mulHe2zxnidyU2TvN9cYKaw7J0sP39u663qxBe0DsrR13DThygM+KLznL/Lrpxa0dDN7utm/Q1frurYRhPHWn0CHgIwgZgrCmyq3gDaTGhXW4XsmQ2g69aRwRG++EinRboaIwFdqioe+erQ5z0bBbW2lANaul2WC8teWhtUWjg2N6obPiY7/jJtYltjzWJHWnj/cjebeQVqJGaM0qmO+MkXVaO1B445c1fEeSfHVCApva+q3b4k3oHp1VXw2Htdyvq1BSfM7vOpse4owNswOWd7R7wGqtJSScvHMnnQqklSVu6Etgt+b5yKH9VmW2JVUIq/JURwl+Au7VZU92meE6Ohsw2cakqbgt3dDb7QZyT2Pi0jdWotaEQIVFfSRPOnZratVulhCJLOsNrns40QB3I62jQTIO5+k2KXcWNXmdMrQakWORyRwuY66rek/R63K0DgFe8V2bYmuI97elcqToy21a7jY5WSTAbCqNl0A1o8CXVFgxqLiO1AqruWW7xlc7iI5QZcIsRwlo+u3D22/PMd/+K++NzQ9z/tueGz0f/3x9B+TxJA50r58evD79l6T86cNb5URAxucTtDptg9eDp795fvbxX3gqOxMcny9sfX3y+nzc3VjB/PbzW5S7gEA1fqmL9PGeCNhht/X8gmT9VZXfP3D8vargtADjSfWlKb44Vh2+ze8vzu9/eG70vD2fBq9njB/e3NerSl8wkvjiVeWs+uu1gtlF7/A79vbr/wV0teEqtS4AAA== -->
