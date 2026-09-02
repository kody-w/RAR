---
name: "rar-cowork-cookbook-teams-update-analyze-maintenance-costs"
description: "Drafts a Teams channel post on analyze maintenance costs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_maintenance_costs", "rar_sha256": "fa7d5b22c5cd0376b255ba276a67a1e5bb8236adf1ba273919a0e48b0cbd4a10", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_analyze_maintenance_costs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-analyze-maintenance-costs:63c8447bdd01233045b4f1c29923ef3a16fef066ddf5545cc0cfca27fe2878eb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_analyze_maintenance_costs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_analyze_maintenance_costs_agent.py` is
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

Analyze maintenance costs Teams Channel Update — Drafts a Teams channel post on analyze maintenance costs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-maintenance-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_maintenance_costs_agent.py` and embedded as the fenced Python below (sha256 fa7d5b22c5cd0376…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_maintenance_costs_agent.py` first:

```bash
python3 teams_update_analyze_maintenance_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_maintenance_costs_agent.py   # or on stdin
python3 teams_update_analyze_maintenance_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze maintenance costs Teams Channel Update — Drafts a Teams channel post on analyze maintenance costs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-maintenance-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_maintenance_costs',
    "version": '2.0.0',
    "display_name": 'Analyze maintenance costs Teams Channel Update',
    "description": 'Drafts a Teams channel post on analyze maintenance costs status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-analyze-maintenance-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-maintenance-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '906081b0cccd8080',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-maintenance-costs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-analyze-maintenance-costs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateAnalyzeMaintenanceCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeMaintenanceCosts'
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
    print(TeamsUpdateAnalyzeMaintenanceCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjxpbvV2Fq/mh7qC72rW7ciIeQhATaWYRwO6pZkkViE4sAefzdJ5FU1d1je+b6xYt4qugqASfPfn7nZNK/PTlNHeXl0+uTBpwMkZ0kiSNQIk7mI1Le5uUJ/slPLvyHeHlWl7Hb1HlZPT0/+aDyyrio4zyDy8elE9QV4iA6cNIK8SIny0CCFHlVI3kG+TlJfwVI6sRZDTIn8wDkV8EVVe3UTYW0cR1BKmR4XDpeHV8AIvpOcfsiOaWPBHmJnJvYOyFQCycEL1AH0DlpkYDq6fWXX5+fYvj96fW3Jy9xKnjr6aaKUfhODcS7/OU38dIgHbJInCyEtEUP/ZDB6wKUUFIKb/kgQB5XP1UgCZ6R//iPU+uUYfXz65cMeXy+PA0/uyZD6gggde5UNfARzykcN07iun9BxKR1+gopQd2U2eCiChqQhS/3ld845QXyz+HZT3chLyGof/rylEMVnMHJX55+RqALvjyVzfD9ZeBS/PTzS5K3oPzp5298qsY9Aq8emEGtX94e1w+2kPAbaRzcpP4Tcr2H0wVfnr4zbvjc9R7shCufXo55nP10Z1yU+eXuzJ9+/iu2XgS8UxJX9b/E95c74wg4PrTpofjPzzcn/4qgD4M+eP612AKG9e9YAsnfxT0jD0f9Fe+b//8b6yTOQPXh8T9l92cL0H8iv/ylbf/Tgmck+PI0BgmsjtJxE/CK/PambSbSL5/8bzc//fo7ZP2/stHypvRuHN5SJ4sDUNVvb798qm63P/36y6emgLkGa+mtKZM/4/lnfr3J+cGDD6qfflwL5RvZKcvbDPnIdOS3vPi38vcXxHSS2P92v3pFvq+X4YMigxHvQu8u+K5mKqjrd378+el3iBIZtKbxbo9hlf/7vyPL2CvzKg9qRPPypkZggOs4BYPyehRXiP4o6q+aOl8sXlL/KwLvDuUOIcJpkhqRSyeGYFfmQ8QHC/IA+fp/vBuAfvYeAIrVAx69NTdAensg4tt3iPh2Q8SvL4geQeF5GYcxJEJ24maDQMDL6kHsLUGqJv18GSRDreI78uyk+YA6VZOAfyBf/zVRbzeuL0U/GPQlgxGCFJBlDdIiL50yTnrEGRDL7WvwGYItRJUyTxLXgSg8/GqKl8FL+whkD995EMNBB7ymBkiSe1D9IIYA/QzDX+UJxPJ68Gh1ipME8eMSuisv+1u7gV5/HZh9/frVdaroS3aHZAq5t5kKgwQfCiOfPxclCJI4jOovGfCiHPn02++fkP9E/qdVN+aDjA1sEDevwbROEEVbrxBYo00KySpkSBAIQLcY/vb7PRyDdhnsi7Cy4iAGt8WQ27eEGCy4x+g9QNDmQUVQPiT96DekjaBfkLiG3oLVXj1/yQYWOSQt27gC7068L767/j3idzlDTKqHD2GcgjJPb7S3XByC6eWl/4LMA+TDU9BcGNdbm46GxuyDAmQ+yLwernTqbyHM8hqpYAVVQf+MNBU0deD81YWsB+ekEKac+iuylDaw4+UJ/DU46CYers6zeAj8I2XvtyGT8hPMsdE7ixdkBaA3kcIpnSIqnQrc6ALnnhGw072vh8wdJAMtMvR3MMToVtu3zBP/cq64zyHSYw65TwHIl4bECRr5/zCs3JSV5d1EFvXJGJms9N3hnlnDWDUYep/E4MRwW3wrk29TxDvgvEPxlyyJYTTK/h93yuCWTHeaO7w1JcyUnbi78R/KurzxjWuYEkOMy3JIY+dL9o75z9AfMCDVAF+wck8DDuQfAoen75pGsDyH62/9H7ln21AFMI+RonGT2EMCAPxbytdRORTUw/swP8BQXLACvOgHqxDIHcYe8h/CEEOHw75wc90KFgacme5Z/kEeD1MV1MJvPKgtrBzwguyHRIbJWCEugKPRQAO98OnGCkkB9DFU8cPDVeQUd2WGUfehoDPEIk+HhPkuAo+HMCmH5gLlfVQc5OrA9IK+bGEQYEF198h+6PmIFVR2SKl7lH4M98NW5Pvm9I+h6qCO36AfTudDX//OORCqS5jBA3TAjnuqYF2n4JFAMBNuLfzl3oXvbf5Dl9c/zPc//b0twK2vGj9G7hWJ6rqoXjHs3vveW9+Ll6cYzJG4ANW9DX6+96bPj1r7/F2tfb7V2g/c7856Rf6ehj+weKT2K0K84C/48GgRe2DI3ccHOkT6PDp8poenX7Id+BbpRzoMqAaR1u0/mss7CewwYQnCgfjebKqhR7WwLd4w7tYsPrLhUSsD6oRDZ6zy72p4sGmI7T10H1gMH2UDyvvDbHff+ySD+hV4es2aJHl+ypwU/Kt7ngFzYdJCjwzbJVhAcF6qY3C7+pidhosf93i30oKY4OevQ4XB/gbn3GfkY2R9Rt43Ebe9WdbAXdQvw7g8iISk8M8H7ccG0gVPcOtW98Wg/X1nNExpj+n5j0oMhQU19sDQwfOPSh0k/oEJ/BKGoPwjk/Xti5M84ALC+tAVYTN+FHkF9fThJPWMwPjB4oP1BGGygQv+KAbKKQHEeoi3g7nf/PfNrPxuy+83N9T37eVvT++wMXy/DwX33IEL/ub4Njj2ve2+DeydgcltyLr5+TakvkEb46G9fvcoHGaFt3tCPr1C5AHPT4M3Yc9K4uttX/101wka8228hRwghnyuhnEBg/UEOcEmXgyGnCD+fSdguB37N/rhy+ufz8T/Kxi8spTH0zTn+j5OkBSF04xLB4RHCgJJgYByCDYAAc6yvh8wDM14Hu4FnkNyASB5jgcuVGWIaeo8VMGIIRrQiA+X/19O6093LrCPkAwL2QQO5zMuSXqM5+MUx7okw7hQEdZhOYcAjOvyJMU6fkAMdymBEBwc0LyLe65PO8TNlY9J8a7a2/tU/h6fOzJA6WkaD4qTjuPxHkfQvsA5rAco3KU8QJCEz1EAZwQq4HlAw/UfSx8xGkJ4t37IYTgkwhHtMsj57RHzIS9ZGlLO6Gou3j8SJpiOu8fcXbRAywTtOqwKG8bMFcq3GEVf5A53ZMQ57gDpZHZa00qckrhbotvv6WJEmcuVGOAmdrCoxeYqMcFumazxahPhy5Fir7mKW1w3S7yabnWR7fd7EjVTpfZ3TGGptoLnpy6x95ep2bueVWiNw/SVRu20vFQsjmPMoKuV7aKc1JuTFati2Uz6w54/sevanpouzIhy6oSThe3150AzJzEoFpvj+Kx1eqVLCZgGJTNVjMK2F9MDIys8GmQML2yohBMSzbtYBYdleE6d2fmiI3aSmVgqsTk71co9M3t5v1C3lcflssWW22lrwVqJ+Pioe1q2uO5Xs2Yl2c4pEg3JNy2nMDIF9ZYUnKCNIj2z9faiHsVG6onwwh5r70ps6+QsJrV39pWzo6A2M1I5VViCHdusMqkuTGzHGXZeukyhKdvDub+2Pm2dfPua7yTW0vbKglWp0ZwEZ6a3jVaiZAGvEmguP7o2exkoG2a17eoyWx84ZT8KLom2mJyvXB5HjpO0QZJnp9k60aK9yhFOP0n3/r6Ty+u01cf+Nlj2684sR/U6zVcwuXtPUQ98oUxP5A6rWJdmp6lvFge1qzZXQkxGRr72d9JRwfV9lZ2D8yVYnVSYoeNcO4kzpSEt50J0Epe5dehfarpbzCMzHSVCxu77XbzmtDaeyPjc7ELHRjXLPF+X+0tCh8BfWdrBcCYqTx/Qej5edU5yNA1y2Ryw1hyRvNFePOZYS+2MWnqnYjzWOmq8UA1htBQuNYUTE7Y5q821YqVjdDxkwbS30+CgzfE5FN3tE4LT0065sKVSklVaqnvfzLimxScMn1oMOh6jaxuMRBDx/gE1IRZXCwOjJ51+9oNAxwS1s2cMW15Lmhf1gxvEs/DoThdnmLmzsXE6JXytLQ4n+nAM7GoVhmkpL7f8aZZfD3IwYba2eTqv6ekVnBOVLUaLzAtCVm+pxB0d+rjyMkdVk+m2FxONMnZbQtsVUzpPadmeaKFB7GOVCZVc0abV3uj0VOqq2QS2rL50RRarFcYWznTHnU5ezCqXSTMMk7FfZYcKm8nKhN709nXFE7o7L9bueZylOFm0PW4wE6zSsVAwG3s2iXa4wu/TEYH2F2alxAJvHARnJEtyGzuc6kxH9aYbx83COLf1TlbNfIGxuxNa5o26uRjCtsQWI0ndq+diuZMPZFKgvZE2pnMSppee3yUBO/fFlcXCpwGWxS4zOcfYzNMYRwzSTB2DbE8KKxU7s3tz3cRafNnPOs6SWEqzS8JYzMmVOWOmcsW4VGeotSZs8MkxBwFMTqDsFiqxtmaHSXbRN3RmuSq+6HKSP+EiqRgBOT9OJDmZGArtOm62RKOO6aJ+FGxckQCaGtdd4pPOodWLZHnaUXOFSJTsmPoe2/fJfHKOrJ3FztYLPMTEpiDasJbSNUNii/2JZFeGFzhm7owx5XyZXCxmeQiDi70lUlOONp5BbNi0O7K7K8gTLmhotWys7uBvsHKnXS5ga0VTBpeqWFd2O8911/qJsKlyCVZ7mWEZw6B2UaMcwVomz4ZxNeSegqVTGU2s6LqBzUyhVWeenGdKY9EggL71ova8z2xq5WRKxZNLfAvnx24khWMxketTzwv5NMTlw9jpvdAYaYkSzpOz6y12NUtybrNdHsd2LjppYhsB3q+AZKu6MwHFtYAbPIOezuMjRHrj6pyOEJai7WW22XlN62hr0jL2xf5aqEK2Y227PKKLZTcBJ1aYWQuc21glzswZWzQ9+8wuSiYweyatMko5BuVsy3DbvDE2aZm3DF+pdVJfuZkbHeYxs8ZmVtdiIBIDBU+1zbFACVFTqU7Da9unLmeeVqZSdpj4qjM5XnXZ3huuZcS0uWbPV+coA67Q9zq7MFftZL+NyzLgveWlqAIaGKLBQuBkcOe0PQh1eNANfcUadJ+pvK2rlXOhzU1/xKPwJB2NhYWmWWKfyMTiwJzVUi8MfMNej/Akn8YzhdpWnF12u7nhL9UuXztLwMzPJ2oU+yuiuDoLiUhrR043y5Hgyvx41aYlaaSe7ViHq96IbdUxV6ubHmXJTiMDW4GEyrayiprbaShsGhpnz4RQWav9WJXt6jJWdlNWy8+yaU2Pc8ZqfJ6rd6vreFts5hw33/B2PI5RFOgNN29tpbuwGVjF5G4UHsKzeJ7bMkVdDdUcidtJG+kbX05L56CG/vKIWQ6ljs29JoFih3f6UQ6X/lY214SnntN9s0EXaSoVy4Iiyh153CXS6Gg7vOSGChhteGNx8k6sTjhgRnQZvpio0JDD5ZydzVHdEZIUzbFJurVxVclYjWc2meAVJ3+u4ePVgVfogxQpsHXou/0pnYLFpF4udtullcKEbLNTLWzk1XLb7IMEpfzzAnbPhe7sUmOb0rlimbFxzBnqgMv5rDhu/L4O9ofL1t9FU9oqzteJiel5pLBLYlNPprZJx+DUG0yIZV1mUIt1303HUqa0xyYkr3UqJU4sx9rac7YbSjyn7WjUTiR9lUuBcNzhcFqQDifprHAoSRDVml/rbnPwjua1NUXblGLu0tXWaLoulk7TxL183CutIAgsqtcYp4ZyvdwXnspt3GWfsfluNqqu3lmnjqHncmOixxvdPbvWDr1O+2VigPrSXJeVxF+VeDQa16YFqLkaadt228rtldjMGLfYtRsh9+f6QamdOReps/KKNr0xOquwPc+otCrN60Y2yrAdW9uTsG1LSS6MszYlffV4BJRbhYVV7vYowN3GlGxdF82eM5v1BBX5Xmx3EqpSaRL6/XxyYma6CmI4O+lCe7pa40gbjbN8Sayz61qcrF2xOc07vKcVXBubmNHwxFif8NPVwsjRIxvpYLvpgIFVczuqEqWT60Le4eNg7+GNRiv1VF8b4/ksjwAa0TtPNWQan+tmbyxmtLY5h9L5qNprY842/mTVeLxxuo6aZb4iJGJdLVqYUYSknTjbXLEbXY7FA1FpMz86nC+qitonYacK7TSZ1BflDOdiNHVO5lTNbXMZCaclZ1pMSh0rIlxFjADm52UAUEOx8p3Q2W53RYtCWhDNKme5TLsQ3naeoRoxL5ULGGlm6grr7QVvVFxpF5HSqUsr3MljZ4eK4da+evPA2KymImlEsEX0xKifUQvSE4vQolGWvZbtSumJCDtp4rIv1SUWsaDMGr1ZL7Uk92WrnBU+m581MYNAEkpBPssz2cjJubSrV10o0LqiexsWV0eb1bYHhqbpEFB3DrVfjGWum5K1fphy+2i9TKhtbFCu04WrahcdlVN5KV1tvW3R+X6jKmpm+cZBjCsBVTU4KY0XFwjpK92liZNGL1L2irfbLWV2ebTlE5HTmrRLV2U4DkcQYOlV6Gz4Q8ezq02h6uKa3zCxQqMuo5BM1btGIo9kMAuTqs8NF4vSoqZylCHYYwthPXZGkUlKBZqB6WZkHZXExkvSh9tYPSAhdPVXQauY3JuvF6t6zi8qMumLJu5Edhzm+PiAG+CaS+nU98sphOko7b3U6grNv/jYaE5YCrUTM1EsEiqxOzcfJz1Vb+V0Ot0WhzPHkJ5jThjhMAEHO7FSfD3p62q7Gi93wGKilLBXHoYe3Jm1dZkzC0cRs+UVd0fjC/NAXcF4Lod0Yx5Qx25CBxUMUymLwBdnW45RSaFJ4K6PoZjZbNbZ3WZxLveCUAnBIl2emWQjJGCW9KmgYfyiPFgMv4azvJ+HNCnUYIKWxVx19inlHjHH359Tf+Hn5Go2shVPWpwCOE9xPcMeSoJcUh5nzk4YyqTSnDSOawhC9JZfDptCOYhh5/TauLxMGWxfTy+gRMejpF83qIrNeVa47iXLELzAPx4FKmM7hh27G90lTZIvLBYlphHNVlxwrcPLXG62swid7ovF5UC23L6FtrEuJqBhjYqLtucWOkpcsYneo5eL7wloyfJd2CUAS1b55qCZW+GIn2aho8+mo3F+AUqrUKvxNLuONspyIlYmppSq64iq56/Xh6gXMZEvxp7carN5kF7X46NHng+W2/hVxxt5Y+3tRrB29Hq6b828SD010mP+AgyeLqstbC9VdNi5o40grd0uTKy2U4VLT6bbixa07tjr/FFFZ6WAtfvQw1z3Ukmo1uybvl8Vu/lB2GYpmlF7vwX0MtXG6L7LF7HC8ScN39RnYqaQF54oBRejjoQYJVsr8EecuNwrEyHdtOR6dHWu9Yy6TjTCEeoS0N00ncMmaWc2WhcccJnSnARWsxxfZcwyPFt30RI268rrxK1Fn/1KkFA39ii5k+YaHRpupczOJWtmyx3lV4FALY+k1Ea0y7B+vaVGUsNnV7hlW/LeBKxsvOvoyXpkaIIKkW5rdLHDz6vOplOOWJ3qbFY5BKxW3T2OK6rstxTBY5tRJM/dRsT2o/1443EeJlMjZlLNgb04iInoHxt9MWrnyxUvS3kVXNEobWhyJO0BFs9pDURpW1IkXckkw1WL5c6jYte/4qeq23XZksHI0J1iM06UwuVpSrtgOccY+3SJmiYnSZeSr7WMgZFE7L2QrUahxdfhwhqHriyPLx19GG8OjRitGy5gAmXZOVdqT+0KsZGllnNEN/Wr1UVL2D2qr1crckWVB7PZXgnujNKzKVGNrDPXSMEybedGtlpas/XR989eN8/H/TK4KuymD21LodebQsyb3mHDvcBjo5AcNghUJDozcKnYMX0t3ZprrSWZUoKPXykurQF6qEfB4pg1RDM7hQFO53ZAbkSCwA6WjUX7yHOtlU8JvF8dfH5DpCLwXZefYahprZfz6EJi4apmFpbgbZcnFxgGMVqtpaJyztwcWwVUHbqmW5k5bZZcoV7CNV/yBzByttJhCsF7QXEkaTDjbjHeUzOqatAD3ztc0mXn637Epqhx3tplL0daQnqGuNleKz4U5WPY7iL7TCtLzGtrcaXrrlC3sqW72MXWeE9wgNPtRVzU6E0eVJGQHc/yRS/4RvF9sluincxj3mlk0yIX0cbCPWwOwS4ZJ3PUTI3xWlxSNXPKZ1QNKLmYVXB8SxyhKfoxb9ujCcrtebbhN+CySaYec/F7b4We0pAoT/jF4q2eui6pS92Pr5yQqZOuXcbkCk3NFeFoqz3cZMR6b4iEKyRFvWkaG185JxZuLMIlPprMeJ4BE1k9sRo7kY61UG+PaHyJ3e10dso8O+iPRzpeNE7LjRU2cCqlZ7nxKcBEE8XPI/SobkXx6fnp9nb36ZXAWUZ4fhpeDTwO+P/+0XB4jYu3Bz+Ko8jnp/93p5X3k8P314C3437g+K836a9/V9Vfn59KL4Zq3Y+Uq6QJH8eU/+1s9vO/dmo88Ojvr6uHN5dd/f6upHbC29F2nPlNVZf9W5Unze1gGzq+qYb/ulK9PV4yPN0MhGPEcPL/nUHw0vFux/5vdf7mx1WRV8PN2zvhFPjxnWa4DB8vBJ6f/B5GMfaqN4pl3kBZDCY/XkwNJ7nDm6mn3/8Lz/dDGpUnAAA= -->
