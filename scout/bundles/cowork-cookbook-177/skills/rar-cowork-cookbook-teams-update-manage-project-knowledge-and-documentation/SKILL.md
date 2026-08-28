---
name: "rar-cowork-cookbook-teams-update-manage-project-knowledge-and-documentation"
description: "Drafts a Teams channel post on manage project knowledge and documentation status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_project_knowledge_and_documentation", "rar_sha256": "9829779fdaeabfdae982917000616ed978313846a49e1973e787daffe50095ba", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_project_knowledge_and_documentation`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_project_knowledge_and_documentation_agent.py` and in the RCI capsule.

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

Manage project knowledge and documentation Teams Channel Update — Drafts a Teams channel post on manage project knowledge and documentation status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-project-knowledge-and-documentation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_project_knowledge_and_documentation_agent.py` and embedded as the fenced Python below (sha256 9829779fdaeabfda…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_project_knowledge_and_documentation_agent.py` first:

```bash
python3 teams_update_manage_project_knowledge_and_documentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_project_knowledge_and_documentation_agent.py   # or on stdin
python3 teams_update_manage_project_knowledge_and_documentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project knowledge and documentation Teams Channel Update — Drafts a Teams channel post on manage project knowledge and documentation status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-project-knowledge-and-documentation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_project_knowledge_and_documentation',
    "version": '2.0.1',
    "display_name": 'Manage project knowledge and documentation Teams Channel Update',
    "description": 'Drafts a Teams channel post on manage project knowledge and documentation status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-manage-project-knowledge-and-documentation',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-project-knowledge-and-documentation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f94cb2ce1850b932',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/manage-project-knowledge-and-documentation'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-manage-project-knowledge-and-documentation', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateManageProjectKnowledgeAndDocumentation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageProjectKnowledgeAndDocumentation'
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
    print(TeamsUpdateManageProjectKnowledgeAndDocumentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZeb2JbmX6GjHpxZ2CHmwXflWi0kJCQESCABUjqXk3meQQiy87/3QVKE7cp7q+veqoeWHSGGffa8v70PxB8vVteGRf3y+UXzrBxaW2kahV4NWbkLLYq+qBPwVSQ2+IGcIm/ryO7aom5ePr64XuPUUdlGRQ6WL2vLbxvIgo6elTWQE1p57qVQWTQtVORQZuVW4EFlXcSe00JJXvSp54IrkyC3cLrMy1tr4gU14LtroD5qQ3AXivLWqy2nja4eNHet8n6wsGoX8osaqrrISSCgFuD+CpTyblZWpl7z8vnX3z6+ROD45fMfL05qNeDSy123U+larSfdFdo/9BHf1Jnn7vJ7ZQDH1MoDsLQcgJ+m89KrgeAMXHI9H3qe/dR4qf8R+vd/T3qrDpqfP3/Joefny8v0T+1yqA09qC2spvVcyLFKy47SqB1eoXnaW0MD1V7b1fnkwgbYkwevj5XfOBUl9Mt076eHkNfAa3/68lIAFe66fnn5GQIe+fJSd9Px68Sl/Onn17Tovfqnn7/xaTr7HgTADGj9+vV5/mQLCL+RRv5d6i+A6yPctvfl5Tvjps9D78lOsPLlNS6i/KcHYxDtq5dbueP99PM/YuuEnpOkUdP+l/j++mAcepYLbHoq/vPHu5N/g+CnQe88/7HYEoT1n7EEkL+J+wg9HfWPeN/9/x9Yp1HuNe8e/7vs/t4C+Bfo139o23+24CPkf3lZeikoltqyU+8z9MdXbc8vfv3gfrv44bc/Aev/Jxut6GrnzuErKOPI95r269dfPzT3yx9++/VDV4JcA6X1tavTv8fz7/n1LucHDz6pfvpxLZB/yie4yKH3TIf+KMr/Vf/5CulWGrnfrjefoe/rZfrA0GTEm9CHC76rmQbo+p0ff375E4BGDqzpnPttUOX/9m+QFDl10RR+C2lO0bUQCHAbZd6k/DGMGgj8n2q79oBfmwg49kn3RLtJ48KHfv/fzh1QPzlPQJ21Exx97e549PWBkF+fa76+I+RXgJBff0DI31+hIxBX1FEQ5VYKqfP9/su0OG8nVcraa7z6CkDGHlrvE4CnT9MBAFLo939R4tc789dy+P2O19EDy9TFZsKxpku918kXRujlT8sdANzezXM6IDctHKCkHwFU/gh81BQpAPB28luTRGkKuVENxBf1cOcNfPt5Yvb777/bVhN+yR/Ai0OPZtPMAMG7OtCnT8BaP42CsP2Se05YQB/++PMD9H+g/2zVnfkkYw+6wjNyQMOtpsgQqMS72SCoIA0AzNwj98efT58DNjnojiDOkR95j8UgkxPPfQuAJsw/YSQF2R5wPHB6VhZ1C9AcitpXaOND7/oCodOtCe/DqUm6Xunlrpc7A+BqAXPePZkXLdSAODT+8BHqGu8u9Xe7tu4qZgASrPZ3SFrsQXcpUvBrUvNOBBYXeQTc/54ej+uASf2hgbg3Fq+QPOUuVFq1VYa19ZThW4+4gK7ythwwt6Dc67/kU2/13jPk4R5ABDzjPEP6aYo5mBoykGhu8yb7TmNNPfB474X1l7x5FolVT6FwQNMAQoMucqfW8bdnSjVh0aXu3X9A04nTMwruMyr3HJT+63PGY1BZPAeVx1QAfekwBCWg/x+mmcmc+Xqt8uv5kV9CvHxUzw83T4PYFI7H7AZmiPvie0l9myveUOkNnL/kaQRyph7+9qC8B+dJ8wC8rga+VOfqnT/IDODmie89cadErOsp5a0v+VsX+AgcdIc8YCeoclAFU/K9CZzuvmkaglKezr9NBPdAA7OBx0ByQmVnpyBxfM9zbWvyQVhPxfcMB8hibyrEPoyc8AerIMAdJAvgP8UlAjEDneLuOrkAZoK68+si+0YeTXMW0MLtHKAtmHS9V8gA9TPlUAOKFgxLEw3wwoc7KyjzgI+Biu8ebkKrfCgzDcdPBa0pFkU2ZdB3EXje/Jbxd10m9QFXC+Qb8GU/AbPr3R6RfdfzGSugbDbV6H3Rj+F+2gp9367+9iW/6/jeC0Dpp1On/845EEhAkNJTpk7I1QD0ybxnAoFMuDf110dffjT+d10+/2VH8NM/t2m4d9rTj5H7DIVtWzafZ7NHd3xrjq8AN2YgR6LSax6N8tOjbX16FN+nZ/F9ei++T0D8px+K7wdxD+99hv45lX9g8cz1zxD6irwi061d5HhTMj8/wEOLT9z5EzHd/ZKr3rfQP/NjAuN0AJ35vTO9kYD2FNReMBE/OlUzNbge9NQ7NIPgfMnf0+NZPBMuBVNbbYrvivreokGwH7F87yDgVt4C2e40/j12S+mkfuO9fM67NP34kluZ9y/ukqbOAZIaOGjab4HYgAmrjbz72fu0NZ38uGu8lx7ADLf4PFXgR2iajD9C70PuR+ht23Hf3OUd2Hf9Og3Yk0hACr7ead+3pLb3AvZ+7VBOxjz2UtNc95y3/6rEVHhAY8ebpoHivZIniX9hAg6CwKv/ykS5H1jpE04A7E+9PWrfQKABerpgUvoIgXCC4gT1BhK5Awv+KgbIqT3QCwAeT+Z+8983s4qHLX/e3dA+NqR/vLzByjMGz+ETkIP6/dRMbXQGUhcIBOePJAP3/qfG0idbgI9g/gF8WQZjaZr1Xcuz7On3dAGlEQShUMpzWZrBUZwhKItgPZSlcY9maNfyfY9EEJa0LcDvkcFfpxEimlT1EN/DWRRzXJzCSJIA7DCLdS2CtiwXYRgaoX0XtJBvSxMArk/7H/ZOzn2fkCc/Pd3wx4tNEYBSIJrN/PFZzFjdsi97W+V2MJ0yt+1IEiusJxcmh2ZSow+YvSzPFK9zolIU210sarc92MrzalnKNAVKdSsw8yu59V1khGN9TMSg7srNzrqZCLs/IhS7b28933taOSr6OrI2yJ6KEr70yM4hT1HkDEdEr5K8ypmkNLDuGKWXDS0yFC41rL6tie6UJiXjtPs90QqlfjP1JNwnZiT2bSie5VnX3tiQsTuMSEvToHox170q5bO0Jg+EhpmcwJBpdq5Q0TH27YnoVF2vnDmTJ7R0vebhjXHMSwV4E93uUt18P+x2ul7kfMC73kJPTQPdV1bD2hWFrfOdeGgculj7VHVY9WYblbcQyTICFQ0YYVxCL/Mq4rnDBT25Vqox3q7hbMVUUicF5ujiljydV4NhJHzIoze3Jo32ki6VVCta/MiPg6ZjOnVm4/RsK7av2V16tZRWJI/bfboI9XPOpda6W5C44VAnrUlPZay5vh8ke/HShHJdqJcI7tpjbS3hPux3V5/P4CE8a+2Yn+R07McuxWZ8F2t0HAb4TjWVI9zwTkbq1Wl3G/WLUVS3UcREPTO6qPeNfOTjZiVo9jGtV1iFNPlCy67ro7pVcp+WwtBLqzw9YwvmOmfck3hA1/Oc0NvBCbCWpFKKGMbL0HnyfFjhpx0yDuyCmRX2mXb6Veu2++3Q2/5cty5dm2fnW4jxRDxvifVsMPBRUGHLMQ16e8RXaOyha30RRzavzejzot6cSMK6ehktXc7j7CalO8732XniFtSGIeMk3xCioRQXW8uLXY4isr1zDKwKKtpc9BpexoRvrCI3aIlwQZ1M/XCyZ4q1wYWuz8aux0YvbBOnZBjh7J5no5Z2okvKxJIQaNbdOUeYWbH0cihBKDwNn4Uw4oz0bCZfSRWNnOtq4fY2urN2O95sVPp8kbUVqbvyQlPx9U1sNSGKFDTrsc2eZc7DMjLi4wrUAb9adIYX0/PRoJpTZ57dhub7DQJ7ZHU+rk4pHVIcKEDr4PDRPDxWYhG5RcEHs9V4PnS8GyYL3Nml0aa46IJkXPqVHY4SLhSd21c1wsBO51ny9TLIm8yLBzkpmNgSjbBdJcu5ha3jCjbrlu8aAVFmLJlnlX0RQIlrDtz7oye1hqLtic2M8aW8ibOrfEq62vV35sVkMvnm0eYJ1k7rlBpjatxalVtLZ7SORrXbuUnWGywVFjBdVNu9r+2p1fESXM4hXF+yDU2rx8q/8Ozey1IJ2VIqhSFFJu+vY30j+SqCc3FBWnM/24t7HWtbytFnkmud6koSK5yAm2DejbWQEFagr7hzZQwJE3UUYRXopVof9jOJv50jjyNhlR7IyDLNaB7VfanAWxLD2IVj4tcwXFWnc6O7TBxx3Omig3hk65BdC7h4cNJD048YwZugFg97qemYXFj4G5LQIpozulpizrc6t8xEN7ISRc2iJ4h41Yi0JGgKsj6v9gKro1lt1Mec0kRXOZ3lQ87RmuzyI1MycSoYF97jXc3OZpW72l92MnWYtfCFOsPDdW+qfrZkPaGobJS/bTL4SKrqrXaVBMG6Pb1V9nvVEmjZjspirw7c8nhrK3IdoJzTmP62MTbO2hyb2YpkGVGQdlxORqe9N5YJ6oQBvVmvlxyRbRsGG2ZhhoQcl/CLbHXs+NVydjgArJ5bY3LRd2s7SDqNZjpzdcZ6kV/FB2KQ5WCVLeI01FNlJS25bRkd2VjETiJhzjfdVu3Z4yinB6QQRx0NESzfl2HTV4aClSdjwGah046BjwkAyIaLh6wQ0xwJ8orHGFNsz/O6uVS4YM68WTxcU+Uar0lMRXtF2QIPpKvDbQafFR5uR3y5TKWt58RUQsAazK8j+jprCfx6294YmNnQkdzrrdtZrj2U2MI4DNR2tRDaDZOWqZ6ulqhXYUclkSKTIzMcGaJg6SgrZF2VZrAONoNu6ph60hTtKnndQQyrTdaMrAqUTqgLlumMGLSqdbqlJaqus2RRjfJoBitjH1e17Ni7lchxx1QVYGwx8zYnzrTX7lCLUSm0sgp0wLayARP8sqLSxEbPRtPmZLlVzOsY4oFdrVyPysZ4pfYSggannWI72Uk7DUF/aTCnGytDlnXlOHc3/bJk5fRC+kdFj5Xj5RBzbihWpwJ0QpO7llHu2Ix5zuhsEWrewW/QWdwcRLPypWqL+0kwR488Glb5nmHpNJkjWjHPSoRFC1Lnq/kxW50ZtDJaMkgYND75e/bSc0gxSoNWl5W9ls1S7OXIORWprqGuy5iyTGnu8RqLsZQVojAuBhThhLnGLJlzkW9KGc2znt0z2g4gXO3Oz8VsBxTGcL4IVtpixg8HdbO71NSFlfAr614Sd6PyqSLNRyJTuYUw1mGmpMbxvJYaLVZlMqiZsbAbnmlbsriVUYrd2M6YobfTsq20i9ZQBM/KM5FKDgkrHOjsNM5dKaUV1aR31VpwNkdvZVnNTfERajN4R1kDM5Ohe5tiLaNyEaiMvVW0XZMc7Nt2cDZ2IQ+jZZdG0RZJsPQQU41087IOzougjFDMh5GC0mcqt9E4v9jAuUFgW0sOUdxWyIQgqUQ6haGE56ZUIPa5co+GehHUbsM3rITMRpQmq4OeF/WhW7mBa7kua/bXfL071g1KCkIH31hb3iUwnaN9h507NRFrtFuiJQbA1t0HIs9SvW33oUjc5tzIX0buQswN8eQs6bPQHvBz2BQX0FvMcZgp1cGwh3DbN6c0HrWIO5e6WvIdsiJV/uSp+sH19eq8C3EvEDauOeJxlbva1RQr6XLoQM+2rrczNj+I87HrSN1cN4u9uF4hsHCoFtcAdS7MradPcXhRlvtYRodgVPi5Qs+b1WZ3mC0AT0azUe64q89lkywHa3S4epdnzdZXpFOvnFNip2FLi1jisVCnS21tDVEqkl2wCUUG2VjulhcJ9GDiGr+fX9KTa+pwOJS70wgYjt46sezbmMK1gMXpkuGScKaWntsMNbt3hWFu1Q3l0YvbytJ1ZtxSCdJJlKNiTlULHkxfxDN1EqMM0YTxcKxMf21669haYnWIEhUBJlwiGjhRjw7drjaUSsUP7FhbikLgxjqchclsaCOlr+0MTcnItTSZTFV/qXjaRtmqsLMw9VVcSHPHFAV9eTsc9XR7cga0DQ7hasDyOe5s9T0KsAYTyqW98yN5Iw/LlXItzEY46gnbuxzNIDI/D2udMrtKDA7yUKHNKh9kchuWB9nnczswmgPNFCdhybQcb96Qebrig3zYiieqZemRq2BVjjXFM0CBXzdLnUllauhED+/XKKfvx/yghA67yY4bblMF4yFNGTaVQa5qqafCnm2MQ85blLgeIiRujuPqVnbzfjUnjWs2r/acy204XSNJP9kLnXTB3IWADNJciA9LipAIu9jilENZJ329WGdCWDsDGFvHxNAXNOI6NHs4y+1Cn88DjJ7zs2MxCEFJDoDPsjjJPI+CLVS1h9M9k5yXRtjjyRmPkXas/E0m2gLnSMI62PHRAvPmWFGP8rmd7xOJGpMBbsyj3c8CTT4NLnLY9vNtmZJqY+ErzOx79FBanMSbe2Wcnbvcj+dRu2wqaYx7fFUcVUSL4oyUJRjsoq7UoEogy29DQ+X5Mh7hilkrFzynqg3jHOlKpJi24OcH+Yz6lwuGyq5seE7Sj4tbpN8uXO6dvJ1bsRu2vyLsFknBZsbTm/bKlQa8PlBYyWDrgZIvZs7MYbMiOq6+CpuxVsOWtmCZzXlJD9qzokbXVil1K8tPllvIgZsEXIhwkm5QgytLKUOlNcpW8XBsCNTZjqdaSo4ko+4ke4bdDjMewRaX3jU9G6VbcnfYzCVBWIYXlzJD4CJaY05hSZEUuEhdXTMZ+DWu4seGxItyhElreYZlzG1JbEyTpS8eEXwZwBKNhw1JKVe+mJWe7zOb/XmVrXPXnsGWT1Bng2zpWiBL36R2XLNj+y2TEtGWErcK6EE7s3IOirOSx46zmJzg6UrecnEIa90FvRwATB2Ot7Hn4UN6zsstGcBzZCs0xpbyljaYe92I2B83A29uPdIgMUkI6AFF7e1qfkHZmaixxDHe89iiA93/EuKM4JhUGAtgz79amCyCmac9FWMcQ8dlIecgOVh8wZi5betMsCdRMqOsmz7fcfvkuPORkaaDhRlmQ28UtK4ah71A1IZaeFYxk1Gzus5qE3fk0/aCLJYsty04kd0ICcusS2zvKn7lZVGILy0UU1cZv16FprDN2trGdJ1wRdfU5MVxmGkeQ8X5lhBwX+TGINvMnZlLd2Z/KpnNirqCvVnnLCSMr1GM1W5GQruNz5JIinF9uLFJygUdgVtWTD6ioyLNHN5TLox6IwCBdFxpGR373ch1fTSr8oXtuSW+vAlZchaxJUmo4l7sBJw1cTpGCX5jgZ0Sh27ksxReO1ciHYFXb+ElaIKjsyDb/nJWtttQNs96WjP+iUfRNSadjjOGUvgWtPGVvzC51mZYrGZ0EV+o3ogk1xt3S5tVjeb2lkVxZR4yBU/HJs/7hD4q9cHU3GXu9hKb4HS/OQ1jk+uRtJiBjmdRp/By7vewm81HrA6Use6u69nCObOpVW+b8rALg1bBEouK7aWNeN4AegdZdnjsnzaVF+K5tkNYoQ4sBY8Q37ny6bw/XCkusFgLZrvlHA68+W0mLYuZdcmcPCHhrT5XdN/gzdIlbAVVQG+f9TuDdjGDgKU1RqiOmXYYNrt2lTJzUBPhD5sZ2489jMdgZKe2yP4KX8ONG4PtKsI4lJCl6YL2SCEmU9h3wgZphWvP0WzMFzTpH4yR0WlqX2QHyRMVJ6iY+QmWdRfhRxOmSRHkjmFJq4oieWPOYagfHfv9cb5cbjUTdf39jA0IcYNX2CXmehsAa4ri2+tVL5qWLRhJ1IwaW4VRIjmItD+ASg56LwgOl+hiMTtwZWz7lXq0b22PuUfbvx415wDbfnQzNsxS2+zqqxPCeZzx1yXJeBfXN8LVLHZvPblZoH3oc32hIf2tZ+JqD5LSuBwkYjOqeKYFBazTJytVx4xd2Sfn6jTueu24e6XMihUe0T27TvSb4eLb3pzpVpwrxwXrl1S8lGuPNjb7/ZVyimO+GY5nhL5iwk71qoGQHN3XgkXlM61UsujYgRkhFwiS4aJg05NGbhPBjT8erc1BU3BcX/hWpMEFE9WjCnONv4UZeDgmcnbjrjFOF0EHOhCYMjiOPrhgjp7Pf/nl5ePL9FD7+Wj6v/v+enow+D/2fPLxKPHthdb9wbRnuZ/vsj7/tzX97eNL7URAz8cT2ybtgueDzP/wvPbTv/h2ZGI6PF4gT2/pbu3ba4DWCqa/n3qJcrdr2nr42hRp91xhd830hxvN1+cD85e7C7Jyevr+vcmP63dr22Ii9qOJ5P76M/Pc6EEynQb1mzbuAKIcOc1XnCK/enU5ueD5ygVYjr0ir+jLn/8X2VAhR7ImAAA= -->
