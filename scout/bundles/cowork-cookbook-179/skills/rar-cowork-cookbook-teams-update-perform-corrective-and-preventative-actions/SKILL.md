---
name: "rar-cowork-cookbook-teams-update-perform-corrective-and-preventative-actions"
description: "Drafts a Teams channel post on perform corrective and preventative actions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_perform_corrective_and_preventative_actions", "rar_sha256": "c74539909d88da0e54df5637546a773d0d5a1ce855f538f98876d24489daed2d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_perform_corrective_and_preventative_actions`. The original RAPP
agent is preserved byte-for-byte in `teams_update_perform_corrective_and_preventative_actions_agent.py` and in the RCI capsule.

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

Perform corrective and preventative actions Teams Channel Update — Drafts a Teams channel post on perform corrective and preventative actions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-perform-corrective-and-preventative-actions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_perform_corrective_and_preventative_actions_agent.py` and embedded as the fenced Python below (sha256 c74539909d88da0e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_perform_corrective_and_preventative_actions_agent.py` first:

```bash
python3 teams_update_perform_corrective_and_preventative_actions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_perform_corrective_and_preventative_actions_agent.py   # or on stdin
python3 teams_update_perform_corrective_and_preventative_actions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform corrective and preventative actions Teams Channel Update — Drafts a Teams channel post on perform corrective and preventative actions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-perform-corrective-and-preventative-actions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_perform_corrective_and_preventative_actions',
    "version": '2.0.1',
    "display_name": 'Perform corrective and preventative actions Teams Channel Update',
    "description": 'Drafts a Teams channel post on perform corrective and preventative actions status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-perform-corrective-and-preventative-actions',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-perform-corrective-and-preventative-actions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b991b2cc8e6a5545',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/perform-corrective-and-preventative-actions'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-perform-corrective-and-preventative-actions', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdatePerformCorrectiveAndPreventativeActions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePerformCorrectiveAndPreventativeActions'
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
    print(TeamsUpdatePerformCorrectiveAndPreventativeActions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abeiaJbuX+Ge/pCZZcQRRECiVq3VTIKogCgIZuQ6yTwPMgrZ+d/vi3pORHZW9b1V3R/aGGTY7573s/cL/vZitU1YVC9fXo6elUO8laZR6FWQlbsQU/RFlYCvIrHBP8gp8qaK7LYpqvrl04vr1U4VlU1U5GA5W1l+U0MWdPKsrIac0MpzL4XKom6gIodKr/KLKgM8qspzmqjz7iLKyuu8vLEeF5yJVw3V4LytoT5qQkAERXnjVdZjDeVa5f2AsSoXAhyhaxs5CQT0sgLvFWjl3aysTL365cvPv3x6icDxy5ffXpzUqsGll7tyWulajac8NGI+FKJyV/lOHeqhDWCZWnkA1pYD8FQOzp+2gEuu579b9mPtpf4n6C9/SXqrCuqfvnzNoefn68v0R21zqAk9qCmsuvFcyLFKy47SqBleISrtraGGKq9pq3xyYg0MyoPXx8pvnIoS+tt078eHkNfAa378+lIAFaxJ2a8vP0HAJV9fqnY6fp24lD/+9JoWvVf9+NM3PnVrx8DoiRnQ+vXtef5kCwi/kUb+XerfANdHwG3v68t3xk2fh96TnWDly2tcRPmPD8ZlVQCHWrnj/fjTP2LrhJ6TpFHd/H/x/fnBOPQsF9j0VPynT3cn/wLNngZ98PzHYksQ1n/GEkD+Lu4T9HTUP+J99/9/Yp1GuVd/ePzvsvt7C2Z/g37+h7b9Vws+Qf7XF9ZLQSpXlp16X6Df3o4Kx/z8g/vt4g+//A5Y/z/ZHIu2cu4c3jIrj3yvbt7efv6hvl/+4Zeff2hLkGugtt7aKv17PP+eX+9y/uDBJ9WPf1wL5Gt5khd9Dn1kOvRbUf6f6vdXSLfSyP12vf4CfV8v02cGTUa8C3244LuaqYGu3/nxp5ffAWrkwJr2Wf9fXv7t36B95FRFXfgNdHSKtoFAgJso8yblT2FUQ+DvVNsTfFR1BBz7pAP5P0V40rjwoV//3blD6mfnCanzZsKjt/YOSG9PJHn7hpFvACPfvsfItydG/voKnYC8ooqCKLdSSKUU5WsOIDBvJl3AktqrOoAy9tB4nwHXz9MBgFLo139V5Nud+2s5/HpH7uiBZiqzmZCsblPvdfLGOfTyp+0OwG7v5jktEJwWDtDSjwAwfwJeqosUYHgzea5OojSF3GgSX1TDnTfw7peJ2a+//mpbdfg1f0AvCj0aTj0HBB/qQJ8/A3X9NArC5mvuOWEB/fDb7z9A/wH9V6vuzCcZCmgMz9gBDcWjLEGgFtsMkIGwgkQAQHOP3W+/P50O2OSgQ4JIR37kPRaDXE489z0CR4H6vMBwyPaAc4HXs7KoGoDnUNS8Qhsf+tAXCJ1uTYgfTo3S9Uovd73cGQBXC5jz4cm8aKAaxKP2h09QW3t3qb/alXVXEQQQkP8K7RkF9JciBf9Nat6JwOIij4D7P/LjcR0wqX6oIfqdxSskTdkLlVZllWFlPWX41iMuoK+8LwfMLSj3+q/51F697JEpRf5wDyACnnGeIf08xRx0/Qzghlu/y77TWFMXPN27YfU1r59lYlVTKBzQNoDQoI3cqXn89ZlSdVi06X1q8IGmE6dnFNxnVO45qPwTs8ZjWmGe08pjMoC+tgsYWUL/K0aaySCK51WOp04cC3HSSTUfjp7GsSkgjwkOzBH3xfei+jZbvCPTO0B/zdMIZE01/PVBeQ/Pk+YBem0FvKlS6p0/yA3g6InvPXWnVKyqKemtr/l7J/gEPHSHPeATUOegDqb0exc43X3XNATFPJ1/mwruoQZmA8eB9ITK1k5B6vie59rW5IOwmsrvGQ+Qx95Uin0YOeEfrIIAd5AugP8UmAgEDXSLu+ukApgJKs+viuwbeTTNWkALt3WAtmDe9V6hM6igKYtqULZgYJpogBd+uLOCMg/4GKj44eE6tMqHMtOI/FTQmmJRZFMKfReB581vOX/XZVIfcLVAwgFf9hM2u97tEdkPPZ+xAspmU5XeF/0x3E9boe9b1l+/5ncdP9oBKP506vbfOQcCCQhyekrYCbtqgD+Z90wgkAn3xv766M2P5v+hy5c/7Qt+/Oe2Dvduq/0xcl+gsGnK+st8/uiQ7w3yFSDHHORIVHr1o1l+fnSuz8/q+/yt+j4DwZ+/r77Pz+r7g7yH+75A/5zOf2DxTPYvEPIKv8LTrV3keFM2Pz/ARcxn2vy8nO5+zVXvW+yfCTLhcTqA7vzRnN5JQIcKKi+YiB/Nqp56XA/a6h2dQXS+5h/58ayeCZmCqbPWxXdVfe/SINqPYH40EXArb4Bsd5oBH3umdFK/9l6+5G2afnrJrcz7V/dKU/cAaQ08NG27QImBODWRdz/7mLmmkz/uHu/FB1DDLb5MNfgJmubjT9DHqPsJet983Pd4eQt2Xz9PY/YkEpCCrw/aj62p7b2ALWAzlJM1jx3VNN09p+4/KzGVHtDY8aaJoPio5Unin5iAgyDwqj8zke8HVvoEFAD8U3+PmncYqIGeLpiWPkF39019FQBpCxb8WQyQU3mgGwBEnsz95r9vZhUPW36/u6F5bEt/e3kHlmcMniMoIAcV/LmeWukc5C4QCM4fWQbu/Y8Np0++ACLBEAQYO8QSQ0kSJt3VyrVgD1u6PoajBLbELYJAXdjFLMTxVhjmY+jKJ1crAncXy+WKdC3PXbiA3yOH36Y5Ipp09WDfQ0lk4bgovsCwJYkQCwuQLwnLcmHAACZ8F3SRb0sTgK9PBzwMnrz7MSdPjnr64bcXG18CSmFZb6jHh5mTumWf57Ya7mZVOrvdUPyAaqWWLNrtFd1giHB2jA2VsZcRjuqN7nHNIJ4RyVGT1tLcnJcjBWfm9Y5I80vpdEV4zI+GQElaYEenmpDHthv7Xqf3QlEer0bZDJubeEyPUUmW5mmvIbyGJ1WaGgdlJY2JXt3OTqascb3KWqfiSFi7bgd9NpvpxsqOtGFVbPFjcjwhnHnus1M027BjxS6NtLmByQ6JNid5i+jbZgZK5qDPZVFPtzWtdtsUcaLsqtWtziRenOCuMq5mXl71M28YZQN8z0dOq0hnWy5FwQjSi75oTnhW7c54i4RXZkh2gozT2Uw/Mi2DtHq7PxQwypXDDGFVItayc7k5rKlc1xdXXRz8nJWIqyHp+7RxQ0+80M4lvaoavG+qjcHM9OpoH8ZSu+6Oy3JfSo6Zu+miBX39sh533sLqQi8NjDLJo4Cu1NThtcJeGol7GQv1iBvHs7RDkBlzqENkSMCOIG1FvLooyJjDnCy69jKBefjEnFsHD+vQ4clVY5hpZp00b59h5hbDXYSKc+OaHsMZzzVbEOz9mq/3uSRJu3iW0ZkYm2ILI3x13rXn8KJwqejUWXQisx7BTty8anbiUaNxr4SXmySsalG87eIrHpKnm25jcHqeZyvnyCb0tUQvTYJUxCp042ZMzitS2K3rFa0DKFr4l9OWN0+txAiBLYjRak8qWKnqVY0InrGgMQ1zRPlSHKp5GG9XoZPT1xl+TW7pKMw42OvW0ohuTeIA0+QoiNtDr9XuYVikysFWQCE2kupX16iqffay83glIpdnceGMAWeXBze9qD2HVGx9LmNCKtcL95SzXXMjc+2G5HN562GtH/SRXzsdryg3G+1Xc3qshKHi4LOMz0lKsfyTjeKOXwhr2M6vOxkjDyCqTbTzmLLV2mtcVwwvYnypX0NNVRf9kr9d7BnrnZ1jeLm4Kh6aq+MQL6vL0en1gVzipzK58C67YAnldNTqtNtsVdw/nLRUFDlaFjhd5YiLKtK4mN3W7qZiRb5bnkdOPwzXrVnHwYiykdkqumOH6vmGrAgPhu1gTGLVwTbJyT0idFIG2U1F4UiVyJ25n9tX0SXQwqOJ0Ze0xbA9LfAAm21AIEurczK7v8wx/6K4vNR6tShZQntuxw7bVBEJG+bsqPMFPsbWKFql2Cq0ELe7ywZzbUZgbLqbH/bC6K7Vyxx3r6dOvjo23zHFSTxeY2HcKJYDF+nOhVP9Sp/nixBXbZ7rc6mrqrRfRbpqx+HFaSgf3hJyuOhOi4bgyetRT8ZrpUbskVJtuXBOtyujJeu8tLfqcJ0XSdGdi43O8DV8QhgVF/KbJMTDrnTPIoN3VIIuI6O6pOLtNCdjrTzGWnTtCvQQZKGummkptU06EkshF4tNQ63qHlluVBG1svhyO5Fyxi1VHUDOmWtd+YLdKlvWFKZuSHuz9X36hnLicr0c5TVZOYHsdQMCOMa6IMxybXsu8s3eJ1wO3rD6WFC87l4SdakuiNZeVDBHZrXR8LMYRk0ay2YGZs7PkSMLTbdTsbGfwYfLxSAqV8qTOaVUN27fkUdhB4yYOZQ2kHYUqlfsbBLUCpu1sEblnisU165L1SXNytQmBbXgeQpau/u4rDhqG0fbXKxnsIMWyepCU1nPdSkdCYiAHCM63/Q8kmHdZr1LOoUpbq3RHJGjJfFsPy4lj1pvwBCoZvEegbdU2QTHIWd5DiR3oNU7fTWqJ+l6hGGp19UQReNdwSRjmZlImXSirng75SScFWVZj9yeqCpCavJy4XRGCavHJbU0Rz2/bubRkKRKF5+xhXe7yTJdu3J6OdzmM1sUWjtveVSDM4wRbjoyd6PZKh/cuZbOd3QwrDyP82/ZcrNQfUVubmeCFjYXkgtpdpF5w76/Hq8p3rqqmB85fez80R4u6kC3QjSwurHrKa22t+WV2FzptYhmkrFZB0hinzGvKB3F0h3iUDCIaRXS1hpMxN35DG/qmW2tN+I6xo7XMa5L0zadoxFblZ9yyrw9HNaLvgPIVlwtOaZ87NIMqi61DIUXlZ0h8JoQLXmAPU4x4lUfyrXEwJ2rXtTquuQBZlRNtm81XNxfDpd6WcqGru8uu+ZG367LjDDPbRVc2kExzzEdh/RVLwL6bDB5meWOTQpmRGRMePQO6MJvlrs9nRLsuB9UGCv3ikaLM+ugRBx/y4KmKOBLP0csUeM4ypDXGglbVlNSLYkIACDOpW4f4+QkbvGsr02ETxBqgY3HKNVHfdHdSKw8atZllWuWi9Dq1uSPHXVxGCMwt+ua5MS2Xp2NZhbRC3aV+gWrsEtdP+eLIrwEOAhbemZC+rL3N34pz3ZV4+QFs8k2t573uNl+e2hBv7311aBRQxqd8a2/4fyFx3h9njSkxEvOoT37XYTOrrvEbcaTpWbnQ150mKFHWmjiuQnzhVDmijucO8s99POO2cHlaZ2J9ixWmRN8udqeuI2qm7BGurKhDGVcb8bMTSPX2sinlHXpDjjiskN0kUsO5jHCNzFIl5SlDqv9Oal6Yy0c0dlGZA5bkrbhcY5FZ3jjuaC3WPLRKUdxcxlpDIFNpc3kXEtrQ9XMkdntDux8BRIYEfjLcISrUjMFLwjnvrQrb3G59HxSqmBv0zYGMrNctiXzitM3g3vCjTOBrJwdqQg95zHkmkT3B4Tehn0YSGGwWK1jatvqy5pFOCsU68NNk1SSr9KFlyOiJV0Oeb/YHodLhVG1czXhzHD2y0ParPkyuOKV1htsiyaHw7XKO0OXccRsdc1iQ+e65lM/E1dUrNGx4w6LTuKpQHN2xUrOtEU4z5SM54+wsxV7l7y0V42/9AEdm+ug5DOljwRd2eekat7w89a+hVxSoxt7ELEdk8/D9V5JRDD1NdSAUJ424iVphPzyWg7RpVj0GwMVmVO5Dwy+YObXQ2iyGhh58BM80zfW4HNS5gTweIrlfYFYMuwWfqA7yozbxU2q+yVRBAlnS/kRNc9idbx2majoV+QGhk95SEGpo7kvAsAKNA61DzOLdRkCG6oesSkw/B+VtX++1gZ3PohacVqDnn8bZ7HQCIgs1TgRq52FDtxpvkU31a5rpUzPVHLcGJmx1jgSWybLVLj1oLu23BkbncLVlDWtnrVUHZXzgmY4Y2c5rNtn2hzNcsP0rnonzc5wgG72Gj7LJbNtS5EocNa4Fda1pM8V3LiaTgV2alRLWkqIQWWHAJStjFLyJkQvh6uc3yy5yOMiZLYiLWRnrURsO89YBA5svvBWUnjIZxe8wrY2sj4dLXkz0q5jxJKIsEtVOpbJcPRSKQ938ZKQ/UEL0u1qXK4WZJwsTATW3JArDSfLdvnRoZMtHZX+XtW8c680jBUO42kfKntzrK+cUq4cSjkH+zRvbih16lARRgprw0nOjrGwVC+MeL3C14sCJ1E8Qi1LaymaLhfUBc9oWKHicTnWuIgV1+2tCme0xrp7Y5WY7Dns0cREY7gZr/4m29oC7ewFPthxEbPwKNSsRslsKCXZ42MyzOr8ZM/94ChpgwsfxJ5alzl2qW10vTDaWxscE/6yaS0nXyCu3PH02hJu2iUT4pVy4OM6WQvSYF0w9WjYSLJwNzYYg2/IOd8ZxWpwZUPxbsvllY013R18FZaCKxsSXEWUzGJbNbdTkqU8tZRxXtlSxILVidQo/ULzfCLeLEmeuHa5dLoinVrYjQMGNMzhqWqcnTspdA3qhhLF2NNhQ1gricw5Te8bu43XleUerwuJ4hCCiumLuGJ2BV9cmyHBrcsOWyhGt9OFBCX7ujC6kr/IXbwMzc04b+B0tikLbRzwdpVXo6kBhx5MWc4ZnCgqNo9DdF005ClFyYWswLVvJD3HozR6qjG0L8e5aLGHmbRwG2wxpgnrb+MlygorDO2IU1WtnDieSeRsDvZxlNMPxO40w7F5ZA9zuXM1Uq5mK7UgU2++lgvFOZ7VdYOshcByhZRmC1BLsGisFT4n6U7ccxSsz8Vqe3Eoa+/KnhkOmzm1KuM935+EjZuNMluBXZdl2K27GlfqZjDOl5Y01KW8lqm0rjJnGxAp5q1KrM+3qbjfuUwPBoIOlxx0ZLZdGCXkXm/g0UvmfcRjA85eQiUnV1ojiDMU9c31qpItd5FYx0HrCWYPz00PJnqst5yAj+bpwdDAuC2uC9s+dvKp9DHCwFGyEoyjrNEH9Bzj1KVmRHKvpI3DjlpuKd3VTAcEJ3Q2inZ7MP9FkTw29hldZaJ/NfF2bwq5NCvdGyK0aO25qzCTGSemTyTaejZ1yJfZ7nJkOfZMcOp1i9YXYm12R5k4zux5uNmzDdUrKAymyI4xLniX5wHHyMRmZfZYXPXVnil5K1RQL/T5kx8juatwLY6P+Rgo6+0tXYliH519BDRifLWad2g/Z2FhEcghXYW1QqJlvgv6QN7v9uuaMSmQHuyOHjc1HeFM3fksHmVtgNDR1Zsz3PKYpWO/63VnSbYjaupmJHYckFaGlyhmaWvXpfKCQIkFtQZdZIcsHFOdi7ZiuqSvVgnWup0lzVbMel8TKmKyVIfMqUW3ps7anp3nWLAnoyXL4YQxCH3JK975OtjbhFmaO7a58m256BfkLm8MjFsiqKN2+rJ1QpD/Ow0T1mMro9HSc5R9Rh2MnNzv916g+KgaeAeFM+fZDfabwyCfll53dA9kaiDxGvc8gW1OVUQrKwZpUTdvldhrGtTfr0bb9lFDR/3WQnFzQ9mz5YXo7BuyFRrK3gjE2C/kHlXBUCAd14umlsaDjTUmbgcsmoAh3CBqzp/LqSjLJ1RwRt6bpbmY7PiI7bZbn+IVVj+7J5CLuHwKEBzJx7XVyhYfUHptLJM5q43j7qauDH+EYWLBRLLVZCbs8IXsXSR3sAjE2rG+rbDbJL+SoWmWpCCxLEwtlWIvFBuON7Nzx4wsvCccWtMWK9uRcm2BEjCc80qWL2s9UCg4YvAcBUPdEgt3/coXFicDKU7o6tTuBZE6t2AP1UrUOdtPW98Tlhub8UrnVGbuV0eHF4bciuFCBnuW1GIbImWLYWRpDNVIql35YMcDB2001li7nlGj6WGDaVTejvex8IJaGIuR6CllTJwfTvx8ZDKioZeVnYy39Lal8HQ1wIscRfdLAVSwz8Y9j28iVrWcjmGFo0S34Y1bzoPNlsTFDR4PYicpy/UgrYVR2Mr9YPMLYu+354AQOtg4xcHCXK6uFEX97eXTy/RY+/lw+r/9Fnt6Mvg/9oDy8Szx/aXW/dG0Z7lf7rK+/PdV/eXTS+VEQNHHQ9s6bYPno8z/9Mj287/6imTiOjxeJE/v6m7N+7uAxgqmn1K9RLnb1k01vNVF2t4fJn96sdt6+glH/fZ8aP5yd0JWTk/gvzf6ZfpFxSSyAOub4u35+5P75ek1lOdG71SNFzwfcX96cUGmZpFTv6E49uZV5eSG56sXYP3iFX5FXn7/vxzvHX3BJgAA -->
