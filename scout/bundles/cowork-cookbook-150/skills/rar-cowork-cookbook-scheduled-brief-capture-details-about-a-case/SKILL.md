---
name: "rar-cowork-cookbook-scheduled-brief-capture-details-about-a-case"
description: "Builds a morning brief on case capture details from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Team"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_capture_details_about_a_case", "rar_sha256": "9ffdfa158c3cbd602c6f2af28bdaa6b44b1c591240a4c96ba6d58e08ce985592", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_capture_details_about_a_case`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_capture_details_about_a_case_agent.py` and in the RCI capsule.

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

Capture details about a case Scheduled Email Brief — Builds a morning brief on case capture details from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Team

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-capture-details-about-a-case
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Responsible owner who receives the drafted brief email.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run, e.g. weekday mornings at 7am.",
      "type": "string"
    },
    "teams_channel": {
      "description": "Optional Teams channel the Communications-ready summary is written for.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_capture_details_about_a_case_agent.py` and embedded as the fenced Python below (sha256 9ffdfa158c3cbd60…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_capture_details_about_a_case_agent.py` first:

```bash
python3 scheduled_brief_capture_details_about_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_capture_details_about_a_case_agent.py   # or on stdin
python3 scheduled_brief_capture_details_about_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Capture details about a case Scheduled Email Brief — Builds a morning brief on case capture details from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Team

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-capture-details-about-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_capture_details_about_a_case',
    "version": '3.0.3',
    "display_name": 'Capture details about a case Scheduled Email Brief',
    "description": 'Builds a morning brief on case capture details from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Team',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-capture-details-about-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-capture-details-about-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ba7dffc7a700a91c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/capture-details-about-a-case'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-capture-details-about-a-case', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted brief email.', 'schedule': 'When to run, e.g. weekday mornings at 7am.', 'teams_channel': 'Optional Teams channel the Communications-ready summary is written for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where capture details about a case stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on capture details about a case for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads capture details about a case, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on case capture details from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Team', 'example_request': 'Give me the 7am morning brief on case capture details in USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted brief email.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am.', 'name': 'schedule'}, {'description': 'Optional Teams channel the Communications-ready summary is written for.', 'name': 'teams_channel'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly case-capture brief for the responsible owner from D365 F&SCM, with a drafted (unsent) email and a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefCaptureDetailsAboutACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCaptureDetailsAboutACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted brief email.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am.', 'type': 'string'}, 'teams_channel': {'description': 'Optional Teams channel the Communications-ready summary is written for.', 'type': 'string'}},
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
    print(ScheduledBriefCaptureDetailsAboutACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916a9ebxpbmX9G8/SFJY5u7EO511hoEEkLiKpAAxVkOV3G/I0Dp/PcpJNlOznF6Jj3zaeRlS0DVvtXez7PLxW9vTt9FZfP28U0PnGLBO1kWR0GzcAp/wZZD2aTgq0xd8HfhlUXXxG7flU379u7ND1qviasuLgswfd3Hmd8unEVeNkVcXBduEwfhoiwWntMG4J+q65tg4QedE2ftImzKfMFNhZPHXrvAl+Ric1QXP2bB1ckWQdHF3bQ46dL2p4+LrqwW5CLugrxduNMizivH694BC8vcyeKgXdzaRRcFC+q970yLpgQeAPXOLWica/Du4UkRjN0CzAKmtu/mwcWiBQNmc/3GCbtFkAOrgKaHoHIoQASqrJ+fG4GTA2eD0cmrLGjfPv78y7s3YEP29vG3Ny9z2naOnRcFfp8F/np2mn36yj1dZdyy7xgWBAGIyZziCsZXEwh6Aa6roAnLJge3fBCs19WPbZCF7xb//u/p4DTX9qePn4rF6/Ppbf5z7IuHoV3ptF3gz8F13DgDMfuwYLLBmdpFEwATitmBFqxZcf3wnPlNEgjqP+ZnPz6VfLgG3Y+f3kpggjOH6dPbT4uyAfqafv79YZZS/fjTh6wcgubHn77JaXs3CbxuFgas/vD5df0SCwZ+GxqHi8+6umFfuprAi6sACP+Df/PnafpL3Cskn5+Dfyyrd4vvS579+Qew95mVLpD7fbEgBmDm24ekjIsfXzqa8hYUTuEFP/70V2LBAntpFrfd/5Hcn5+Co8DxQbReIfnp3WP5fllAL9++yvxrtRVImL/jCRj+Rd3XQP2V7MfK/pNoUDqgKr6s5XfFfW8C9I/Fz3/p23814d0i/PTGBVk8V6ubBR8Xvz1S5Ocf/G83f/jldyD6fytGL/vGe0j4nDtFHAZt9/nzzz+0j9s//PLzD30FshiU8+e+yb4n83txfej5UwRfo37881yg/1SkBYCOxdcaWvxWVv+j+f3D4gxwyv92v/24+GMlzh9oMTvxRekzBH+oxhbY+oc4/vT2O8CgAnjTPzEN4Me//dtCir2mbEsAZ7oHMGcBFriL82A23ojidhE/cbIJQFzbGAT2NQ7k/7zCs8VluPj1f3oP3H/vvXAfbr+g2+cHpn9+YfnnF5Z/dmaE++x8noH+1w8LY4bQJr7GBYDyI6OqnwoAxEU366+aoA2aG8Asd+qC96C0388/FnGx+PXvqPn8kPihmn594Hv8xMMjK8xY2AIhH2avzRnonz56gNyCMfB6oCwrPWBZGAM4fwei0ZbZDWDpHKE2jbNs4ccAbQDJTQ/ZIIofZ2G//vqr67TRp+IJ3vjiyX4tDAZ8NWfx/j1wMczia9R9KgIvKhc//Pb7D4v/XPxXsx7CZx0qoJPXGgEL97oiL0DN9TkYBpYPLDgAlMca/fb7K9BAzExWYEXjcObCeTLI2TTwv0Rd3zHvMXK5cAMQ7WCmz7LpZoaMuw8LIVx8tRconR/NnBGVbQeougoKPyi8CUh1gDtfI1mUHeDPLm7D6d2ib4OH1l/dxnmYmIPid7pfFxKrAoYqH7TavBgLTC6LGIT/a0487wMhzQ/tYv1FxIeFPGfponIap4oa56UjdJ7rApjpy3Qg3AH8PnwqZlIO5lA9SuYZHjAIRMZ7Len7ec1BG5MDfPDbL7ofY5yZR40HnzafivZVDk4zL4UH6AEovfaxP5PEf7xSqo3KPvMf8QOWzpJeq+C/VuWRg+w/NT6PLAYmP7qir33DYvNoQB7tw+JTjyEosfj/uaOaI8Pw/HHDM8aGW2xk42g/V2xuMueVffals9EgbZ/V+a3N+QJlXxD9U5HFIP2a6T+eIx/r/BrzREkQKR+A0fEhHyQZMGeW+6iBOaebZvbb+VR8oQ7g5uKBkyDeADBAQc3OfFE4P/1iaQRQYb7+1kY8cqbx50CBPF9UvZuBHAyDwHcdLwVWNXMdv5YZFEQw1/QQxV70J6/mVQN5B+TPix6DygRx/PAVzp9Pv5j+p4nPbmme8ugke1DGzUMAsCOYDZyXcIg7gGZO9+zpgZ8fH0KAG3nVzb67oJDyd6+bQRPUfdyCpHmuN4hrUAHwfj9/Pz2d7wZjBWoHBAtkedWD6D5qak6fHPRCwIY5X4MmjwvQG4CgvILwEOjkc1YDAH41r0+Jj9svh4JHIc6k9mXi7Mg8Z+4TniXgFNMfccT4XpoAefk84qH3nzPtq7ZZ9oylLcBDoPHL02dD8eHZEzybjsUXuR//ZdP049/bVz1Y/vTnBPi4iLquaj/C8JOZvxDzB4Bk8NPW9htJv3/AxPsXPLx/wcP7B+68d97P2PEnHU/3Py7+np1/EvGqk48L9APyAZkfia88e31AWNj3a/s9MT/9VByDb5gL1APU6WZOyKYZjb4Q5JchgCWvDQAxMPhJmO3MswNAnAdDgBX5VPwx8efCAwRUXOdEbcs/AMKjUwBF8FzAr0QGHhUd0O3P/eY1+DBv02bzwYbtY9Fn2bs3gKnB39nlzayVz2nezptEUFCgj+vi4HH1QI2xm3/+eQOtPH442YfFS+QfU/HFNTPX/qFint4CLz2g4d3CBzFqZ24E3s7K52pzWpC+IHNnr7qpmt14bgjnFvLBDZ+f3PCvBnEzh/yJPgAA1n0woyzYrTp9BmIJbs2k8l3xX9vXf5Vtgg5hnuuXH2eyfPdCHfANthzvFl93D8Cp135u1hAUPdgq/zzvXOYoP6bMP8Ac8PV10tf/m3CDt1++Z9fMRv9q0zFoK8Bmj8b4SVgDaN9AjIP49gLYB7XNzeuDiR8U913PvxTj9xwHTPlsiN4tgg/XD4shCNKZZl8sD0ioW1BO/l25oP/L27m9Au1F9tcp9KDYdvEa97CcBU1PP3deD8Z+PxMQKLUedELNg00HAICAzf4iVYDqB/wDEp3j/21hv4W3fOwSZyPBcnTP/9T47Q1UgQPS0nnVwWubAYYDtHzfzm0UDDADKATXz+oGz/6vNiAvWW3kgKYXCKPD0A8dlFx5uOf6SwTzliHmhNjK9R1n6RKEi3okjWIE4hAevXSdpU+uAmTlBfSKJGkMyHvixee5b4xn+0iaChGaxkICxRAflAJG+P5quVp6JIUhDu06pEvSjvttahoX/svpp5NzRL/uhebgvHz/7c1dEmDkjmgF5vlhYRp1YYJyp/0OshD4OA5McbhsShe2sWNv3O0AHzGO0aixxuTVNhY6pmvj8xhNB9LdifyQs4y60QNpQ08WesJr/bJ1TLelttjETqvVAC37pl6GFmriqrdyCylfNUyZCZl1UOQtKzZKvd0eNqf4NqrdVNab6rSXlji/ttQYjbuRgyG6CMebUBusqG7l+KYrW0zca3RWn1Pbr+M+zofG6ke9t1FOdClouIcxLKOudGpOZnxhK/PsUa2mUjS02kn0Ng+smB95y6lvWw/01K5OcV68T/MczTagxJtGK2WkXBXpZdoTZaubERU4p0N/thFxPFRQqSURb3qVVbEpqkSSvbMTrSYPpRUjpHbZrOr+hJqCeshKWFB0bLW7Yk5nUSsyVMNugNODF8JhhNsQBAns3r44JrG1hLob07XLr6ZrrcWc6Z8nKolEahs1SI1i5/W43xOmF8X06ihZkrmva/+qRaaes+JIdSm1j+mEKC1hrE83q/Ku1vqIOFxhT8kxOJyweMPF7dhvN2lpWqaAcah8OzoSXhz7UoYvhIVdzofLsaxPznU4TIKOXLmwxk56hB2ys6ifCP1MMKUpoJcuP2j6fdMFriJPyD1VnUNx2eSk5mdkk5LDit9BEXKp73nvniRlFZDl9VSbJ3STnZyaUM5X7bhtKjFpenmQLtvUXLlCTHnYZX1LQjI++UFciAHXjzvUjMKajLlTO+qlvTobpE/VLiKP0FGtK7XXKpFlsrw4e9qy9KVltZcucQvi4LfnteUqAj4qgWFId57cG7KyKRhl55yXyG5Cj+j26rAhkyr7LcgzOUNAt6CgfpV0BLfVDlHj8pFYmcy5cvN27fo9VmN2Jgyr8tb5UYodkAA9Z+eIqactJNDwFNV1IY9ZhhajbkFTvLSgLSThcX+Js/Aq0iSz2uijQlhSdDXDrVVKeQIhskFYOSVKtDVgLJ5FjhyStuv4/MlFDdlb26tmtPkmGWSDv+rZLlvm3qlaD919vSuIfucFmd6yxLhFYTKBxx2v5kan36gdcpzkAocIWIclLiIq2j4ksbsXGwYVrt0pQVF8u9sipnQkazMEyc/26HBit7qbHIeIg+BUKcpt5G5qhxcj07gRZzfXl/tGPeWBivnraQoOEs5veudSWxq/qUR3jW8FMeDVBNuQp42GMkS4Vg5Vvy40wZh0Cr0sPWhzllqouEuEtIft/BIN63O+RaADfkTco4lkxMjobd4K5b7hBfacDlcGFSVkfbgL8XlpIUppAegt0aSI/WFLm7ZqTBt5b5ob1wpJWQ/OUJvwSJ8jHKWiQYFU6Fg3InEZ+cwc+gy7toTOkRYTR213EAi53OnrPLrF7q0qBt2g0URgoNRkOenaHsjLYX8a6v2hrCJatW4OHLM7e9neGVVQt+utmo02mYqShYXbpKSKhs9tmMr1jFU4KbNbptQV92LF+h1ba/eKYM/H5dHxPVlw9AOmS7Kg90vxhot+Abtshu7WdUEr9xNOxLjhNvfxFLgsIZVRApk7iBc8aYjFFefb9oFd3sloJJzM5Pcuwu9RhcopbOOpFMf6Wt1E+1N8Px1Fee+nY26ip/Fw07slJVpXOE/01rWxa8xSJHxgSxSzoQt02nj8iUfxXUYoB3ocG1umvQl04FpelElO1XtHLbdKnZhdgMQCNZ0RGl6GKYIuO1yI+YO39Ucx4XI0PecBXxR8vAEBU6/oRU7jbMBLTGhKR0gmWCJzKsoPQ95I91U47q4nfKPzNAD1wzrZMWmU4OzVQBNmcqZYwrt70Kq3Ky9sM69iT2N+4YzTNkLlvmQFbb/OlQjZoApbXjG067ODYNtrIVs3+/Z0PJrWwKb6BcOnYFgZx0Mmp2vtfI/ofS+lWb9ntmUzqJ4mms1RU2juCNENtSU60185qbXuGGjXNvxJbTFTF81gk5oXOChQDO5wyhsqJvLKe7FWjuRNKTclqodtqcHXVUnLUbLftGQNhZSKZZvhfNtxXTlG17E+HOldjVqEyZEQvUmglXPTsOrsk5wZ5agPHbqc3SjC1STKLaE4mSHqsb7ub+dia+/tWFutlKHYrOXEQniCL/vbVR7GVYwdku1uvdJJbaBIZ40bHetsjHHHVqPBGs7hWqw3J/6okdV65JLk1LXL3NgdXeUoVdsj5MrDoV+dlckJClf3QON6Eg91KRHhsAIFS9/VQ+GR0CU2sHW9u2MmWTqbIIoI09gwRsKESykldKVXZUkwDm2PaSkp2Fp6FNWkTviqgi/F/uJwajBEFj56uCYwnqlami4w9PbqbUoymYrOkqiN7gujZFT3VebLa+cqJUZuN1eJOIxZZaWYdkmcuoC5TisHq8x0e3mjlg2tM3XJsnZvec5OdLTIkMXdlRyq88Y/M5tRP/rHiw9Amxx4+oCc6qb38gLaKXTqnIXzNt3lu7MUXrcsFNX2pMgRwRujGeuT3ipypYXJVHHxKrmurzsyPGe8F59TucBcptgymVZClZVjaOjie+BJ5G3p1mazMWal1W0JQRlSm5Fcm9uDcWGU6VIHxGFwoQCthcjrd/z+FvHW9a7irYbImtTv+bWzwip7L46IMl4lbWcoDoKRDl+Ka1rSjBY7nEC8jBVcTsiaZqPTNFa9ZKg51eymi6Atw+1gHvbLS7oVt6HEw+yZ0dKdppUeutWSzXA0qigSmsvAcIdyZRE9fPKNcF+vl6UKKdHUbrE9C+uScrGBnnhHjW20ofi219T1TaTkUqawoLUZTqKQYYTdrYTxxvF6nHw3oy8YFOnmlAyE5lRL5nTbgf62cKMc7LCJa3bmK3d0Lk685m+36wUkrGrzd79KU9A12Ze9QIgpqwW1pu1X0DJztyKPXsRJPGjNmt9rWldf2tJVRegq5tc0J0p2padK1VyizdIuVDZlnfFWOBrk0t5ShOE77KfultVO8QmpyZFkueuKuwmmXdtjFORIjKZdgKqmHh+vhJJk3VFVYPl+XR+NDYGEau6JtopQWsiwbZlJ7LSJK98JUSFZbuhAGgOU0B3ZH/BLCMMQK4j1hFz6FN9LhHy4RHRFq93ppkfMBIUDe/G9UTOWukExLqmpNNrKvW0sb1AgXQuoX7YHPmN0Bj0s7xum0I/VZq9FpWWc742YYtCEnaLu7tx4ZmRGOA8OGH+BlMNWtHh/H3HXs23WTJ5XyzN/Sa/mIGrH3WbcHqco0BiN4C+0eML34vJUyV7OQ33C42YZ4vY6azKpFeo1DFKaJVJPCHIDPW5yQjbOp7bBp9wn4OtIu5VU27dBv00lJFXLPeadVoXZE25K0B0SZ1Kyisyycxlmb5TGhFJL4tzXul5wLnNiPLE9J8wm4111je7O69v+bO4P06pvRXMQqJFSxk6tXZ7cUI3j1il9LPMi3vSMHCsONlzcdnORYpNEsKnRTessxxaSpUh5sU9cVAbphtgfr1Ztlz7P890BDw6CKTDhJmb3CZMpS9fI7BUjE+0xYfIU6Q2cZL3rUb4LR5WDTdMBIgXN3jo77sKZKWJZdQVwy1pyxIDCd3ppXJAwtk0Du2zpSc9yc82HfHjr450j3nyIrccVMl18YWfpZ4qrSbJwekW5joZ5P4qrTE3dPaVk14IWrRuNux5YlxtyZyuhNbr0eMc7ajdsj8R946hZvr0pNIbWiSeMR5LrsqxsKM22hIjDO56tVRPrNoYJLdcqpQiNfFir3gR2B2B7bktLzTn7hqlC2KEvKxG58zuWN3bpeZeePBnslxDLw1HGKN1T3m+ug3A+GtxObRqzdgsGkg41tJXV/LoqtntIELPV2LoyXLAMZhZxsU3tlKGR5WXd7iRXxPLEUJQDdrDO2jkt63Q7HPvVHpC1B/g8PMKyCBMYlF89CxHO6GqgG7wumlxc7rwbZuVRE/gyBzF5Fp9SNlZ9uzmslRTZi06pn+tD3zN8sx8FX2Y9zndFN4eSPqI0bpCkxiYpZiw7fz+QKCNlt2FwdyrPES4sHZ1jLsFVaS1tBT+XxzzjAPcpZromPCGssixYBik+YI5td5yGylvZwAuihlbVCZ8s7D4eGfssXiyDZKONlcrnliui1Y1UuQgs4n0fXooDDC6SwThJtjmff/SIAEv89VqWotlF7B69D34cwUwQl/SdYaoSJoblWjCc1VrCkRRGi2GU8xtnb/vJOx+96Ir4CmOjUp7jCXElSPbmXLhd77YdezqzQSJ09JLbrlvQ3EGXY4cE7V5Y5QelHYzzITCFxHD4/am0R3GieHTPkGCnurO9sStQeOMIjcrkAONDBmpd3bgiqt0ksrM0b8SmXdupl2dnJ6+5e4ENSbAV6Wtx2nXHg7Q7wx5d8B12x6yWMjftqnSTFXXFyB0EO0wTpvR9kCKE4G1ZNKmbp5kQ2h+MKBRI8nbAe4dFkHHgh4KD8A2xW4+NDPaRWMShoRncR0ejcTGvfIU+iXTNxRB1QFs0vSw3dzTDd9ERoQ8y2+UkmReHiu4bSjZlNSB3DG+fo3OmOPE0IWqycixrWXkN1xpVZa3xLq8EcbWC1LBFzoYVHm+ryC9vETfde60438PT7hCJTOo28XjbtjcTq0vRcMIctLZtEDe2Cud6Xl/GvjirFBvKZ+627WSYFKuautGuDfvY8hbGBxrnx1upVPF9Vdjhnq2kHYHTYNc7rRzG1ySbw2CXHmkYjhI6LsmDJ8rwCsrhcSRyXM5w+9JTWaffTazMqYzTetReMrgX3z0K2eMGleFrHDcYKAwRAWwCa3+dcLg8rqfS1Y9CQCbQ9ZqOo4aqPNymd+qOuDEqbpeXLJS47aXfAUpAELWw9VhzsbV0cloyU6zAJuCjkOzTI5fvgnAZXHpuI+MpEVj+pF8DnSHlHRzIKH1Gl3TMqTUROcogdb1lX9oNR+SONpx15ayOnhkbcI1R5rgMOzLGo5NlWLflmdOWSqV51BEqMlB1tKkohNd7eFZLwjrXhKIY6G13w/emnweQEJv7ysRaekjrMkCcyW7p1ucx9MZdT3WVWfWK0/l7sgMNj0veeQpmKDfgjesFc8HmthdwIhczPdxwJ9BOZodUSOVYMuIJZlE/2FyYQ8xpoLWtRjeAenarOX3Bk9dlUOsqJa0FzzzLV0potH1DTlw5Gd5a3eqKaHsawV0GSDB32Y3VSOeUwrCZgKCotxCiyFtYs0hrT+tjCDYiNazuo0QKEnyTtxRo4sK7ch/avnZZWGyVsxm6YhYjqwlaXaat76t8crakkOiTXovvANaTbMeV/SW/LGPiDMgZvZeMfDVLbWjuDtYuaWRbhrmSJyJ5cFC3j1ndLolyeVPWantam2qSNOySbQYYU4bW2mUFhIVCuDmh7l3HbljJeihZYGYEI7TQeiwZYvH9BrYEsMCTYuopmjfiByKI40uQyLYAXdCBF/QIdJXciBvXQRR2MBKumtiXNY23Vzv/nhxKJwoqcre8AJHtSpIphs9vFq1EthSKfAvHFYJP9N0y9NBCddo/eh50V0OuOuOKapX7LafeoZ7rFCO81Gt8s7MyyOXrXqxWg8vfmpuV5vuAhBL+HgagFdzSh8T3pYTquESp7iaSddkyUpx9wrfMeXV3z/RWmSArWOK1xAuIJ2Eka1OV3YjFpkhida3eVGWA4lqtx8lTDVhAmTo3zgIuBNX+5KLJ7dKNy015P8DKMcfDNo6LFW3xzNYV6t6GhQ4sNgK6UfWKr0fimNZbRVEFASR5sxIkzhBSo15deArRs+Fs6EsHLzdJUmvwtBTvWs/fvU6qAC/7kK/ts9LcT7dL3xLUHt761BYG29CAkXDtWFpJooxHbJ/uSzWVERk6bALnBEnqadxdqgvNpGI1UiE88FvoQh27i0WeT7t6QJoLlkEntRMRtlKmchPsoFu7FVaBa3YO0l6m8da4x87GzW5Fh6dDfc5a2abFnZxa49I1zV537mLi+TA/KOugwNK7UeBqg4h7S6E1k3QOObSPQywQhzY+TucdscS4UL4xXVJygdVsbaRaFVfm4uwqhaVRUCPISbagOhBEHy3Nk0wc85W3ika3Vv2Jl/Guoc692dzQTqJPgb2FDalx2kJdnfu7GhjBzTV3SQjpUn2jrJO/uZRX0E2XV2/FFAkzeQoRUHcKhDgmzaO9Yl2Ey8ri3HgWYE5QI3c/rKizG0g4WoGSgqy76/oBrBo5WTUN3pd+YtGHK6U7cTgVDp8ckUSjHUEkXBMN3FVMd5RJH4NRsXf7vqMTtAogBD/Amg4LSNbax7I0lEvr7zFLDAPQaZLUNWv9BNnh+jpJs9I7xozR7I4goDiAxOt6WMpuOurbC4pRcyMRnjzK0qx7hkDbRuUCz/exXl4yITOifbzcVSdjaGt5OQ6kf0YPwb6hBgtCfA5aNkbokHgEk444Wv2qP8HY6ElcWOLrboQon6UInyeCC8Q4x0Dtm7Ovp9DdFrcogjbeRc3grcz5BXbSj/DtthIlDC34xtRvA2web60PkRhgfg4FmxL2tr0hOIf1wsiujhBEtxzPOzfBuwX0SkWaPnKowqApfCefSIGwQqm7bDCWyVgctJb9BgHtrsJXB1tc7cU+xwiZ2uLn/sbf1trVUQiUEi53ueRJZnnaHQd4eVytN/oSc3ML57aev2Fvt/vOTQqOgjMcviRISa+TEOfU3hc6yjmS6iH2yp2Dj0G7mpT9aaJGNdrGXiVvzpIyKI6Xx4RyGBuq8sFu0YoRgvOurkTAtpwthVbhHX9t7y0ehi6TL60sNldgLnLlMIVkjCB28NDhKx1Bu3Q+YvnHP97evc3Hw69D3v/WW2jzSc//swOn59nQl3dJHuedgeN/fOj6+N8z75d3b40XA+Oeh21t1l9fx1H/dNT2/u+8RjBLmp4vfH051H6el3fOdX5R+i0u/L7tmukz2Ig/3jABM9y+nV+pbOe3bj3w/ceD3H9ybj7Tnd3oys+Pt/S+iIiL+Q2SwI+dLnhdXl/nke/e/NcbUJ/xJfk5aKrZ99f7CcBl/APyAX/7/X8B7zDsNvcuAAA= -->
