---
name: "rar-cowork-cookbook-teams-update-update-access-to-systems"
description: "Summarizes update-access-to-systems status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_update_access_to_systems", "rar_sha256": "c0727a7f0481b89a8d8ae569e8a1ad6bcaa1cc9342f9ef587e321606de24a517", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_update_access_to_systems`. The original RAPP
agent is preserved byte-for-byte in `teams_update_update_access_to_systems_agent.py` and in the RCI capsule.

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

Update access to systems Teams Channel Update — Summarizes update-access-to-systems status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-access-to-systems
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-update-access-to-systems-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_update_access_to_systems_agent.py` and embedded as the fenced Python below (sha256 c0727a7f0481b89a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_update_access_to_systems_agent.py` first:

```bash
python3 teams_update_update_access_to_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_update_access_to_systems_agent.py   # or on stdin
python3 teams_update_update_access_to_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update access to systems Teams Channel Update — Summarizes update-access-to-systems status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-access-to-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_update_access_to_systems',
    "version": '3.0.3',
    "display_name": 'Update access to systems Teams Channel Update',
    "description": 'Summarizes update-access-to-systems status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-update-access-to-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-update-access-to-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '52037b978e7a59a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/update-access-to-systems'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-update-access-to-systems', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-update-access-to-systems-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of update access to systems. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-update-access-to-systems-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads update access to systems, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes update-access-to-systems status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted.', 'example_request': "Draft a Teams post and Adaptive Card on update access to systems status for USMF from D365 — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-update-access-to-systems-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams channel update on update-access-to-systems status from D365 F&SCM, with an Adaptive Card for triage.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateUpdateAccessToSystems(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateUpdateAccessToSystems'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-update-access-to-systems-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateUpdateAccessToSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abeiyLrmX7H3/VBV18wNMmreddZqEEUEmUGw8qwsJpkHmQSq6793oGZm1ak6t8/p1Z/azL1ViHjiHZ/3jR38+uZ0bVTWb5/etMApFqyTZXEU1Aun8Bfb8l7WKXgrUxf8LLyyaOvY7dqybt4+vPlB49Vx1cZlMU/v8typ4yloFl3lO23w0fG8oGk+tuXHZmzaIG8WTeu0XbO41mW+aKNgwYyFk8des0AJfLFT5UWVdWFcLK4lEGARxn1QLLIgdLJFULRxOz6kqoO2q4sGDADrpX55LxZ64AB0L3KKIsgWVdm0MxIYUiwo3wES9sFi69T+4qhJ4uIaZ8GicfrAfyxUB30c3D8sirJ9TA38d6BcMDh5lQXN26ef//7hLQaf3z79+uZlTgMuvT0WNB5qPn9TD131UntqCgAypwjByGoE5i3A9yqowWo5uOQH18Xr249NkF0/LP7zP9O7U4fNT58+F4vX6/Pb/E/tioel2tKZJVt4TuW4cQZs8b6gsrszNr+zRwO8U4Tvz5nfkcpq8bf53o/PRd7DoP3x81sJRHBm331++2kBzPD5re7mz+8zSvXjT+9ZeQ/qH3/6jtN0bhJ47QwGpH7/8vr+ggUDvw+Nr4svmrzbvtaqAy+uAgD+O/3m11P0F9zLJF+eg38sqw+Lv0ae9fkbkPcZfy7A/WtYYAMw8+09KePix9cadQliyim84Mef/hmsFwVemsVN+y/h/vwEjgLHB9Z6meSnDw/3/X2xfOn2DfOfL1uBgPl3NAHDvy73zVD/DPvh2X+AzuICpOpXX/4l3F9NWP5t8fM/1e2/m/Bhcf38xgQZyMXacbPg0+LXR4j8/IP//eIPf/8NQP8fYbSyq70HwpfcKeJr0LRfvvz8Q/O4/MPff/6hq0AUgxz90tXZX2H+lV0f6/zBgq9RP/5xLljfKNJi5p1vObT4taz+R/3b+8J0stj/fr35tPh9Js6v5WJW4uuiTxP8LhsbIOvv7PjT22+AfQqgTec9bgP++I//WJxiry6b8touNK/s2gVwcBvnwSy8HsXNAvyfWQNQW1A3MTDsaxyI/9nDs8TldfHL//QeDP/RezE81M689uXJ31/fnjT+pS2/vGj8l/eFDsDLOgZcDbhZpWT5c+GEgKPnhas6aIJ6Zld3BFUA5PTH+cMC8Pov/xL+lwfUezX+8uD7+MmA6pab2a/psuB91vMcgeLw1MoDPB8MgdeBVbLSAyLNFN98APo3ZQa4v51t0qRxli38GPALKGCvWtIVn2awX375xXWa6HPxpGt08axsDQQGfBNn8fEj0O2axWHUfi4CLyoXP/z62w+L/7X472Y9wOc1ZFA6Xl4BEj4qEciyLgfDgMOAiwGFPLzy628vCwOYApRi4MP4GgfPySBK08D/am7tQH1EcGLhBsDMwMR5VdYtqAGLuH1fcNfFN3nBovOtuUpEc3n0gyoo/KDwRoDqAHW+WXIugw0IxeY6flh0TfBY9Re3dh4i5iDdnfaXxWkrg5pUZuDXLOZjEJhcFjEw/7dgeF4HIPUPzYL+CvG+EOe4XFRO7VRR7bzWuDpPv8y1/zUdgDuLIrh/LuYCHMymeiTJ0zxgELCM93Lpx0dZ90rQhRR+83Xtxxhnrpz6o4LWn4vmlQBOPbvCAwUBLBp2sT+Xhf96hVQTlV3mP+wHJJ2RXl7wX155xOCz9i+eETyb4muj82xItq+G5DXsc4fAK2zx/1OjNBuBYll1x1L6jlnsRF21n86Ze8XZic/2chZphngk4vce5itPfaXrz0UWg0irx/96jnwI8BrzpMCuBsKolPrAB/EEnDPjPsJ9Dt+6nhPF+Vx8rQsfgPoPEgQeB9wAcmf209cF57tfJY0AAczfv/cIj/AAxgDGBCG9qDo3A+F2DQLfdbwUSFXPKftyK4j9YE7fexR70R+0mn0CQgzgL4AQMUhC4Ir3b1z9vPtV9D9MfLZC85RHm9iBjK0fAECOYBZwdvM9bgFxOe2zNQd6fnqAADXyqp11d0HOAE2fF4M6uHVxE7czPz7tGlSAoD/O709N56vBUIE0AcYCyVB1wLqP9JmZJQeNDpABMAjIpjwuQOEHRnkZ4QHo5DMXAK59BeAT8XH5pVDwyLm5Yn2dOCsyz5mbgGfYO8X4e8rQ/ypMAF4+j3is+4+R9m21GXumzQZQH1jx691nt/D+LPjPjmLxFffTn/Y+P/5726NHCTf+GACfFlHbVs0nCHqW3a9V9x2QFvSUtXlW4I8vYvhn/PAH8Kfenxb/noB/gHglyKfF6h1+h+dbwivAXi9gj+1H2v6IzXc/F2rwnVfB8mUOImz23ghK/rci+HUIqIRhDbgJDH4WxWaupXdQvh9VALjic/H7iJ8zbmaocI7QpvwdEzy6ARD9T899K1bgVtGCtf25iwyDeff2yI8mePtUdFn24Q2QZ/Cv7drmmpTPkd3M2z2QQ6Ava+Pg8Q2kqP9lFuQJ9+s/bID3rzvfAuzPjPphEbyH74t/yccfERghPsL4RwT7OK/8njSg8AER27GalXlu9ub28EFgQ/tniaTHByd7XzABIMus+X1WvCrcXOF/l7xP+wO7e0DzD4tZtGauyEDt2Shz4jsNyCSg41/K8ihCX55F6M8CMXP5+kOdmmvm13r4so6hnfZ/if2tR/4z8Bk0JTOWX36a6/OHF/uBd7Cv+bD4tkUBGr02jY89ftGB/fjP8/Zodv1jyvwBzAFv3yZ9+1OHG7z9/U9yAcEelAoK04z1XcjvQ8vHtmpWAUC3z78C/PoGwswB9nVegfbqy8FwwEAfm7kLgUA6gsXB92figHv/dx37C6SJHNAsAhQPJhHSIa8wtl65642z9tdOgBObYO2sHJ9wPcdZed4GxZDrJrjiazJAkRUBE36AYA6+IgHeMwe/zP1WPAuGbwDcZoNcsRUC+35wRTDfXxNrwsNJBHY2roO7+MZxv09N48J/afvUbjblt83DbJWX0r++uQQGRh6whqOery20WbkEKrijcFhORGCHK8VPw/QoFc463zCHauOcyS1aDHvCxH3UyBo+jtZbpaANzmZY6qIS5q3nlMDj1ppLdqx5P2o1j4qVv0JU+zjJOryRrbqoDkVgiz28YnKtCUPj5HAyvc9dlF+dlryf9gl02fbJeWdtmWtPWtA6n8re13OXgHBDpfWljzSFLh/zcwrD3XrNc/7FbVQBN7FCuY44LCWHBB7O8oB1yEXjxbhEpEFPuGgwLpAhsNxqd2GV5oxPvb8dbgfO3ONp4+2o+uBdjlkw2GN11/nzcbRTLWr0+Kwl+oHTd7E3bNfedXI3BNfahHGSeWZb5JF+QBUiL2Ms1oubVsM0JhYWCm02jWVNG2Ij0UaP1gO5JOEeLQ9Xjssmb3tM0/NST+gwpvrsbKPsZazOEkHnSzhw+JWkXFi63QWVdXRlaMd0uomq1ImnhIauxvX16pxHo/Fv2HQk2rtVo5wyJZxYejWtNxeiNu7Lu29Dt9NU0uLxGKb9KSoFHg+idgz8cx6vNjp52pWVOpQC43LcLuROIV2AWqdRYAdgalja7LKA4vepaFyO5E4bzcpzrfPdDZCDfzy0sWtT1FQfEqKxuaI9dKTcaxXuwuR21CNTNMQ9wZUlZtKZTN87/ryVM6vL1hJO46COmOlZYjzCpqHCr/SqDUZzSGLIicZWkyPdJkzEjXG+0IhzCVWX5Vq1bqV8s2/h/rI3OrWiHHapEfrRd0casvVdco/Muub9JDECmhzIY3xBYSE+la0Q062pt4Oxj3p7y+xTmZPxqt8P9B2ZklNLCPiQGVp36XUnqvfOdlXe2fVFDLpbdeZ8Xk+0UUK2pl2j+C0dKW6PKO0wRZu9ZhmdXvH1Ueh3yVIdI2sT+zwZMtmSkUlkj3FZ7N/jC6M0y9G726KwaR303rVFHuR91ux7Znc/oVOIKGiDjc7ZIDrpYKjYPgwdkUcAiwg6IvWad8Dv2bReFVAor7euPOWMV6zDGJer9XJZ9GtZuJvdyrhSd01x6Opy8hnuZoAaVPc6TVet7E2nMtLI4nLhQojlRjnlhAGeVh51Ww48n4Uwo/ZefOeVqBtV/ARDRwRRiEu3V+w61gqHFUbeG+8+l9IZOyaasgx94Rhk1bi0sFuOHVoql2mxsbUisA7xRRdPVTPJTFIjx6u94W49jSyPpjnVupG0FgffbjHE7lZNM+qVL3Pwfj80sbpNRkZUl9ZkHBs47dusAwUZtwM+FritH/brNDmynWHWkzuSOikUXoF14t2ZBMwmmLC1VwVepWWYYBYVR7d+yzErylNi7rjNiEt+Sq7n8pbXpACfbDi7sHGKq2KekWUu8f62sJLl3e5R7Ral0E47ZcRNoOHucDjRQ77U3B3kOuuxyuXlkB4VKiOzs0AJu8iEVQxO8VASV1UzaIO6KTOs5097fu/T1EGjaxiVO949jEia2odVv1uLkArsNvEXF8fIQfBPrX7vrvfNnrKKccOdUHqVH8ik2KGXoOO5pA1P7RQh4nCczJ3C1Tp/vXdLSqv4syScVmbpSIqXLW3CsjoJ8tPp7k6rDGlPpq5Sa+h6sc/OSoKaJW9ItUM7QtKsD/srYXkBG6T2+WwojHsvzMnIs+vRZq+pPpHRGQrGwuuvFPBBEohqHcW2uPEGhtmyUmaeXLLo/Z1CbFYFTFAUnByrkxpJarmsS5vr8k3LxYS6D6YU3ylraIWHO303nvHiwm3XVcBs+Z0CGyfStTmquNz3BBR0vttLfphWPHXe25iylKnppgnuPdFZ3tUpXTEFprJXsRFF17BhNG/txWd1r+CdwmvqGfKONVNKHGJayjE6IzKMjHq6JccGXSfoLlpxsCHH9/JKiWa8OddszCCCP5TnDQIn/A4BFjUTaSsLJ6jXK3wduGvaPns6UNgJ9S0U+CoO7CGPl6FJuhBmJa5hQpxfX0l5SHb9pWMPrpZso8LAME8+FAi+bCSrX/nXsfGhdL/GOpTX+21lr9ejLJmNEkZVqm0w2c1IftzGfG3dNqt0p3KaKzF3caAZ09zU6c5E5YFOQs9F7f0u3m2P6CHg2GA64LtbCNmGYrW84nc5nZLTWTnumTivV9uclkF53do9e95V1ID5W09nT6OclYSr3HMnUxXjwPmWaxRD0FwmHrlcMi6qEOpEjAdc7gyIJ1T0VobpqVprBERI7lB41G5DobmjDat9Kx1qW6HMY91E1WgM0Sk6C5yn52tte2rPR1tpQuSwMoM6xg7NjdqNRUWfKoeLz3vt3rIkf+nMTS+q4rBVIlmQYcDdZkyNLeOkgUk61s5I1mQqxZAImb6X3pkL7lEraSNa+NLQRlqnTBJErpcX1Hky6DK9blcKZErNfXcQUjOhtjRdhqc4kW5CJtbXiGwvBp7us0CtCPFYejRnnfaBpA/Omo7XRrVrypipndOBgXOFNDmfOnc+Dp/L3bSrU189FVTAhXZ0bNNqZV4tUyxTrDuxfWNvk0FgZUCI/sVZGhOVmnUcEc14xmRVBmG/hfKLE3OWQK86i9Ay4rTa4zVb3Rpv7aRHZ3kGLZMkYjJN7fRCFoNz5DqGc6Lc0vKrtLNiSV8RarpmiVwK010VHJGdetP9I5Qc6fBAqADezI9HU2VWkdWce4NH915YWIoM35vGQO42mLJlodRgRYI8wBHmYiIl7Okexq77TBo4ZuSmS5Y415NgGcxlK9x2YbsHHrQ0N75azcq+7xoSeMrdNMaEucfj9nDMztaqYIgDH/Ayo/NtYuxvQUHCWHdlGo+FhojfQjY6OgMfY0jehKyyxBODTdq0KLf5aB+ZI3lLt4oUH5QKW4+mvhekjSNsjyeq3u+m0HGMSeWQwIIoa0/tRVy5GKxygbMxj7BmbAU92txGlQyu7am7Zld8ee23uCD42H1zr7SAjhWhMiNWGQNCOB+l7RonLypPnTZ3pGLYK3KiabYKPVbIV8HF60Fbe7rTvbGN6YthGjdfWKdqxgTQ1j633q6kUE9EXOiKLh36BBoaEc2IKt/zpIxuZMc9H1d5KZnTklOFOrGiK87JIQ2kLW4VZ/o6hE4ST7V3oztQOlxuvfxmWVy48xyL226Bb0av81ZeV6/L09ILc5bXhKO73+qp4wZdujQ3DS4wcKH0qWtt7vXNgK9ykWDDVaexZcGg8KoSFBvpKfigIYnoksk6q3a9HqOO6zqXUA75DLR/yd6wJvEiKkeOvjA7tWW4Ndhhq/cSFltvmXa6BtMmwcfI0iKRcNPW+Fk1SDGshdHf9OSmn1YavtGsZeoet7irZT3dYlWV5a25LZaKEewUqVboVI9aSe7C6OZe+MqQLQ+53rPcZ+F8iJ1YwTnb17xxe1FKOONuSuQWvLI2HOPo59uc3akGI+ntSosS1BYjdmvbVogKl5RzOAxhREO4HQg4q+1+s9VGfNgL4ug0frxkceMwQusJ2+z83TlSl4MAbwg4Gn3yjB93rns7I5OdNZcVsC59ovYnuLwNwg3TcMRzVB83TySlV/uWHo4mm8fJ1ckvDEr2uavepHuaGK0ehCGnsyZT0vep7a/w9kiVVIepZxK9qH1s5aMft3R5JXRFlDeQHi21pTnqDDS15KCAlmhNUIdzSq557RgiiOMePfVYJIK3BNuXUyiWNtq3Qqm14ZRDR1prRjWnFTyKCf+4ukqjFztL5eygNO46Yx6KB2KH5PqZE0S/rk/SQNm5ObAYeVneHesE2tHr7jZlalPYQ5OKaECOUpkhdyQNhJVj7zdGrlI8dlmnW3SZcDQ7bgwuIBHUggZ/KRLAwFlMMtlhJ4mghcmYIruQhdbBrn2AqGW5Y++YutTpSwTC/IxSjFDZJXsXOUXge2Zs7ClcpW0LVtUOwVGjnVzYyvZ5t7vdJBbAUGKmTh3Ojk6BTw5oDasDchPWp84Jp3sn8TZzji4RVZrmmc0T7Go6IFiVVX8xC9TDtGWXwC19XpKatoUrOq7O+cHnVVU+u0p8Ydmyp5xdYKyWqysx8JTX8GF3io9+qYSF2lWWjDARymDcveWZPoZK7bRNuWyVJ9lFw8BuQIec8zbF+VCMEJILle3N9NU69DWk0jCkpPKNTOwT6UxmWsrVioiNeMZLt00nmXqcmdINv0+DfBvuqOeyGwduGu6sEYkrBDaksPGpolXKvq+HMpbaa0zJOyE55PlZhqlYkE746VZNuSBOYZ7HmFInhUrBpgKI/Xb2z5YcBxM0rUKSxI/TDW9VK+CJrrUm+bi9m1ctvSWQHzpdmS8JXy9dOUK6DW3xCcdi5/taIgO6kRKw91wRcNwlo3fDIhm5rckK6UVqvRU2Tbv3EbfWeHhqrmwnYZCwA42+eIOTeFluVk4FmCe++zV6xJRoG4y1QNqFaFuHqcaaHvQXLYEeEViol9KZqXGCOAR1UmW7EDp5DAoqkVlbqAHBQ8uAfW865T69m27r+8XYq6JquoKdE23imvwp3qDFqqH9fb4hplPqM/ZlDe39tmQ7NLmkaBusTZbBnOWIWG1OnjdNP9xlYwtBBNov+R7hy/J4QS81tFavQ0NPOzNYLVmyPwqXIVG2rFtcKr/Ur/QGd+NRibwrFyakPcQ4pITGXEk7TryaMasqSBNqm2m/po/HpCmuMgt16YQqsJuiujO10/VGx/GGbBD4UNggg11sX5TmlhTWPh5OhSSeNPvqyRIOreSCi2oEsuqK1/eMmnFsyG4hArIs69pmlxMmaasOY6g1CZgipZrrMGqiOeQjlolDE8R637V7JHWUFo/QwbAYUBbMzMako3GtCTJSZGKzJJnLeiXvbkwaKMwuVuVDgiX6tRsb0OJh8ZFK964zodv4FtUK2FFPxACTrraWaO12MIPbXdy5onBJVBJ0pKsrzlzcYTzRMimNeAvTrS8ckEhI2CSLjnGmppp2Z1XCucJ+Zp9ZhacPNXtiVhsMa+t7EUh1bRdtevfLi0ivvPhCNSIVMe6ArB22UaXlDlEy73wnI4ydjlPQ97q4NUvSgMm1wQzY+iolZN+vqLu1zLANg9x8Edj4OJS+z4AGSzxYpzvYKzNl3tymA6SXXmXAhnl1+3GvwlQ9XQu2zBFNRFWUU91YKuiRicrukvpEDFs6z/c1F/qccG9DK0c5nMUHgSJF39+eR8us0Xp7hLUkThgcputY2KIhSoZxfVszpE0m0iCYqNFuaNyShMA5D8v+Tk+H3HcciYBMXHQOeoqMk1XeMpnxWw1nGAPsRBLvoKunXr9d7OUlu7PciSH90xFG/fAucAcIvsIRLPM3LjkFjDRMmbHXeiyjN/7+zFjBztmEjF7fINeWTgd4U6JcdzVbyc7yfV9kruernrckZZm5magkuyVaVhnuocyQC/12JdRhltBXSdCLs7G2u9pdWRly21nXq3o4W1fKWtXLhD3VZx/aYhshzyohWxl7izev0tamctB9rLWy64ukvqHIuTWjgU/CcydihihWpgcdMV4dVDKabpBXJnHdHw8DkcZrVTvmqZbq55RQiTtaohjuMPZeR4xJrtHIVyG5j6jYD8/TzkuRDWs46sYpGjsSTsK04iP2sN7xlm4sLydKwQyPUCdXrMdEY01TqOog1CSpYqCD3cn2shZHGAF8tynzYN8cxvXAXqwgN5tLCrX7YDBXoexHjHg/OEuUnjzDiyuBuzR1w8obFSa5fIiWBZcUAkrFyWYp4cgSmiRH7Hloe0s20jYlg3un6ZC6SXjFy5ftVmqD7mjFGwPV24o3Gnec4NoRM9eSLIQvsqNLS71/n477TXAe8trYi+kw//XBZuketBLHdiCS4spp6tQbYqtpY9dgPQHT271hnHJ1ue8pqENCsLelZR2Jm7MKJXfaFJkxp7U1fi/XfHfzjX7NdA4sCEbDTcutr8AgWAXlEvgTP9UecSFRP6jLYqwmjdxEyh7tJHdjjemhRxE6RKBC5mt2Oh9o9nL0bQoOgws14dHFp0t4s9xApIVelnUIL9cdbCCDs9oCT1oEQ7q+xQPQQia9vAftVAYblCMLRJ91ubdpR7xiEKsr/cjyKQOLb6E+Hhw2Uls2uo2RgLnSCuzPKz9PzrgaDJJ9ODbtKllVwXIkd5CiQUcYBARdlrp0afwj7O6vAdzpOBlmjZ/AB1SjkzQrPTWm9PqgivR60ld+eACdRcfsMT/N0ct0aTaqGufXWmYqzQ76tT+MqwJ0diW9ZA4KfL4PZrIU9BBIykMjHPcVggF9WoFYGRmwot56/jLufUtdZuMGwjHS4CG1Z9xoA4EdGCayWHBZUoTmyF1t+lc60z1TWdWeuUp73KLb1eY4nvxVA0UXBGlgYsgLj6nvgJasunA7wUH3K/k0rk1IP8kOpu8Ow4HcEPeTjTfkat3iQmUpKpHWnR6ctJBZSRgrbdJQ2ZcsmcFTJDa0oUROcNvKfIJzlcQscX/FWImlNGew2fU2MLfM4IMbCgqtKldUX1cHhVUmCQo0CXMEpktWYC/k7hyyQyGjX5XiNoEOohyIUkvGFt6zqRd2WTmZAbnC2JYAXSisYYMDG7eYzwtl30q66h1Ee7VZdxA0kINjMN19n3vXPDWXt6NIFDHu7+oEXacuahW2DLnCac+2G1EB29jkzoxaGZC5rVAU9fbh7fvp4tu/96jUfKzy/+x053kQ8/UpiMcJWeD4nx5rffo35fr7h7fai4FUz7OsJuvC16HPP5xkffyXTkVniPH5HNLXU8/nEW/rhPOzum9x4XdNW49fmjJ7PA0BZrhdMz/b18yPf854vz/s+7064KvjPx9pCOpZm+dh3nw9LuanHQI//v41fJ3zfXjzX0/nfEEJ/EtQV7PSryN1oCv6Dr+jb7/9b6/cWO9qLQAA -->
