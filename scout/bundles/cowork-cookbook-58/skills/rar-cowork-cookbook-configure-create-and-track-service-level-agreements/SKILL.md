---
name: "rar-cowork-cookbook-configure-create-and-track-service-level-agreements"
description: "Applies a bulk configuration change to create and track service level agreements from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_and_track_service_level_agreements", "rar_sha256": "68deee7354572e81832ff42288e2d70954e23a9ea24d21b61cb13e55f96c1654", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_create_and_track_service_level_agreements_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-create-and-track-service-level-agreements:5adcb06db29d2f6bfdc3a1954c2751181bb1b6cb6727427a1a1c6e946cf4752f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_create_and_track_service_level_agreements`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_create_and_track_service_level_agreements_agent.py` is
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

Create and track service level agreements Configuration Bulk Setup — Applies a bulk configuration change to create and track service level agreements from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-and-track-service-level-agreements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_create_and_track_service_level_agreements_agent.py` and embedded as the fenced Python below (sha256 68deee7354572e81…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_create_and_track_service_level_agreements_agent.py` first:

```bash
python3 configure_create_and_track_service_level_agreements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_create_and_track_service_level_agreements_agent.py   # or on stdin
python3 configure_create_and_track_service_level_agreements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and track service level agreements Configuration Bulk Setup — Applies a bulk configuration change to create and track service level agreements from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-and-track-service-level-agreements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_create_and_track_service_level_agreements',
    "version": '2.0.0',
    "display_name": 'Create and track service level agreements Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to create and track service level agreements from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-create-and-track-service-level-agreements',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-create-and-track-service-level-agreements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eceac0b0ead6f015',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-track-service-level-agreements'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/configure-create-and-track-service-level-agreements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureCreateAndTrackServiceLevelAgreements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureCreateAndTrackServiceLevelAgreements'
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
    print(ConfigureCreateAndTrackServiceLevelAgreements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZeiWLfmX6Hjfsiqa2QogyDxrlqrQUTAARUEobJWJMNhnmQQsLr+ex/UiMy89dbtd7gf2lwZIXDOnvez9+bE709WUwd5+fT6pAArQ5ZWkoQBKBErc5F53uZlDH/lsQ3/I06e1WVoN3VeVk/PTy6onDIs6jDP4HamKJIQVIiF2E1yW+uFflNaw2PECazMB0idI04JrBrcyNel5cRIBcpL6AAkAReQIJZfApCCrK4Qr8xTuA4Js6KpkUXnwMdemIBnpA3rALlYSejeqQ/EyjxJ7Bu9pijysn6BAoLOSosEVE+vv/72/BTC70+vvz85iVXBW0/zh4RgfhOJyVx1EEi5y7MexGE+pIHUEqgC3Fb00F4ZvC5A6eVlCm+5wEMeVz9VIPGekf/8z7i1Sr/6+fVLhjw+X56Gf4cmQ+pgMIVV1cBFHKuw7DAJ6/4FYZLW6iukBHVTZoMlK2juzH+57/xGKS+QX4ZnP92ZvPig/unLUw5FuNnjy9PPSF5CfmUzfH8ZqBQ//fyS5C0of/r5G52qsSPg1AMxKPXL2+P6QRYu/LY09G5cf4FU7263wZen75QbPne5Bz3hzqeXKA+zn+6EizK/gMzKHPDTz39F1gmAEydhVf9DdH+9Ew6A5UKdHoL//Hwz8m/I6KHQB82/ZltAt/4zmsDl7+yekYeh/or2zf7/hXQSZjBJ3i3+d8n9vQ2jX5Bf/1K3/27DM+J9eeJAEl5gdNgJeEV+f1N2i/mvn9xvNz/99gck/f8ko+RN6dwovKVWFnqgqt/efv1U3W5/+u3XT00BYw1Y6VtTJn+P5t+z643PDxZ8rPrpx72Q/zGLs7zNkI9IR37Pi/9V/vGCaAMYfLtfvSLf58vwGSGDEu9M7yb4LmcqKOt3dvz56Q8IGBnUpnFuj2GW/8d/IJvQKfMq92pEcXIIStDBdZiCQXg1CCtEfST1V2UlrtcvqfsVgXeHdIcQYTVJjSxLK0wQmA+DxwcNcg/5+r+dG9B+dh5AO34HT/B2h8s3iHBvN7h8e8Dl2w0u377B5dcXRA2gJHkZ+mFmJciB2e0gnMJngwy3aKma9PNlEAOKGN5h6DAXBwiqmgT8Dfn6L/B9u7F4KfpB1S8Z9J0FHQrBHaQQhq0yTHrEulWFvgafISJDvPnA6uFHU7wM9tMDkD2s6kDQBx1wGlgnktyx7rBfPcPAqPLkArFzsHUVh0mCuGEJDZmX/b0INNnrQOzr16+2VQVfsjtY48i9UFVjuOBDYOTz56IEXhL6Qf0lA06QI59+/+MT8n+Q/27XjfjAYweryM2E0FIJIinyFoHZ29xr1xA6EJpu3v39j7tvBukyWFlhzoXeUCnrwV/fhcqgwd1h796COg8igvLB6Ue7IW0A7YKENbQWxIHq+Us2kMjh0rINK/BuxPvmu+nf3X/nM/iketgQ+ulWcYe1tygdnOnkpfuCiB7yYSmo7lBeB48GeVXDwC5A5oLM6eFOq/7mwiyvkQrmVuX1z0hTQVUHyl9tSHowTgoBzKq/Ipv5DtbCPBl6g/JRG+HuPAsHxz/i934bEik/wRhj30m8IFsYjSVSWKVVBKVVgds6z7pHBKyB7/shcQvJQIsMTcAtcG9Zf4u8+T/ckcx/6GnYoc1RIFYVyJcGm6AE8v9bCzRoxyyXh8WSURccstiqB+MeikMnN1jm3vzB5gOBzcs9r741JO/Y9Y7qX7IkhO4r+7/dV3q36LuvuSMlRA4XAs/hRn/AgfJGN6xhDA1BUZY383zJ3svHM7QV9GA1qABTPR6AI/9gODx9lzSA+Txcf2slkHt4DqrDwEeKxk5CB/EAcG9GqINyyMCHa2BAgSEbYco4wQ9aIZA6DBZIH4FChNDqsMTcTLeFmQTbr7sXPpaHQ4MGpXAbB0oLUw28IPoQ+TB6K8QGsMsa1kArfLqRQlIAbQxF/LBwFVjFXZihu34IaA2+yNMhML7zwOMhjOKhTkF+HykKqVrQ99CWLXQCzMDu7tkPOR++gsKmQ7rcNv3o7oeuyPd17m9DmkIZvxUOOBAMLcJ3xoHYXqbVLeRg8Y4rCAQpeAQQjIRbN/ByL+j3juFDltc/jRQ//XNTx61EH3/03CsS1HVRvY7H9zL6XkVfnDwdwxgJC1B9q6if79n3GXL6fMu+z4/s+3zLvs/fsu8HVnfLvSL/nLg/kHjE+SuCvkxeJsOjNWQ7BPLjA60z/8wan4nh6ZfsAL65/REbAyZCnLb7j9L0vgTWJyi4Pyy+l6pqqHAtLKo3hLyVmo/QeCTOHZFgjany7xJ60Glw9N2PH0gOH2VDjXCHntEHw3iVDOJX4Ok1a5Lk+SmzUvAvjFUDeMNghsYZhjOYWLAlq0Nwu/poz4aLH8fNW8pBrHDz1yHzYKGErfQz8tEVPyPvc8ptEswaOKj9OnTkA0u4FP76WPsxy9rgCQ6KdV8MityHr6ERfDTofxZiSDgosQOGViD/yOCB45+IwC++D8o/E5FvX6zkASNVbQ3lFVb1R/JXUE63GUAf2g4mJcwzCJ8N3PBnNpBPCc4NLOjuoO43+31TK7/r8sfNDPV9gv396R1Ohu/37uIeRnDDv9MUDlZ+L+ZvAy9roHhr3W5GvzXFb1DhcCja3z3yhw7k7R6oT68QnsDz02DaMoQ173ob6Z/uAkLNvrXTkAIEms/V0ISMYZ5BSrA1KAatYgiS3zEYbofubf3w5fWve/B/HDFep5br2BPStTHaxTzS9lwHt1B6SjgYNUXRGWrbqE06NklhFIFRFmqhDglognQ8gppiHpRr8HZqPeQao4OfoEYfzvifGBWe7iRhGcKmJKRJzlwAAIVPiSmFgRk6wzHPIzBsNgOYS02g+ADDLRpYGOFiUH7UsVEcTKceTTooOSUGeo/W4y7n2/sU8O65O5a8QUBOw0ELzLKcmUOhhEtTFukAfGLjDkAx1KVwMJnSuAd5E3D/x9aH9wbn3k0xhDpsSgcdBz6/P6JhCF+SgCsFohKZ+2c+pjXL1sf2IViPymTUdTi5x49FPykvmI+LI1TQ3ZPIpBy4OrxxLKtF3Us6unW0uLGOWraUwx05H1drKsnMAlzg1hORs2XMGYqLm5ibkN5SXYh+zU9zXSmCTascD0Z/CXidtx1SCyWt7nPNSY55rfGm5ejT3jRJ7aD36NxQT6hXRHagmKa+xvExrZrXBFhnjdekRc1yuCXL6JU3V8nCXlA4blURY0+Y1J1qx2JdUwudp87aAl9ohVs6Sq1matR0q7a1Dnl36cudqgny4SxfzdmsWU9J92JTxCHpZ56AT9tJPzuFlVIyh7Fo1b29L1yqUhV+JTlWD6dbpxaL8X6DT/K9RsW16LFpIp/zeHNqQmUTb/RcWfCHTj8czwvTzZJZB8i41a68ddqMlzNWlkNji2220VpVsNN67h0m57ZYE2cnvVR8s1o5oygxS9n1lLJJqFMR2IkTb85hcbTF86KM8PmsL1au0utKqM3GuLjl/NSWONlcpEZRp5Vb4hd8AViHEkPcZxgLi2ybmxeUdZqPbVmb4B0XFflpPjrG2n5Goqv6sPHWI71QwvNVLMRCN9fbdTRK2VSKDKmJ0WWkrxu9MXcLnnOqNFTptMWm+9gr67WkHFkSSBNCjIOykhZtfUDrfHe8HJeYJx2i6UVgwqkPzq7ulSmtegs7dZrzdjJa2nzlxJplNk12Njof440oT1S+K6VxoZ6pSpfqbVVS8767nENJn0jQ5uO+W+iKfJSXZRbU18VoMXZOSkJsyp0jKstxEUWxuIfe8MWhz9ucotEZG5WNFp5Mncqk3uls4kpfkqTahl47lyYlQCUhM8+kLF3CfJ4JmKsKmKlG9rZc6p4TF5QyHXFs0HT9TJ2NeYJOI0yRK0+srr3u0QIWpd6uRDlaHhsnfnLWigjg3t4UdTcU7HmXn2QFr5WYOPSsmZwObN9fQVvhsyVaGR3XK/OoC/mZvw4rowetNncbUi3iE+aMUg5fq/O4SkpROfSORfFGaxGcIzMlJ6dr7ij1q6bjXbHkuuWZ0K8Lbd9zvVdFftYIi9YBjYnPwyoq6b4oSr1Oy3pxLamAZVJz1yzwiAiw3q0odYft1mgaAjwrthcSWFKdVYWrS+NpR2+nLRpPl+NAHdMzxZtjqYOeldlm59T11OuLE081VXeMK56lzzx63muZ2oBQ4I+6frhak1186aLxJNrOcHmfeHpZ9doo1nS+aGMJXYJwE+fBars+KB46m5aucDIZjyPdcOmN8T5EGW10ioLOKNjLdc1HIaVjriyOj1Wy0sGy0MwZsBRWNU+BckT3Z3525rRknri4Mj5YW/0k85JU8pu5QXMUEUpXUiq2eheSVybGifAUQRDqzdEsOBYqp8zPl1aq87UUUte9uemAexI6mlCiBSWkqY4z85lgnEmWT1upbTNl1YrFpeXLM7pbblbFJE2klboP6QOq4TMHBHPAgt3Vxyxa5LKSqFeqm6OHbnzu5umZn+4iz87TZAeLOzHvV4kYenPm6l49beQntX7GnBU7ckp/3APKMTySZQSu72JiAlxKPCxI/Tg746oh4RVHtipH4cdg1Gu5zHGMEzHENLcU7bxtvZVi02tGHEf7kZ0RIx+w+2sUG1O5NWHlGWflMlx1S9ZonSI01y6+IyRhbu9PDCN2R5vdSuOjKJ3TDV+ZcqywylRa+9W4DHBt24T+ft/KFK0wrDPPjaNuXudzqlNsmOxs7wZM4xPsmtl7uzhRzaWic6Mz2U6pILp2uqGxgj1R1nx56pfyNbtgXhwrMTrZZw498uzpyDmtz20dQkOm5cZ03W4sJKfwOMtx6bq0dm27GOeTxkN3yjXrMQUXcKHaTY77gAwN6N0DvYiMrXFJiBnwRgu302ertLhuZHp0pNi1aGyZKFDPMVAg6vThgWw0pUP1FctF3pU6FwdGvwgKudCEXbdofGM1bc7SSl5Ku8wAvaTs5tJxgepqvnLFCb9dTVYEc5xPxDm22QvonlrtXCjZrp7upnwwZc9X/pIb68VGNx0uPshqb5mLQAtoqg3caiVI1WxF2uI180dljM5q95oKR7Rk0iLbmmWW2Ze89RLVZpa1I1IGKh+pksbVcLl20PS60cRotZyF0mleuOPijNoU7aLGJu6yxYyZiFax9RNJdyosUq5dVXiNhC23h+k+CdapNScubiCIHLkleZbcd91FKY+FW8xYRi6VzExyKd4zK49czdPqwh8D71SecF/Doil+6ogW7P06K/tO5XHJRCthOlfdYystksrWBVBpChMcOVdssqbkku3CXDQOlSeTXJMnZ27Rq2pTmwJ/KAAh95tjgWoOChHh5K5JldeEaOkbabWyr/Nex+aYLzls72hXOOKeQxoAYbQ2c5bLZF/TL/25PLB1d6xkamgFxFm8XNDjYlRNZ83VKARlUe8n0S48LOR6P62LjmKLQ3bqfckV7LS8XLcoiIS4prfW1tk3p6wyJk24JsBmrVqHVN+X+WUqaOExzKmMmCxzoch2DknJFytlqH6RFRzGmzPVGMvkJhFFNeqPZcfQ08mZlt0dty+XB23pq9hWvgZcHWSpah9klF8uc3+fcbNNeHaZmGPcZJM2xQTfrhWhX5mL/dESvCLzqEVhkW6tXglLBk7BaWKlbklsRmwa3EqPE67BYZ0MqDE9pevzTuMCVar81hBcP2nmth0Fgj01WtJo13mAYV6mRXGNTsBM0jkJ3QSuV+NRx9rskRwFqjjDjhTo+KMZMvOUwZZC1INqkU+FtN3Fpm9gKAc7uF1L1ide9nTRQGOmq2ERKaZXR3QZcmtovt8sJPtwOBd9c+42fEs1U57T5NJz9aWF2o22Lzg1WPHYecMXxBwmU+BsR+hle2SKxV7KZ3K2mApcSWSwfsWNoKSOsFOK80FKHdEwMHkvHhrKVyUzH59VIM5N195ujWB50G1/ZzqTLFhPuzCVOhgS5Tpn6e3hWG7HIuwrRvFRUreTVSWd2iDNgEJkqLjaBznjnU99mbDFpQm6gjKuhun3DVnFTNSsRkfOxANZOpEL2IBu4+JMr73jaL88LgvB7Zw090s+W3XAVGGdK5bby7bEU2YsqpvjWcOP3KGxOHdOTftz29nMGXWOF8E7yfFpoauB2xNkCkpy6WgJvqevJex8x6dNbYxbxZvqh53hbulZT4MNJsmjUNpFxY5dCrFPy+w8h32XwxKNAo4uz1x0JwkOPOfvV4vT8uxwdZv4izL1cesoJLy/1mA/7CVSaVDkIjMaGV9R7WiuBY1BFdtt7VtnMV5wx3Nl0dIsch3jvOC8wxojluQCLp6yLc0d2SXpMl134KWZ2gfLEndme+sS9UbLXbJKlboEECT0mqlOdly4EW1K2o9RlzFRdRJqm5wsVfOosI1yPc18W1IiaTRiK7HYCcp2zRsspuKF5k/5NZw0/ONZCCAomBXrtUW+zdGI9NrlZiz6EWlc/IW/J5seFy+hnKkZdW6lRFHyhWe6PaU4oVIBTT3anq2pNsFu18uVCDNxLk9imYU+b1dmetC224OzTdj2MqMXer/RS5EQ+q0dENo0NhP3WIT+aDmv94vocDDlyd7Pr7VRMZd4Q6o+ijklrIAgUtB96x7ztXx1nFkz0akzuR77Vn5M5iDkoqi4NidV6IxAj3hNPgeUOm87nxAOZmeRqXuMeRwt527Q+/juWq7jrS7Yq9atL70WA9pgMFLG0Es+X/oH9uqqGr1IVA5UpnZt3CWrLpbGzOSmdqlmWZM0dsdOYkoosdqvxyiZVXSFdXJ6UU4stltSyXXSlCNiKVNVdFgIy2tdtjjmyAd9jnrGcudMSF7zrfaQY96VMwuCiUTJXG1HgLTQHYFxsOFzhZg3oQbqUkpNWVBbf0OM6a1RjET5jF0NcsNjUF/Rijpf3Kyz1dr2Sya75hveKGhVv+4wWUArTk3ayW7CCl5VGLOV2i1sbo9tMbcmcS5J2bEcEGi2Jad4TZvXCRzar6MRNhoT4ZjRxbOLZmP6OL7WwTrEm9iLt+hlotmGSvqHiT1l1hM1d1mT0LMjzhzxNUmweTfO90BsieVKIikl3+ORYMfphmY8X9E7DGIKF4JYxa/5aAe2JTqRRy4lxUZY5uWmNIglhzdTi4Tgl8skbKUleSZ1XmizOJNLVXsdRaFEd7NoCgpO5McuWk65mdiFoGmvZzjnavBe622nGN6dxCtxBUUKm2pnXhcjiXSOEUX581OQ9i3EEDguK1lBrrqJTaWk0LsaKMZWR+ORmW0sqxuzG4zhQcr1YMQRpNAIAiqopkKNEoPK5918fm7LqLou0ZpahTiWyGVpsRLlnYWNe6DTcXS9JJuuVWNR9hoavxpzOG3R3nov+hQuhtvDerYAnbWeaA12IeGUBNvN/WY3o3foBmcFa5Zd0U7ejJwFkE3y0E15jK1UVknxyGlUtmnLmSfH2IxSSyr0tkyr5cuyDbeAt7Idau2EDB+N9BZzulHOxYq1P83x08juRVHkrstWDpjYoGH8p3A40ZnODcDpwiYHFzdsottuPRbuVJULsd6fThTECbef6ERIYSAnKBEYuT/TQ3KqbtcTmtJXoQizmhZkfrzgy6oZNXk5lSm8nHY8Fey7CJr4wBH4NW3dqNuj9ZyhWrqCU+GpPWUU6x9225G17dxCYvL9mq0bGYssEnO5otxVYU0WRYF39PokWmTVT2QWdemup3X16k+z43weUkVxYEnWmtMbtWcIOIZWtGAenV08EqJJFHOmRmvXUSAIBFbgbYDPGItyx9lKCEd0TVL0eqOPMPdEswBnvbFuLZa7UAAUOXaVYLpf04uZQu93u/J8wa6LuDPPVo1fiIt6jYua3AEBK7AxTjCjER2J9uxSyWYj07R4XsesEEaZuLow/C7STjW+6cczYb0/j43rwd+dcJm5BCN0PbMAa+3nxnSljNYZRZLalD1soYqTvRyp1G5yxh3dmul9P8GiNi1wqzZTofVYfN/Wmw1ncaylcOz6asIhpHU5+cpqKF1Zp62N1kFDu9uuwA2at3zWsGASGiM7QjmhmspC5I96K70wjZeDA0OLc631d/w0nztjv/XD8rJSAZf6S0d2QpUX+tzeOuedExWlFSUEPwEtF60JqcZmdZyOG4LgN0kyUxiBHtumJ4X2aR3CyKgL+7Js2SIZH1AAiGVoCGvZjtbSmqCE8Nocxqv9PB/H2IUq1R116vcOVSbtUmaSKDDq3Xm+mMOGpONX1G6/5OHgntAHcymco5lXZYduhrVqClAguIJwOTMNStA8HZd9gC76imGYX355en66nVI/vaLoBKOen4ZDisdRw7/5Ztq/hsXbgzhO0eTz0//cK9H768n3o8rb0QOw3Ncb99d/S+7fnp9KJ4Qy3l9vV0njP16M/pdXw5//hTfYA8H+fjo/nLt29fvhTm35t3fuYeY2VV32b1WeNLc37tA/TTX8DU/19jgKebqpnhbDucqHDLeTgAq81fnb7c843jeH2XCaCNwQCvi49B9nFs9Pbg89HTrVG05O30BZDMo/jtGGt8jDOdrTH/8X7Yy/+MMoAAA= -->
