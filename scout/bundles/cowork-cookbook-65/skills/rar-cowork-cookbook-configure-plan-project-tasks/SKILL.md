---
name: "rar-cowork-cookbook-configure-plan-project-tasks"
description: "Applies a bulk configuration change to plan project tasks from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_project_tasks", "rar_sha256": "0ace5071a7d8a219fa49afd77c211b56adce388a17426e114b7c59bd4f7fcc33", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_plan_project_tasks_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-plan-project-tasks:c6c8f086208017305b34e12d6627da3489695119f79c5a3391440d70ae788b8e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_plan_project_tasks`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_plan_project_tasks_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Plan project tasks Configuration Bulk Setup — Applies a bulk configuration change to plan project tasks from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-project-tasks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_project_tasks_agent.py` and embedded as the fenced Python below (sha256 0ace5071a7d8a219…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_project_tasks_agent.py` first:

```bash
python3 configure_plan_project_tasks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_project_tasks_agent.py   # or on stdin
python3 configure_plan_project_tasks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan project tasks Configuration Bulk Setup — Applies a bulk configuration change to plan project tasks from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-project-tasks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_project_tasks',
    "version": '2.0.0',
    "display_name": 'Plan project tasks Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan project tasks from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-plan-project-tasks',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-project-tasks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'caeb3df6a02c3a94',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/plan-project-tasks'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-plan-project-tasks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigurePlanProjectTasks(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanProjectTasks'
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
    print(ConfigurePlanProjectTasks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOj1pbtX6GzP5TdykqBACHyhiMeIDQxg4SQXI4shsMkJjFIgJ//+ztIyqyqtn373oiOeHKUS4Jz9rzX2gfq9ye7qcO8fHp9MoCdIUs7SaIQlIideQiXX/PyBP/KTw78g7h5VpeR09R5WT09P3mgcsuoqKM8g9uZokgiUCE24jTJba0fBU1pD7cRN7SzACB1jhQJ1FKUeQzcGqnt6lQhfpmnUB8SZUVTI3zrggTxowQ8I9eoDpGLnUTeXcxgVJkniWO7J6RqiiIv6xdoCWjttEhA9fT662/PTxH8/vT6+5Ob2BW89MQ9TAEq1K3eVW8HzXAnvBLAJUUHg5DB3wUo/bxM4SUP+Mjj108VSPxn5L/+63S1y6D6+fVLhjw+X56G//QmQ+pw8M+uauAhrl3YTpREdfeCMMnV7iqkBHVTZkN4KhjDLHi57/wmKS+QX4Z7P92VvASg/unLUw5NuPn+5elnJC+hvrIZvr8MUoqffn5J8isof/r5m5yqcW6xhcKg1S9vj98PsXDht6WRf9P6C5R6z6UDvjx959zwuds9+Al3Pr3EeZT9dBcMk3gBmZ254Kef/06sGwL3lERV/S/J/fUuOAS2B316GP7z8y3IvyGjh0MfMv9e7VBk/44ncPm7umfkEai/k32L/38TnUQZrPz3iP+luL/aMPoF+fVvfftnG54R/8vTHCTRBVaHk4BX5Pc3Q+W5Xz953y5++u0PKPp/FGPkTeneJLyldhb5oKrf3n79VN0uf/rt109NAWsN2OlbUyZ/JfOv4nrT80MEH6t++nEv1L/LTll+zZCPSkd+z4v/KP94Qcyh8b9dr16R7/tl+IyQwYl3pfcQfNczFbT1uzj+/PQHBIcMetO4t9uwy//zPxEpcsu8yv0aMdwcAhBMcB2lYDB+G0YVsn009VdDWIviS+p9ReDVod0hRNhNUiPL0o6Sd1AbPMh95Ov/cW/o+dl9oOf4HRHBrUDeHsvfbhj49QXZhlBlXkZBlNkJojOqitgByOpB2a0sqib9fBn0QVuiO97o3HrAmqpJwD+Qr/9MwdtN1kvRDcZ/yWA2bJgiD6lBCkHULqOkQ+wbeHc1+AzxFCLIB9IO/2uKlyEi+xBkjzi5ELJBC9ymBkiSu/YdtKtnmOoqTy4QDYfoVacoSRAvKqEpedndIbzJXgdhX79+dewq/JLd4RdH7nxSjeGCD4ORz5+LEvhJFIT1lwy4YY58+v2PT8j/Rf7ZrpvwQYcKOeAWK1jCCbIxFBmB/dikcFmFDMUAweaWr9//uCdhsC6DBAi7KPIHQquHxHyX/MGDe2be0wJ9HkwE5UPTj3FDriGMCxLVMFqws6vnL9kgIodLy2tUgfcg3jffQ/+e57ueISfVI4YwTze+HNbe6m5IppuX3guy9pGPSEF3B3IcMhrmVQ1LtQCZBzK3gzvt+lsKs7xGKtgtld89I00FXR0kf3Wg6CE4KYQku/6KSJwK2S1PBgovH2wHd+dZNCT+Uaj3y1BI+QnWGPsu4gWRAYwmUtilXYSlXYHbOt++VwRktff9ULiNZOCKDBQOhhzd+vhWeeqfBwfuhxmDHcYOA8JMgXxpJihGIP/fRpLBXma51Pkls+XnCC9v9cO9uIYRavD1PnXBAQGBA8a9U74NDe/48o68X7Ikggkpu3/cV/q3erqvuaMZbHoPYoZ+kz90dnmTG9WwKoY0l+UtDl+yd4h/hkGBOakGF2DzngYoyD8UDnffLQ1hhw6/v9E9ci+4wXVYykjROEnkIj4A3i0IdVgOPfXIASwRMPQXbAI3/MErBEqH6YfyEWhEBGsV0sAtdDLsDTgi3bPwsTwahihohde40FrYPOAF2Q+1DOuxQhwAJ6FhDYzCp5soJAUwxtDEjwhXoV3cjRnG2oeB9pCLPLVr8H0GHjdhXQ5cAvV9NB2UasPcw1heYRJgT7X3zH7Y+cgVNDYdGuC26cd0P3xFvueifwyNB238hvlwEh9o/LvgQLQu0+pWcpBgYZmGeQoeBQQr4cbYL3fSvbP6hy2vf5rlf/r3xv0bje5+zNwrEtZ1Ub2Ox3eqe2e6FzdPx7BGogJU31jv89Bmnx9t9vnWZj/IvIfoFfn37PpBxKOgXxHsBX1Bh1ti5IKhYh8fGAbuM3v4TAx3v2Q6+JbfRxEMcAYh1uk+WOV9CaSWoATBsPjOMtVATlfIhzdwu7HERw08OuSOMZAeqvy7zh18GjJ6T9gHCMNb2QDv3jDABWA41ySD+RV4es2aJHl+yuwU/A/nmQFjYYXCQAwnIBhtOAvVEbj9+piLhh8/Ht5ufQQBwMtfh3Z6vmHiM/Ixjj4j7weE23Era+AJ6ddhFB5UwqXwr4+1HydDBzzB01jdFYPR91PPMIE9JuM/GzF0EbTYBQNj5x9tOWj8kxD4JQhA+Wchyu2LnTywoartgQUh+T46uoJ2es2A5DBtsNNg80BMbOCGP6uBekpwbiDveoO73+L3za387ssftzDU96Pj70/vGDF8vw8B95KBG/6lIW0I5zu5vg1C7WHrbZS6Rfc2dr5Bz6KBRL+7FQwTwdu9+p5eIbiA56chhmUEGau/HZCf7pZAF74NrFAChInP1TAUjGHzQEmQqovB/BOEuO8UDJcj77Z++PL691PuX/T7qzt1Zz46m07QGYpROEo6OAGwiTedTijPxokZPaVJDKN9inZJG8dpjCBQj0JtQM1mzgxAA4b8pfbDgDE2RB6a/hHef2vqfrrvhbQwIadwM2q7gEQpzKa8mT2BZtgEbfseRbkTDHPIqe25AJ/NbIwiJlOAYYRDuSTteIRP+a6L44O8xyhwN+jtfc5+z8W95d8gQKbRYO7Ett2ZS2GER1P2FEpHHdyFEcE8CgcoSeP+bAYIuP9j6yMfQ7ruPg9VCsc+OHRdBj2/P/I7VN6UgCtXRLVm7h9uTJu2sx87eiiOymTUtvhUw3fFLr3YgjIyu7NSTRuNlZd1RArXwjps/JNRn22i3LhoTimSzPioOT5YuKj2HOnrUqKcZmqIShx7BFRFKd1MjeUdzxgxRmaSbi7tDNONaFfaQlcrW4fananzLtna5EgolbIyFuem4MaqI5Yj4STMhbrcMFGRm6ewPx47vEv0pclXLj3ZH8/ydaF4C3yX9DWRCqEsQkDcNPLK3Ce9uBWAErvtdnfMq2hidpt96y0Eu7rWq5xUs35GqdlmMlYu4TEr6anrtyNBntQLPtHOJWFUZ2pXeM7ONDBFsM+T2lhq4YHEdWncmoETNM5id270JFEiMmksPOL4VAoDjfdM0Sx25WLknsiKdKdmt+8xc5dbiR5YGzg8yYslmZ0LZ75ntTNp2rts1nO6NWHQWpZ83Y7UbF/n2FjDE0uoXTI/GcWukFJPwHQ8BC2ZKO1CKBKF9kuXD48enm0SnxMlS95Hfpn51drlpni7qBlmgYcYiiqJg3bNYjRyy+ISWavtrlnNap4ISOxsCuHWL/e7pIvP+Dqxj43B29ZqLMWSvtQcvzgv9pXlXjhjLwpCe5RPF0rWE/tc4qa9N075fEZvN1d9M7cORlHY8XIS0FvadI6zZK+mM5cTU3ZaYEevwkuHiL0+abUGR7tDnZ2icith1axbuso12x35wj3LR38seMzUt2AmZxeC68hmumUNdFNpC39yXaSGlI6Ec9Ym/WLEjRQx1N3RNlVQWItu2xknaSGudlJdbNFlj4+bSZo3WGKaEzWpkst82SozkaeU49WQ0Rx0FWfMsOLA2aOcg306x/bbsu4lizI8KyM2GC7GhLwi9mqlCvI21MhiPFstjq1yGRejUXza6yNwrqZnvOmOmIPuZ4vtofDM1XG/k4zO259NroriOiDkqJvMlnxFYHNjLETYZT3jE9SvWM4pWCP0wmtfUMyWIsu0CCXTsJpVbq5Vj7scxJN8XO48gz+GxqYYbSb6xl07orDcXs2ePxqdIByqPrji8+jYqEfXCT2rTWZEis4OeWbwkXTanub6sl27x1GFuSFl0ZKRdqCgiwjtj+dUpFddih0FwTP7MTVOcs0Bx258MuILia/k8enciKujH4erkbzvxrHdb+y4wFV2FTeis25k20hDdVakPtFwp/OoNuxrTE/CmOUvsi7lliK4pHkeLfqenhVFOCalmuL4bdqjE90bx4l+jFkPnIMtKmByMzWntGrjO5UGBpoUO9s1cX2qN9OwVZf5xhibfbmrkzXpeehlZ5aX0zrsR7tNzDtq0I03473d1vOilfQFgeZjfkodmlDZrKzeiExOcs8hHQpFNBH5Yl1jF81XtBnhhFyyCtPlmOWWCrprnLVoFddrZqxPp6i5JnHRq4psH7sk6Z3tzmh1sOhPrsfOgX4U+yC2rzO/lfd2valHTr4m0akOMB7Fo+GsIAe+5OZCL8ZM4Bsbit4esNG6uJhC5wtjPcMI6YhnY486XUwWKyf8bH+6HLasrjeZpRQoGvk+o1xWmoHjayZKzyLfCpuwwjE+OthBtye7tovQLFjYICPOlwurUeGSJ6WupLpZtXdOy4W2I86kxdNyluLZbC4wG03G2Z4p5Gsk+1PJlcW9N3FjQd8SjbEj1v2kdXvqkDQGvp2nGiowi7xYmouzewosY59OWMF2tdwSoz1jXFOr92RpcpxzDXUq53O/We6JxSazJLZU13uj8Ss4WilX22uP6eaIb63J1r1sKxpYx6tuTJnk0FtNc0GvkAfiU0rLTnykVgxBLBbYFKu5lYqlp9JpwMECWyZuMFNdZFN/LY5A2M6KbDYd+WDnd2nOT7qLKtetMWUzRqN3F5ZLU7eriMLIMaLxzE1mLLN+vO1sw9xu24aPjPnOKq/spnKEQug3Z30jqBfDjRRDTSFkY4IFhGQO526lNuTOws9zI61S6cymOJ8KiUrmFVh5e+k6MXq/7I+TwyrfU4ze7ZtoU6UqScgGAScvB2I2Gu5dOSHEvY3T6IljIGH6ItftDlMaTWredCp3Qy35yaEj9ENwXbSra19WfoPm+FlMx6vTha/P7eocm8x8FxqHKKp0zm+uRTNLDzm9sGyN7zfBxqhFytVYFz9pS9bA7bPYKZ6wm6xmc+YMR0JeZ2KmOecqGgjClDb1zRjUFmDxvZo1WgZRIuYO+4uICaZrniYQYA2PW7cH3qyps5SeNwsm1YSWKE61s9VlPtxXhQ85rbHNnXxacA5XXC0Im+ySTNZLx8RlMxrLrRZVza4cKXlOFtxi3VfzA7u7Sg3TKMKiWxreZnJR5/2i2LGEmGkrCnInds4nB/kYlpuIMDZSERAwUDgtgpLHljoai41E9oe6ZXdiW7p7KRFQ26xOGqUr1JlCr/UuEEnK0fW5sxCxkHBrtYi2KgTVaXI0A3HqTExsHYr7JmxkPWWmJIUqJ/E8yddgFcqERrC6j9rSFsQbg1tPIz4a63V6EGKA9sFUH5uFkwMy2kqogR88Mu0XWq3rerEWd7lSrs/72Ya5ss22hvTsUVs0RkMuP81jTRxPFvTFoEW9PJ7cmOw7Uzue+c6pRkCeA6XYGcXyoG1bZ0qFs8wZX6uglr0o0TgvALYrj+prnEzSC7spZyOlpuMpeTQ3Na04S7NqYTubVulRsRMy6yvhMzo5wzS0Zjc7IWLYNJicWHps7gUXzCljYcA0O+dMIqKIBBmJGX2/329cNjlhnMNoixhIgisWjb82ujDe5aa3mHhCGIO5pWm7GL+UlmzXuFBIRS6ZHLVrlPWYmU3Za8ONbDytGV3Z8Cd7tZ2CKFjMtvT11FvzwlDmWS5hStYrDC85TMGve1clTzPMbzcQ46VmeAiviZtSvi6rBhhXSHDtliEjK4jFHSwqdSKljWTmtiMIuzKdsiNenLhhgafNktYOp/UBhNYo5M/Xzk63cNQwMH4iOBLKnpUUdVt3YjvKbN3aY22B9nmVyPvCGWUC0wfoxmnEU1uZViZnQgvI7aZfFsv6Iue4H4zXW2l/3vGYoyv23OMosiuvmMPYmGurC2vfVBa/3xZeR0xTv0ylPLYOo74EsrLaX+I13hmXdq/7blOXs36WMeWmmV7XWlyorbA6Ba0SllXS8hyrUAUnsE0+FbpUgCGw1opuEPg2EINFLukzyBHGmkmbY6o3+4zens8SHZLTPKv7SrLSJLdO6+nFSPSFzhvRojSbi8s328vmJHLsYXmiTqwSWceUy6fuojECTznzxDpKQLEw4gS7AEK1dLY6hNkVXxgOlQliUqiaWQsMGXcLqpX5PtupgDc5GGCZ2i0BT6iXJrksBO5UXtU+PnQwc7GlXScSSDxuZzcy2y21fCmYaJu0tMOcGOFs+QrBEuM25vo8GCUlw43Q5ayhhSXJeSNKSRN2E4RFiFOWdE5Yd6ZEGQ6iMrNy0VmudW2qhwuaLEDMMGNF66SustnubHdxcSB4NzrluK4xTmbj276Z65aQ0gYfVtJicpWWXNO5zOFa9qFTXeOTNN3GvaKVBuV7cUfqV1o7ihokQnGxv6QWh1t7srkuz4uNlh0qeBL0Dgnf0nvey4vESl0l6KrKlVnJBnsyPJnHhUunfbrLw8y0CS/CW26tgvJ8jkZ7TWfQ+aKns9Iwy/bUeb7Caj4vgp2OV/MtbmTL8Xw9viT766w5zzp8RO2oPTya4oJHcYRaZFt6BFYJ1WyiZiVnytw/TBaVQzUKJCqO91JQoWdyS9gQmPbLni1kmguDg2QK5Nnb1AlZrspqUcbdsXRHAr+Z6jCRBEWALNBFbQM6wfYkVOEm0Rg4M4i/OsleJYK2bHgyHLlsq47VM2gWTduO6rntKlzQXKUpHSt0oniT8mCv2qavL0rlVoFDotaSIEZzhcZtj7ZgrP3kchlPuRXBVfN5U4/HkjrzJPE4obGYMi5OzVwmJnngCY7WcnJu4NoOLApUZJZqoaRzm5oTPH5ebdgocEcEzAFxnRSLeJWLM47r1M5pWZftDPXQxASJ1aBJJv3Fk2JGdxIqcVYaCqjGKOrjupgrZUMa1oVzPTK56r3QbSXpEjhRM6vXI1HUDhuAz3e0ppb4AY7BEkRS1zkCXFq1wKs9q2PGPZWoKBacgx3wo+qyWIMJxWBXu6oWkZpo1mmL0UKSO9S+UfraI0t/itPZyuKWJquNtdhm7MpgackPXXeOW9l0VZ/zusNsajfvojV/FcuoW7Y1ZU9mkwWAFFlLBBxXQO21iXjBXdubBanEuRd2W+MVECUtI7L1kVstxSW11KfyPj9S/AF3VNrzpDKoeHbZ2BmFblqji4UZvdvGI59ZbVPAu4buXa1lw4c1UasQS/mtX41TebXyPf+wJYklV2st4GfltdxQo92chkN82C7XTsPQe3Y/VwjK91mLJXl3zR3FA+My7riZO+x1LcnRlMsrvx8FaZNPWk4A43hNGPtAuNrj2tJVp6InyX4dO61SkdPD/pBfr/uIIrd1Q5N0xqqpy9FetuT98aSbrHwLtUnFyfxJ7F+YcCsqqL9nruJofpXLVlskc2ZMjg5zWAlMqzTTGT+T9QhPzlXaskyz5K6UHZYxXcmXA0maI12RPRx1EiDC8E2rrlB00qXimmhW2RyOWvyCHGs1ZxUmXqOH1WneLiF5eStqJ8Wn0apE4516NGlYM9UqkKjdlAi3Y6Z2LvgRHjDhydgTW1+aTHAawwKVSpuRZjDLcbME1GTmGSGl7bvNSJlpcelhF3zMwIN/ac5dnIQHMjWdHGjCOabYiGL98Yk+reZrCmsOse8bXj/lY3aBJws1mFvhuVTK9OATzpoBtB3Tcb2ay3NfEyYiYfhtdGBzdrNtypKoXJ9qTZ5exnKhqJqhSqeGXDhwTIway0pn+gjzAlTcjfo4YKdLLwvgMHpYca4o4SybUukiZ6e2DeqG6aYOoM+KFWcXm14q7TLg9my9ok9qRXhaSwE/JtZiM9mUnYhPIOeJW2bhivPQcZjVfCrlUnlJNjXba3NlpegbLiZ3ddiYq0ZHxUlOgo27kiSiG4lnx17Zm0s/TvXV5qhKMevrWKlWrSwm/Soao2iNh4dg1o2LrlbduS7Fl8Tc1mlCm2FrE/k40djdeCpeOmurUlanueMyuS4VJo7Dg6eeOZ6T5XXLCpSqyxsvEsVz1gvqZklMaGolo+N0e1JSjG1iPD4HTUHQ7JjasvuQiE4Mw/zyy9Pz0+397dMrhlKTyfPT8A7g8ST/X30YHPRR8faQgkPKeX7633tmeX9++P5u7/ZYH9je6037679m4G/PT6UbQWPuj46rpAkejyj/29PYz//s6fCws7u/ch5ePbb1+2uP2g5uD66jzGuquuzeqjxpbo+tYWibavinJtXb48XB082ZtBjeQnwoe/p41v1W58NKPxruR9nwPg14kV2Dx8/g8YD/+cnrYI4it3rDp+QbKIvBycf7peG57fCC6emP/weS+XpvPicAAA== -->
