---
name: "rar-cowork-cookbook-adaptive-card-set-employee-growth-goals"
description: "Produces a reusable Adaptive Card JSON snapshot of set employee growth goals status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_set_employee_growth_goals", "rar_sha256": "eca50196ff9593f72c56e6c26345d8278c3d82c14ff97f41ada999288744a749", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_set_employee_growth_goals`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_set_employee_growth_goals_agent.py` and in the RCI capsule.

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

Set employee growth goals Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of set employee growth goals status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-set-employee-growth-goals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_set_employee_growth_goals_agent.py` and embedded as the fenced Python below (sha256 eca50196ff9593f7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_set_employee_growth_goals_agent.py` first:

```bash
python3 adaptive_card_set_employee_growth_goals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_set_employee_growth_goals_agent.py   # or on stdin
python3 adaptive_card_set_employee_growth_goals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set employee growth goals Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of set employee growth goals status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-set-employee-growth-goals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_set_employee_growth_goals',
    "version": '2.0.1',
    "display_name": 'Set employee growth goals Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of set employee growth goals status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-set-employee-growth-goals',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-set-employee-growth-goals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a00454dbfeb1bd84',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/set-employee-growth-goals'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-set-employee-growth-goals', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardSetEmployeeGrowthGoals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardSetEmployeeGrowthGoals'
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
    print(AdaptiveCardSetEmployeeGrowthGoals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZPi1rLnV2Hq/WH7qbsEaEN940aMEEIgCQnQhnA7ytr3fcfj7z5HQFW7n6/fXE9MxNBdBZLOyT1/mXmo317Mtgny6uXLi+ya2Yw1kyQM3GpmZs6Mzvu8isFbHlvgZ2bnWVOFVtvkVf3y6cVxa7sKiybMM7D9WOVOa7v1zJxVblubVuLOKMcEjzt3RpuVM+NkSZzVmVnUQd7Mcm9Wu83MTYskH1135ld53wQzPzeTelY3ZtPWMy+vwALLdZww82dhNnPMOrByQKz+BB6YYQLewRrFNdP6FYjkDiag59YvX37+5dNLCD6/fPntxU7MGtx6eRdnkkZ2G+bJmr1zZifGgERiZj5YW4zALBm4LtwKiJGCW47rzZ5XP9Zu4n2a/ed/xr1Z+fVPX75ms+fr68v079xmsyZwZ01u1o3rzGyzMK0wCZvxdUYlvTnWwEpNW2WTvWpg1cx/fez8RikvZv+cnv34YPLqu82PX19yIII52fzry0+T7l9fqnb6/DpRKX786TXJe7f68advdOrWily7mYgBqV/fntdPsmDht6Whd+f6T0D14V3L/fryB+Wm10PuSU+w8+U1ysPsxwfhoso7NzMz2/3xp78iaweuHSdh3fxbdH9+EA5c0wE6PQX/6dPdyL/MoKdCHzT/mm0B3Pp3NAHL39l9mj0N9Ve07/b/L6STMAOp8G7xf0nuX22A/jn7+S91++82fJp5X182bgKiu5pS78vstzf5yNA//+B8u/nDL78D0v9HMnLeVvadwltqZqHn1s3b288/1PfbP/zy8w9tAWINpNxbWyX/iua/suudz3cWfK768fu9gL+axVneZ7OPSJ/9lhf/o/r9daaZSeh8u19/mf0xX6YXNJuUeGf6MMEfcqYGsv7Bjj+9/A5QIgPatPb9Mcjy//iP2SG0q7zOvWYm23nbzICDmzB1J+GVIKxn4P+U25UL7FqHE9A91oH4nzw8SQzQ7df/ad/x87P9xE/YfOLPmw0A6A2g39s7+r090O/tjn6/vs4UQD6vQj/MzGR2po7Hr5npu1kzsS4qt3arDoCKNTbuZwBHn6cPEzz++m9yeLsTey3GX+84Hz6w6kzvJ5yq28R9nXTVAzd7amaD0uAOrt0CPkluA6G8EMDsJ2CDOk8AwDeTXeo4TJKZE1bACHk13mkD232ZiP36668WAO+v2QNYkdmjdtQwWPAhzuzzZ6Cdl4R+0HzNXDvIZz/89vsPs/81++923YlPPI4A5p+eARLeyw3ItDYFy4DTgJsBjNw989vvTxsDMhkodsCPoRe6j80gUmPXeTe4vKM+LzF8ZrnA0MDIaZFXzb0aNa+zvTf7kBcwnR5NeB7kdTNz3MLNHDezR0DVBOp8WDID1a8G4Vh746dZW7t3rr9alXkXMQUpbza/zg70EVSPPAG/JjHvi8DmPAuB+T/C4XEfEKl+qGfrdxKvM3GKzVlhVmYRVOaTh2c+/AKqxvt2QNycZW7/NZuKpTuZ6p4oD/OARcAy9tOlnyefgyYgBajg1O+872vMqcYp91pXfc3qZxKY1eQKGxQFwNRvQ2cqDf94hhRoAtrEudsPSDpRenrBeXrlHoPyX7YI8qNF+L7F+Nou5wt09v+/F5lkp1j2zLCUwmxmjKicjYdNpyZqsv2j7wINwZ3yPX++NQnvEPOOtF+zJAQBUo3/eKy8e+K55oFebQUMd6bOd/ogDIBNJ7r3KJ2irqqm+Da/Zu+Q/gkY545fwFEgpUHIT5H2znB6+i5pABSdrr+V97tXgRVBHIBInBWtlYAo8VzXsUw7BlJVU6Y9nQFC1p0s3AehHXyn1QxQB5EB6M+AECHIHQD7d9OJOVATmNmr8vTb8nBqmoqHb50Z6FLd15kOkmUKmBpkKOh8pjXACj/cSc1SF9gYiPhh4Towi4cwU2P7FNCcfJGnIIb/6IHnw2/hfZdlEh9QBTjbAFv2E+o67vDw7IecT18BYdMpIe+bvnf3U9fZH2vPP75mdxk/gB7keXIP3W/GmYH8Sus7sE4wVQOoSd1nAIFIuFfo10eRfVTxD1m+/Kmb//HvNfz3sql+77kvs6BpivoLDD9K3XulewUgAYMYCQu3/qh6n6ea9Bnk2ef3PPv8yLPP9zz7jvzDWl9mf0/E70g8Y/vLbPE6f51Pj4TQdqfgfb6ARejPa+MzOj39mp3db65+xsOEtMkIyuxH2XlfAmqPX7n+tPhRhuqpevWgYN5xFzjja/YRDs9kAbCe+VPNrPM/JPG9/gLnPnz3UR7Ao6wBvJ2pd/PdabZJJvFr9+VL1ibJp5fMTN1/d6aZ6gCIWmCRaRwCGQT6oSZ071cfvdF08f1Id88tAApO/mVKsU+zqY/9NPtoST/N3oeE++yVtWBK+nlqhyeWYCl4+1j7MS9a7gsYzZqxmKR/TD5TF/bsjv8sxJRZQGKA5vUky3uqThz/RAR88H23+jMR6f7BTJ54ASB9qtRh857lNZDTAX0PQPJuyj6QUAAnW7Dhz2wAn8otW1ASnUndb/b7plb+0OX3uxmax/j428s7bjx98GwVwXKQoJ/rqSjCIFYBQ3D9iCrw7P+2iXySAYAHuhdAx7VNbL4gcc8jMRLxiKWN4S5uL3EExZzVkljZCHizFyhYQHjoArAhSXK5WhEoahIoCeg9QvRtagDCSTR37rkIuVjaDoIvMQwlF8TSJB0TJUzTmYOdc8JzQE34tjUGaPnU96HfZMyPfnayy1Pt314sHAUrd2i9px4vGiY1E0YEawh2UDYnh7OH+wlHq5lSOptERPIwHPE5Ubu0jKTGbXM6wVRs9fvhwKL+8qznWLw6c2ivkFxH9qhPifyYqXjGoCtZtUKisxBy5S6R9fx6FoVCVcpATK9to6aclp5bZBvWkT3WbXaRF1vTvQrcEtJa7qAVGUq6jjccOv6608uKo0O10jXZRNkaxiDImQvGqbkuK23ow3HrgTZ60UKjuAaU6UpwBEZuA/raSB1z4kLHYDblTlgNGKbL7K22IhX3jtUc9ZAKx7vesj0iXNjq8QBvy0o9l3Rp89xSaRalJVt1MyJaYcV2IXNRmV3hSDAunKMnzhqho4ss6xVxdSA0ESKJZXiukYtybLXQ6BR6MDrHZMpt2TnKZrgx20FL835Y1gEtYNqCGaJUTzQ9nQsxVyG0mXomoYfz+UUST6TgXXW91WRW0A5sWBrM9nplxZUwSHax5AuNu+6bQ4VTJw7x0y1/Pl9JkMZz5NIdKV4uR4TbJmtKgkec1+lx21uZj7CXxMlqrpXiRC7J800atEI3Qxe+zPO0FMphr7FYa1K4dFxe10Yp+svlTWUbs7268eLgqFo5WhycGlHmFmamXnW6tjarVV+dtGKTHcY4xg+WLiD7xbbrRhBe6LrPQ5nKu22HE/48G9iqE4rI8aIkRFyZrw4394ZI0hxbbIPtURsKPqhVZ7jaF9PayvstErmLrV4aGzUQuiQqV4GdrWMIL+JB6zOImbsXObBC3rJO9ZoUdgwaBAsb97W4dPvxCkMRYYaEfiu0pZfx8qrezyuuTa6ZRIcindShPRairzJXR4y1ncKVUnoEP9l26+AOdrLh7UBnRhJsQjdE3duaOOzYY6IXaBWKx3Ej2nh6gVe9ZyjruXExJSVkfNoSrLk+bhWzcaSslpVDkpSNVmjGXNINeKml2FkJIpZrZWZ+bZi9HMuiO+p0TPmK7lz4SxQzEDlCmzL3N7lO9domabLDNl34IGdycZ5HRV1H+nHQxVHC1/RZcex9tfTbPC517Kpoks1yORp7AnRmjYuySi7esTlujzgmGd5a2HDILorJiOBY04v2km0wc5lUshqy1liWJhaW7S0RblY7OkTUQkZsJwrgHlYifQ9tjsj6GBqnFNakKhz0bkA3e7Zkho255Eq4yCSJY2l3sZavFtsft/Z2EG7welBvFb44Hk5HLark+iINnDZCzPnoMNtTvuFFnb1Bl3DL+PBQ04SXLw5XGBYPl9qs+JXM54kuQGNytqQkyBSzW6aLHPhTk/gbuoqzRAGxIit8pKZDji+3vrZAZOjsdnvVZ/hwOC+CK7a7LLZGFioy3iiZHMipFwtbCcwuqRdcSroZioJJiQTeb6CzoGnWqUrg2ym+kqOXsgSV0WJBbdewVRqCJpht32cyp83Dds8l0O3GK7qrWlSaaDiuG0F+86+5dTse1ivWsoUIMttSK45Oyq08fNVbZeEkKLzAFHN/yFuPugkVb7p7EhILZyH6WZOlZJ6pHi3ku6s1wDgKMWQuEc6G3h6snOBlt28aTN6ovcfS9tUt4yMkaxvXMKPxuouukeWDkAtWOb+wVvHBaC+1sruR/opKM7EsRiWks4gkRP0ILcRzX3WiokKKJen745LlT2uWmi9OBrdartQINdR6HRVHeuPHa9kMRTvdswtrJEFeNwl3GknKWBRnccgj0QtN3rKZS0Ms+1Dacs6ax0NB2Nqsbh5W/A5FiWMyrGVu2RPj6Ftr/URIco2RrcJtPI6+IgtMbLIrZHdCTXIcG+r1ucgQD12WsrIZLTc9cDVJn5ww7DFyXo8erJ/W18x2BtgM/PhI9oa4uwCPxKXG70Lrmg3Q9kSlQh5cCdfVrGFk1sV+7/CmHtzOElPSArU4tInS1vZp43ln0gFjtrGkzs6mJBKUknEhVpFm5OPBdNCzNu41UV1U8cXnOQ6VmayNOZI+8kvJ3mnSeb+nPSk6iJQA5wrP0XZKSZetSmmlm5SFoQbURuHlfYeJBNfC4tDreCLtS8uIKNevr6i4chp5jtuXi1bWRKha9Vwi5G7Z2xSlnsFADDDuBqX7BjqoSMRbh6utHYzrgokwLOp3KEOcWC+bEwmwzdKJ+lPe03HJ4JKMASciJAz6xnDXMOZW6BUPhdhTs2e9mpKt1B8KbLWSBl5I5sqAkX3Rb0LsEFRkQikYLec7DDTT/B4UT6Pwa1KBAUSXlcmw66OvJEcoDkrnwpjzdYCPZosK+wvW0kwybo08D4swVfaU7/YHk4GZ3uUdlMu46xaK8ZE55iwpp2rr+hrmtrfqdOZ6JJLO7IX3qDzNT7pQyba4bJX5YMi0UYt+eGqhWj464yLPy1NkFd6ebuc8pCztVAlMukOaZsOIodpdgCMQMuVYUrspmiDOqe7aOZ5aMg2LseiCZTZV1hhjCaYQZNxHp5TkVCUbxGhOFKMakop2KYbdoZ9vx2B1GUKfRzLN0NKA1rAz1Ou3beOPzVkeBIZVjCra493InUfGiMjC9wZUxDxofj1dbyfaKhYw4S/nW1cYKjG2o93tJlF7xF8lS09KfbhTk+ZyNTDRy+LchWGny0tkrfZVel4U8qY9cQe7jWPmjJNclik4yspCoZFOqvdEpySBsLq6xVgZDijz2zRUGfngGyO5TPqSZtZxeRJDP4VcaIkKUt3flsEqOISpmvuVePaO2QjvezO32LqXenOaetwD6DjAeC7W0DmpaFYdVUdb2tQeOnQXbi1nbtjQQ4nYZTLizegoN7WtGJLillQfSKR5SZte5HKuGKX00DPUtY2VbRXN1WEXpxxkgbvrYuWvDZ4Kr/x6Pm7OsJpC5/iGI6WzyrKr5p2OmK12OWhYQ1cB04J8qFfspicKFFucXYVx1SNHtWcnEPLBwCJm4NVUi1GdavRQLp0RD4nCZuWFOnDWgSKLZULWZ5DtrlPajHH1/Ov5iAtrRUxVtBh9UT+4+g1EvpFoi9uVry+BOpKDea4swhwJ7HidC6QaqSRtxcdllvWJeqmW6yFFR3yXrux4wTTX/AJHh1SoMNrVpCh3QWW6KIFjKsatV9qtKkpzgojXya7Fz5SIa3vcSvcDa6n+GOrEmPYMqKTCItM2w4kXk71tc4vmwDFVirjrDj2V0u5m5Q4LFfsr7PpbWMpxN6uCkOE2yXCNe6zhpXm+vvJJ2SMxXTHELa0aU/cx2m8HvWjPtWnFkZyDOqqT+1K3r5p1SZLAZVaEy9l0wF4hfr6k2kNfyWf/ih7TG6M4GbD7qTWcOZ/Gy8S0oNLG17sO1gaXV1l/V/DDTZUhFmMgDMvtDc9silspUvzuBNpXTeXSQTTDq09nF09y6QEJ2J3fcat+adCLaGWHZJUuZAci5qm253iiQy6HzL7ZdoYIEEKrIqLqiLxMWn8nSDdFsmtpnY2obN/EsCSyrbiUxcw+Sa0Nj+cYBDU9nGXnyGdSEvomvWQZ1JCO1Jljdzayjgc3OvDJ5hDvFzcV7+vsYsDp/CRqkD33+fIoJOZWqRWlEVE63e5PQigfVsdM9+fOPh8CJ6zzzXro03kT3bJcDopdwq6d4DKiJsZcWEKT0BVzYLMbJXmMP18tg4uq0nrEs3kM2XvSBKAnQAazVxeXYxngBwLtpUWoSDcd1RF4Ryyc4bgrLpZFNJpLpGM51wDSHjdL4tA2Dl7B7SaEdjwSIleD3WaWEEoHjQkEHem08uAUoIyKaMjuzguRTD0Ks30TG8mFlXn+8Wg6mlAvoCsUMAR7TpVsu8rPudAR3qm7MuJ+I+7NkXc7cWBEUnXjFcPuBkQVoOxWIaduJAutR5bcEdHxbO3nRL0RfexiBomXEqq+i8pbDXPtFqMWRbBybkh5JlKp2+G3Xb7a8B6MJFd4BJigGaYteR3aekqC7qrebb2LvonqZLkq6pxYa6fNHDmrZyXNU5dztttxNQjYNq/h/NLs856BO+yKKY5PFcMCQxXxcATlx0C4brtGjiMHJ/PLtks1Ak+8A7ntxRHHqz7Hj+t+wPzqejmgoLuryjV2viWskQiHCKPGEfI7/uAit33ibcY1YTvOnHISL4dYaMSD63AMyZY5+iuCJ6pYCFCAQUl9Pa1VC2cphNi7HbFR+sNS94cdVoLxZwEJ29wjtFYiG2dbeTgCd7tdekhloqKPxjrd77OuJ4Uud1mfOBJkxNV82zW2xO5rlHJa/kAcFw6Qxmig3EuIyA/X3WKTShkZwxEJJ4dlr6gG7UHO5WbSDMTg0CU+04jEbWFe3bercK/niF17ZDIPh3VvUIQwR0B+qe2KryMtXm36PZhobtgt5Pcnul5gVIpEhqSspb6E4I6+uM51IFGASzVnnWVo75wcJdpB9W5zI2BvAyDhRKrrQRAdwbPoi4gxIrM2LINJ+nPgLl36djJwYW8GfVcgDF6CIVuUmdaEoxhT2tzzt1ALRS6CEpVmhGI9X26ypuBCj5XnOmKu6wtxrBmTKs+XaOGqZxQidsaGdM7IaCLd5RIJGRMMmxTfxf0+geeGNKCGCUXUZrSXPnoRcPaGzAuiE1yzGZArst5SLRv2xDK67AmDk27kcHF110S8hYOg+eGEIRafm9GCWFBWbx+DXbw5iczWM6A1km46Je/3+W60Yf08t50TLymo28nOmYyRRSRi8XojNA4Bplyanjs4VNhHmrx6yAUMOUvd87S5hVRp4BFGQHlwl0Hzcpcy1lJCHbv3+EyDEfSA4NsTRJRBesOgARK6GlSPc+l1JBTCMG+xFh11EhGKC5JHDvn5EO9chjd89rjRdEInmD6z55vY0o4pP3cOCw+/XvruLMEsluuXeMm0XVQUSL1l7IVpw86Ab4WbCIZIfegORpVeMb+h8I4xGdOysZ5xNi2CUevysJN1A3NNVtpJuxNSjwtHsYKkX5KWaXWW4qC44cmkTNUb+UDUdojx8WV52AUoegyXRdUfs3SXnkTflxsmp5rGV9IVq7HahpQt2V5St2BU5ZMBaYJhxQOukgyh2x1VkwgYfDxFJGLstoZvTjjHqRHiXNpDBRU+BGKXzHcyvDR0bOh67erVjm7YwplZj0KJCqfCWBi23vHHxckHgKq2Nra8QYuVv8kcO6DQnsXGRoyu9Lw8iOJyywgbZYtGvnArY6Hdo9J+CVu73Zy62IuBOKQF2ZK7rqulgCDXi1PMSPqVP1HUy6eX6XT6ecb8d79Vng78/p+dOz6OCN+/ebofMLum8+XO68vfluyXTy+VHQK5HietNSjIzwPJ/3LO+vnf/NpiIjI+vradvi4bmvfz+cb0pz9Degkzp62banyr86S9H/h+erHaevpziPrtebD9clcxLaZT8u9UAtcBaB3fmvytchvw6WX6e4XpSyDXCc3m/dJ/nkB/enFG4LPQrt8QHHtzq2JS+PlNCNBz+Tp/Xbz8/r8B0aiDxfUlAAA= -->
