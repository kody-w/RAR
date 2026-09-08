---
name: "rar-cowork-cookbook-scheduled-brief-monitor-service-assets"
description: "Builds a morning brief on monitor service assets from Dynamics 365 ERP (legal entity USMF) \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions \u2014 then saves an email draft to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_service_assets", "rar_sha256": "82b790d157ff0933ec122532287244d711b7b4a351ec7696dd454f90b15ad0b1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_monitor_service_assets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_monitor_service_assets_agent.py` and in the RCI capsule.

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

Monitor service assets Scheduled Email Brief — Builds a morning brief on monitor service assets from Dynamics 365 ERP (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves an email draft to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets
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
      "description": "Dynamics 365 F&SCM legal entity to query; recipe default is USMF.",
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
      "description": "When to run the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_service_assets_agent.py` and embedded as the fenced Python below (sha256 82b790d157ff0933…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_service_assets_agent.py` first:

```bash
python3 scheduled_brief_monitor_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_service_assets_agent.py   # or on stdin
python3 scheduled_brief_monitor_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor service assets Scheduled Email Brief — Builds a morning brief on monitor service assets from Dynamics 365 ERP (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves an email draft to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_service_assets',
    "version": '3.0.3',
    "display_name": 'Monitor service assets Scheduled Email Brief',
    "description": 'Builds a morning brief on monitor service assets from Dynamics 365 ERP (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves an email draft to the',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-monitor-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'face2d6da5a5bb67',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/monitor-service-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-monitor-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; recipe default is USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where monitor service assets stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on monitor service assets for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor service assets, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on monitor service assets from Dynamics 365 ERP (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves an email draft to the', 'example_request': 'Give me the monitor service assets morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; recipe default is USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Use for a daily or weekly scheduled monitor service asset brief for the responsible owner, drafted as email (not sent) plus a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefMonitorServiceAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorServiceAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; recipe default is USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefMonitorServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+V6adObWLLmX9G8N2Kq6mK/rALkiY4YSSCBBAghxFbucLGD2Dex1PR/n4Mk21Xd7jvdE/Nt5LAl4Jzc88lMH35/s7s2Kuq3T28X384XeztN48ivF3buLbZFX9QJ+CoSB/xduEXe1rHTtUXdvH148/zGreOyjYscbN90ceo1C3uRFXUe5+HCqWM/WBQ5uJHHYMui8et77PoLu2n8tlkEdZEtmDG3s9htFji5XLCKvPg59UM7Xfh5G7fj4noRd78sPncYghKLtigXy0Xc+lmzcMZFnJW2234AkhaZncZ+s7g3izbyF9RHzx4XdQE0AWLYd7+2Q//DQ6Pad4ss83PP9xa5P7QLQAGI33xjEfn5ogFbgCL5ws/sOF14tR20gPn8EGjtD3ZWpn7z9unXv354A0Kkb59+f3NToNVsRDfyvS71vc2svfjU/PJUfP3QG5BI7TwEa8sRWD4H16VfB0WdgVsesNjr6ufGT4MPi//8z6S367D55dPnfPH6fH6b/yhd/lC3LeymBfq4dmk7cQrM9r5Yp709NkDdtqvz2SkNcFwevj93fqcELPqX+dnPTybvod/+/PmtACLYs10+v/2yAI77/FZ38+/3mUr58y/vadH79c+/fKfTdM7Nd9uZGJD6/cvr+kUWLPy+NA4WXy4yu33xAh6JSx8Q/4N+8+cp+ovcyyRfnot/LsoPix9TnvX5C5D3GZoOoPtjssAGYOfb+62I859fPOri7ud27vo///LPyALnukkaN+2/RPfXJ+HItz1grZdJfvnwcN9fF9BLt280/znbEgTMv6MJWP6V3TdD/TPaD8/+HWmQNyABvvryh+R+tAH6y+LXf6rbf7XhwyL4/Mb4aTynqpP6nxa/P0Lk15+87zd/+uvfAOn/I5lL0dXug8KXzM7jwG/aL19+/al53P7pr7/+1JUgin07+9LV6Y9o/siuDz5/suBr1c9/3gv4X/MkL/p88S2HFr8X5X+r//a+0ABIed/vN58Wf8zE+QMtZiW+Mn2a4A/Z2ABZ/2DHX97+BvAnB9p0TxAD+PEf/7EQY7cumgJA1sUtunYBHNzGmT8Lr0Zxs4ifIFn7wK5NDAz7Wgfif/bwLHERLH77n+4D/D+6L/CHm6/I9uUB7F9eqP7lhepfnqj+2/tCBdSLOg7jHOC4spblzznA37ydOZe1P68HaOWMrf8RJPXH+ccizhe//WsMvjxovZfjbw9Aj58YqGz5Gf8asP191lSfcfyplzsD+eC7HWCTFi6QKYgBfH8AFmiK9A7wc7ZKk8QpgPoYIAzgOT6LRZd/mon99ttvjt1En/MnYOOLZ9lrYLDgmziLjx+BckEah1H7OffdqFj89Pvfflr8r8V/tetBfOYhA+1efgESHi4naQHyrAOlClTK2ckARB5++f1vLxMDMjmo08CLcTAXv3kziNPE977a+8KtP2JLcuH4wM7+XC+Lup1LYty+L/hg8U1ewHR+NNeJqGjaheeXc4nM3RFQtYE63yyZFy0oj23cBOOHRdf4D66/ObX9EDEDCW+3vy3ErQyqUpHORbN+VSmwGfgTmP9bNDzvAyL1T81i85XE+0KaI3NR2rVdRrX94hHYT7+AavR1OyBugyLef87nIuzPpnqkydM8YBGwjPty6cfZ54u59gPHNl95P9bYc+1UHzW0/pw3rxSwa//RLABRxkXYxd5cGP7HK6SaqOhS72E/IOlM6eUF7+WVRwyKP257vnUIC/bRXjwaha/9x/8XTdRsnPV+r7D7tcoyC1ZSFfPptLnBnJ377Eln2UHkPhP0e3fzFcG+AvnnPI1BBNbj/3iufLj6teYJjl0NJFXWyoM+iDPgtJnuIw3msK7rWXH7c/61YgA9Fw94BIYHmAFyahb9K8P56VdJIwAM8/X37uFhntqbLQVCfVF2TgrCMPB9z7HdBEhVz6n8MhXICX9O6z6K3ehPWs3OA6EH6M/ej4GrQVV5/4biz6dfRf/TxmeTNG95NJAd8FP9IADk8GcBZx/2cQsAzW6f/TzQ89ODCFAjK9tZdwfkEtD0edOv/aqLGxA1zYeXXf0SIPfH+fup6XzXH0qQPsBYIEnKDlj3kVZz/GSgBQIyAGQBWZbFOWgJgFG+xwsIl2zGCIDBr571SfFx+6WQ/8jFuZZ93TgrMu+Z24NnJtj5+EcoUX8UJoBeNq948P37SPvGbaY9w2kDIBFw/Pr02Ue8P1uBZ6+x+Er30z8MTD//ezPVo7hf/xwAnxZR25bNJxh+FuSv9fgd5CD8lLX5Xps/PvDi4wssPr7A4uMTLP5E/an4p8W/J+GfSLwy5NMCfUfekfmR8Iqw1wcYZPtxY34k5qefc8X/DriAPQCcdi4I6TgD0dfq+HUJKJFhDVAMLH5Wy2Yusj2Alkd5eMDIH0N+TjlQffJwDtGm+AMUPNoEEP5P132rYuBR3gLe3txghv77PJfN4jf+26e8S9MPbwBU/X91pJvLVTYHdzNPgyCNQNPWxv7j6oEVQzv//PPIfHr8sNP3BeMDXEqbPwbgq8jMRfYPefLUFGjoAg4fFh6wTzMXRaDpzHzOMbsBQQviddaoHctZhef0N/eLj8Lw5VkY/lGgPxWS3X+/bMXFnyoJAMGq82ekfQkJ5lW7Sx+t3VxlfsjyW//6j/x00C7MRL3i01w5P7zwB3yDmePD4tv4ABR9DXQzBz/vwKz86zy6zJZ/bJl/gD3g69umb/9D4fhvf/2RXD2ItH+USfGbEhSzR2f8WAKCrpj19eP7C2ofxQwE8bO0PVLuh5p/TcsfKQ5K5B+6oweNDwv/PXxf9L6fzLX31QKAwtQuKDv7AQfA4gHMoLzN9vhu6O/qFo+xbRYGmKd9/i/D728gUm0QOvYrVl99P1gOcOxjM/c4MMhpwBBcP7MPPPu/nAheVJrIBr0oIENjDrVCPHRJBQGywnHfRTFsiWMYTWEE4VEo6lAOYeNL1HcpckV6HrEkghXioEvbA/8Ces9M/jJ3IfEs2XJFAVIrLCBQDPFATGKE59EkTbpLCkPslWMvneXKdr5vTeLce6n7VG+25bfhZDbLS+vf3xySACs5ouHXz88WhjSHMilnaA2oJjuzSdZpq/C46hdscmriVV62+2Oo9lCHbAV7K28PHJKdy6Tbn7vB1LfwOfYLfZXcqHxaD7trq3ZYkvvtAG3WEHQRMS+bGm/K89OeKQ4hzZSCZyVaX93iS+IdL3vparvKst3thtSOzHyPpWpzmc5Vp0GnIIDHva+p1eFmbeJs0Eu19eLRhsbdekUqNnZ0tp1PocclarGKgU/Ly2FcBRdpH2u1oBxjBD1pp4ALIKjRzcHyLCEiDoZdtazbeYjUukqnsSOjOmNyrnmSFI+MdwwYXVpeiatuCWeuu2jHTrERJzJ32/rYpp02tNGqupHXdXRAUlB4AlK6mOraV5B4RzTyLtJGTT+kPhNaskEtaR92RtLppiUkNBnu3e89vDuRvWHp2WE6l1ZqdU3BYHdXUsaCwHhrSxqnapdjGdmNCWodhcQ7cKU17gUcWy9d8qoueSU6K7qmmfzqnlPLlNaOeZVthy6cdtVw3MbE8SSsPSfzK02sznxoizbHuoluXA6YF2MGQflQjnallJ8pPFMMO72W9ZojbZ2/XK+MfIT02KTYS5USR1sSqHVyMVNLySrtaG3b4e5xSplffTH1B36VJk6P36zWK0+bmC5WsuXhlFzrqan7/vFQRYmksJq6k3tvP2wQz+EdySfx9ZDoikXq1n5lxT0DreDsoKDk8dpJ/KriqnQNa229VumJJTU5RSCtu+TwxPpZBJXbuuIvl6aqxeN4Q42LJV3O5JSqXKvQF6C0ppdDJfMQHdI83QpbUt0wHXfT+Kk6QGQxRo299Xve1VVbphEjXkamYRGZT5wlZl1K9QUVWhXdNjcbCTd+07XG6lok+9sSst1z1mM1VLtZxafC+a4wOXyU+2sWxJJwP8XJnU41pKMd2swvdwJK7o2KQaF/EEzueuh6opa3t9N+OsH2roQOqpZnVm6N7J1jRxERWD3JvUrOBu4mZgyfqBvEf/zdIr7EG86ZhtkBwu5Hl931yETL976B18Md7np6vCOcZQ2nHEdg+Cz5TEtW7fXIXwKeF9YoGwIHkAV5HpLLbkraiSjcZsmV3voo9ntmtWUujugR4eEu2jGz0SSYdPj4Zo6GJTFZ1Ss0d3bpXKtFJzqAATQVuVhL05BEoy0exVemkHdhE2yjexrzB+iQnXmXvwiSs3cH9iqGdA4fMDVnYnMvBGu00fCQhNvWtvy73KjOIUzG0b0ozumwbuukYlViqRySmlyfarifMKmlE7Xb5aR1oxOrPQ/pzp8SeOnlrLGqSGiDEPxqclUITvcdgykek7umBjAFF3f5lmRiNz7tRzEJrSHu10nEQWXm6gKU5bcOXyaqRGUXNE4t5oZoJ48N7UoXZQP2V3XEb5yDYR0NhCm3qJH0VO4YvDqQ5GQiAWu7UC3BaHS4FJVwjVt97WdTmO/wINzc/CMnnivN8MRySV2aJalikrlNSS4fJCeHxpS1OCkyGQlWDSLBPBwRBjzWYcXulajTqGEDx40bCtSJ6PlxF3O4SPcI5DZbNHHVZXk4tTEzlKapVjutkoSYdw6126edelg66VRoSkbGJy0cIKvd7Nq8WrO7aUVrqVU3+CoftgPqKI4e+1xITIkXD4RHKqm1O4fyPTyBnDxCQXTNKslFqf3RweM6gpfmSuAETJC2W0FENhN7EAUTNpIEYWR/eYw0qpaP2Zqz9uZIrLbyJo9r3mKI+orLeQZvrshSHhz5vlFMhadOSnTVoP31ft5BPFY0uxaoM1jMnsJOrUEhgrCO0OU1EtgRK3N70++yXLGYifV6nCelo5td+kDomjEJd0J4ts67oxWxVzW5rMtr5rQ4R58aRC0Vb+3FrSuXkpJnzWavkGvivGHFY72JzECKR2joai2J0TbklvUGJ/JyROXTLsmw4MjGEnPIUcjLc3QKEju8kiEtQme2QyD1cgNWurAMsVnxpMyx+sEZB56Wg2mzvrfdnqOUIVKG6nCRUT8YUmEDHxT6nqYovbzjRzWMQDPq21xyQ/hm7XjX+3CTxlViRpeoQsnW253Ts2hYvHLOxZ3c5v29sWMbWqt3LsNQzSwGCxEJh8gFtratSNIHee21aphhDreNZIEvxCgaLsadjbTMUvOBy27m/hoQJMjK9NKxtFceVTUZT8oJ84UkbdpA4k2uEASXgSr8dL1aPEjYxKOFppHUiXKRqzRsJF7U9qCYglpJ6+SetUfNMX03pM9nLM3Hyso5RI7UjCriFGIy9YoG+LpvJX3b9kMvlAeUMNXsILu5F9WZFzMta0t1eaPTldjZZxFMJ2buL8+HUU99ThnYkT7DkG0PXN8pxxRkEIIafrrZsjt8uN69PXe0z+d7yzC9SehVhFXu1izZfLoYO+ssxWVzuW4StIESNSAJvIkuh+MNw2pG323WF8tGt2G4gxjGbA2+3Gn7DHNlUVlHxaiT/RmBnLExS+zA0pCuNusxNA5rTuu8LqtJvxRTBgSwsZ3CA7MnWf0eaCtPOFy7OL/etxZurj3MrqpRaHBkXNlJ5LYct7xLptFQnJEVVlZwLauAEKEU+8C1yGkTinwe7Fy9p+xtddiYZny1kmuZt/tbCStJwSzZbZPH3tU6wSyq35tw3eveLlSOh4OWMtQ2EO3icuwtxNguL8Nx0+7bJszi21rRsXPvVrchiKeVgkjbfcHaIUyQwSnJzYKBWdMfp+40DRQ1iApHjWFJQ9BdEKSlVCMrsz831F1gOKbRVCI47BhuD+UCiXsok7fSLhLaa3nY4id8OXpGqGA+s4FVQd9hcIhc0F3Ret66i9ARIg57xxHMnWf1F1/tDBaUqesmnAZGq3y+dbyk4xsidni82lh1nI1qQ3f7tYfsdxi61s/bk2yOpMEjF0tOSzHwZH5JSZgTyLEE+XmN7gZ2fXMEkViFUa9sbqYgabLU3wX7nI5XWQ7Q5HoVuQO2lSpnwNHqGIJCe5r2E5Rvuwk94jt6XWzZiu1R25anw01f00pDuWiiXxiaRZZwS8MTeaguBNU19/3hcDnnFJS3LZmSRrLRR9A4J7uhJO5xwqFr/FIYVGlarhjgAUVMa+By6Bazt1Dp0HEswrNWOGK4T1wTZ1EfvWBuH26pFMwRehZM9alFJ2qMz9dpxGqHsZb9sa92mx1/wa/ymJqFue8V73ZWRF2j1goemuswO9NIbV8IiTRBp2zp/ThViFHQcGuWabidGEg/wRtsy2/WdHQ5alssrm/7e5HYOqSNNntRA6QNkvh8mU7aPeeVEU32WR1o4j4Im13GJWUMX+tsl9o7TZ/uCmiOzoRaXFGk9K43ozuFhzWpHeiNaR0gj+XYU35FW1U/VViVlVqA0oohVtkVV0txF+2VSOHRcM2wG+tacnxC5pl92+15/5iwpo5FhxWNgKpgrm3IYvjBSt0smXYSX192RGexh9jr+HGyicNut1F2XWnuCDHfa7ZwgBCBJHL4NlB3d2hbwqXEIefOFcuZmwPE67AbokYfuKub5hEmciH50ynZdHk6TBV6dVe8mNU30tjtJb7t4U5aaR7GU7cIOmhg8NAY4eyNxg4u+1Qm3EQVterUKRyNCJR63BQBpTYbibptNNl3nGNwUPwTn6UcEh/FM6rv3a1OTOdoQ23T3oSKvgazQIGsstLTN6rjBFd5sjUhQ4L9WJ2JCLs0J063quIC2hUR60LHKSazvBG7XXSIo+K0nlzdTsRa8q5256uZWTrJFYGrzWQzHFGSfYiVrldLd3fccqD9qC3oLCfChcp5gTcdy0dovpeOGIjLamyPe399gfuoikDBi/nawfA7oTqQgEhemKqGLHe+ZzmebZQeMjnDkq7vGa7AvXjchnfP3UaidtvmqtGnYGo/ouzOKMCAg4snu+NOeRbgpjz6p/t6W8bT6STFvTgwddxEcmHxjSdKB8vCg97OsXgVTQ4OD0WHJ6GSpVv5qp3EbJvEvFKmqZdBWWTeR8fde9WlhSiSudNGVxMsiR+dA1Zujses4TV6a4vsyJlBI+uew2Fn9hQZ93GLrls04UwFtsG4JDpZH2Eth080v6kYIjQv2LZXtdqi9KDfcPS+tO6rNehuT8452Y1TsmuO53SzTIMzKTI6W6n06ZiZ042gD+OAuEasU0rOIFitRGNLIGKVomtj7MkoXPZbitvsGdA9Nd5ZagiJKySxS4hj1IJWwi8E0L86MCHwnnIdB3idg1phMEWtl7XXqSUKqmqC9xepJGs3bRlUVbTg6uR1zUn1vXLdxJZWqQ+G5nHN8+JZp8sTueEs/K4LAQbRyBU5QmjXtYjSoL4j+tyKhDuIC/UjCiFkncCuFgoGdQlabIntW19OScSgSUpE74ZvYYebEXi+1juIhVG2h0noCSrNo0VNRd9ybH9Shq2msVpZE7a988yNJU+XneXeqQzBw+NpvBLqSiwYt8GWXiubLZQGlR2t0WlvsvlSXkXn43HjrPcGfYvHIym2Z+2oZwjcntUOI/n6YMCnVtpP6lG2YSkdLxyQagB1CXyL3spAO6eA8tVtCRq3KG5EjsCZ3e1munucW+G3cF/eYVgMAvrqNdrhqJqrMoBHGZKOzLlwolpDl/6IHdp9ueF1jiy99NLeQh6XytsZvdYn2IPXXpUvD8tLefU2pWsIKwa5sMjV0n3+FvFE6F7RNderYeJD9s3VO9toM6vpRRVDoA0ltZslxgrE5Iakui1kK3B8XZpyQStM2JR4ZOqH6QymFXuHXdM7jbZjsploKViqyA7Fd0F0yE+3rIU3ZJ47Dn5gmHF/soeq2e4D+9Adbrjt0aiWocZxeZO7rorNK+THUrmPltVtZWh2pcG6fDfNwp1KgmAVaS0p5Zr2g6gTO6qaiKEF8B7VOoly+jlFUyQyuEOG1hamLQnv2PonemuBXs0XCS9TKZmzNRzbWyGQExVJf2PIwwnfD9viQvRmbl74UrRYQwRjbnYnOecuhNVurSK3/W4J3cyrRJ+1XBtaYRlZJzCMsdRFcXs9S/k1Rgf3fWiwl2W10lnaP7l97MpqCu2cPkpBJZCD1Fl5aZ7jtB9V3CpUNnR1ZZXOz3yIEg/LMtrcqC0JoAe4QDhxneVpELeSevl4oIjuhss3gTjmrIan9N432k4OGgnbZXznjKdkCfork1NycYlgeS2s7id/KypnFQfT8X21yg+wtPE2GJjrBDVjrNa9DZvck64WIZBTL7SDgqbeeiLdLW5mdSGosOkjwTqZqhHD7si0WRYCiGcOEqq9jwiRb+9Xy3pZr3Z65MT9wNzODRxVJyGtZEPA7y6+Fs/a+Y5k/ti4+oFYA8SF2FOGoGxrMb2Pb8QiIksydZ0qJBuYWhc4vfaJ1Z2ieOAfc1dTDb20ZBtfIi7p0XBvZKRw42AHuFbtplAmJ9aYlg2+QVeym1ZCtw38FrKlgz/leHZKbQyiUAlhYrhZlbgVHMO0rFdShs6AsOR2S5WTSxttonSZtpXIOzRznqj67g+1j9+1JRpvQAnW766nV6Tfdctl2SNyrnbBoaRTNlgyYwPJTUptuqOa7r1EBvPpbmVTe8+Vw1S28mVprci9SLSQvJtC0HPWecYRwrnksF1wjrYb1wgtbbvnIPZoqCJkiTzoj9xKQY9UYgUnsounxFB9/MYmgQoauZgIYSjBuYsxViELZqP1SB/jpr5T9PImBpRmuBrscuUYZT3TLvFmcq90XErEGuAOA2sbowm9G7M6KZx/hdyKQViqlFf7AC8ypKbJbosUstreT5Qgr3h8bMKxxtBjO+DkEdEdjHTupZFOJ91LKWs1SS4ZIJ131YoTSQuMY1L0EVvjdo9WXTMQuOD2J+52Xq5q8UrDywTxRhS/i2llxGV9M3FsjMV9XSy3t5VjMIF0Z9tbyfhGfSUQC8rCQ2lzrbSl2SG6ETXZSBOP7HVDz4vjBF083vYGa9WyXO2PMYmDknnB8265yfwAYQi9MFWKcWBjRLg77kQNBCf3ahJ8/1bdxG3WnElTFkMr7k9ZhMAQDcNj3TO2fpTzjgqti4De8U3v7B3Qz3Zxt/Sd6EpLln8aO2awHNRdUXU5xUareizDyN3xnkYnNivxplxFhGmrvH4vYpIVWiWHkWxEJgO5NkEbJTjlFUvKgDPnZpp1kFxszF0j18NNwrqGNLgeRjp1CZ/T0BvINXdY98cREVm+ue4HVD3fT/FK71melJwQsjmzbCG6MdyxWA53Owizsj7daXfq6k2L3c0NdOPOiN4P6A0SbmdZ93fG0lYMDKd3oMGUV+XkUJXDkWevgFd6HZAr2hiN1dAGNA7V5xN+76fCCNaFcyNYUcKTq+NjFyhXD0bcOGglZOMEa2fOga/X7NQSsLIc0e5KTll+PeI9fVreO60j0Boa0+yWZynEr0qdaaBlcTMdfEWdRdlldM6CCGAeU5oEI9jDRHuB4P1ObT2A39GOXW9AswDvHfPYhuvYJ2O+UIVD3d1Qwt1xxiA0uqCr8elEpsGWZFqQ7CFRnLiSvN6WDG/lTrczfHE34DyJwWIb7TqcgmuDHLlIoRwJ9sXTCo+NMucSuvCSgtJ9Ac333qiJEbQFAzh18JSdyjQMlh+KEwM19kDqAUyv6H26JtyNlctUJPjDLlqppdntxeEO8a58WTN9sC/O/tGvkFzKVC7E6Q3SpEcdB+P+ev2Xtw9v88Hq63j033xtaz6D+X92FPQ8tfn65sXjTNC3vU8PXp/+XcH++uGtdmMg1vPoq0m78HVE9HcHXx//teP2mcb4fCvq6wHw81y5tcP57eG3OPe6pq3HL02RPt7BADucrpnfNWzm11Fd8P3HA86/U2i+81KlLb683pR8m18JnN+x8L3Ybv3XZfg6F/zw5r1OeL/g5PKLX5ez1q9zfKAs/o68429/+9/aR6uRFS4AAA== -->
