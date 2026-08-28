---
name: "rar-cowork-cookbook-teams-update-define-asset-accounting-books"
description: "Drafts a Teams channel post on define asset accounting books status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_asset_accounting_books", "rar_sha256": "38085e691dee2f1a6c3c97c1d5bf9d74ba18709eb16bc6cd90e93a16e604ab8a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_asset_accounting_books`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_asset_accounting_books_agent.py` and in the RCI capsule.

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

Define asset accounting books Teams Channel Update — Drafts a Teams channel post on define asset accounting books status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-asset-accounting-books
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_asset_accounting_books_agent.py` and embedded as the fenced Python below (sha256 38085e691dee2f1a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_asset_accounting_books_agent.py` first:

```bash
python3 teams_update_define_asset_accounting_books_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_asset_accounting_books_agent.py   # or on stdin
python3 teams_update_define_asset_accounting_books_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define asset accounting books Teams Channel Update — Drafts a Teams channel post on define asset accounting books status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-asset-accounting-books
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_asset_accounting_books',
    "version": '2.0.0',
    "display_name": 'Define asset accounting books Teams Channel Update',
    "description": 'Drafts a Teams channel post on define asset accounting books status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-define-asset-accounting-books',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-asset-accounting-books',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '66ee95ac0d59aaef',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-asset-accounting-books'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-define-asset-accounting-books', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateDefineAssetAccountingBooks(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineAssetAccountingBooks'
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
    print(TeamsUpdateDefineAssetAccountingBooks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6ebeiWLbnV6Hv+yMznxGBzBK1aq1GEBVUlEGQjFqRDId5kkkwO797H9S4kfmyqrrqda/V3rhxRc7Z8/7tvQ/++uZ0bVTWb5/fNOAUyNrJsjgCNeIUPsKXt7JO4Z8ydeEv4pVFW8du15Z18/bhzQeNV8dVG5cF3C7UTtA2iIPowMkbxIucogAZUpVNi5QF4oMgLgDiNA1oEcfzyq5o4yJEJsIN0rRO2zXILW4jyBmJixbUjtfGPUA436keb3in9pGgrJFrF3spAiVxQvAJygEGJ68y0Lx9/vlvH95i+P7t869vXgZ5Qbke4hiV77RAeMjATSJw7xIsJwEglcwpQri8GqE5CnhdgRoyy+FHUHTkdfVjA7LgA/Kf/5nenDpsfvr8pUBery9v04/aFUgbAaQtnaYFPuI5lePGWdyOnxAuuzljg9Sg7epislQDdSjCT8+d3ymVFfLX6d6PTyafQtD++OWthCI4k62/vP2EQCt8eau76f2niUr140+fsvIG6h9/+k6n6dwEeO1EDEr96evr+kUWLvy+NA4eXP8KqT696oIvb79Tbno95Z70hDvfPiVlXPz4JFzVZQ8Kp/DAjz/9I7JeBLw0i5v2X6L785NwBBwf6vQS/KcPDyP/DZm9FHqn+Y/ZVtCt/44mcPk3dh+Ql6H+Ee2H/f8L6QwGWPNu8b9L7u9tmP0V+fkf6vbPNnxAgi9vAshggtSOm4HPyK9fteOK//kH//uHP/ztN0j6/0hGK7vae1D4mjtFHICm/fr15x+ax8c//O3nH7oKxhpMp69dnf09mn/Prg8+f7Dga9WPf9wL+RtFWpS3AnmPdOTXsvof9W+fkLOTxf73z5vPyO/zZXrNkEmJb0yfJvhdzjRQ1t/Z8ae33yBQFFCbznvchln+H/+B7GOvLpsyaBENokOL1BNC5GASXo/iBoH/ptyuAbRrE0PDvtbB+J88PElcBsgv/9N74OZH74WbaDtB0NfugUFfn0D49QGEX78D4dcHEP7yCdEhh7KOw7hwMkTljscvBcS5op24VzVoQN1DXHHHFnyEiPRxegPxEvnlX2fy9UHvUzX+8kD5+IlYKr+d0KrpMvBp0tiMQPHSz4OQDAbgdZBVVnpQriCGePsBWqIpMwjN7WSdJo2zDPHjGpqirMcHbWjBzxOxX375xXWa6EvxhFcCeVaOBoUL3sVBPn6ECgZZHEbtlwJ4UYn88OtvPyD/C/lnux7EJx5HqO3LP1BCSVMOCMy3LofLoOugsyGYPPzz628vM0MyBSx10JtxEIPnZhivKfC/2VzbcB9xikZcAG0N7ZxXZf0oW3H7CdkGyLu8kOl0a0L1aKp4PqhA4YPCGyFVB6rzbsmibJEGBmUTjB+QrgEPrr+4tfMQMYeJ77S/IHv+CGtImcH/JjEfi+Dmsoih+d8j4vk5JFL/0CDLbyQ+IYcpQpHKqZ0qqp0Xj8B5+gXWjm/bIXEHKcDtSzFVTTCZ6pEuT/PARdAy3sulHyefwxYgh9jgN994P9Y4U6XTHxWv/lI0r1Rw6skVHiwNkGnYxf5UIP7yCqkmKrvMf9gPSjpRennBf3nlEYPCP20ano0G/2o0niUe+dLhc4xE/j91I5PQ3HqtrtacvhKQ1UFXL09jTr3TZPRnuwX7gcfmR+J87xG+Icw3oP1SZDGMjHr8y3PlwwWvNU/w6mpoMZVTH/Sh/6ExJ7qP8JzCra6nwHa+FN8Q/QO0yQO+oBVgLsNYn0LsG8Pp7jdJI5iw0/X36v5wJ1QbBgAMQaTq3AyGRwCA7zqTDaJ6SrGXB2CsgindblHsRX/QCoHUYUhA+pMrYugmiPoP0x1KqCZ0Q1CX+ffl8dQzQSn8zoPSwuYUfEJMmCVTpDQwNWHjM62BVvjhQQrJAbQxFPHdwk3kVE9hpn72JaAz+aLMp6D5nQdeN7/H9UOWSXxI1YEhBm15mxDXB8PTs+9yvnwFhc2nTHxs+qO7X7oivy89f/lSPGR8B3mY4NlUtX9nHAQGIIziCVEnfGogxuTgFUAwEh4F+tOzxj6L+Lssn//UxP/47/X5j6pp/NFzn5GobavmM4o+K923QvcJogMKYySuQPMseh+f9ejjM98+PvLt4/d8+/jItz9weBrsM/LvSfkHEq/w/oxgn+af5tOtXeyBKX5fL2gU/uPy8pGc7n4pVPDd26+QmFA2G2GVfS8535bAuhPWIJwWP0tQM1WuGyyWD8yF/vhSvEfEK18m9AmnetmUv8vjR+2F/n267700wFtFC3n7U/f2HHCySfwGvH0uuiz78FY4Ofg3BpupDMDYhUaZxiKYR7ApamPwuHpvkKaLP85zjwyD0OCXn6dE+4BMzewH5L0v/YB8mxQeM1jRwVHp56knnljCpfDP+9r3YdEFb3BEa8dqUuA5/kyt2KtF/rMQU35BiT0wlfbyPWEnjn8iAt+EIaj/TER5vHGyF2pAdJ8Kddx+y/UGyunDtucDAl0IcxCmFUTLDm74MxvIpwYQ8iHsTup+t993tcqnLr89zNA+Z8hf376hx8sHr34RLodp+rGZaiIKwxUyhNfPwIL3/i86yRcliHywf4GkiMV8QQGaxXwA8ABzaI/wWMbDfMoNWJ8hXQdbMHMWuBjterTns3PAEg5GA3pOOu7CgfSegfp1agHiSTrccbyFx2CkzzKQHiDmLuEBDMd8hgBziiWCxQKQ0FDvW1MImy+VnypO9nxvaifTvDT/9c2lSbhyQzZb7vniUfbs0CTjDpE1q2lwaZLZPJ/HBqPb6y3ri4euxZyYs27ExVluGS7Zx+pBzOUbwa877GLxs1O0KFUqLZjifuRiLWNc+VLGN002lXWgFMeeumdLVdzi4CoZXSYJphz7aV5daW9XXWLaGDLMWRiFVA9BthZLSx5cP5OqudajxHglIm20zfspdOSDyBtDUkV8tfFH36Bps6zr2nJ5Md1aenQefb2SR0vZZ8UYEQfbNqVM7sV77R92pFa22FiCxKNnM2UnDqpf1CMN4m3XWwxBHiOnP6TXdJnc5I1oMomTz3FUNFt2ddJte7xaBzrKF8qwOVfWyRxUJgPneuccA3klU3gdhacVnKqvWm7Fg5/u7HgWGftz0156cX8L1mfHOLuC4Iyp3GcbQ8eVg3yGn3B1Ju2YjZsHF9LMiZRYxUwJ2Mx2KGN7aY3YuGbLuN5toz4CLrH3tcrU8vNOA1V/48VkHLx1lBi15xIqbdrHzW2jYBeKTG/NnFgrHU8ljXM7spfjcLbdi7/XtVbcM0c6Ukc307JLv/HVpFKxi3HWKNN1aHk5yw+5tLvIbYOta3PTqpUNVtnBb/JYY9YzXOT37JU9ymYjkkCiqK0RXRtpv5XuOR215k7fEUOR3zN+QS9TsbsQdZsRDLY8ze44U+5sxtmrI2lfQtuyZ0TaZcSysYf10lkdt7eWI8s5R7rNYEZWvKTmmF+panmq72lCz0OPEDvzcL4vhZXYJBF1VfmZNeO2QtAMw7iSFPeuaVScNdcgnAF8Vs/smMSGimIO9hj1esOzyt1y1vGBz5rksJF1p1WCPD/WSl6Ihb57/mU5ZmypbifYynDn5dVCRIMEoCu23oyVMTejdU8LJ48uCmKBolpjqiNrULP9aWlf9/1w3BXusqqMtrBvmLRtg1q74pKyFi3cTbytIw/J6igJ9B4XUgkY27Mt37tlSNSV1l1PJkNYpILH+xV12S0NRcVBKS3Nc3KKz251SnVnm8dW2Lipk6prXRe0bZOXXZnmBmVbYj4XYmd2PPNudDYHiqWE+dwViZyQDmQbW/7ullOSUnspI9nDZWnstfYG0lXuUlSO2xpFaNbRiNggzarjWIV0gUqzq88rB2G+0qi9wjeHoqcOVczOmoFOlYN3CDOsO2GyDkB8XI9tJQA8VMXd3kRZ7ha0tJnoBNHPN8A+NaoseWRqr6lkpqV1ezZtIdPnwWW+FQw/VZhoVd1dalwcjqvMPJNz87TjLBbPTsz8ihMVZS0orNIYo/PO1xt6lFnLzK0DuJ4v66orybKcWzt9Jg/n68Vex40v3GlhL49tppkVQevblKdtVFwwNjEou81cjMM1tVuhl6Q57WzDPlkRW7VglP1NsSa2hbdseIza1jW2NjdGlahKboyqDMLCNDoAKGZnAs9ZLhXM2xxlyRg2/Ay9j6HP5wpFo9e8xGj/sggcqXL0+7YJVpFl75MQDalTllmKugGGKTD5UDOS4PQYo/eo03eG7vbHnhBGtFdDohIpi+6vwlLVQ8uFbQtWBfUWtPKKokViX6hVJ/WeYtKlYe7Oa34IGm7bVulmVUiz3Z1ZWMpW1Y+CYQ+saN0xRhRkxTk3TBvkVzkQ/M1S3p3W8okPVzim+u5ifcPT28ndQ2wI1jKXLrU4bsNshzPuHOICkx7kUJB5O4us8/68F9oqG9W5peQYSsbhqhM9mRo3UnZZ1As1A6TnD3dyqPZ0bDJ3Wk5rA1YRiug7C+D3PTaqda30xYAH/QYbb23Mu2pWb52uY9FN5nROsN7LzZ0IPV5baEpmnwYUtcWN6hadQmiLi8ivjpuxxmjNG3vbZxfX3HAig5fMUcajeq+wC1IIC0NmY3UV9dpRMqnz+YSx5jWb3yuiQzeLZq/nqx4neDdcGdmK6I9BSAYngHakPrg2Th3G1UGJh529vuRN7jbJIJo2pZmBcy6oijOiImGk2FGvCWngINe9c8ByMZzoRhEODlZ05p1rj3V+4Xe7NhFF8SDNB2Id3rcjkyZe3UFEiSozZ/nMX7aOEu+siDrJ3u4EGxbCAAYtE+Wgz/ZsM7BDNywj3Kx3Mwp3mPrUca0vLIdN3PdWfzA7Be2jbBe1dcNvwjJUT/asSpIg9a8EwGuczMmQNPLUQhVicU44jY6u1pVakaw59BgAbDvXqrLmdpwX7mEViDq74FR5yYVnnThnhK6KybFcwk7EOevNdbdUjIq2rV3e7wOP95eqcbzOHPiz6/OwUup0t1G9QM+EZWjLsyWIJbBMT+f7/NTR485fbpjtantYn7vSw49mdr0f2kG+LTXhOKwqCptrp32wFrnepy/Flj6N68ZbCeFwirmSOOGNNho2p1FZBNbrMN6Uuhy2UTDgeBWvcdl053vbBfcVN5uX+vWcUpwK5k1Rqryq+0l6SfYScbdiesb5LpFu+xPOSoZeDEqyYMrRiFntbFWD6F1OhSLuA6O6JDFz5ev9zrtLCr1z92u0FkkpkLZpd9gJi/hsUXxI8vsqnrMBPS9pC435U86HS3TW+bfGnBsJ06u+oI83sN/Hke0RKY6F+Oacs7pp24WenZYUvWvRop7Lh1vrebVMG/mSsOWT0oyAv+CztOi1nOoMxbzPmMMh60CCJbvRBlVcX9icb8QorlfagXMzljgPPM8n/orbHZfMntW7zJIX+BKN92OKbx1tVc60bLHo73mWr5tG3u/4ympwUp8VMn1YWhjXpVv5Hp1XxZVO78tFQNHLuDjHLE2XG6M+j9dC8VHqrBxns0EruZstzNZMmp2ccDuvgoUuqdsrLc3Ik10ntyqM7vPOSe92wa83h9jUVg6drFa0LZXoVQ+2mo26vtBy+7hDw2Ckyv5kEclyr8PY0RZduHa4RTUTcV1N1sA4ShClgki6aB5trEij1CPe2xGXHlVDTKV0bZsWUtrqkNF96TmanW0Uq6hFe7PekIelsIhsx2/GK1dUCeDSgah2zV27dldZgR7Z5Xq30yQXuFYR2MEe4yoZ8249JVBbatb1O7HeUAnn6vPT4sJTgkwZ51m0IcSs6QNMrraoSeJF3flH6AYuDsTdKW5yltSqM9VtzjzqkB6nl0Gsx8al4GJsaYhCtFuNA6ajc063tX2m4fQgnmIKRqgLeOtEdMD3dQw3G5RZDFh12roYy6Oh4wOdWM42naDOyblo9s4UfypHXEv8xoOSyHMlDbGV5jcH2CGTd0nzjiNRqsfjSTYNjQ+2TYk5BN6v1xdphR8ulOhqdyUuDyfZuLnyENqeGgnOHhAmc+Vump/qCs+DrC8iOSAZGU0rVTKo9EC3dSGJY6/Z+FrPtPWFXDvFSpcN4aDNslYlXQ7bS7ggC2f0QgprkJ5YQUnmy3u4WVgDkXq2svAI1IykUrtz4dHF9e7Sr7UdjjqJswmuundJeCxaZclFImJYovGlt1Ts/H72mTGn7RNsg3Xdmmf+qJZ7N9hpKtX0siVfY9momz2fXJQNX437PVVKFpzg4fCzH0+JddBrHqsAFQVhurT1sOc4NebPahSVQncjfHKdi9KpOkfj3WOJvhpXw6q8Eddwsd3bkVPO2bVYjZ6ZA8PocdTe9wF6Y1OXtZX4uAWHSzw0C2kvUXNLd+b3OJbXuTPL56hz7ELmeDDP9pUM2r182bGjcugqcJmRBBWIjKanoHewgpgNGKu4Zp1gUVMvFt1mUxO3cUZkrCdsgo5wucOhd82o78hzXKYVizPrvLCujqVJjhr5c6DDykJu6iJB98RJPwNYjsiTQ85yWeG1OEyku3SLQbq7iSjba2i2OmxNj8PSMxu4glbMBE4YOFLeee2FEzxANfwFeF1MDTelIPxynizhyNtYazJb9CRzxbHFgbd7GycsQzC3woJKAsATXgCCmgdJKDnojLAslNvMpHNS3bAAHZZo758UK1xc0OPWSSm9rfRoic974xgOOwlbh4N202lnl5aaO5aDj94yTVXDoxfE1j1vSqHYuHHueeHxttkZhNSLErGm9uhIbdQ+xxiqCPaCSB9vWAZL9BwIEdHAUf6QLkuf7i+79AjW5KY6hEFprkzjjKqYMrs49wXIeFJkgoMvCex2uIKOvDr6+S6KjLcNDhSOD15J7LrF3Zcu13JpbHCFPuI2G5Bcf7rbzn0b5Nt6t0nmVl3Oj7t5kNPXg4ViCQuSc2z6S3HGNR0n+rkwmrNkTm/a44Y46qLGsDWGD2K8Eg6RWUh5W5OKJZL+mrW0A3+TUcNY+DqT98kdzS7DTTcufDBjibvDr2bilbVSCAfzbeyrMstxZC/SPOEWd1+XlqFXmuJsllzMA6l1XLZgeT08EuImWZ9zLxKXIbPtNaljCHF7yVHOPZgzqaWjm3mP9wdnMFgJPammQMxKlyKYxVpQtgy7nJWCtsDD9r6IPKI5zVUxb0MtXq4HxiF3Ijek5g1bRrOgkTBLI7YaKbHyIik59qwUJMssAtjqsSAmTVK7KP4co2XgVWUDwo0ddB0VcsJZK3hnYDeR6JXx4nDbAMKl1nZPMOHRkpO4EG8Hfi8z3HX0hfKG+YrAcFS/HLLznKgJmkK7PQDdwHQkd0tNwdUCnzwMHb0ntNkoEVUHJQicdlybpQ9tRsFia115Ip4HfM9n3PzU04eTxi6VxVyFDdexuaDrM+61q0GBEw40mioYdzwRx9VSRxvdjbgjrxCdpXrGkY1xdFR44HYtiu6qe0Ec3NtxtRWYxWKhtKdFmsCRX3CJDdnkPXq+24t2Lglwhuu4Y3pOXLQAjZ7cayYoUXRkB2ZIDwvCW/Z95bM4v4MNbSYeTroeXt31tRvTXY+eyHVmbkRHER2Uvtak3hdBItyEE6dztTZferBXicOtKQEHp7gkw/CisywvB4KpjUdscxu09QHcFrIR3eMwolfspuG5ubHmFSGwIilj1oercHXc4NDxI+0GLCNbySYJ7ri4PXCrTqA3ZHmqKDqq53SwuRqW3+hEY/XKRuJMwCkrsORxnFc2c/tE6URmZ9w9FA5wkpSXCWO1w1XdKO783Kr3M3Wi9w15Bf4G+BbY9BbJxx1/7yhlifqJEWCxE9TdUbzYmUussSXVzu5njSPXqrshazmkW2ld78KBshdXTq7Q8TwUhLVnNqzmBUmzhXNQkkSO32sCbKkOGL8847NwrqGrs0zHkhS2R1IcmoIh/MQbSsKBAMuyYYErRXnEt/nMS1z5xHFvH96ms+rXifN/4xHzdPb3/+wI8nla+O1p1OO4GTj+5wevz/8d4f724a32Yija8+i1ybrwdTz5Xw5eP/7rTzMmOuPzSe70IG1ovx3bt044fUXpLYYzVdPW49emzLrHIfCHN7drpu9JNF9fh91vD0Xzajo5/71i8NLxHsfPX9vyqx83E6y8Td9lmJ4QAT9+rpkuw9fB9Ic3f4T+i73mK8SNr6CuJrVfz0imU9zpIcnbb/8bhtaeagkmAAA= -->
