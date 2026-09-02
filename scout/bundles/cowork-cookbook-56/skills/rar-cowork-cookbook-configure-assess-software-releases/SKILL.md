---
name: "rar-cowork-cookbook-configure-assess-software-releases"
description: "Applies a bulk configuration change to assess software releases from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_assess_software_releases", "rar_sha256": "dd39638bf65b3e3ef81af376dc14cedf6b102d1734ca1e4d0e6806c6b8fc7cdf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_assess_software_releases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-assess-software-releases:2113a9668b9678d44307d0ae1942912cb9fa1cc962d20b11ec5e802860989ed4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_assess_software_releases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_assess_software_releases_agent.py` is
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

Assess software releases Configuration Bulk Setup — Applies a bulk configuration change to assess software releases from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-assess-software-releases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_assess_software_releases_agent.py` and embedded as the fenced Python below (sha256 dd39638bf65b3e3e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_assess_software_releases_agent.py` first:

```bash
python3 configure_assess_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_assess_software_releases_agent.py   # or on stdin
python3 configure_assess_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess software releases Configuration Bulk Setup — Applies a bulk configuration change to assess software releases from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-assess-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_assess_software_releases',
    "version": '2.0.0',
    "display_name": 'Assess software releases Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to assess software releases from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-assess-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-assess-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3d6dff430f4c9ee3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/assess-software-releases'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-assess-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureAssessSoftwareReleases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAssessSoftwareReleases'
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
    print(ConfigureAssessSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZObyJbvV2Fq/ujuwTYgFgnfuBEPrQgkQGxCtG+UWZJF7KuQevq7TyKpyvb07bnTL17Eo6JcLJlnP79zMtO/vThdGxX1y+cXDTg5snHSNI5AjTi5jyyKS1En8E+RuPAX8Yq8rWO3a4u6efnw4oPGq+OyjYscTufKMo1BgziI26X3sUEcdrUzfka8yMlDgLQF4jQNaBqkKYL24tQAqUEKHPgKCeoig1yROC+7FlkNHkiRIE7BB+QStxHSO2nsP4iNotVFmrqOlyBNV5ZF3X6C8oDBycoUNC+ff/3Hh5cY3r98/u3FSyFLKN/iKRDg7hJoTwHUJ384P4UywoHlFRokh88lqIOizuArHwTI8+nnBqTBB+Q//iOBs8Pml89fcuR5fXkZf9QuR9po1NVpWuAjnlM6bpzG7fUTwqUX59pAnduuzkdTNdCeefjpMfMbpaJE/j5++/nB5FMI2p+/vBRQhLsFvrz8ghQ15Fd34/2nkUr58y+f0uIC6p9/+Uan6dwz8NqRGJT60+vz+UkWDvw2NA7uXP8OqT786oIvL98pN14PuUc94cyXT+cizn9+EC7roge5k3vg51/+jKwXAS9J46b9X9H99UE4Ao4PdXoK/suHu5H/gaBPhd5p/jnbErr1r2gCh7+x+4A8DfVntO/2/2+k0ziH0fxm8X9K7p9NQP+O/Pqnuv1PEz4gwZeXJUjjHkaHm4LPyG+vmrJa/PqT/+3lT//4HZL+l2S0oqu9O4XXzMnjADTt6+uvPzX31z/949efuhLGGnCy165O/xnNf2bXO58fLPgc9fOPcyF/I0/y4pIj75GO/FaU/1b//gkxx/T/9r75jHyfL+OFIqMSb0wfJvguZxoo63d2/OXldwgROdSm8+6fYZb/+78j+9irixGbEM0rIAxBB7dxBkbh9ShuEP2Z1F81cbvbfcr8rwh8O6Y7hAinS1tkUztxisB8GD0+alAEyNf/492R9KP3RFLsDR3B6wMPX9/w8PUND79+QvQIMi7qOIxzJ0VUTlEQJwR5O7K8B0fTZR/7kSuUKH6gjrrYjojTdCn4G/L1X7N5vVP8VF5HRb7k0DMOdJePtCCDsOrUcXqFkD2C+rUFHyHCQjR5x97xn678NFrnGIH8aTMPgjgYgNe1AEkLz3nAePMBur0p0h4i42jJJonTFPHjGpqpqK8PUO/yzyOxr1+/uk4TfckfUEwijzrTYHDAu8DIx49lDYI0DqP2Sw68qEB++u33n5D/RP6nWXfiIw8FWuRuMRjOKSJosoTA3OwyOKxBxsCAwHP33W+/P1wxSpfDwggzKg7GQteO7vkuEEYNHv55cw7UeRQR1E9OP9oNuUTQLkjcQmvBLG8+fMlHEgUcWl/iBrwZ8TH5Yfo3bz/4jD5pnjaEfrpX0HHsPQZHZ3pF7X9CtgHybimo7lguR49GRdPCsC1B7oPcu8KZTvvNhXnRIg3MnCa4fkC6Bqo6Uv7qQtKjcTIIT077FdkvFFjpinQs7fWz8sHZRR6Pjn+G6+M1JFL/BGNs/kbiEyIBaE2kdGqnjGoYjvdxgfOICFjh3uaPfQOSgwsyFnUw+uie0/fI4/6soVj80IHMx6ZEg8BTIl+6CU5QyP/nhuUu+2ajrjacvloiK0lXT49AG9usUe9HZwYbBwQ2Ho+s+dZMvOHOGyJ/ydMYOqe+/u0xMrjH1mPMA+UgDPgQRdQ7/THL6zvduIURMrq8ru/W+JK/Qf8HaBron2ZUASZyMsJC8c5w/PomaQSzdXz+1gYgj+AbVYdhjZSdm8YeEgDg343QRvWYX09PwHABY67BhPCiH7RCIHUYCpA+AoWIYdzC8nA3nQTzBLZODy+8D4/H5gpK4XcelBYmEviEHMe4hrHZIC6AHdI4BlrhpzspJAPQxlDEdws3kVM+hBlb36eAzuiLInNa8L0Hnh9hjI41BvJ7T0BI1YG+h7a8QCfA/Boenn2X8+krKGw2JsN90o/ufuqKfF+j/jYmIZTxWxWA3fpY3r8zDkTuOmvuIQcLb9LANM/AM4BgJNwr+adHMX5U+3dZPv+h3//5ry0J7uXV+NFzn5GobcvmM4Y9SuBbBfzkFRkGYyQuQfOtGn58JNvHt2T7+JZsP1B+GOoz8tek+4HEM6w/I8Qn/BM+ftrFHhjj9nlBYyw+zk8fqfHrl1wF37z8DIUR4CDoutf3OvM2BBabsAbhOPhRd5qxXF1ghbzD3b1uvEfCM08eeAMLRlN8l7+jTqNfH257h2X4KR8B3x/buxCMa590FL8BL5/zLk0/vOROBv5Xa54Re2G0QnOMayWYObBfamNwf3rvncaHHxd795yCYOAXn8fUgnUO9rkfkPeW9QPytoi4L8zyDq6ifh3b5ZElHAr/vI99X0m64AWu29prOYr+WBmNXdqze/6jEGNGQYm9EZ5HoH6m6MjxD0TgTRiC+o9E5PuNkz5xommdsTrCovzM7gbK6XcjqkPnwayDiQTxsYMT/sgG8qlB1cF67I/qfrPfN7WKhy6/383QPpaXv7284cV4/2gOHoEDJ/yFFm406lvpfR1JOyOBe6N1t/G9QX2F+sVjif3uUzj2C6+PSHz5DOEGfHgZLVnHsIbd7gvql4c8UJFvrS2kAIHjYzO2DBhMJEgJFvJyVCKBoPcdg/F17N/Hjzef/7wf/lME+DwhCNJhGWbmssx05lMUiU993AEES01YYuK5bOAQnscyE3+CuwQBPBrM8MmMwdkZC3wKijH6MnOeYmDE6AWowLup/y+69JcHBVg0JjQzbhT4JMuQMzdgaJcEJAhmhBOQU8b3CApWpIBxCXziE1OS8hwCUD4OmBnOeIw7C7yp5wcjvWej8BDr9a0jf/PLAwpeIXxm8Sj0xHG8mTclKJ+dOowHSNwlPUBMCH9KApxmyWA2AxSc/z716ZvRdQ/Nx7iFDSJsz/qRz29PX4+xyFBwJE81W+5xLTDWdNwjdh4iHq1TdLD16VaP9WrWbg3TKtf8Hlh8Ofe4vne2PLeyk2NXbvFy1+zTqbmXOCxR0ZNFCxaR+SVIRCXvkmpbePk8zvRmKt+6/kZdTqrPF7d1mdbuPDN9TNCKVKSNOk70kByMqs/w+jiJ9Li5OtjKBJWb1AMzQ7F4J19vy+O2XJ+1Q13y2YROGtOJpWSLDvlgZs7kEPnz9cTXYyo9Vl7Na51dbWWC6AeR3PvAOV21rZ56+a00hj7akCKeqoQyr/wg4Ne0Z1j2ddYrkWftCBoEEdilQ7v2Wq2qtmbDFJPS3+G6SMgCqORW2xhleqtyG4vreb7WJ3WpeedeZF1RgwGgq3gUz+fbg7TJfXNR6OkEWLf1tDqk1t5s4QpgzSw98ziIie0eQWw2vbFy6tRMNWvwaAWclj6+OjFnQlvmaltImEkc6fRkNkkkqE5W7ut6stijru3QemNuKwrrrQ253E44cS3ah4tIbkgcpNn0Ri1ysfFn6ulwkALKN33O1mb7KVy55YB2T+0VN84h5hC7bWduzLg5khsi21Vx1hzF2iPnK6k+s5maiXUhtQ2xqI9uppfCkjeXpybTAjYTJ71J3Kq2nh+NCAX2ihKT+bkRjFmv8q4KbLkym8mhzm+eHEnDgvWoBkVdQpqpnX1lCtKirqc2T7Ja3xMNe+tOaiRTk+0xNd0rxpgMutvEBWmL3axvdkNZpercwQWYHv4xWSZxyLCM29ykVY8KybVZmxi1UCfn4nxLZOiUMDXpxc422LnHYtO2rXZnm7D8mnYF9zq0eh8T8i33VmdfzJsdp9lZXV2ywrn/MmdpIpfVjrzabk5JJOWmlEJSmjLjxfRWmrS4Q/lBHZSebDo05Y/zwa8aZkL2lZPuKP1KTy6OY+0mDbXQtJ3F4FUb61G0YjOK3G/05jQstQA9Ez2F8ukgN+r+VEI08+f4tZzuj/X6YpTR6ajhR6m47SU/a097Q4w3V1NYSFyyMrA1dgq7lZ/i3AwV6Vis7HUqH+2L7UaDRPJF1F6qmsJR33bcuSTg9CoDsiCE5wU4ncBgg8TTU44QUiDQ5RG1ryl1OAf5vnKjpCwna+yqzGj5AMqcA9phh0nzmYIeK6r1U1RJ1JMD9nt501CunHuzFZDSE70RCgtmbqRhjJqgbtM5Sm1tCp1N2va4boszWS4dQfQT3jFWVspJRpm3WE1PALNnm/msL4jFKQj6W66urRTIq1TDN5jUHuVp67o4XqPGdV/S2pEw8wFTlc1EDKAt1npV4rZ1jZ2qE416l5bLNCzoZhVFSl6AwChl2WzFithbor3KA8Of4ayzPyq3cIFXmnNQBeyg7OeaZNkHq2SLzj8zviJLxUGmp/a6vhwsvlk3crnYxP6+vMQGyzlN6VH+bXI8z6jL1Undcn2qrvHVk9XDuaealj5EfQcU5uq0WnIkFTz2GK/o7djlh+16IqTUas6LQlMJs50lSC5aVotgkF1pUuTXMhumvtK5OklOfX6Kh2vqClzU0oWwKC9qm1v0wjkzV/18w7UIvamFXS0VWUM9Z76JU/Ps8dckNPvm0MxoZfACxfEvi5WHM7kw2aAo6KmrXYeGdnYs1knKWYt7fOgfbLBkuOXSXGf81R20fchtTmdn8IWGS68aH5XeSnLNDgb6rrusIm6Fc+1Oa0Xz4JbizUrP6UIxpu1FPAieWEd9AixxiPSKcqgLOY3y/nw8SatmkuGGfMQaQzr3wR5tm8zu07NMMSi2o1HvuKsubbww1bTe274/RRUR2xS01uqZjM+jq9SpNgDzoKZUqjHYlrtNeWax5TB6rzTUkcFRtF8KTKXgNV6yzJxcuxTsEfbN1GKtZtVECr7Yr/eVSgu5XIsrsiKMKtdPU1w6YzAB0lV/wOUUX1SdFc6ZbWW6pqwbqqwF8oVd6Yk3c4BQJRPMYPRAdMwgRVflRAPm3jV8AyZf0ne41MoHEoLPsSrOZ1qRs1o8SmhxQTNHibrjojb6Lt2q4l6gFKegg5r00gGnLVhIuV12ZAvHOhs1Ifkhd8NW0+bs0beu41l5awk33t2vjeO+cPapRQ+7ToIZLk8JzAyv5saWLpetoCXOBqTqjdLEwZqg+4hKqJO0MTbOampXoh9tMIXzoqk2O9LazqmcueBXKNmfNnPzplI7U9hy1VLDNNhFuYS5yFkG9yneP6GBJxoyN+zFfDPrjdS8mduDG1DOaeOIs6zt7VNP2LvD2ghPwXpvTh1QhqFH0OSMEKNKZdMuLC/2oneuB38vzNbtQa2lapoUZNBRxQJ1xZScGJZBqMuVO1m2YU1lVmgra4/ebUu8IPNoyhGV6KS3cBPWaJHhuLvnkqsbO43R6ZqDbqa6P/PJDa3oK397XSuatxFPh7xDGdo5apInqWGZN3U/lYnNJE0kVg4n1dZy6+Eo7sz1TOHqm6Zuw8uKlTCRSQ6Jo5wum4Lk/D095U820RuGooQZK5wulVJJvI2pSTnnPFuboIcQeCKmb2+XW3VJTLOw0lhvqAN5sumMONxaFSJxN18fyHVsuswiPMwVIcNVuSMKRkXVYaXNp4WE8hozIUBbEgNQ1IamnULaL0qJ3AXH0CBPlaDqMiPMGlbGsVs6ZZqDnV8uF2EOrjKryOjsZN6minVLiOmub4eIYTxSaFtpOrGbwdMFk899vtdx7oyzAadfZoZBYsPc0DVukXH4Znm7xM2qoPnsoiR2YkyIJUcR6yvrkWtZN7sTkcxjyjU22UlaKo1Q1GUSUJtLtLQr0xcI37FDsPTcQwJL3c4rHYkUU68sr+vF1NhIhxk3HBYwytDJNKkPTiWsihOvM/4CqCV9pqMobvlF7PHBkXHO88zbHpyJcBLVzZXVbaHAKhNsNTVwJaEIM9tyD4rtGUG4K4cwEwa+LzdWcm4oGG70VPcWlV9U2twvJMpp/dsmA9UlIFaOFgkYz/MYumZqXaxUNGNoHtyKaLhoYSXJF+q8bGYTn9KqFD0n9vngO6DReRZiQhmWEelbJQRd32i9qcBY3tljDG2yyvpg59IbJy4tS6mo83W7PJwrK8gsNTs7PFWHN4qySQZ0s1rWj4SOuTueNRwDdkbkre54+cZMJysdE8ltLfbdEf6oLLO1CEsC6z1NNVS6Gy7b9tB2B3ox7BPfYFPufPRSwWg6bDC2nR9SvBvtOL7fzwk8VZzd4dhZ2bkz8lavK42ImWmTt8tCCjYRTMHVtBdbdT3nrNisDVlJ+Imey4m7n3uTkKYiK7LKTqcce3WJC18WbWEbd55tgtw8n30qcLXI84b6RK6P/DIST2apHHxUvAxni7gNDn6xDEVbm9ez2rYJIZ+2mIKFJaURC4dFeXuIbcVntN0lWphkaYb0ul6etPBU8Ze2CpaneTLXDzvDzaM62tuMOrdwKjhQh6ikE19d8lvrnE+ri7DWjsUqcP3r7ioPqqkkUiX1LVOaOJevz+vVJj/N88zkudlCOVjyrWyzuIg2PXex0XO8szewsslr9JxdZ7XHyGIi6KfTLgr38lxLYE5t+ekatcv1VphFPADZcd0x0+Majw9OdsuSucwt/E4R2DVgugrDJUM8hsqOT3IBNuzLejjZx5AmRDqaKsvLvJgKOz0h5iIwjHTC6vK+EQ6ulxK0BEP4AgbBJFgWP11jcQcbTeummQ13ydF6syj28UaRZ9NJLExLKwnOCejxDToD8SDnE8ycWctut0wVPw3gCmyGxorAYOR6sJY5WQywr96QUnvjJ+Yq2sok0EXbL2+CiOPYUiioLBoOF6kTUz+WS/RKS2eC4CdzWko7L1lU2PYmXGdgJR7WGNsnmL+KJF26hV3YY0R71WkjOHiizBEkXC9wueRB0JJky8QpSlGnzExTw4GRGSlU5ss9QGvD4aPq1mJy5M3CDb0A+cxmXJnFXJ919cQIih6bXvckxXXWrmmVqaLMVGXHxCyhk12fbC51hvcdl8tkvAwKY8XE+qVFS7C12Rq/uKaLcZmvzgupWdbkOYz6jUyu9id2HoTisZzoQFxW0tWepleQA6kmrjLq8ULiXF2nXtQnarPEwJUwXGHJ2QSLiRpL6Wd+dV10qqHZkcUuTxaV9/zAanN7N9ALlV6yilqBjqoXQjP14otHKRk7Zbg+meMLxVHL3dpflga5YWEysT413x1utnPbBhXM+VzHzbrAFQkPMsaRdIw4T7tNvWqcg4BxzYRbg2x5VdEYZ/iO5wlFt7UpWxETdZ2t5mlk8ULW1u7EXFO+6Fv6fC5Mg4r3fHWaYjwZiOAWZtvQw/xpn+OGOBMY2krUJdnNV27s0jdWuxwLHEyCYc+oN446NMqMXcFGKkxV4NIMVa/8bqHwe7qgZs6UA3NQ6u4t6G7z7pJivmzgM78klwOfJSdxEruXCK6BbaWfoEBR8jC8xTJ5ABWH99JhFwRrS6JX0kq169MqDlUD3HSOKlb7mNnUjXJjQ6423VO0VRSC8AVX07e7YE5yreuxE2Kyjaap3NPTg3UqqOsxvjF6m6KapXFBVRjT+qhssYGUqHbpD2TLoCrqsii1JC4FRd+8ZXiepYN9kge8cCZnrr1AyKMmNbMbpgQ1zzeKcjy1kxm3F9bhBM8tV/Hc7kzcsCb2mbq083x67A44IbSep1cMmSu432+2GeWt1mtSY4YAn1oteSJDbjgqs4Ll15rXJyyv41HC0aZk3tDE3WwnKXk5kzPOmfqBl23igW0mJFuffLpjSGzK+iVLwQXUPuAUFhsuDLG8xjv6SFWoDvYLAiMK5UbIheeTGrFFYfUQb7WBUoOfkQBTgz7jtCWWsktXGay8stV9mFIFfV3Ul7lOESZp6fueKK+E2Mh7/LQj2IGqKb11sA0fHhMuk7WkjxkURen5wdDydQWXkxfHs7HMJ9dZv25gg8HNlpW32u1WAx1zErOR6ojTDyde07YeKfHZLuMLdXJa9MYk3LcHF+tVbeaxy4A8GSHOafgcJwcP1SNyaUUUqnhVVx/Snso9T9a41ttaF09ctfu9p2yZ8zXNt7dqnnOZs59pHs9fc/vAmGv5zIjHgvTppWfbqs2S+AzvZoHP50nYxawPV2ssfTsB+nqyasBvTnTk9MR1eZuiubiiL/tkIg0GMZ84OnEkhf6qDwZHuFih2n3X2bjiJQzsHMI9Pl/zMU4Hq42YOOp8EdsECAqRZQSR0eZCL/G0ScuqZNC1LnMqDti5viaqvMBmHFVJu22CVxzH/f3lw8v9FPjlM4HPJuyHl/Hc4Ln7/9e2jmFmla9PWuSUoT68/L/b1XzsML6dDd6PAoDjf75z//xXxPzHh5fai6FIj+3mBi4MnluZ/23v9uO/3lEe518fR9njMebQvh2etE543/KOc79r2voKBUq7+4Y3NHbXjP+dpXl9Hjy83BXLyvEU450lvHf8LM5jSL1+bYvXx0nA+D7Ox/M54MffHsPnIcGHF/8KPRd7zSvJ0K+gLkd1nydV407veFT18vt/AeVaWa6yJwAA -->
