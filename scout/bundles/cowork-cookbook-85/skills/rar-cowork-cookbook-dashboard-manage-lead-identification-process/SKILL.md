---
name: "rar-cowork-cookbook-dashboard-manage-lead-identification-process"
description: "Produces a self-contained interactive HTML dashboard for manage lead identification process - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_lead_identification_process", "rar_sha256": "ab534ab02f978f85512bbab9aad6751a60e015f5f05a32559e742d04f07e1a22", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_lead_identification_process`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_lead_identification_process_agent.py` and in the RCI capsule.

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

Manage lead identification process Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage lead identification process - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-lead-identification-process
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_lead_identification_process_agent.py` and embedded as the fenced Python below (sha256 ab534ab02f978f85…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_lead_identification_process_agent.py` first:

```bash
python3 dashboard_manage_lead_identification_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_lead_identification_process_agent.py   # or on stdin
python3 dashboard_manage_lead_identification_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage lead identification process Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage lead identification process - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-lead-identification-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_lead_identification_process',
    "version": '2.0.1',
    "display_name": 'Manage lead identification process Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage lead identification process - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-lead-identification-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-lead-identification-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aef2cf17888ccb26',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/manage-lead-identification-process'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/dashboard-manage-lead-identification-process', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageLeadIdentificationProcess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageLeadIdentificationProcess'
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
    print(DashboardManageLeadIdentificationProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZejSJblX6G9P2RkE+FiEYuiTp0zCCGEJEBikRAZeSJYjEVi3wTKyf8+hiT3yKis6u7smQ+jOB4uwOzZe/ct95nhv704bRPl1cvnFx04GSI6SRJHoEKczEf4/JpXF/grv7jwB/HyrKlit23yqn75+OKD2qvioonzDE7fVbnfeqBGHKQGSfBpHOzEGfCROGtA5XhN3AFkZchbxHfqyM2dykeCvEJSJ3NCgCTAgUN9kDVxEHvOKBUpqhxKrJFPSF6ArIaSoF4D4lb5tQbVRyTLkQVJU4jj3YdlAPhwPXdAmgggXQyuoHqFioLeSYsE1C+ff/n140sMv798/u3FS5wa3npZvGkj3xXZQj2kH9TYPbSAghInC+GMYoCQZfC6ABW0IIW3fBAgz6sPo/kfkf/4j8vVqcL6589fMuT5+fIy/tPa7K5gkzt1A/X1nMJx4yRuhleES67OUCMVaNoqu2MJEc/C18fM75LyAvn7+OzDY5HXEDQfvrxAlKq7yl9efkYgtF9eqnb8/jpKKT78/JrkEJIPP3+XU7fuGXjNKAxq/fr1ef0UCwd+HxoH91X/DqU+PO+CLy9/MG78PPQe7YQzX17PeZx9eAiGruxA5mQe+PDzvxLrRcC7JHHd/Lfk/vIQHEF/QZueiv/88Q7yrwj6NOhd5r9etoBu/SuWwOFvy31EnkD9K9l3/P9BdAKzon5H/J+K+2cT0L8jv/xL2/6zCR+R4MvLAiQw/yrHTcBn5Lev+k7gf/nJ/37zp19/h6L/SzF63lbeXcJXmLdxAOrm69dffqrvt3/69Zef2gLGGnDSr22V/DOZ/wzX+zo/IPgc9eHHuXB9M7tk+TVD3iMd+S0v/q36/RU5OEnsf79ff0b+mC/jB0VGI94WfUDwh5ypoa5/wPHnl99hrcigNa13fwyz/N//HZFjr8rrPGgQ3cvbBoEObuIUjMobUQxLVH3P7QpAXOsYAvscB+N/9PCocR4g3/6Xd6+tsEo+auvkvSZ+fdTDr2M9/PpjPfz6rIffXhEDrpFXcRhnToJo3G73ZZyUNeP6RQVgdezulbABn2BN+jR+Gavnt7+yzNe7xNdi+HZng/hRtTReGitW3SbgdbT6GIHsaaMHCQT0wGvhYknuQc2CGJbdjxCNOk9g9W9GhOpLnCSIH1cQjrwa7rIhip9HYd++fXOhhl+yR4klkQfD1BM44F0d5NMnaGKQxGHUfMmAF+XIT7/9/hPyv5H/bNZd+LjGDpb9p4+ghmtdVRCYc20Kh40MA0syJKLRR7/9/gQaiskgJUKPQozAYzKM2Qvw31DXV9wngqIRF0C0IdJpkVcNrNtI3LwiUoC86wsXHR+NlT3K6wbxASQ2iL43cpYDzXlHMssbpIb+qIPhI9LW4L7qN7dy7iqmMPmd5hsi8zvII3kC/xvVvA+Ck/MM+jJ5j4nHfSik+qlG5m8iXhFljFKkcCqniCrnuUbgPPwC+eNtOhTuQHa9fslG8gQjVPdIecADB0FkvKdLP40+h61CCgPMr9/Wvo9xRrYz7qxXfcnqZzo41egKD9IDXDRsY38kib89Q6qO8jbx7/hBTe+0/vCC//TKPQbl/7qFkP6xCXmnfeRLS2D4FPn/tYEZDeREURNEzhAWiKAY2ukB/Kjh6KBHCwf7h7s69yT73lO8VaS3wvwlS2IYRdXwt8fIu7ueYx7Frq2gDhqnIW8IVHe591AeQ7OqxiRwvmRvDPARQnYvd9BimPcwL8ZwfFtwfPqmaQSBG6+/dwN310MgYbDAcEWK1k1gKAUQCNfxLlCraoT16SIY12BMzWsUe9EPViFQOgwfKB+BSsQwwSBL3KFTcmgmzMSgytPvw+OxxyoeHvcR2PCCV+QIM2qMqhqmMWyUxjEQhZ/uopAUQIyhiu8I15FTPJQZe+Sngs7oizyFgf5HDzwffs+Buy6j+lCq4zsNxPI61mcf9A/Pvuv59BVUNh2z9j7pR3c/bUX+SFV/+5LddXynBFgMkpHl/wAOAmM6re/Vd6xlNaxHKXgGEIyEO6G/Pjj5Qfrvunz+08bgw1/bO9xZ1vzRc5+RqGmK+vNk8mDGN2J8hZVkAmMkLkD9nSQ/PXLu05hzn37MuU/PnPthjQdkn5G/pucPIp4B/hnBX7FXbHy0jT0wRvDzA2HhP81Pn6bj0y+ZBr77+xkUY01OhjG93wjqbQhkqbAC4Tj4QVj1yHNXSK33Cg098iV7j4lnxkACyMKRXev8D5l8Z2ro4YcD34kEPsoauLY/9nshGHdFyah+DV4+Z22SfHzJnBT8td3QyBswgCEu43YKwg47qSYG96v3rmq8+HGjeE8zWB/8/POYbR+RsQP+iLw3sx+Rt+3Ffe+WtXB/9cvYSI9LwqHw1/vY912oC17g1q4ZitGGx55p7N+effWflRiT7K04j+z2zNpxxT8JgV/CEFR/FqLevzjJs3TUjTMye9y8JXwN9fRhn/QRgV6EifjgihZO+PMycJ0KlC2kUH809zt+383KH7b8foeheWw8f3t5KyFPHzybTDgc5uqneiTRCYxYuCC8fsQWfPZ/1X4+ZcECCFseKMxxKXLquBgRzBg2YCkKJ1zXcWeO49MMhTs0BjCcCqgAoxySoKgZYKaEj00DjAG4QxBQ3iNav45dQzzqB7AAkDOc8HyShjOmM5whnJnvTBkoFGNZBmMCH3LE96kXWD2fRj+MHBF974RHcJ62//bi0lM4cjWtJe7x4Sezg0NPGbePLLSiwUk+o1iKxSbj2oWk+EslrRlZ45ioxQh+PsxXtnR2XMmMqGnk01i7rKMFxWW39Y5UrVVsdNuTsRRjuXHI5La+UrOJ6u+xg6asso3OTLVqzrH2TbJsnbTkVsUP/LFq5FKQQb8+7julxgvAd65S0kEA9xqeu9wtfY9CJ8HFmiVD1clLsS8uWm+VoHS3aR3poXKjT801sPRq56M0CmT8uMZyTp+iR1AcCl90llm1NOqpzU4mQ3dOffzIF6tzlxk7usTDBF97vIbv1qkfBBMyxnw/q/rpzJZQ0FlVv2d7cLKz6ZU4ysrkcHQOWbc1dvghKo/sqczqcp6hEp4r9rFoAM/o+tK4BRbaNe00yU3pyPDRAAoxnAqWPcxOwnLm1tVGJWzZibbHY7GR1tHark4gt/GVWTT8suCpgz9d6Q0B01MJeCryt7mPni9mobM3zjCkRNlL8eTG21PS0YVbk59Us6D8kPcVMbaMZJObxoa08YOdElOBXawNPEvDm8zPq8nKP+xTa7dU95VCDA3uMO5CSPFyPfgeczoca6NGB6JLj1SYLfcmnVfEfjcUa08juKpS1jQe32zbOkdqsh36KtvpnV9dj4FDGsPF5oAVA3VwJIdanFVnQlFc4WzJXY8n6UB5rDvHbm2+KrKkXFLdaT9lvOuysTtGYGs3mM+dpjl1fMHw9RoXxXk/tbGz1m5UVhaHyq+3DD8MnVhga0ci+mRinwc21jO9rugq0ZdDhtaFaoVFUDv4NcqN2dZzh+ViQyV8dci9a+lM+pvj1CnhHwibOm404qTau97PYDvOaWy0SQXTPVmyZVnqpuou17Y9oW1XWKqINTAve8IJwszK1kxtk9Nzc0IhxmFxO0ymy82t9YOJsZjw/SnbYlpmA3Z1afRJ0YdEatsHV7MjnZVIccCIZpH2/XndNyd/d+pT6xKbaaUH00GOiU65SvJUXYNwuZ0W8yjz8ZBh1qZiKKdN2niZruzoPVmLutAZhXSJxFKvuaAGlzWv8a4Lm+x4faqxii4p++jNY0e1j8OEMtI5jpbHG2ZcT6WhyNNwMC6iqOdHQXepuFij9kHvjHbvJOR1onhpWYXooHmzqhmA0JjqlmRg0Qhqsgjx26X2gqLfRp2Kk/3Z21X4cpdewmBXC7S6iSDt35oQc/f9RXGcG7/u4ilNl/RhB2hviiqFJdGldhzsRsRPEjhGZKPxsEpOGpHFOJRkFUw+y+tCIISqPFW33jTXhr1hsLQli/RI3zyluA02vlyfCG1Ft7QrXJj5PL4BBZelS15dL+zBaXxn2R95ZbF0thlmB5du2poilVK5VLH4Bc3zXcMLjDJBh9Kk5tv+sGPd8GRwWGGKPitvaHPXdSEuR+tL1oRy06ti6LR5i2arRSDRpyGmuLTueMy8ukegm1EmNzhp1Xt2Jm7tiMxBzOYyJoMdtVGI7bFysxm/ELNSEKZGOCGjI+eoHqplJ6x1VLkh3GiyUcNMNo+33JKDC73ZCVk1mbhoIkbDrCzA3F1WnTvkedfDrp1a2Gf6aiwOPXETJGo4F7IRO37UYImmzaWu4uKG5yQrU9BbxdAhEHQRVe2hxLqdRQ6bypluZhoaXydpGd8InQwjbJ3wKs/j9BznqdtEWl+X8nGxYf3iMt8XG+OaqQuHyo8co0+vG9HhBBh9eKEfeqlaWDwou5OQUdd5KtR2vtlGWHoA/FwxUM63T15U3CjOFcREdzB+kW3dfnPE+915cZVi3Gzjub2csahqTTBGNc9SmEyLfBCqXRdoxSHHd0Ozaaw2lCVtPqjRklhOJmtlfqy6QrSckyJHi3Z5DoaZTULQlkt8djlaVeehbD5JFuY6XTJsijfWXqJ4srxMuRN5JpNovjmo7cnNlPCgk510vfUnjzLyqcVt2qS92vJifvQvuKJdCIntaYq/CIVzaN0LGkiDtdsMOk2aRHg5lpljbBInEq+TamZ5dtAc3J49JGDnLs9MPsuUKekPqWfBn4W+XUzPSmKYPXrY63qtYapeCEFFgsPN4dpse9Cy3ZKm8UDMVqR3uvBrDjcdnbqYNs/iM1nGE5UpdWzqckVTHE7KrWdRv8vXx4ya7YB5DBZd61B0mLX7tWUqh/MhnpB6SMrkacubidfpGdAIeblJdtlao6aiEa1OaN/efB/3YGl01/W8WpoLAtzkeg8LSs7L+41R176eZmlw3Ste14mpQCY7R1pejTJdOTmHXXjhWFxPcVJOYcY5a8wMo8DEV8ZaMhf8POVWkWvbYH6Y5ftDx6e3yvFWE9zLD7ZZc6IW4BfYXxxqYbJVwu1NvhTHc4reJkGFU83BXFqesG+2HW9uuVNoKSRe0VmoAHGSiB2mplq9ve3mHXdjUzLZL+zVtqmofTMpB1Qti2KDl5ah8n6+tPphG2VFt7a5TQwdf4Q95o61ulMkJ35hGUpXrlf2RLtIDZXmZWWb9MLcl/MqcIb9aT4rzrormtlGpLlpTaCDGd8OWyHMzITfZ5GIRxIM+6PdKQbTzmYSIPrtfmHtFzOfOZ+SXFhZjkenxjkrtYMuXGDxctMz2RwLfKEdDj4vhPwNmxiwJ5kM4dWzPTIN597Fo10F3VzPF3EVODWOQSf2txl72SboJDtck7z3jL6oZu1iW7TRMHV23Lqe0cNJPyvScOT4HtPPnNLiIi8ECyLfJZta7g/yenqpenbSxp5YhgV+ndOSQSyZYhbjQJoktzCQ9CE6HwpzzU91gbt1xdmUSpshlfjYiMz0OHetWbOv8SOOBRyucCdrEWxd1Awh6QmYQ97MetkNbiljzZVxXX5wxYkp4C1vX6N5djqExZJe5tpi22IZq516+rhxo9ASapJbDWuq4rNJuhRVUpg2FrmMTgsl8s0NYKSTpquY1QsXM2wEvTfs3andOF5KiWK4BTkppXybSPq50ggt1bY8ZvPEdKj4FRYauSqbuz7dTzAzWuPuwcqpo2Nyu+B0UXG5OJbUVmczyfAu26JfATaufcZvpkWiBbHPx5ddxmVmi3biVTli86Zp035xdMvN4FqB6pcRkekZzsv6YnBdizBieX8MZANQm2Ps+hN7W5hWEMZLaoNXYdqpAikUKODl2GyGlQL0sEVPcQjKYnnQL03Ol9VKW571jBs8oezigWQ4raM1sZnkvF/iTLCoYlZYL69XWKDt41E5mVye6Bhz7hdVPd2sxTjc33L1IG3zZVkOmC/x+nq/SQ8rT1gqu53oXOfMjXV1zoM0dspsc3XOxVbNQvF4mXt2u7y6pu/WuUbb9J6eKTelii+SNEuZbCJtr3pcoMS8lmYr9bCNt63GL8jsEOLLit97Z7w8xMlBtGWOvIm5XDaZb4WyTcO+/nbdcVrN2VqwwrSGV45JSzTieh+V0YIgu010njVb1fXLRVeV6+amOblyERT1xkMO3anVNdj3drln5NleV47zq1JnWDm5nFfO9GThW1ticVDwCS8sjydlfhUX3GHNL/nrPDm56s0+Ldko07xytT7rSrVwRJi9S3LPlTmaJlVE9CvpnFGox/Glvd5bZtFFMYNvV2daFqp9mXdc7va9ZE59BnbyMD/l8rqhnOYsRwq+oJfR+TrsOX6XeReDKQc6bZKlcJxncRfUjHtt7bUa6zpGlztnOWt6YrbakJtOmOg5OznMxYKChQ5k1V4zdyemIy5NcgWGdqWnrGhdWeuAqkZIZw4tzjvXuqnUBcyFxXERmoAx0qNZFIuNeCacFaA5VFvOYd9NWiuwBm3hlBO7ZMOjq7VC1h5K3WJZiW23gZKRu6NwBniBLwlwRbcNsSrbGReapGD5+eSkBkc5m0ulU8tzSkMd2px6zUoRNJJxDk27JsomqgORWRMsrQ3DNXAMjDyHDMuQUU3RaidIEx/uverTTlqC+YV1J2geTGnzSDZMtSI136LXlLxl8/UtmYYcvZ6reQZL9L676NeKYCOhaoghm83XtiJIJT4ZcrilhF2Vr6pS3xQoR/GprUwL9cSsYahJtMq7FtMaw1XWpG6KtSQoLrMVv28qV9obfH5hmxuZ7lQ7PcS3DbaX0S5nhrOC96eg6+mEmR0UmjsPAWacwczXVFG7oSAXIUPtyGBvs4Vq+sTF0fsqn3ECPUt3jt+DqSLqMW5takhGxJRbVq6l56pbBElOTslZtYq11S2uXXc942R9LaDMznHplV6rDJgUg7uxTLVaHYTjdK9Wm761K4eYJQew0jOLCcML25nJbrX1bxsJZShD8QRKXGRMZwzEGbbmaof3yzNOLSQxz0CY5XrJXpjzmd1luiytlORMe6mbLjGj79YY5Q3n3WG+OlfBdFrrTHixOF0ka/cyC3VxHeRGonRC611ZjSpEvslRIOyNoZjfWMJHGa/tg1UdNJyv84dlVxEtsXZXSYRF81BpuVDtFjtuGgm7khGr446BFexYEn3soDsCgq3KdrQlFi5eOVZLABY/MovqBmC8SMAmtLI5kEPmKjduJQtR5m3Y6NxxnZY4K+ac23Sr0Z7IOPOBNj1z2mp9x87ms6oYoJF7cjr15qm/4vzM8rsJismnWeJU69oKt0nuq8PFoVyXY0gUeNFQUEWbnAMzv+CLzksPhgm6+ZQB24jqWYrn8ijAon1E8zNqveDQEEj9xKwk1jmlXnZhgDDEqzIr+Op2YovVibRkOZgqlS8OVynI5jW6IHjbausJti3wbBcN12VNzSctClaaDDyts9GeIaw6FLupptWMQS9hH+obu0mn9x5BMJBsbOJM0isfpXQZYJNatSslo0HtnzdAUtm8YLkTezBtDLutJvYJPVvZ8SQfyilV28zy2Af1jZUNDrYIfID7wcowruxGSkpC5jwKOovd0MyUzGKc2LD7VhRC3yrn0SZXPUiR+1vNhpxzDq9anztTSZ5414ZTjNyfit48K11jRtNuvsq12bbfx9e5YJAnNDvj81VNgZWRo4aTdhwKaqBxsw1faRzYVvsl1UXJfGmiF5HdOhf7SsWRYnZ8X0e4CQpDV/HV1jzAztw4V7QokCR61QNyksdAH9riyKOoe/Bg0ljbSD1M/cLNjsw8JmdZybBRofRefO30xyHa4ODWTN8r+8mptmSIfIqaOTUxtqHncSSwcxxctoZwvRjmPq991bqIXCckm6MONopdoSsv2M49qjNUQSMAKi+WhJpdJizfCOa822Mlx3F/f/n4Mh5UP4+b/0fvo8dTv/9nh4+Pc8K311H3o2aowuf7Wp//Z+r9+vGl8mKo3OPgtU7a8Hk0+Q/Hrp/+yguNUdLwePU7vk3rm7eT+8YJxz9teokzv62bavha50l7PwT++OK29fjHFfUfzm7ht7S4n5y/Lf64WRfAa742+deyzRvwMv7xw/iKCPix834ZPg+l4eQBejD26q8kTX0FVTEa/XxFAm0lXrFX/OX3/wMJn/6yXiYAAA== -->
