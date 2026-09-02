---
name: "rar-cowork-cookbook-configure-define-learning-paths"
description: "Applies a bulk configuration change to define learning paths from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_learning_paths", "rar_sha256": "e687b6514a290fc0eddf7e6c726574bcbc2ec26e2636afe95a4703d39872d2f8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_define_learning_paths_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-define-learning-paths:9070fb4026969a7923be5a846d63022fdab2fb67fc1a8962573d13a6c1ab8ef9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_define_learning_paths`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_define_learning_paths_agent.py` is
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

Define learning paths Configuration Bulk Setup — Applies a bulk configuration change to define learning paths from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-learning-paths
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_learning_paths_agent.py` and embedded as the fenced Python below (sha256 e687b6514a290fc0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_learning_paths_agent.py` first:

```bash
python3 configure_define_learning_paths_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_learning_paths_agent.py   # or on stdin
python3 configure_define_learning_paths_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define learning paths Configuration Bulk Setup — Applies a bulk configuration change to define learning paths from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-learning-paths
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_learning_paths',
    "version": '2.0.0',
    "display_name": 'Define learning paths Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define learning paths from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-learning-paths',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-learning-paths',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f2a4466caad25d3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/define-learning-paths'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-define-learning-paths', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDefineLearningPaths(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineLearningPaths'
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
    print(ConfigureDefineLearningPaths().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaeZOjxpL/KmzvH7aXnuYQZ79wxOpCQkJIAgkhPI4ejuIQp7jB6+++haTumVnb+54jNmLlGA9HVd75y0xqfnsyq9JP86fXJxWYCbIwoyjwQY6YiYNM0ybNQ/hXGlrwD2KnSZkHVlWmefH0/OSAws6DrAzSBG4fZ1kUgAIxEauKbmvdwKtyc3iN2L6ZeAApU8QBbpAAJAJmngSJh2Rm6ReIm6cxZIkESVaVyLy1QYS4QQSekSYofaQ2o8C5UxrkytMoskw7RIoqy9K8fIHCgNaMswgUT6+//Pr8FMDrp9ffnuzILOCjp+lDGjC7sZce3HcDc7g5gtLBVVkHTZHA+wzkbprH8BEUF3nc/ViAyH1G/uM/wsbMveKn188J8vh9fhr+U6oEKf1BS7MogYPYZmZaQRSU3QsyjhqzK5AclFWeDEYqoCUT7+W+8yulNEN+Ht79eGfy4oHyx89PKRThpv7np5+QNIf88mq4fhmoZD/+9BKlDch//OkrnaKyLsAuB2JQ6pe3x/2DLFz4dWng3rj+DKnePWqBz0/fKDf87nIPesKdTy+XNEh+vBPO8rQGiZnY4Mef/oqs7QM7jIKi/Jfo/nIn7APTgTo9BP/p+WbkXxH0odAHzb9mm0G3/h1N4PJ3ds/Iw1B/Rftm//9BOoKRVXxY/E/J/dkG9Gfkl7/U7X/b8Iy4n59mIApqGB1WBF6R397U3Xz6yw/O14c//Po7JP1Pyahplds3Cm+xmQQuKMq3t19+KG6Pf/j1lx+qDMYaMOO3Ko/+jOaf2fXG5zsLPlb9+P1eyP+YhEnaJMhHpCO/pdm/5b+/INqQ+1+fF6/It/ky/FBkUOKd6d0E3+RMAWX9xo4/Pf0O8SGB2lT27TXM8n//d2QT2HlapG6JqHYKMQg6uAxiMAh/8IMCOTyS+ou6FiXpJXa+IPDpkO4QIswqKpFFbgYRAvNh8PigQeoiX/7TvmHoJ/uBodg7LoK3OxK+vSPh2w0Jv7wgBx9yTfPACxIzQpTxboeYHkjKgd8tMooq/lQPLKE4wR1ylKk4wE1RReAfyJd/wuPtRu4l6wYVPifQJyZc5CAliCGamnkQdYh5A/KuBJ8gsEIc+YDc4X9V9jLY5eSD5GEtG2I3aIFdlRDaU9u8o3fxDB1epFENMXGwYREGUYQ4QQ4NlObdHcur5HUg9uXLF8ss/M/JHYRHyL22FBhc8CEw8ulTlgM3Cjy//JwA20+RH377/Qfkv5D/bdeN+MBjB4vBzVwwkCNkpW5lBGZlFcNlBTKEBIScm9d++/3uh0G6BBZDmEuBOxS3cvDNNyEwaHB3zrtnoM6DiCB/cPrebkjjQ7sgQQmtBfO7eP6cDCRSuDRvggK8G/G++W76d1ff+Qw+KR42hH66Fc5h7S36Bmfaae68IKKLfFgKqjtUycGjflqUMGAzkDggsTu40yy/ujBJS6SAOVO43TNSFVDVgfIXC5IejBNDYDLLL8hmuoM1Lo2Gcp4/ah7cnSbB4PhHrN4fQyL5DzDGJu8kXhAZQGvCsp+bmZ+bBbitc817RMDa9r4fEjeRBDTIUMvB4KNbNt8ib/anTcT0u5ZjMnQhKsSbDPlckThBIf+fHcog9XixUOaL8WE+Q+byQTnfQ2xoqgaN730YbBYQ2Gzc8+VrA/GONe8o/DmJAuiWvPvHfaV7i6r7mjuywex3IHgoN/pDfuc3ukEJY2Nwdp7fTPE5eYf7Z2gX6JliUAGmcDgAQvrBcHj7LqkP83S4/1r6kXvYDarDgEayyooCG3EBcG5GKP18yKyHG2CggCHLYCrY/ndaIZA6DAJIH4FCBDBiYUm4mU6GGTL44uaFj+XB0FBBKZzKhtLCFAIvyGmIaBiVBWIB2BUNa6AVfriRQmIAbQxF/LBw4ZvZXZih0X0IaA6+SGOzBN964PESRudQVyC/j9SDVE3oe2jLBjoBZlZ79+yHnA9fQWHjIQ1um75390NX5Nu69I8h/aCMX8Ef9uZDSf/GOBCz87i4hRwstmEBEzwGjwCCkXCr3i/3Anyv8B+yvP6hu//x7w0At5J6/N5zr4hfllnximH3svde9V7sNMZgjAQZKL5WwE/3TPv0nmmfbpn2Hdm7lV6RvyfadyQeMf2KEC/4Cz68kgIbDEH7+EFLTD9Nzp+o4e3nRAFfXfyIgwHXINZa3Ud5eV8Ca4yXA29YfC83xVClGlgYbyh3KxcfYfBIkjvSwDpRpN8k76DT4NS7zz7QGL5KBpx3hn7OA8OkEw3iF+DpNami6PkpMWPwzyecAW9hnEJbDGMRzBnYHZUBuN19dErDzfdD3S2bBkxMX4ekgrUNdrXPyEeD+oy8jwy3GSyp4Mz0y9AcDyzhUvjXx9qPidECT3BEK7tskPs+Bw092aNX/qMQQy5BiW0wVO/0IzkHjn8gAi88D+R/JLK9XZjRAyGK0hwqIizEj7wuoJxONeA59BzMN5hCEBkruOGPbCCfHFwrWIOdQd2v9vuqVnrX5febGcr7MPnb0ztSDNf3huAeNXDDv9qzDRZ9r7VvA11z2H3rrG4GvvWib1C5YKip37zyhgbh7R6DT68QZcDz02DGPIClq78Nzk93YaAWX7tYSAHixadi6BEwmEKQEqzc2aBBCLHuGwbD48C5rR8uXv+69f3zxH/lcRZ3LQonGZ7hTZYnRxagTY5iHGaEk6TrmBbpWgzr2oTJ8QxJsyOHGJkMvLU44PJQhsGLsfmQASMG+0PpP4z8d7vxp/t2WCVImoH7AcOxFkMTlEnyuGvjwHFcFjA2SzI0S1m2ZZPAJhlAMiPGdAFPmxSLj5wRz7GkQ7rcQO/RGdxlentvvt89ck//N4iXcTBITJqmzdksQTk8CzUFI9wa2YAgCYcdAZzmRy7HAQru/9j68MrgtLvaQ7jCXhB2YvXA57eHl4cQZCi4ckkV4vj+m2K8ZmIUZZXtEtVxbGLV2F5X83J7pANhnjn0ck1nYyNo2ZkjFIJGCms22hxgOxEZdoUWS48V9+h+xXUH3giDSgtquMVOA/+qJwt6NUvdnqLLuppfVWOnaqcqWweatMpKSVPLg5qbJLWRNTXns8U2xq/cSbP0tNa7/ESg21OScBqtG455UpeC51ldbSX0KTrnK6NRWm256jij8NfdPK/yU2BXo0rNhWPmXMWYIU5UYZ1APlXplSYq2SHyKkNvaovItUyfpWaiY31v1pLFsa6+pCIpQmFUafy6ZApBTXxte5pb8siU5axsHRFvriQhWHFBH9c6P26x7bGtTLQwVwdwOQacSZ4ajG/l1eXgCXM+t8szfm3Xda91LaAuezngj5UAnTuZ2TJJLvDQ0MC6KuJiE8tm0GU6nXOLK6wQkudcjmee4NcVA1BmcwDXMDpVylru8FbB2ckClFSp0uQ60zbLxCFLcS1fuOgsaL0m2XlyQkeXaudtlVhlRUGQx9uapPJ42wmNm3hjy+DlNkws5UBKPITZK62lhNTyrIancZivW/MqSzY+4Wy36Kbt0ZqUG5BuTB50fHY901mmhaSCFbSw5U1iK3aFQKECTRlHL1eFbVNqnTOuco3SGKYfGYwC7HF3HG0kYtSxNNs0cUvmhWTAeeVCeNBnYl5grnQMWI9cEYIv7OQ2WXGRdWXKeFXKQT6f9m1NBoZerNJ9jkWXjPM2pi0s68MsBukSazdR7mszdBKVKSly0ewK9k1b8Z4QmqC5Gi4/GhHHrkjMumS3TUFTGn1aubGRbBeBPCWK2G4b/nCk+T1Ol+rRZtKaUMp0daE3hcXM5xLXc/qSWS/JeXjiCVh10Kbnz9RJYmjXPRz6OQWuGnnxyIogD22u+YVv45Z+KFnh6oR2rl0JMY0NtHFj3rD82WJRqCGUa0/vOnWmtBvW0xxme8yXosYzGrcUtNPJLibBdSmdK3mjltRGnKMza11AsD2pJgjyQlmq6xZVMj+y2zleBEySi4zR++2mXl4ip0kvIoNxC8ZQcqxwVwKtkwdFaBP27PenSVepwcYJWyzgcMiDPpgSd+E27qWA03VBsrspNtmqaehxHF5Zs32AVs5oFRVudp1N/XS+P1j96goDd7Sc9wIoJ+b1RBeTfCRxWexS1Tp0XJBx+wQtZL2/HORzmmH4QdeW0ysuXrhKctck56D57tz4IVPyYXLoWUkTtjsaX0TLnaxnZaKmepZvMw2zprp/Qk2cSjcX4+CUvuq0+6uMWuvFrNcUYk8Cy0GZXNhP666a4yCjuf1RoMpscqJ7qg8vM4JHV5HWTVTO5vc7azUVu8TeofOkksxsQQYjnY+mWNJvybNmT22RDEUY6teS7FVGKGwZD4qDmHeCyZSSpEsqI409NMDP9fEs8Fgyu+712D301LyqDwuud+RrZ7KbA4fh1HFECPT2sseS1t2flQ2jxCfigBf75VFSsbUMBwDyxHLXlJuuiSXB0lhHcKvRHEQ8PbtQLd1xa1VNZZ/p8P1+d1ltN7WiLjF55pmi1NLSpU3mZCNsZdEVNZMnFGFzWLRnneKSanI4BLJNyE07azE+MCLN3+cbwq2vZrJm9107qehwvjt4axtfTF2xjkTjzETxxpmxtH301oqtJLP5zNJAUJlJvZ0fw1k3D5OgnK3GktAdSW7VW73sH21BXYT7StCUdVaqYQH6JnEvScWf5rJYkQv7VEjH9XWpkQVwDwWuZULs4EQu1wlB2HXi86q6miRpr20hapV4GC2ODCoburGce9Q8knFG2lA7bDQZ530FKNbxG3MdTl2pxaTDgea4zjwWy4Q/uRNxulLb9Tbro+jEwXXqfqqboSCeSZ2r1bW3Emutv9ZTfGJJ8kye4tEaonE1bs3e3ksbQd1YQrY8FITIjRaishmTmxA75GOaypoZWO8X9WSkT3mmadsybIn9bsoxYY9Ts4TjqfDqR0uYDgdBm+Cnaxmrh7nIrpqAW5t5W3YM7ySttup6pYvnRXphKT72SlFpSwan9dFZuM5LEBYaOhLctD5447linooSMNI2Eh10Y/eXhbXRbHlzPhNC0qoQRMFUXmy1kXPpnE639hlE+iDYb4hWX7UieXZl98Ipk04yq2C2aMPVPjvQm3EU8hvGb8mjoVmm6ZB1sxhrZ/oSEvuL1xTZjpBPkU+nvcTwEkPYTAPQfrat7DYRyqV1ylinW58k0jVYNlqNKb9blbZtbqbOZMcJVesApjgxpohrXIUJlyudlpSTzplJIHHXlSA00fTUCuTpoPe0EmIlpYyy/TVampp2ZOlpKOFCccyohdzqu8k2stYltwR7f7/Hr8aVkMKtpOcBic9PQPFoWEH6aL+h4zl/WeAV6+RHXjzhF2k3pdfnwJ8sR+wJm3ZHZ46PjFSAbcOYSLL6nPkYTS5CYkbVK4IaV05tXC47x8YJtXO8Hc7qFrlWJKxSmI3ib2gqV0FaR1h6VFVfxpVxa7g4s+rAZQLzdGQFWy03j9dlhjlXbxw15ExJg6jaO4VWNAw6Pphq3B3ELWc48UoDR3XmiUKsHyI62Y8ijFWilRKn662nU2CmGwRTxSWudBt3t6HGG3TZ6WeOM5ckr56jYMNwyQwb8RLq1M0FFxqCm8jighIbgmEWe2W5LGT0etC9DiVPu1wo1ZjE+aLnYyl2TteptUdNR5zHy8N8GtR+4DBz/7qgx5O9Z42mStOTqMZdpPOSEZutcZ7w8krh6zyi90fiTO4Mb8Ev9iKpT7g+C84G40j8/FSI5qHUcF3A061Mu3wwjQCMF+2iVLS21pxF7bnrrEVdzszG9mKPBRV9xhc2oxrLtJC8Qz7BA7uwt3EiFl5b90rZ7KVtuN9aiyIRJeOUTQvSJYQ6zDZ8WcWFlxiau99ByKpTyWoDcIAzm1rUxXLbYdmaphXlsAbH3WoakMJ0eywN45Lg4YIfR0l6dLPltQDXbMzos9A5bTvQCtY2IsXVZU2ywFg6i8WSEbRYmPo02a3tDa2cRuOLZeBOPD9pl+NI2iRXTdUg76XBmOVMxIJxH6mF6R/ZlS665W7nrZl6W6j6ps1xXWbX0lE2IrEHKFpGJHferZcKucMdQ8q6M9l6l1qY0wLOshcrCk7UnpIoGaeobIPO83nWgsn8OinWy6kqEn0VpemC6UNrLUR9t8D78FjJJTXmJtfL3OLFER5MVvnJyCwiwzZMDDAv450DiWILU1Lx+XFNuiq517S5GkxyTXHBnIQI562b/cnJtifvWESkEefb5Mw26fJwTXZTsYSd8jGlHUv3ZwWu6ovC8GGmRgSMJI1RRSFRQ/KMsRW6NjZaPxv58ybj2N4ppydlW7JsZbUnLxyjqwXQY711oZjbNms26X6fbClynGqqR+Unr4hlaz5PJzjD0ksv2HHnhluspGzdjmt+wkpe122vh7oHOJmuNosNB7vTKKA02C9ur0JxvmYEMyXpIDzK4dnAgKLP8bG9Lo04OjnCKWU21gmnVo2iSsbCmHeoEFzCjjNthrxO50mxmTTNNpn63WYTxRIRlIuztl5YYns9ZVpmbAHtO2l6ytU2HU/xaZ0fJYwWknjkrc9Hf7KVJpe2Y/BlSE9OCz3Ntf15vcW7ogDOZEqZJ1Rs1sUVBdwpW6NGlVvNVnGPIcfHin4Kt/xhJYZdPY5cWdTq0aUupYJYyCoWrbH6ElmJftErDZXaPXeVFRS99iOHJQ4lwPTTdIXVM6+tOKzWA8JlPVfyO5Y3qkIaj+SoX1brYB8kVl1fj1aGrVYyHS8So9zMYnfc296RZlCLTc7jnXvmddYmUNhkhiQl9ec+cPDVUcCw+rwsAjH2e1KUPKunIARvCZ5Ux2PdW/KNe92NL5hPr0gBCGM8Rsv53CarCx9Qo5mhYVMBtk5+eoAZgfKjsRMFaBFlle9edrVFepiGC7AZl3oM8yf8PlfE3HIvPYauk4hfThhKqHUeDUx2zffTM+z5yXBPyniYqjTs3NT6GsQzlpWpEEvF3Sps5AVt4AoDlyV6EqwZ1d6DY14dDOkQ7VojoftKcmSpHq1IaiGNLbk8uskeB5K31E5FNO0vx6Qr01G03eKGfeS6bdjPJHqO583S3QXXRtj0KH9ZETNuqyRVhfeBWFgFesCnCe06fHtca31fFxd1schnaoaurm7RM6632e170+gpK07jaJdQ+VahwCnFCIIwcyxPMG6jrQwcHTFTtZkdT/tdkjBuMqZLGnVH/fxwLgEKG5ZzsCymJFX0hTshud2Mw68Zp+vKLLzo+ZI77EY9Ko/Q/ZZU1ctYwvrr6SDqbjvRO1wVt3QnJsd9faC2Igo8pyOwxcWfTy9F6wM3RQXdnWfnlb3bx8WsXMNRsbkcQjHdyBuhFOMdaNyF6npEIrnziqL76apdTstzB46RLVI+g6YYiZu75YXf4LyCprOgwY98i8ocLN6qsvTl0MQm85A18FXk0Xg85me+q8PKrBZWuGHmleGugE2PjnoTjEZuVxscbHliKqB2TkGza2Akq1qGs1XACvh4Sazd1Vxj4Uiz5iI6dP0K+q4zRgCtFy6A5WApdxva2+th6bFLxcvX85nbk+1Cbe2VD1ipGTUj2Lpy/KVKvNl6dZajFVvElVbvGboewdHNMBKwLEle8K9LcFH0Ge5ocDQFM4UTuXE064KcXu5PmOp0zmIijNHswp1hXcf3Ib1TUH4VzeXDzpRHUios0HZUzcecyDq4JE967iwnKNHw8ciS0AFDCO5YL0R/4u4uiY9Xyzhw4Vzku4vdUiBqdmRjHvC1/DRzRnDCKjyXcYntwR6hI3qHFXIdXJUZcLCJZXWn2j8G9HhFK3QwNTeTA8zwSgtaTkGVFLaugRK6OiZpYOZwLKfzM5xbWZEw1ndYnqbTaXA416OlbVdygUknNiYatTvBWQqdrA+VlKYNr853zFJI+wYOPtsm3WtXCHYSDHS27DS1KGkBdpK51ROsycZJ0bbGdS94QYqVS8GVjlO097ltpNgaIYMVylFcMyk2Y00sp0JejO0R1aXdFTvGeCJ7G8qOjuFiF5lkisc7NUkTs4+YyLOp/iLRZgLqar9DsfiYNAsdTccHzDdHxnxVclXKJn4/Hg2NiiTxybWf+cY42BK6JjDySsglr+cBZ87XVwy3nMQpsNISxzSmi/vtZlLZF8kl9+X6Mjs4nj9t8BYYFJwIsjXTSbNArhuj46oZ3y9Cs2ATCwqzu/I7pW4ERpJye6am4/H455+fnp9uh75PrwTOMvTz03Be8Pjq/ze+Gnt9kL09CI1Yhnl++r/7rHn/xPh+Gng7AgCm83rj/vovy/jr81NuB1Ce+2fmIqq8x4fM//HZ9tM/+ZI8bO7uB9bDkWVbvp+VlKZ3+84dJE5VlHn3VqRRdfvKDW1cFcM/VyneHkcNTzeV4mw4t/jgB6992EK+lenw5Ta4PQiS4RAOOIFZvt96j/OA5yeng56CTevbiKHfQJ4NSj5OpIavu8OR1NPv/w1jyeHChScAAA== -->
