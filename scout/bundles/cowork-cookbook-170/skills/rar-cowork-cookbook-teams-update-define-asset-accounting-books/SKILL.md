---
name: "rar-cowork-cookbook-teams-update-define-asset-accounting-books"
description: "Summarizes the current state of asset accounting books from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON file."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_asset_accounting_books", "rar_sha256": "4b8789499a42ba6d53da51ac248195056b376afaf7c20abb2c6c407b11ccc4d9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_asset_accounting_books`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_asset_accounting_books_agent.py` and in the RCI capsule.

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

Define asset accounting books Teams Channel Update — Summarizes the current state of asset accounting books from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON file.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-asset-accounting-books
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
    "card_filename": {
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-define-asset-accounting-books-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_asset_accounting_books_agent.py` and embedded as the fenced Python below (sha256 4b8789499a42ba6d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_asset_accounting_books_agent.py` first:

```bash
python3 teams_update_define_asset_accounting_books_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_asset_accounting_books_agent.py   # or on stdin
python3 teams_update_define_asset_accounting_books_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define asset accounting books Teams Channel Update — Summarizes the current state of asset accounting books from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON file.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-asset-accounting-books
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_asset_accounting_books',
    "version": '3.0.3',
    "display_name": 'Define asset accounting books Teams Channel Update',
    "description": 'Summarizes the current state of asset accounting books from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON file.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-asset-accounting-books',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-asset-accounting-books',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd9e29b6160427b2f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-asset-accounting-books'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-define-asset-accounting-books', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-define-asset-accounting-books-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define asset accounting books. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-asset-accounting-books-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads define asset accounting books, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of asset accounting books from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON file.', 'example_request': "Draft a Teams update on define asset accounting books for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-define-asset-accounting-books-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a drafted Teams channel update on asset accounting books status, with an Adaptive Card for triage, saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineAssetAccountingBooks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineAssetAccountingBooks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-define-asset-accounting-books-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDefineAssetAccountingBooks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WbOj1pbmX1GferBdyjyIUSIrKqLRAEKAxIzAeSPNDGIUM7j933sjKTPta9/qe6v7qeVwSsDea17fWutsfn2z2yYqqrdPb4pv5wvGTtM48quFnXuLXdEXVQK+isQB/y/cIm+q2GmboqrfPrx5fu1WcdnERT5vb7PMruLJrxdN5C/ctqr8vFnUjd34iyJY2HXtNwvbdYs2b+I8XMwk60VQFdliP+Z2Frv1AiXwxUEWF0EBJFiEcefni9QP7XQBaMXN+BCrtruZSV8s7KqJA9tt6seGyu9iv/8ENgJBEq/o84Xq21m9cCM7z/10URZ186AAFKU8G0je+YudXXmLk3I5L4I49d+BXv5gZ2Xq12+ffv7bh7cY/H779OubmwINgJ4PklrpAbX2fhDnPjUrRn3TazurBaikdh6C5eUIzJuD69KvgJAZuOX5weJ19WPtp8GHxb//e9LbVVj/9Olzvnh9Pr/N/8lt/jBnU9h143sL1y5tJ06BKd4XVNrbYw3Ubtoqr4HaNfBOHr4/d36nVJSL/5yf/fhk8h76zY+f3woggj377vPbTwtgvc9vVTv/fp+plD/+9J4WvV/9+NN3OnXr3Hy3mYkBqd+/vK5fZMHC70vjYPFFEQ+7F6/Kd+PSB8R/p9/8eYr+IvcyyZfn4h+L8sPirynP+vwnkPcZfw6g+9dkgQ3Azrf3WxHnP754VAUIKTt3/R9/+kdk3ch3kzSum3+K7s9PwpFve8BaL5P89OHhvr8tli/dvtH8x2xLEDD/iiZg+Vd23wz1j2g/PPt3pFMQuvU3X/4lub/asPzPxc//ULf/asOHRfD5be+nIOcq20n9T4tfHyHy8w/e95s//O03QPr/SEYp2sp9UPiS2Xkc+HXz5cvPP9SP2z/87ecf2hJEMUjUL22V/hXNv7Lrg88fLPha9eMf9wL+Wp7kM7x8y6HFr0X5P6rf3he6ncbe9/v1p8XvM3H+LBezEl+ZPk3wu2ysgay/s+NPb78BCMqBNq37eAzw49/+bSHEblXURdAsFIA7zaKasSfzZ+HVKK4X8ROEASL6VR0Dw77WgfifPTxLDCD5l//pPhD+o/tCeKiZwe1L+0C3L94D3r48gPvLd+D+8gDuX94XKuBQVHEY5wCfZUoUP+d2OGM+4F5Wfu1XHUAsZ2z8jyCxP84/FnG++OWfZ/LlQe+9HH95wHb8xEJ5x844WLcArmeNjQhUiad+LkB2f/DdFrBKCxfINYN6/QFYoi5SgPbNbJ06idN04cUAaUApexYVYMFPM7FffvnFsevoc/4EbnTxrHE1BBZ8E2fx8SNQMEjjMGo+574bFYsffv3th8X/WvxXux7EZx4i0PblHyDho/aAfGszsAy4DjgbgMnDP7/+9jIzIJODogy8GQfxq8KCeE1876vNlSP1EcGJheMDWwM7Z2VRPcps3Lwv2GDxTV7AdH4014toroeeX/q55+fuCKjaQJ1vlswLUL5BUNbB+GHR1v6D6y9OZT9EzEDi280vC2EngupUpOCfWcxn8bfzIo+B+b9FxPM+IFL9UC+2X0m8L85zhC5Ku7LLqLJfPOaSPvtlbgJe2wFxe5H7/ed8rsf+bKpHujzNAxYBy7gvl36cfQ6aFdCP5F79lfdjjT3XUPVRS6vPef1KBbuaXeGC0gCYhm3szQXiP14hVUdFm3oP+wFJZ0ovL3gvrzxi8NkK/KMm59mG7F5tyLN5WHxukRWMLf4/6ZtmI1AMIx8YSj3sF4ezKptP58xd46zRs9GchZmZPhLxezfzFbG+AvfnPI1BpFXjfzxXPlz6WvMEw7YCHpAp+UEfxBNwzkz3Ee5z+FbVnCj25/xrhfgAFHzAIfA4wAaQO3PIfmU4P/0qaQQAYL7+3i08wqOaDTAn3KJsnRSEW+D7nmO7CZCqmlP25VEQ+w/P9VHsRn/QavYGCDFAfwGEiIH9gbHfv6H28+lX0f+w8dkUzVseDWMLMrZ6EABy+LOAs3v6uAHAZTfPJh3o+elBBKiRlc2suwNyBmj6vOlX/r2N67iZ8fFpV78EKP1x/n5qOt/1hxKkCTAWSIayBdZ9pM8ciBloeYAMAEFANmVxDloAYJSXER4E7WzGAoC1rx71SfFx+6WQ/8i5uXZ93TgrMu+Z24FnlNv5+HvIUP8qTAC9bF7x4Pv3kfaN20x7hs0aQB/g+PXps294f5b+Z2+x+Er305+moB//tUHpUcy1PwbAp0XUNGX9CYKeBfhr/X0HoAU9Za2ftfjjs0x+fJbJjw8w+PgdDD4+wOAPHJ7Kf1r8a1L+gcQrSz4t4PfV+2p+xL+i7PUBRtl93Jofsfnp51z2v4MrYF9kIMxmF46g+H+rhF+XgHIYVgCawOJnZazngtqDGv4oBcAfn/Pfh/2cdjMQhXOY1sXv4ODREoAUeLrvW8UCj/IG8PbmpjJ8THSPJKn9t095m6Yf3gBo+v/CJDdXp2yO8XqeA0E2gV6tif3HFUhW78sszZPmr383FNOvJ99C7buh/gykHxb+e/i++Of9/hFZIcTHFf4RwT7OgrzfalARgcTNWM4KPufBuYN8INvQ/FnAy+OHnb4v9j5A0bT+fbq8St9c+n+X1U+fAF+4wBAfFrOY9VyqgRVmG82IYNfJo7T8pSyPuvTlWZf+LNB+LmV/KF0ApOuvNfJlIk0R6L+k/a2N/jNhA3QrMy2v+DQX7g8vWATfYPT5sPg2xQCNXnPl428BeQtG9p/nCWqOhMeW+QfYA76+bfr21xDHf/vbn+QCgj2wFlSsmdZ3Ib8vLR6T16wCIN08/1Dw6xuIOhvY137F3at1B8sBNH2s5/YEAikKmIPrZzKBZ/8XTf2LUh3ZoJUEpDBns96QGEnaGOLYhIejno3DtotgG5jEVzjhoGvCDuxg7SIr23EQl3Cx1dqBYdd1MY8E9J7J+WXuxuJZOpxcByuSRAIMRlYekAbBPG9DbAgXXwMapGPjDk7azvetSZx7L5WfKs72/DZfzKZ5af7rm0NgYOURq1nq+dlBJOxA5toZqit0XW0Gy6QVO75yroq1XOPRa3q1dpmlx9BYLjuUTmwPeFLGqcJae/+OrA2OEldKUCfkFFxUcUNzundZxc6QRrfTlc+mUz4t1Sa3IvTIWEjlWVLBOroRWdttcrJOB0Vzaq1SuRH1OT5XsayvkpVKY01dp6ymQFB1FDc63XrdSRQLqNSMQVfYYgP3aeRR9F67XYdl3GxQKZ86/4QejC1dksuNk2Jkd9cNzscThlU7/XKKzzozhNyqyNjO2rIc70EyC2p5ckzkytAl+0RId9SX2xQP2SjGd41YDUfWMRhi0reeIClOrCjxRHUqnbnDfmP5vLPGDGKMDDS7rXCu7a43aE3UmWMtgxjxvO6aQ12s+qt8kkp7vxx53irV+yQltYZQeWaNuqat1iLr8GvBO9E3Qj+41ZWz1sPSCh2ZOkvSfrxThTsYHLwifQFNTrXvCee42GxslsLUUaxpDUfqJDHixlN5BvfG6qpJd7wUDroVeWUnj2QV3FylQtI1nPlSEY47WU0OhIQ7KuZi1wyP72eqOmmcPnEYlSzDA89mySRHNx3uCmTvIBJZst5GdaQDw9ahJxUOizb7duJbDt9gq2o7pHFsF/5+pVsyd885f7/VjDrRubZA2DWQTpaJduwp86pS4ma95nbnClFkU2qywr3r09JITIwrbc/I47tTBea0rGGnZIN7YNs7Kjlx48hWrCehd0+ug31tHW6bWGevnAcfFOx6pFrEi93QP49TyODkVi6SANbWtb41HYQKewsbg6XtDK7knuvVjbdikFM6dWe82j4sU3Nr3Gq7P3TI2i79WLsdNel0RWzLrK73ajWx4kiPdHvZicWdIw5MUHpWGWC6R8galg2Ry9HdRl+yLXLYD/Ka2kQ1ctyW68wPLzZ6NVfdwJuFUCHm1F985hzh13Lf4oUliwrEIoaZRphsjTSdDCkG2SAAhnQdXOttHewOy5vgIlu/lnYQcyI323W496BGt1JodQit9SVHN5tlv+lke63L7v580gsmXQ1IHd8UlCZacnU4+JZp+PrqvGm9PNntN+aN3UhRYI9i0O+q9aEgjKPW5MeRLwqYmU5cDnr3vLL2ZEastun5lETKcLCXCpW0x91BxbdNuTocyWOXLvF2ueSH5SmTT03v8Tu6VUMe86VxRBxhivq1d3cyUeGKPu1QhbhEhq3FxeAEd0FD7Y62+Ctxo0tIx9JS0e/bw1q/sORZvPvyreRP1rqDq3s/nWlVSyzNa/QgNvCCvHuCkfsI5VqeakDJtj0jltemrJROTNcRk5pll+gSOfX9bCttY0ISc6FQUT3LyY2AGw0NLJPCMqWFlCOsXIkKty1ZQuhzZB0CmexXNRpjslHmRMJl3aYePKPGdrfzMllaawQuS9WF8BunJOIyMRJfXPYlEwJVt8QEAxXI8jqqnY05HBKt+ohTpK0WuqS3xhIWX3Yli+0wNLscg9LZ2NXFPuGYTQoeGdo5R+K7PbRbikK3RZnDJcw3S7Nd0jxcxhdyHwMXcxOaqGy13zmUc9wROGUk9lA4yb2Y4mS/jWIP03PIOnvMpneCyWA01hXF41JNkcru9uINMiO/VZHAk6Cjrq6vNb7cJobmrzaUSjk1ebc4sVqeRwkS2+NGO47eSC4LP483DG0kDIeh+PogCJzjy3oUEFsSxdO8CGxKwULPEgjUKFZSZY2HKxlkG9llFdiczpnli3ey353iinfHM0T7WimH+u5s3xkrrg+sXd8zMhCPjADdxD42U8rJhIgemt5drm6oy2JInK16ATtrPWGcnYztDWxHyYfWXLpKq6SRvJFsY7oGkrpW65OZyZpUDjrSrValP+jjdWo1fNxKOsdt4QYx4Jtndvo4NDctxgST6cXUGoYqu0+RB5B6NwUQgbWTBQ+ByIlOsksOd+l2c4Nh0PcFPwbWPWl7gaNIkyVwcbKrCQ1XJtUxqCWp/jI5MHQASyK0vhFYKXTHfEI2R9LYk4FRtX1S9mtLFM9kL9uHDeVYWtRT5w2ZVluNRoyYvBXsyHdOi92oeIC3qmNtlq3AmVG/8YMbvQ5PpGgLSluKShF45TZGekbEcMzfXmkLu8UCVsWnlJambj/RVAlzbmBu94dqlWY6e7Kb0FL4WzE6Ht4bGeEk9WkZeK2W3vFbPXFLJfZa/pJhU3mOcvzINRDtrIPR5nlnZWOXZs+GdWGHkXxd6YO6bUlXEgueRPD8hBx2U9b4IpkTBn491Tvu3B4AQgj7ScDvmA754Z6+lITE2kJ4pAm6S9ibBWeph2preiezAOiHW7D1zyf7Zh6ZCSPDVEkdVTzdroFeZLodqWHbnzCb848gfXfUXdpRWJdrNsEbEuWctWM8DLx+OGtLbVBE3Si91IyKkF+dIpVp6Ng5Ya1HcH0d1gTHiaeWPVL2gdzrVFJfutDa07vhyAthhgCA3pwOV38kWHMlZjEnCAUdCJy6QemtKjvszrbujW4gXuCcL064rSCGKk1lmPDdJkH1TmcV6BAPRXs7D9keVS9UT4kkAfRgRkp3MkivfJX2/SGXV0fZE7YxmLy0+lDYxNGEGZavwta2hDOt07tlzNonP/UVxl/dhZxklAQNXQ4AZsqU9rC8FU1eX5ge8fBbxZ04OaXPW8HwgnG3kbpARjNey051nG12h/QySCh2y/BiZS6TYB/QxfZSXJb5FavLO0t5+tERClPFgYyg7ut7FTRk94onIMXdL9d5daECVdicyQ4ZtueoXiWsmxpWYHhi4eIYtjkLzGiEOL3c+LmFENYtmjpWlq4Tv9wNwEUDDK+o0auyRrIviG2EvFOGiQBmC+lEESy5yyOs1AWtXsNFza76Xa1d9Z1GVNnOajdnhG3vp2iyJGxjuBqcLfOolPpRtWUSdiskRnByAw0ojbjdXd7u7L2J53l9ZNReyE7+vZR7RoUUQubGa067cBImNrIvcEe73brpQFGt1l/ODO/nFwSCOfRoUih3qqg6Y+9Gli+NwzIUr5FQIO1uFVVttt5D3QSLIXo6Rhk+kd5EpUHq+F1zLmp8WoksFtZsCg+0TsVSQO0bLhVghW88DULXF25LJ/e4RJRDSqkNutvhh/AuaxZLyAPr6vAaAKR+Sm48nrghNkWHsUssXilxyJo6C2GAve/ueNca6HiAPNGddrvjhADsxzt5VQyTT7tGKVM8ilI4n53FfNv1yBLkjrQz7sdM4pZ1lilZQe36fcyY95iqMTXBlCj1KuKOnwL3mp4ViG6c2znkJZ9BLrl08DYwrOX9ZT0gWHudJpiLSqNKRFkIDHS14rLecAc4CIbLcNfAXEFdroJ5H3AAFWoH6/d819j6cpunVoWf4gN8ocdgtUnK23aKZJTbCxGPivgWoKQmktk2Yw6Wu/N2cupOBmjOkdHZCceLlG/bS2VKmszXjJpex/MK3XZucL7090g+8KdBMDO0rQ7MEQ8QGWtjIeTl7hp2xBJWZIvNr9KaP044a64rHZ7YprXOkQmjdMGpkNGLTIFIPMMWzOU0JvBK8neCyoQQvAttHUYSxdDFPeLZmpLInNDKhOaRuzLUqL49OY5qDR2olAcv7k6Fa6sXXCSP+fXKJzbo0KE1TvSWlvQaY8qHaB0m5Jm3CH5kCysw+W1Rb7PBCt1DXuF8yl/7Rj3m+3Ak7m5SHYqrnmf+ITRXZrY7HSAhrMl6bzFw2rE2qm2DS3aw853j3nYM7bh+n1wv8ZgFhzucRQJlrlaUMiBjHLIUYTuqPWCBXoY5buIm22cOojrBSmPLy3m1FSo/iyGfz4dK41xtF1gue5qG6hwIpkIKSF+5uohBBWv2ocwYkZvcde54cnoDrsJKE9sldRHyFGWy/XCFqwGSNxEJY5I1GoUDplbn5FDySSHDY9OXine49lFRIoh9KdL6cK1WpCMQXbcvZGM8S0tLHkDn46PSFTRK2xFrpEnna5gXxTyo4EExrrRgwDAckmSgbW2n4HPPqo49lxYVTFhTDrILFLv9YB6w+IR3xQDqpiA3jH9vLkpQUHmRVkcFuyPMMt5ydqHKuX2A2KNFr6R7uz2dUG+yveK2xKEdPxj7q7aFFRxjDG4dS+oloW8UPLB0Rogr6xgAaeFQ6SkaSYELwpEp93swYiW7G4hFQljR8OXej+xIJX2PHNSrae6KqBwJ78QcGrukt9vprtz2/s6MrFYIIvOM8oo/3I6pPoSZ5+QEFdzY2/LKcc2Bgr11eacQn8PwpXSRNfPU3LOjnu1LVBA8TdUaWzVST1T0663MbCRy9jcAQLexO5VXb28fYFQmxfO6khlxv8QYbokbkYe0VQOvBT++3KJrcMZRpdtX5B32TS+FULVd2ydsvKJWwEP1dFHADGm2jRcM2PWCKlh1a45sp6/vxb4U9udUVDu1Hw4HJtX9bHuJepwv6eGyu6eVT4tQ3Wqw7rn7dILhdH/dqxyYjcykMA2Oam+mX0AYTJxGyixBBQd1A4mGe6HbdsyDbu8M13XWj3bKtyLvqGv+jF2Mk0vG0oQ3/NGXzkvBmM4dA7u1cO03G7VsnWpsCcJWE2OFQW0bQJudiHAFxuKIVUEbXSSQ0Eouo6Oc/avbbAq4296cqVVaBLgnXHvx2MfC2Yz2hLm+0ZCUrqwLjxosHFQ7ZpCQJpTIabvZn1i1zoNjdo2TCek3hDbycOZkWLKn8fZ+8dXuLvrDgRjhnh/kO5lpuDMdj5wZmgICmUurh052hgk2Sl/vuI2W3NbaH0PotPSgqqxKvDoYRoPvsCCyHa+Jsgm77KyyE+4yHy35cWlIJIPuV6ji5Bcj5kcwfnTxcD/qK26f2uKq5EAjfh+QaZ8MiQeZm4ixqNgP9r2BBEqKryx0YNWtybVwaB9oXehiRqXzNK+QrMR9JdIEAldCG8x4GXq8XaZ2IKZxO063hGWCzEt4C0tsIueb3ZHZHx1GobmcTWgQVwlABcPrTAtA2zY0e0iJjRXkHsTd5O3OEy9M2kEt8I2JNJxKLWUmVPO1hNxOaH9UpFtsiM5FGl2KSIm108cjo5/EAF8v/f22x3wfxxORFoerJnO2lUfGWlv15lFi4rN2rhDhgnc6ZogA+oO0u8CKznV3dmIJyGN3a512+rOWq7EBleuUrQcNDnF5XF2FUfBODt+kR6OBhcuK3vg9PxI7ofSZNPGzti04/OJMtxHde0mBFVNASo6JDDQGRsrTnYCo5epCoLUCu6TlBpfrPtGMpvZtidr0eGfkt7L2AhWJYcip6zNxKm+xvdZaqYf3dxZDtytEPa6WrUFluruNjxR0NRqvOZrCbtxC5BFnC0R2D3gqyLmLjXemuMZK5GebaueIu73fb8sGddegNdoTFlwhh5bI8oaYzByHDZRbXUWxnqaeSMkpQoh8yw4bqAqbm4hm91zsTTjr2m2xr1e+cFUbokKWrSK2XYffncHkieIqn430rqIp6acTmD9G4qh0CZejR0G6GiHnl03n9QbqpVsCvQsMr7kcDG+jXE68G7XxLytPZXAPv2IcS9ydG7nxT1x3OMR6uSsP53KXbIFVxOXZCJGtBtRcEyR21YJpdNmDXnOJeasTtBxviigXy73A46VxKTS2h8D4QhDdcAo5mrnlsumUVe7a03iJgvO6pmSZ5ALLoeFzh8utn2kjR6CchyG9yqKal/kwrQ3ZlYT1NQ2GPghZHZYUABhPakZ5x6V11A5tTy1hTvLiNXMghLtY49KZE3GC1KolJpAlIlQQx6mwaevtWlkLYsOv3PIyOOyGy0DXnPhH0Wnuq5U5Dl3lyJUJG80GCg7cXb/VZ5Pkj+fk2hOOYXgSgkhZQjB06DIe652z/Fht6eF6ul5IycDvbAaN48UsD6anKKN+xJANt7z6O+fYM2SIcEO5Jy/U3liJO5PGCVCcsLt9b1RIYtaVtKm5/nbGcHyvXjK5kQdiXXdGg4bp2IGxM97zOcm6JHyJfIxuSfGi+iI2Mrdg6Qr31j5r3sEqYjgU5S1ebEVmm60uXYquUaiBWMSGROmooZK3liyNvzU5JQWOE0P6hWTxDpRa3+Y6/qRuMaIh2mC9XQlJOqnHiyir67DFrGGiYarJL/Vxz48nCi6S7to29123ltee0HFgot70jAKv0yNPkATozKCQHJXTUev3kZvtbjaOqsuLf755iYruKmw6FscQDGwi21MlHeaGENvbJZlHJnXki8k/pmyTrdBq08/QdmMHd6m3+XDWE3PqyvY83KQbxly8oo3WKb0x6B1pYkagp0xwqnBkKtu1cEB1xMEKrwiWlzroPSgfPcjCusSBhmK3lqFsvxuIcwa5p+zojC0NOSfdPdGaB6/gyi3Paee2t/YypEczENygcehLC9/h8L5h/L7O8Ov6ZjSTrPL77sBv4EmpeZmYpMuEdtOSMgO7roZ402rV9U6s02vqQZRyTwTBPQVn+ZrYFAVz5Ma4u6cy5OINLV0lnXCvjVj2DsK3ub0hNtvdtiBUyY1yAQmvCW+HxOW2VIKEjZkhx1f0OKB7mXLQaMh6tL9dyXZ5pLfpvhAcArfIqaJDSBFPuKamFGG0wnmdgVqUXf3Thm1UmCtiPGq3NzVN+HpTMV2boiTEBHQpX9aUYU1LZesQRQIzsU86ZcAEFLsGiNKEWGoMRbpu6+Boj/4NoqwlL7QrRZIo6u3D2/cTyrf/xttX81nM/7MjoefpzdcXKx5na77tfXrw+vTfEe5vH94qNwaiPY/C6rQNX8dFf3cQ9vGfP1md6YzPl5y+npw+j44bO5zfC36Lc6+tm2r8Uhfp41ULsMNp6/kVwnp+y9QF378/MPy9YuDSdh/HgV+a4osX12VRzzfjfH6Pwvfi55r5MnwdFH54816v+nxBCfyLX5Wz2q9zeqAt+r56R99++99h9Ktpzi0AAA== -->
