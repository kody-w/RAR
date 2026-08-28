---
name: "rar-cowork-cookbook-bulk-update-manage-service-assets"
description: "Applies a bulk field update across manage service assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_service_assets", "rar_sha256": "c524b6015e03bbab97a1977fc61ab27780390aa33f08931f50a78e69e2c95c47", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_service_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_service_assets_agent.py` and in the RCI capsule.

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

Manage service assets Bulk Field Update — Applies a bulk field update across manage service assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-service-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_service_assets_agent.py` and embedded as the fenced Python below (sha256 c524b6015e03bbab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_service_assets_agent.py` first:

```bash
python3 bulk_update_manage_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_service_assets_agent.py   # or on stdin
python3 bulk_update_manage_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service assets Bulk Field Update — Applies a bulk field update across manage service assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_service_assets',
    "version": '2.0.1',
    "display_name": 'Manage service assets Bulk Field Update',
    "description": 'Applies a bulk field update across manage service assets records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '78f87de82dc43074',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/manage-service-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-manage-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateManageServiceAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageServiceAssets'
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
    print(BulkUpdateManageServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaebOq1pb/KvTpP5K05x7mwfvqVTWgICCIgKLmpm6YQZB5ENP57r1Rz7lJJ6/fS1VXtXdQZO01r99ae+MvL07XxkX98vnFDJwcEp0sS+Kghpzch/hiKOoUvBWpC/5BXpG3deJ2bVE3L68vftB4dVK2SZGD5WxZZknQQA7kdlkKhUmQ+VBX+k4bQI5XF00DXZzciQKoCeo+8cC3TRO0DVQHXlH7DRTWxQWIhZK87FooS5r2FRqSNob8evxUdzlU1kGfBAPkBmFRB0CbyyVp34AiwdW5lFnQvHz+8afXlwR8fvn8y4uXAQFAMQ6os7vrod7lmw/x7F06WJ05eQTIyhH4IQfXZVAD/hfwlR+E0PPq+ybIwlfoP/4jHZw6an74/CWHnq8vL9MfAyjYxgHUFk7TBj7kOaXjJlnSjm8Qmw3OOBnadnU+eagBbsyjt8fKb5yKEvr7dO/7h5C3KGi///JSABWcyclfXn6AihrIA84An98mLuX3P7xlxRDU3//wjU/TuefAaydmQOu3r8/rJ1tA+I00Ce9S/w64PsLpBl9efmPc9HroPdkJVr68nYsk//7BuKyLPsid3Au+/+EfsfXiwEunaP5LfH98MI4Dxwc2PRX/4fXu5J+g2dOgD57/WGwJwvpXLAHk7+Jeoaej/hHvu///B+ssyUHyv3v8T9n92YLZ36Ef/6Ft/9uCVyj88rIIsqQH2eFmwWfol6+mvuR//M7/9uV3P/0KWP9TNmbR1d6dw1dQokkYNO3Xrz9+19y//u6nH7/rSpBrgXP52tXZn/H8M7/e5fzOg0+q73+/Fsjf5WleDDn0kenQL0X5b/Wvb9DeyRL/2/fNZ+i39TK9ZtBkxLvQhwt+UzMN0PU3fvzh5VcAEDmwpvPut0GV//u/Q2oyAVQRtpDpFQB8QIDb5BJMyltx0kDg71TbAH+CukmAY590IP+nCE8aFyH08396d8D85D0BE56Q8OsDA78+wO/rE/y+PsDv5zfIAoyLOomS3Mkgg9X1LxNd3k5CAeJN9ABO3LENPgEg+jR9ABAJ/fxPeX+9s3krx5/vYJ488MngpQmbmi4L3ib77DjIn9Z4AHyDa+B1QEJWeECdMAGo+grsboqsB9g2+aJJkyyD/ATANugD45038NfnidnPP//sOk38JX+AKQ49GkQDA4IPdaBPn4BdYZZEcfslD7y4gL775dfvoP+C/rdVd+aTDB1Y94wG0FA2NxoEqqu7ADIQKBBaAB33aPzy69O7gE0OOhqIXRJOHWpaDLIzDfx3V5sr9hNGUu+dBXSQom4BQkOgv0BSCH3oC4ROtyYMj4umhfygDHI/yL0RcHWAOR+ezIsWakAKNuH4CnVNcJf6s1s7dxUvoMyd9mdI5XXQMYoM/DepeScCi4s8Ae7/SITH94BJ/V0Dce8s3iBtykeodGqnjGvnKSN0HnEBneJ9OWDuQHkwfMmn3hhMrroXx8M9gAh4xnuG9NMU83tvBYFt3mXfaZypr1n3/lZ/yZtn4jt1cG/hQJURirrEn9rB354p1cRFB8aAyX9A04nTMwr+Myr3HFT/dC6Y+jYk3MeIR/uGvnQYghLQ/9ekManKiqKxFFlruYCWmmUcHy6cBqPJ1Y9ZCvR8CKx7lMu3OeAdRd7B9EueJSAf6vFvD8q74580D4DqauAngzXu/EHUgQsnvveknJKsru9u+JK/o/Yr8MkdokBcQAWDDJ8S613gdPdd0xiU6XT9rYM/vTPVM0g8qOzcDCRFGAS+63gp0KqeCusZApChwVRkQ5x48e+sggB3kAiAPwSUSIDXAbLfXacVwExQU3fvf5AnU1iAFn7nAW3B5Bm8QTaojSk/GhAAMNxMNMAL391ZQZcA+Bio+OHhJnbKhzLTsPpU0JliUVymlPhNBJ43v2XzXZdJfcDVAQkEfDlM8OoH10dkP/R8xgooe5nq777o9+F+2gr9tr387Ut+1/ED0UFZZ1Nn/o1zIFBOl+aOoxMqNQBZLsEzgUAm3Jvw26OPPhr1hy6f/zChf//Xhvh7Z9z9PnKfobhty+YzDD+62XszewNVAIMcScqguTe2T4+S+/SotU/PWvv0qLXfMX746TP015T7HYtnVn+G0DfkDZlurYGwKW2fL+AL/hN3/ERMd7/kRvAtyM9MmCA1G0En/egv7ySgyUR1EE3Ej37TTG1qAJ3xDrAgDF/yj0R4lgnA7zyammNT/KZ8740WhPURtY8+AG7lLZDtT4NZFEx7lmxSvwlePuddlr2+5M4l+Bf2KhPWg1QFzph2OKBswJzTJsH96mPmmS5+vze7FxRAAr/4PNXVKzTNp6/Qx6j5Cr0P//ftVN6B3c+P05g7iQSk4O2D9mPj5wYvYLfVjuWk+GNHM01Xz6n3j0pM5QQ09oKpfxcf9TlJ/AMT8CGKgvqPTDb3D072BImmdaZunLTvpd0APX0w27xCIHSg5EAVgfzswII/igFy6qDqQNvzJ3O/+e+bWcXDll/vbmgf28JfXt7B4hmD5wgIyEFVfmqmxgeDNAUCwfUjocC9vz4cPhkAfAOzCeDgkRjhUghKBgjuuo47px10TtOhR6GOi9E0g+BzxHFwPESYOY6GJOLQTEDNA8ybkx5BA36PvPz6aGiAZYCEAT5HMc/HKYwkiTlKY87cdwjacXyEYWiEDn3QAr4tTQE4Pi19WDa58WNOnTzyNPiXF5ciAOWKaCT28eLh+d6hCNrVYndGU2FUneHGOaAyMqMwb3W08x2RY1tOE5sxta+GtaV2KXY5rYRsb4iNR4sKqyNm2KSzK76oLuuTHZh+LRy1ZeTa41ZfMHC2mc/iFWtxhHRQyWUhV0Tprswmrvd2JuznNnVEiSqznUSEb4Z8UmDdXdczqbmhm7aW2aTol9kZ9buD6gjN/tSci6Lei6NylcrsaJ34Uyrnwd5W9lo7rtcOdZC6FFtiihJrZGFTKFaU0nqHxYY4YCKKbjhiczsxTLcmKb93acLMRiZc4SS8N5lDqw37qmqEtVShlLsld2SUmecD4HEkz2tTsfBFe1Wsaj7a8Ulxt0513sYOLWN0squCKi8keb+/2vGuXpI+KE/So3aDvY4NOgm2OWd4S0zc8MVEyQtrr2rkKiXy3XXhHw+n8rK5Vu18f113lNsHttDtzeNNVOMTdz7JXB4HhgNI9kopy+vr4mDysWRoOZmpvKvuMNreoHifL0+cRy8TLGIlBz277oI/0c6Bn7mbfYOnN5tkb02Obq9zYay3KS74WHvis3M4dGOJ+ZK3WsFS1ABvua5cLMTm4PWeYyuKiJ60tMe1uFCiI75zbDM9LhjGKgejXByWJmNKKxuN5uZ865JMJuozxlPWF446oe68xWuLOO9vGTJ0ODIeNWQbuOwY3ObaaWut2vholGaBZdGo6a7kKvPTpcBHZtA3F+UiCdWQXa8G4xqBm+A6Z9wIjExCPhQFpIx19uYqQqyT7jFHpM0a3y6bq4VxCwXGw3B/UG5rtQ5vmHm7xK4QaojN3K6sscl8zEhSzPNS1NunKLOf3vN9FrSqxgWwRdsdx8GcB6+uc22FLHfO7JoSuyIkdHrFzmbhmh4d77gSxgqtD8HsVDZ9rBtWmxDIKitPsL3bKaQd72uDlNn5SQnJRSGqR/uqkDGD0H1YLpV51mYytljPkaY0N9s5idwKxWqYcTdcpEKhBbRIhI4zPTFa7zlRc0nx6CZ7bdAojufOvifVIttF6foyO1r7S7BaDn6inXDlrC5qZjhnl13eib2xpFzC2ojUCje6hFHDrdlzqDyK2pHpdCpw5DZvSt/ewENen921EG5qgUbgoZMdfO/18vLSj3BC9XZ2EC7AToJnx5oIY99J0RPSdcJxoegKmzvtYivs1JDKTnBCjLsGx+qE79tTpyyxYyUbSSTT1VmXfdmv9aJjakPRQ8nPucWtwgjTh2dYVyT5SDBSLVzWzHg9Uhs0yy1FJ2/yFuyaMqnWz/Sp9OqhlMltJTP1wYzcqhttq46LlRzVhIDYA4Yjup7wUs7aptOes6vD5XDFBdphF1M5gRiBrmorKdHl1Yyryl2wFVqt6V2Nwq1bgqZ8HGCsM6bLjL46ZMFcPdriXSnpI7Go9huwxyyQKCoK0Tcpfqc0yya4nZuCJtcyt1MsDD/Puuq86zj0xiAbf7PUW9m3Bk+gfNHFiY2l3JRMcWYsL/lxuJ9HWWtXaIFbnTEPzpWPwRTexPP9ilhtuITvSM0cLuu6FjZnRhauaSVy3M5nUmfRDXWe9uJyLs6SMo45cjwU+Jo9XL0D0fX9NThy2obSonS12PV5PQvUs1glN/XASLmMtIjHbF2KU8yh4GuBS/PRnZti11Y3UUgpUWVjxRiMAt9tseokacTBRY6UoxF8qCmSVG6HQbm55LlPtIYuhxnLltxRwk1UzkrSKub7PO7t1SoYG6ky19glstnaus5uHo33i2q9i3WNUsZbTc7CAz0yXcIbxBIWnfKKzpkgTYur2Z/FE2ZcpQ0n7/1NfNIPMJUONosfPK8bGF3gxTB0aQZea8swJIjEguekJuQ5XLLMseO5XCDJU2duh3XBLVpTTDdueVPQJOXMNcDoOlNYDB62u/1GRrJidWCTluykzORLUcv2shWhMkOJusGyRJPCVs2eGHlYhPxR7CPc52c1O3B9xmWOsLn4supk19DnTyZ3yNc9lyouKJMVlyH+edCE2VXjy9lw7fFYPxMqds2zdec3zrY1Uroi15qH+EtzP2dYnl8rQ1bjhrMrV13ci568OC3WGZXwy2bZC/J6Ti+VfC9WIkqGVrCzpNWprjk80ZVtoTu7g2JI5NHXwhtjc6PE3OxlXAlun9Y8e1aW61hOQM8+xzBTj/RS6sZbGegYXy1mwa7gtm5AjWvF3B1XbJRsBC4ekYsqrTYeHPiKYLV8fF4NpUm2u+PeXsjjFpOqq9NRykonO94STHLbpHxpXhLJi7phL/OH6DgXloxAXZomP7ekuVougnJTZ/owggI2663RkLV+U439Qhvka02smBt+9i+oiaVSoroilzFbIbdjMF5qolmeVIy3CmHRu6APUkvl1KTzApF5MphRtYtJPYlErbZjsFFYc3BBtVa6O6uwzQ6RxpI1vktv6KpbtMstUMMtYiNEKvUWnOUtr2CMwMNbgToqeaBZ7DDOFbZGBP4mbxzZV0WGVQRhvTweHYGPVAN1MvMWSfHh5rH6Sd6Q4QyRt+Vty5Ylzmy4a5fqGEZfvRXL7eZltCiHwG+LeV+uTqjsBgdSXfVgxseCPnR1nZDFaDgGhIRinTt4xmrV+nR9tsblkV7reHJNTHo8uOIhGn2rsHF6J+bKfFFK6YltBQprB4VPOa/aCkm/CkIRM+vstGZhQwRBX26ul4HmK9Q7kHNLX4g7Ds2cxa7FuB1FjJeDfgwkEYkXeyXztavvrKNg5Z+j0qoMHib0+oB5VWY6NbrOsNLbyjNea7iI12Zorx2iw21rWamvyqO8Osg6om5br6tSyWuuunWyh2ihV6uDlEpzTJc4xLyd4J04M9MRQytsmeWk4Wx1MtjBjXSKq8BKsr6cxf5AyVvndrWNVJNO5uUYkY10iMfLQuaPnWYJXROzhbDfITFTIhswDIrHXLuI8O5gjhhxBth1CZbE3otwUaVoMDtRHlN6kYY1zubGX1WjqtW0QoOTJaPCSdn0fi2FSHmJ9MxHe2TVRfhxE4oHeyOfHC0go44X1UxpVk3Juvtb2wghlhKlsrli57rUNtqeQ869rMLCDqfjulUuYbWWJA7fGdLZI0XJMlPxOqy1TSSt+GCNACQotyKaSsTOEBiCX9KZt+E6Yktx2xva15teuV36kFIP5bJyT+rtdNIN6YRRIxzPXPm2rL050Vpbemucgn1fpKW0DJzRiThmcQvU3ZKlFFNtOeu0gMfO9KwBWxuLlaHaO9sJl0xxqnBcX/Iutbzsj6TA7E3vtA3ilEwvfru4Hi39cuX34XaTqos4sTx75+3JppKd9TKgZ1sNKba03iLuQdmvETEdmYIycXQYAiwzotjwMpZMqGiLbYvU8niwHyK9wVYZiYSpuV4oPsDVML9sUXw33uZocBxLU+VVpi9P5cbYH0JtZa51C7VolDtgnbG3jTiDOdk7bzNY3MdOdkJYKiykdmtwNrmmzIYsxqOx7uuCFITYzQw7um7pBRs0KyMqmZxV2mo49mgqJPFl9OxqzJyDteoct9osqox1WX6+WCjtzCI21wKHPdtcFzZ7kJcHVjfzo3rIsSiexfY+uKyPYGaMj8jRiMDO77yskJrywE3Kuc4R8WBll0B1l55m2DY656ORL2I3qfQLXR0PmI/Q7rk/SQS5667FYNM7iqevh5woVu5i8Ntq3qJg/p/3KFfLBIzHeL0/zuduF+TzAdnPSH/UbXsenShqfq4FQzLqFk/norpDLhmPrBc0yPr4pkfOxlAokxzprN6u6nJTtRenV6ltUsTSTR6SYHlDBHjeF6uhcZJFPgj7Uxtmc0RgbuzS24qy5S5zProVakbsOdMedxtZx40qF9ICbs5a7x4cNgsza2fT5+7WwMps4UUKgng5QiORT4v4ihpyloHtEO5RAR4EeFddkb7qQ6KC85OFHXrPAxPA2mpKbFd2Bb3FhkWDm4rO3RCvWYasoK7QW309wdu9Z3BnOgzBbiaxpYUFmighaNpqucp4OsL4dMxJ9TrzaR63TNofw45LWBHdn0QSASVNxOi+lg2VQGV87cxJ49yLB2Glnkt1GGeLTmHA/EaC7fSOhztqRkSzXbjFce+ESs2xNUKcX10BjM/3ozDzehU3Rb5m90vY6I3ZrW97djixmtBvZp19dignK8KVUWz8MjyRBwqH69XKViuPrvBVsxyXywNGbHJ82OWhfyFnV2RcHsI22GBAWCQ3CkOr1zYMRqJdFHRJttuO6ZerfCPSFzjPvXU8jy8E2NdrY5tH3po5icQhOvH4RljSvEEps0xYs6feDqmKTqSYUCMvq0IArsoGk81DxQQBiiwpVaZOVzVZsbnmb+We6FZalEtW6J6zdb9BiJjhyFJk2wgNl1oN5uDrrDIIJtBJclPOiAV6FCSVyVu/ib1VCoZH+awNJschc8o5aptgUbSzar2Y4UezqtAuPMNnEmWEk6V7Fqy6Xut6Po5ia1Af6/6En62iIi+ekCBbXCHbg8KGXnksrINewIN7G+x4tqSwdSjjPkUdTwGx3CiqmzcWLO7ga0pSV5BCjI7Jlg3H6jnucca9hZ7DMPuY9odFFrXUuPMbQhsaqg/NGdjRlVjezUOzGRerfdcYyabuPb43UmbZHVGWtQ9zVhWCdOXncWRs9ZSAvbxwta20sdJTz2vGIsXRXCPTgKNbv44XOs8jGOpbG/3MNT2Oz3rtYodBhhz1GgjFitgL6T6PkZq+sC62IXxvCLULCjPqoc+6uMzBSEQsmHNz8L0bHs8vbkgzAjwzNqqzhwMNZ92askPQXU9SwEi7K6sFYtU4F1iBJaY/p+5esiXEV1F/HhyG0Mxn2mKrcfKGR7VQWNwYRpHOBTIr3DO2OeR2WO47qtGIPhPKoueqy7xC7CMssyt/kSDEoBWqUCrqEteyc3yLEZVWs8MBI0sP7W3sQmMIbuf+GbErA40ro/cXZK/v+OAWMWpmeDtUC+SAIZiBa1R2P7QboWxYDyfGYsz76uaYFwMLNmOyXazG3m13FwC4Re3cMiqLPOJ2XhNVjdeuJMLBsFQ8IWUUdTVfXurgOjqHutEFyRvaVX2Mxhl8HFPmOPeW145JpcOpkoSDd4GRhtv2u/4SVGlo07nu3cos0nXWr+XBUVCB3B6ddSFKNg+KMuQOuCHlRzv2rzU8iGuEYXFtdI0NiTnujvSPMqHDrIZKlaV5ypZlX15fpmPo52Hyv/6EeDre+z87ZXwcCL4/VrofJAeO//ku6/Nf0Omn15faS4BGj7PUJuui58Hj/zhJ/fRPn0ZMy8fHY9fp+de1fT92b51o+tXQS5L7XdPW49emyLr7Ye4rcF8z/YSh+fo8tH65m3Up2/u9DzMm3k8L2uLr88cXL9OvDKbnOoGfPGimy+h5vvz64o8gRonXfMUp8mtQl5Oxz0ccwEbsDXlDX379b6oQJ+CcJQAA -->
