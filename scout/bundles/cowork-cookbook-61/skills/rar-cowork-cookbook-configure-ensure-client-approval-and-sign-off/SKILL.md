---
name: "rar-cowork-cookbook-configure-ensure-client-approval-and-sign-off"
description: "Applies a bulk configuration change to ensure client approval and sign-off from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_ensure_client_approval_and_sign_off", "rar_sha256": "ade2bdefd900a71eb19059c8e0b6ccb5f14109b228cb25591d346a21d6eb5687", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_ensure_client_approval_and_sign_off`. The original RAPP
agent is preserved byte-for-byte in `configure_ensure_client_approval_and_sign_off_agent.py` and in the RCI capsule.

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

Ensure client approval and sign-off Configuration Bulk Setup — Applies a bulk configuration change to ensure client approval and sign-off from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-ensure-client-approval-and-sign-off
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_ensure_client_approval_and_sign_off_agent.py` and embedded as the fenced Python below (sha256 ade2bdefd900a71e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_ensure_client_approval_and_sign_off_agent.py` first:

```bash
python3 configure_ensure_client_approval_and_sign_off_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_ensure_client_approval_and_sign_off_agent.py   # or on stdin
python3 configure_ensure_client_approval_and_sign_off_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Ensure client approval and sign-off Configuration Bulk Setup — Applies a bulk configuration change to ensure client approval and sign-off from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-ensure-client-approval-and-sign-off
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_ensure_client_approval_and_sign_off',
    "version": '2.0.1',
    "display_name": 'Ensure client approval and sign-off Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to ensure client approval and sign-off from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-ensure-client-approval-and-sign-off',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-ensure-client-approval-and-sign-off',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8c59a3aaa163d652',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/ensure-client-approval-and-sign-off'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/configure-ensure-client-approval-and-sign-off', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureEnsureClientApprovalAndSignOff(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureEnsureClientApprovalAndSignOff'
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
    print(ConfigureEnsureClientApprovalAndSignOff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZej1pbmX6GjHtIuZYaYh7zLazVIAoEGJECAcHqFmQcxj0Ju//c+SIpIu3xvdbm6H1qZsULAOXve3977EL+92F0bFfXL1xfVt3NIsNM0jvwasnMPWhRDUV/Ar+LigB/ILfK2jp2uLerm5fOL5zduHZdtXORgO1uWaew3kA05XXpfG8RhV9vTY8iN7Dz0obaA/Lzpah9ywdq8heyyrIveTu/smjjMvxRBAAV1kYE7UJyXXQutrq6fQkGc+p+hIW4jCKyPvQfdaVtdpKljuxeo6cqyqNtXIJp/tbMy9ZuXrz//8vklBt9fvv724qZ2A269LJ6y+au7MIu7LOxTFDb3VCCIHASATgrEBhvKEdgoB9elXwdFnYFbnh9Az6sfGj8NPkP//u+Xwa7D5sev33Lo+fn2Mv1Tuhxqo0l9u2l9D3Lt0nbiNG7HV4hNB3tsoNpvuzqfrNcAE+fh62Pnd0pFCf00PfvhweQ19Nsfvr0UQIS7Jb69/AgVNeBXd9P314lK+cOPr2kx+PUPP36n03RO4rvtRAxI/fr2vH6SBQu/L42DO9efANWHqx3/28sflJs+D7knPcHOl9ekiPMfHoQna/q5nbv+Dz/+K7Ju5LuXNG7a/xLdnx+EI9/2gE5PwX/8fDfyL9DsqdAHzX/NtgRu/TuagOXv7D5DT0P9K9p3+/8H0mmcg8R4t/g/JffPNsx+gn7+l7r9Zxs+Q8G3l6Wfxj2IDif1v0K/vamH1eLnT973m59++R2Q/j+SUYuudu8U3jI7jwO/ad/efv7U3G9/+uXnT10JYs23s7euTv8ZzX9m1zufP1nwueqHP+8F/E/5JS+GHPqIdOi3ovwf9e+vkD7BwPf7zVfoj/kyfWbQpMQ704cJ/pAzDZD1D3b88eV3ABU50KZz749Blv/bv0G72K2LpghaSHULAEfAwW2c+ZPwWhQ3EPg/5XbtA7s2MTDscx2I/8nDk8RFAP36P907mH5xn2A6fwdI/+0BiW8PSHx7h8Q3gG1vEyS+AUj89RXSAJOijsM4B3CpsIfDt9wOJwwFApS13/h1D6DFGVv/CwClL9MXAKDQr3+Lz9ud5Gs5/nqH1viBW8pCnDCr6VL/ddLbiPz8qaULYNq/+m4HuKWFaz+AuvkM7NEUaQ8wb7JRc4nTFPLiGhikqMcHbHf514nYr7/+6thN9C1/gCwGPYpKMwcLPsSBvnwBOgZpHEbtt9x3owL69Nvvn6D/Bf1nu+7EJx4HgPtPLwEJJVXeQyDrugwsAw4ELgeQcvfSb78/LQ3I5KAKAp/GwVTVps0gai++9252dc1+QQkScnxgbmDqbKo9ALmhuH2FxAD6kBcwnR5N2B4VTQt5funnnp+7I6BqA3U+LJkXLdSA0GyC8TPUNf6d669Obd9FzED62+2v0G5xAJWkSKdqWj8rC9hc5DEw/0dQPO4DIvWnBuLeSbxC+ylOodKu7TKq7SePwH74BVSQ9+2AuA3l/vAtn6qnP5nqnjQP84BFwDLu06VfJp+Dip8BhPCad973NfZU77R73au/5c0zIex6coULCgRgGnagmoMy8Y9nSDVR0aXe3X5A0onS0wve0yv3GFz9F/qIxZ96EG5qS1SAMyX0rUNhBIf+/2lZJo1YQVBWAqutltBqrynnh6WnnuvO9t6mgZYBAuH2yKrvbcQ7CL1j8bc8jUHY1OM/Hivv/nmueeAbUMgDKKLc6YPgAJae6N5jd4rFur4b5lv+DvqfgZXuCAdUAIkOEmEyzTvD6em7pBHI5un6ewNw93XtTaqD+ITKzklB7AS+792N0Eb1lH9Pp4BA9qdcHKLYjf6kFXBEC+IF0IeAEDHIKFAY7qbbF0BNkHp3L3wsj6e2CkjhdS6QFjS1/itkgBSawqgBeQt6o2kNsMKnOyko84GNgYgfFm4iu3wIM/XBTwHtyRdFBiL7jx54Pvwe9HdZJvEBVRv4HthymBDZ868Pz37I+fQVEDab0vS+6c/ufuoK/bE6/eNbfpfxowiA7E+nwv4H40Ag67LmHnITeDUAgDL/GUAgEu41/PVRhh91/kOWr39p/n/4e/PBvbCe/uy5r1DUtmXzdT5/FMP3WvgKoGMOYiQu/eZ7XfzyyLsvj7z78p53XwDnL+959ycmD5t9hf6eoH8i8YzwrxDyCr/C06Nt7PpTCD8/wC6LL9z5Cz49/ZYr/neHP6NiQuF0BIX4oyS9LwF1Kaz9cFr8KFHNVNkGUEzvmAxc8i3/CIpnyjxQCNTTpvhDKt9rM3Dxw4MfpQM8ylvA25t6vNCfBqF0Er/xX77mXZp+fsntzP9bA9BUKEAAA7NMAxRYAJqnNvbvVx+N1HTx52HwnmYAH7zi65Rtn6Gp6f0MffSvn6H3ieI+reUdGKl+nnrniSVYCn59rP2YNB3/BQxz7VhOKjzGpKlle7bSfxViSjIgsetPxb/4yNqJ41+IgC9h6Nd/JSLfv9jpEzqa1p5Kedy+J3wD5PS6CeiBE0EigtwCkNmBDX9lA/jUftWBmulN6n6333e1iocuv9/N0D5mzd9e3iHk6YNnXwmWg1z90kxVcw4CFjAE14/QAs/+7zrOJzGAgKDJAdTAzIU6YOj1GBi2KcR3EAYmGJf2YYd0XYcIEByBGQdFaddBCYJBPAwnbRTxSN8hSJoC9B7R+jb1CfEkoA8HPsYgqOthJNiCMwiF2oxn45RtezBNUzAVeKBIfN96AfD51Pqh5WTSj+Z3ss5T+d9eHBIHK9d4I7KPz2LO6LZznjvXaD2r09nV0qhi2wpbSlO4ilH4W+nd7JhDl9LcEbehSEmSq1pd0rGjyfAXZi2xwUWfnU1Gyq3ck+JS9FBY4K51cvH2Nwv1UiIwnNVGLAUe19tNbKrmpov5Wmw28/2GuIhG5nCkebrt7diUNWetkqSttprN+3vtgswkFTnBZdBjBI/xRgrqYqQcpa2tUK2cCnzWpHZ8OMnEeKuawdDwYzdWZ4MnGS09d/qt1VeYHJEivOh3tG+26Sm7XWXLDHsn3Rgl2aaFd3AQZKS7PiEoPxD0bp2gdGNiuzk/FnB8yUKmJQu09LawtkFkya/kVhVO5YrAtN38qodUWDo6XHYKlspVemmDfrGyxHN4PK40vU72ZYq7gb1AT61XibVF5kWWt0po8kaTerzB51XqLFEuSslyLLd4d8r6RmmrhRsodsndxBkqzOOzXp1Eo1I2unpBddjR1/4ev3QnilerbEchTD8s+OR8VbPTbtNcd4hQEh0zo1nWc04JFooLkqvmTlgVlJRz83OFwBiyTaTWWHRerh0LYk+W6m6+9hTQ+9hhUa9KwxHILce4wU4VBt2Tur3RmHaijp60sUmrXV1Ij2ksGyONytfb83akl9fbsVyezgsvspOMDD17q20RNM1uKU3b3IXvCqxMU4y6zaI2aW+sgaAjI2yl1r0QjjXLL93qGqMwHhe6YyAUPyO2FdmiUtzSPb4YiS5TIwOWmmMaoANvqJw429T5NR3y2WrmmosKp1sXP17289uaF4+h3XvsBtEP59PhMCMcsuPRvYLYSnADxcQ5UUyflnW75shIRc1c9KgTsjLP089+pZ151jsccQ25YcvKKBJsRR0Og9nfju0YYFbvDXSByal5qQM88NbiLAg0htkx5/UWOeZWxohoos5h/CKja00tfSQ/+qqxocxULzTXvRlNvR85MhB2IZ6e8KutzxcRrm32ucsJ/TlOSYJLc58P6Y047BVJXpY4Lrf7sMUtTkS1xUkZ14aIJLS+dJMuVC8nGHO3UiHa4kYu0VFeH1xZqnDmJHW87qzNW5FoZ1mXm351SzbXBh7cLbdfdlLYrOjdeKbne5I4ng8FZ1B4kGeOlW5z7yrLGFbKqFFiEsnMAmY+aqO44W4na9vOrQGmNvMUzbYYooRlKQoUJUg1XTjy+jRfycKlaWob2RnkEU9cZqC91vDkHMnrWaMiutH4SGwylbaDD95JII6Zbnv5rM+durihw9qY5adryczmadZU+YZm+E1a8DPHvgQY2SFlGZDlxTraOFLUfdLFgdecfE4UN72uFWOb4rrfk+t6i5Rkeqzw5pTGSn7xgksTyCs0RchGLOjqOA1TrWNlUjAH+Yu69krX5gJpL2q7G8NcoxRvtUavrguKYgPk2ppFTPcnyfICQV6RlqbwPLn0LJXAiRzuQrqgR0c3Kx7v0EXi705D3YcuQh2JUKQD5ILY7aaVg/JswYTiDyv8UB0BwuyHPJZPmnXScL1R3TWjwSumoVGnVdbZoV6PJxilt/RqpeNyZPW2tqyc6yHl93ILE7VoNYGhur5fGQdUjZbbc6CMdpIceeS4FNfpgiKWMXYL97Mgx9s1xhbekG7c7Iwy5KzT0mTHG5tDuFtUdjau3e1ssQqzE8+yB+JkDNohQLiELaRwX0todxRMaenz1ODkrYBFDi2w4U3k4mF5azdD4SuXS7tXTzIt7W7hdiEdkaHylyfFOtcyuVutZHyj4gQFOsOlaskDp6Ij2oIuNMiJvDBz1SBV2UOQeYNqNN7m6TVYrcpkZ4goRSXkbjMXCsJotUyGuWjc+Urp+9y8tpKrLVE2kaMHFD4q1JjO1VtPl4fS0rDDnIZn8/HGMYQy39ggCWWaxsz9thAaTkNUfyXb19sGi8tNbgKIRDtF9It+qUntNpWT0F0KF6OIcnZLnFHtjAjaKRvdwF8RwmxlGXa1ry6Hla7mqaR6TebBOeMK+sHZWcb2IpN5a2Wkt503sM7r8glHo2sBi/ogyyYOt8p2tlvPzJEfx9DNEjxl42vRcmKwrRmbutByvtGVflvaAxZklxBb99kiWMDwRmWQPJUZCvbK28JHzySBF+G1lYxBqGNaHmD+oM+9JNaXTnsmHE5ISkEt9NvJ3JfbGWXYRIaHS/6CWitNuUhVNFC0yy3WuCMw2trfdBuptRE0x1mWbCsmhcM0Cm37RoiLuA0qK5zNPceXTPuQW12+5Ph4MWO6Lb833dRY24dRzMZDOBD1Gc32jDminDsIydXYe6hSZSljIbJGI1VbKljZhD5uL/JEKcxCcBd02eox4tpucFj65tJcp+dwu2k2FsWNe5xNYYNeSmybF5G7vxgkHQzHgXX0tj0SAE1SzNDseJ2x7np/zdRNrUSHAHSQ3Qy1EjcpF0ZhS3l0WApCIXQVTp0cKUMWBacyqTe30NKGm6gnYAFRFpQny1elavqoiA57S7B1FQ3niGVIo8S1VK/YrJotGKqmN0itretB7QBM68E15kgPtmTlmC9OrRlvtKQ0ye0pEBBVjMlyQdCGmy8Ecnlu0N6wKsmXzuw84elzqs+OhcDmo9XKZtFu5DSAj6M4VPC212p3K7TnYUbN8wJ2G0ITZsop217r29H1WmRXiqbSrZpogc2xhNqcggTjupvEnQaZEs0di8Hrhdw7OVvuA1K6gZks2NrWti9v1tgKy87aTO0Ck7Edvy5u+YEdUVDiVvrRPK/E8/J8Ph/ACKnWqb9lGUWwVGe1K3Mci0dQhglGQxLjxNdcMTpSZLmrll3t7XQedivJUZSK2HTVbccPVGOt4E1FUMj+6LdGnSrygNd2pNTLkHZZxVNECRReE81CrdqsYH+tZWoSIbTCDOHVTCJFXva1u+cuN3m12zmrZiXOvRyEERwgm35l7bo2y1dHTaxbfN109nbgYfyqrfAYuyRbUHy9I0y1M6sI9Q4+SccOFumt2UdZ7qv4BRH8YxSy50on65wvyy66ltT5duaLMTtWs0NBJdhlBntFECJoMUim6WyqXsP4zYnz2lrBzrpUb0p/p7qVpkmYUAptv6+xizFTsnMJerqNqfj20gPAPFYi4rAk4npzwTTXsU2RDbG39APTXA7kxod7ABi3ukO41Xo9E7T5BhUpvu1qw+wU1BOxVN/7+z0hgl5iTQwicy5cbljHhEQo8GkRWaPJLwyZXRSKa5eDjC0M9ni1l3m580/GonXzw5Iu9/Y6OG3Rbd6NPiyHIPWyNj5qGV3pK2PFbSSj9XHm6BOyOyrNwGP2sox50K1nhByVK43fRDBeJpd4I11zndwb8h6LmFbkrzfBy/FqwF1JW7QSuagje71zyN4/LfIFGVHHqjrZXtlkxJVdE2Ay4fH6eMp9DnWdTBvOlxgXjvCV1PGNYg/outAXIV7qR9RZ7dmNz9qJS7s7KTksdttZtiQXl3DXu3kliiW4oFxD2VWqzibUtlN8DdbS25W2k4C0K89nifZ85bgSFXUsjeA9u2R2Nxe1pVLdcM1J5vtQilEl4XZJGIhIl6daZkSnSHLWnLvjw2GlKpG5CwPatLLLKczHlUeQ1tmg6vZsqhJXObJ9XBXsGiXpHtapiqznR+RY2ix9MZfCDXO7LIiHuOWpyhuWCMqHiQLLahIjkeCdLjyGLNe7jjhbMTGAHL+N1UHtRnWWtChjVuWmG/tcEU6Kdu6MYmb7bZgJHDLgHrexbtfxwBWFj+tETijrepbk8kHJyBqldGK/JA5rprhJ814KrX0cOCnVbkdyLc9dIcTlfe+Y0aEhjUXIV8x4ximt0HWlugiJBTaDQrTAjweAnOc9gtpm38iNidoHcaVV9XBphmbcNDknLq/zm21psCIS/m0XHjCHgfsZe9zh8Y4rO7VZcLMN3aqh63Z1dWWFfEnCjjKQpEwCn96onQ/6cTuPituekjsajwRiEeQ7CsX2GIHV5C0vcNrs50hKzK/ssDDOZIAEczwK8pqjbKwDCIgszaJEh3Zk68AcgdYpGDQ0vO2kblvuMWS4Kd78mM4UJTxcbiV8GaJWkLH1zhrZOeu22i6jT7lLiXlnSqSHo70JUnBwM6WX2qrZtEl4PjDU1lCay47LTYwut1gky64mbghekTI+gPdRkBlwsNXF9aWnYGl+OcCMUJJU3IjZrdO28i2cOVRfL2bH9RGdq3vpXJ33xhrPSkI79B0r+YKzVdzlXuctlg7i1hIiokpAH6NUh1kbeANi1ZuLH8DSnt0bJUtnPd7KEVXemCWMnHzKbplCsZQVeeaRq7W1USa1/HVc6/DxpPlrMsHyk0sEBIMtsgCXYnF9uLkgVlbqXACDRMkf21usZMNlFjtmg8QyVi8Z3w+TwWfFZXDQvNv+qg7JlmZOWjI3WYDaPuwakjeYQg9HLZ5T/VCHUjD0xf4gZOR1yG7xjrevJ0YatNjQMDA+gDGRFpaoccsOKeupy+MSw8jDTdY5ZeWfYVeVi33jsOiAXoQV4XGG0V+ZY+EU+8s5y3u8lk9leaT5RqibdYv6xGa701uyN1zmst2dTs7W8ugSJWenZcodU3fDMLmwmpNW7vsxGFRRD5OpVpj73AI13AviLtmeSbnWkjm6sIV+6YGGPsTHgqQYIsTFXChq/by/oay750MUzk25dh2/xeC+iT27riWsxg35iCFEGrtJRaFgTvQO8jYTjzy/ncXpsi/inmquB3EZu4GdwK4ujTMNBlOoE5qboooDGLSda0QmV8Y8XJrbnlJD3DwwMTofqVXRYsYc3zZ10C9mAxLj3Lyb+Wuj8I9K4GEr83a4dkI/t1TBr1M26ciTJa5na2JheSa23DboHCPX/qxNRIfuG8PqZIYRq82FzeMkByMVyx8S3fTq3Thv1tsTgPObEvYmtl30kYzU9Nnn7OPiTGzU2TanaPrEc8rONcp4ub6WSD47Y65h08aIwkgy2CV8bBptnYksVpzRbsXtudCTpCQlivPgDsxSvrE6mcFsCoRiKtlM8uY8q/nV8shtQXbM+SUhr929v05wZqzIduHMeeoWjUe+DhfdOjqmbZhEjHCSTx5hWABt2JuCZWpYzHTKXqoFcfNjvpIBOrSC4OqBp+9lql9h1xkn1pcGo2uu11BUkM8ZT1IJYQi2QRFeSI/zcmwP7lLaJY2OHD3QxurR1aaLuX7kTnNSMt26zr1kLcoBMuJLnlWuQytjCBdLQhYew9TLq8Oit2N1VsRJjSmznaFeMN9Dy5t8zBYYdyNg0TyTs5iRM4LtB7VgWfann14+v0wH3s9j6//eq+zp+PD/2Snm48Dx/cXW/dDat72vd15f/5vy/fL5pXZjIN3jDLdJu/B5yPkfTnC//K13IxOp8fHeeHozd23fXwK0djj9YdRLnHtd09bjW1Ok3f1A+fOL0zXT32Y0b8+D85e7ulk5ncJ/cH/cbErfbd/a4q3qina6F+fT6ybfi+2Py/B5wP35xRuBE2O3ecNI4s2vy0nr59sWoCz6Cr8iL7//b+pv0gCOJgAA -->
