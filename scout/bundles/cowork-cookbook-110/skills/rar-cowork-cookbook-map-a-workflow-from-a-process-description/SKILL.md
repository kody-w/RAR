---
name: "rar-cowork-cookbook-map-a-workflow-from-a-process-description"
description: "Make a workflow shareable, reviewable, and improvable - without spending hours building the diagram by hand."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_a_workflow_from_a_process_description", "rar_sha256": "f2bc882e02104c377f714e9db4d24699caf74d79bf15064b7ba5a81062103adb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "miro"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/map_a_workflow_from_a_process_description`. The original RAPP
agent is preserved byte-for-byte in `map_a_workflow_from_a_process_description_agent.py` and in the RCI capsule.

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

Map a workflow from a process description — Make a workflow shareable, reviewable, and improvable - without spending hours building the diagram by hand.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/map-a-workflow-from-a-process-description
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `map_a_workflow_from_a_process_description_agent.py` and embedded as the fenced Python below (sha256 f2bc882e02104c37…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `map_a_workflow_from_a_process_description_agent.py` first:

```bash
python3 map_a_workflow_from_a_process_description_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 map_a_workflow_from_a_process_description_agent.py   # or on stdin
python3 map_a_workflow_from_a_process_description_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Map a workflow from a process description — Make a workflow shareable, reviewable, and improvable - without spending hours building the diagram by hand.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/map-a-workflow-from-a-process-description
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/map_a_workflow_from_a_process_description',
    "version": '2.0.0',
    "display_name": 'Map a workflow from a process description',
    "description": 'Make a workflow shareable, reviewable, and improvable - without spending hours building the diagram by hand.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'beginner', 'integration', 'miro'],
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
        "upstream_slug": 'map-a-workflow-from-a-process-description',
        "upstream_url": 'https://coworkcookbook.com/recipes/map-a-workflow-from-a-process-description',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2a1cc4e37c979b34',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'miro', 'process_roots': ['work-management'], 'process_tags': ['work-management/create-and-repurpose-content/diagram-processes-and-workflows'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/map-a-workflow-from-a-process-description', 'uses_skills': {'custom': [], 'ootb': ['Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class MapAWorkflowFromAProcessDescription(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MapAWorkflowFromAProcessDescription'
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
    print(MapAWorkflowFromAProcessDescription().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+7eiyJLuv8Ls+aGqx6otL3nUWb3WRUVEEARR0a5e1TySl7yfQk//75Ooe1f19Dlzz5l117UeimRGRH4R8UVk4u8vVlMHWfny5WUPrBQRrDgOA1AiVuoii6zLyit8y642/Ic4WVqXod3UWVm9fHpxQeWUYV6HWQqnb60rQCxknOHFWYdUgVUCy47BJ6QEbQi6x+dRbpjkZdaO18hnpAuh/qZGqhykbpj6CLwqK8Ruwvh+WQcAcUPLL60EsXskgAJeoXJws5I8BtXLl19+/fQCJcYvX35/cWKrqu7G5NzpacmqzBJuV2YOqKrlDyZ/eomt1IeD8x5aMF7noPSyMoFfucBDnlcfKxB7n5D/+I9rZ5V+9dOXrynyfH19Gf/oTXo3ss6sqgYu4li5ZYdxWPevCBd3Vl9BAOqmTCsITwUBTP3Xx8zvkrIc+Xm89/Gh5NUH9cevLxk0wRpt/fryE5KVUF/ZjJ9fRyn5x59e4epA+fGn73Kqxo6AU4/CoNWv357XT7Fw4PehoXfX+jOU+nCkDb6+/LC48fWwe1wnnPnyGmVh+vEheHQgSK3UAR9/+kdinQA41zis6n9K7i8PwQGwXLimp+E/fbqD/CsyeS7oXeY/VptDt/4rK4HD39R9Qp5A/SPZd/z/m+g4TEH1jvjfFff3Jkx+Rn75h2v7nyZ8QryvL0sQhy2MDphDX5Dfv+13/OKXD+73Lz/8+gcU/X8Vs4e55twlfEusNPRAVX/79suH6v71h19/+dDkMNaAlXxryvjvyfx7uN71/AnB56iPf54L9R/Sa5p1KfIe6cjvWf5v5R+vyNGKQ/f799UX5Md8GV8TZFzEm9IHBD/kTAVt/QHHn17+gDSRwtU0zv02zPJ//3dkGzplVmVejeydkYWgg+swAaPxRhBWCPw75jZkMFBW4chYj3Ew/kcPjxZnHvLb/3HuVPnZeVLlNLHyb9a3NzL85kEOgtf5g4W+/cCcv70iBlSQlaEfplaM6Nxu9zW1fJDWo/K8BBUoW0grdl+Dz5CQPo8fkDBFfvundXy7i3vN+98e9PvgK30hjlxVNTF4Hdd7CkD6XJ0DKwG4AaeBmuLMgWZ5IeTakcmrLG4h143YVNcwjiE3lxCIrOzvsiF+X0Zhv/32m21Vwdf0Qa4E8jCmmsIB7+Ygnz/D9Xlx6Af11xQ4QYZ8+P2PD8h/Iv/TrLvwUccOcv3TO9DCzV5VEJhtTQKHQcdBV0MquXvn9z+eKEMxKaxt0JehF4LHZBitV+C+Qb5fc5/xGYXYAEINxkqVlfVYhsL6FRE95N1eqHS8NXJ6kFU14oKxfoHU6aFUCy7nHck0g8UNhmTl9Z+QpgJ3rb/ZpXU3MYFpb9W/IdvFDlaQLIb/jWbeB8HJWRpC+N8D4vE9FFJ+qJD5m4hXRBnjE8mt0sqD0nrq8KyHX2DleJsOhVtICrqv6VgxwQjVPVke8MBBEBnn6dLPo89hzU8gM7jVm+77GGusc8a93pVf0+qZCLDeQ1QcWBigUr8J3bE8/O0ZUhUs67F7xw9aOkp6esF9euUeg7Bu/9hDjCENr58hjfwQ0sjXBkcxEvn/2XWMBnKCoPMCZ/BLhFcM/fwAbmyMRoAfvRSs/AiMnkeSfO8G3rjkjVK/pnEIo6Ds//YYeYf7OeZBU00J0dE5/S4f+hoCN8q9h+IYWmU5BrH1NX3jbrhQ5E5UECCYtzCux3B6UzjefbM0gMn56QHts47fXVe6I1Qw3JC8sWMYCh4Arm05V2hVOabTE3YYl2BMrS4IneBPq0Kg9HIErEKgESFMEMjvd+iUDC4TQnt36vvwcOyOoBVu40BrYecJXpETzIgxKqA/wOhUOAai8OEuCkkAxBia+I4wdHn+MGZsVp8GWqMvsgQG6o8eeN78HsN3W0bzoVTLtWqIZTeSqwtuD8++2/n0FTQ2GbPuPunP7n6uFfmxyPzta3q38Z3PYTLH9xD8Dg4Ckyip7iE6clEFQzEBzwCCkXAvxa+Pavoo1++2fPlLh/7xX2vi7/Xx8GfPfUGCus6rL9Ppo6a9lbRXyARTGCNhDqqxvH22Pr9l3ecRRnj9zNPPP+TpnxQ88PqC/GtG/knEM7q/INgr+oqOt+TQAWP4Pl8Qk8Xn+fkzOd79murgu7OfETESatyPWf1WXd6GwBLjl8AfBz+qTTUWqQ7WxTu9Qnd8Td8D4pkukL1TfyyNVfZDGt/5Brr34b33KgBvpTXU7Y5tmg/GfUw8ml+Bly9pE8efXlIrAf/0/mXkexi4EJJx7wPRh71PHYL71XsfNF78ead2Ty/IC272ZcyyT8jYs35C3tvPT8jbhuC+0UobuCP6ZWx9R5VwKHx7H/u+DbTBC9yH1X0+mv/Y5Ywd17MT/qsRY3K98fpYlZ7ZOmr8ixD4wfdB+Vch6v2DFT8po6qtsSKH9VuiV9BOtxkLAHQgTECYU5AqGzjhr2qgnhIUDSx97rjc7/h9X1b2WMsfdxjqx1bx95c36nj64NkWwuEwRz9XY/GbwmCFCuH1I6zgvf99w/gUBFkP9ilQkofbDsPgAMUxlHQImvZojASsa5MuTlIs61geTbo0a3vYDKVIm7atmcVgKAXHE5ZrQ3mPKP02lvpwNA63LIdxoBiXpS3KAQRqEw7AcMylCYDOWMJjGEBCnN6nXiFlPlf8WOEI53vvOiLzXPjvLzZFwpFrshK5x2sxZY/WlKTtW7CemOjkdvFozdxvdDcX8VDpSidKPFNTb+fZ4M6r1eq88a77OnN0Y+MwiYE5PAfE6+S8mVyJiq6uupOoqSWuzlF4u21wN3Wnw3DczHmxBz22Eas9XiT48WRvT70U2aQZX1ZZ1umFsdnkTm2t6JRkgevd1sosm5bXS4iWG6BsjcM+tkvTwiumN0gT+Ntr7emuUbkm1iRBcT4Ux3zIvYXZl5Ho26m3NkGB8UVzKq5BpdOMZi23sk7thhylWjmfgFa+TeT+BtqSJne3U6ttDkdQ0N2p8te7fe3Q1b4rHGUubGTpUDl0JtikjlJnVNkbTrQU3SMtWztb4vcdfltzVzEp9EbKT1Ix3ZaXkMVg0CTFpNZ2UjtvpALdXiVViWRzjx8LaRE3x5MpbuNEJ4Q5YdrGGrUK0+kJBSSbGhR1n+wdqb4WkhQehshbMKGhuqF03Fv73hAYn1+Gia32bL85FzEuzbCqpg2dnA/6+dxzvpwJLVs5s6jStTV7Xi3xM1ptjX2zYtht4l9uJdzmaZ4MTrC9sdarmTbjS03bobftTbTnbpNkrNUxayXfnNfpydA3bMjgVXxhC3Yn7asVCTYzSzwERbVR81I9ZguqTQszj3ZuKs1m3VI0nK41TblNGzeog5rQTkOCOlF8xZt+W1bT/RABtarEJD/a2rA+U/YgkCqJ974pTznGj+Z6tcm0chpEEhM45nxfUdejTmwN0pj1zCESTYMQ+KDFz+Rswa9XdC4IVj4sYnKa7Lwjod7Kpt0PAhiCpZPY8eS82lQX8SqZfdXhVT5IhTNppeNVI2BSGmmb46rbGsbBXPeXMCVVeSbHpLAkxTW+jIUZmoWxQcynFpmsaXbq6YMsUs0RumXV7S1bnkSYfFgk+TUNgV4creuRP3iVpKsntdPQOOWz5rQ+BNlKDjsjb7FNwrVTtMqP5aK8Fal2SWdEMvczKW63tl5oFr26dJdMCpWsilJL32+2BE+I4WFxpTr9vF05882hOp+c/aWzFJ+M3WFyFM6mycSmqWHrRmzn8qZfV7FYTP1mqkjYbifh61XPhnqSzjarqacckkEyGib0WIU+1rip7WyZnhJTDBdrPyMxdUrPSWYK+ypDPnsGJmxOkT85Ytew6G/7LL8Rc/9gYhFULEBmUpNSvRpF3hQUt3W1gRKWg9eJDXuQZkTqxknE8htyIPZRgUuMozppuD0eDwAT/dvMlVh2F1m6taqPVnW5iAOKGyR5TQtFh99Th/CoT/ZkVp3qiaZceJyaG+huF0pd0p321NYQps1cnGJiK/S2to8mMyNfxULBex7a3pZt2PZZuZc973bshZ0qM5pxJi9B22llWcFmu9hjkrPdoCG72drV5kxVw3DBMK1A0ayl2Hm8WDhmIDuX85RwN9ECtBRpKSA9yWv8esAbuMfpLmtWnlXzCd/raymvCpGZo8eKnm7w3ulPtgp3C6yrZ2w/AcRyRwfOesDTY38AbJHxPH48+CKOxeGE1VlrE2B0caZnG9Q0AnstJ/hKjS5SdjutqNt0gfGafXNMMWzbm0MGuy0pHSU1a7ydmYFtmN7SWUOysrepFNRjOKM67jnDh3gs892VELJNyzo3AYtsOtvvVxtcPs2pY64Shl3viYSRuDkp6fHMqo+HXKOLK32aVNJpbi5yfnubJeHVOJQb2gTrleNMZGmY5+fWApqLWY0tYg0bDXQ4qGEaCE1FTYB5uU2AfNzYPA8WxTYoKJpgwBEoRm9ceDPptqpOSXK8mc0m7XztTxczeojxFrt10YzfXSf6wLpXs7+4njePp2x5lVeyk1scZD7iZjho6J8qQY0VS5tl6Xa5K3lVMeX8QEHuPzZtzOpbMgZUtq39qz4wmpzFYl4eZspSnEnUjcp5KcnCijXNOF03MXbUMeGyXZ+XpW5NJJnID9jCUnkH3c94qs6zsJW8YX9cL5QkKuxhNRhMmGRLZTebL4+M7+Nev3PmfLmuJZyqifzkbDAitS4qHu9OVpxdQu/A5dzSFVf51U5PpyvJoqRvTqThEtoLS8upPDh61OwQnRfEuXSE9kg7JNViuiOx0rDptINa3ZJrHNOHXUwy54uv3DBxwQiEUvmFHx/mCpeYYShhyo6fRheyOXlCbNby+sZh5rIi/UvEy3PeqOIUUwZ8vRvcQ7VJ+vZQslytcJorXPw643dcL25qchPJl9k2tZiDupZYTtjn6LynYU3HNPPcXPQb3zP7fIl3jqHs8BnAKUqORErrucohl8HN648Z7mDtFoh8k/nnhA+76kKowY4xemGSEJHBy3FCb+rICrG15KD49WaLp3RKxAOFV8ersVjtQIRqwRYGh8lFvuwQNZsyc/PgmqFF5KhxZQXqiod9nDE3tD9Jh1ttdMWh2jYFl81Soz7rxPkyS6aT/JRlGXrlrgdTD4+yxfvs3NzgOLtTsYzSJnrAa3ORH6brBYUHnlUlrC6It4pxz2s+YBpaPDFdgyVGUpyr7azQ+sPOm3oEU+sNqnozY6m4vosbC1fanv1Eabt8QIMqIAMK8wjdyO2ycCvdiSAxx/a66i5avk3Ovk5uSJM4aE2xm8/nS86OtiJTz4tY5qZ4gIbyXGk00PAZaM2eyTZJKAsVJ22Yi7c0ZPwwnPvaLheUHpdzoTzk+yPlSFEJiNUhzM1Ww1ULtZujdolsHDMMszHRqVaf+C5QWYtISk60JB69rY1i7+sYY7jntog3h5PmD2SZ5LBQLbZrJTztr4BMrhyVz67TYmnK+1l0Vvp+P1RBK6ZoLXk4r3QT7UrGZyvIe66eXxXQtwtOPmDxtp9fp3jGp9KKa1Z7vuOSRbfWD7yiCxqW5PPbhb4M51k9NFOwFzMqnIrohI2iJbNoA0KrchW/6KqB8SdLJWk0Rg/VUTiuT2BrNoe+ull6aQ8Wk1LmsNKL/cQMdvR1h6ZC2icGUCNriTtWtcjN7qTEoaysYluFBcfro32S7yOqqQV2puHrfsvwsSr1Mh23DTcoXbwUc+Kob/0qF0StvwqbTlxufXG9OMnxsvIIQlqe96v1FobMQjyzIuZfTgvTUCcnjtNiKXbYiX3ihL7oT1O/2JVps8QVUY813eEuil7np1ZaWPvaahTabyT3wqO07ItbUcGOB1Om6o2vtIdtGvP+9RZteZ3CTZWl/aWySW6l4C+d48wLuBy4grBozvV6exZr1aLXObEkArXPD/3+UivXOU+QNiT9wiloWrgZ1wlzyXlskc60Jm6W8SlUQmkOMsDA9EL7oXOSjr6ULezPzgMTruS8Ahwqcrs9s0PrKKXrHiiWAObL3aI7NRfMWpE307nQB9uka802Ngdhf9BOdZu4+dUZOoWQL85Jkss6o+fOaTWda/vVdCPo5IALXDQAtWhWwqxE02q7iLK17pdMygm2VJCmvBVXS+VKUh2nhqt6ySqysp5jut9w3MX340vFZctGmNGospVOvhasht5h8TovyFbMurUVbX17FVwytObFYla3QYptVvWE6Jp+umtNRZtql4r08PiyU2kN51PzHBPeUpS5ipZqTxFxzW1BYUXk1Yy0OapOPKO0crN2G3ei3yZMQBIRWqcXtma97VQ7nnpi0rdDT3og964x0co9JahT0KTa2QZ4u/SOXbLSZYNW0LxW24MBrpMymZtzWKMWke+CI9xxzE50GVM7WhsMXPP1Tjkc0At/cmBqLvYrbypPatgMBNbgrysH1qWze/TcKSMbtg/q23HaKTeivirLKMaWQOJgStUC76hNxIZnAgSxJ8XHUxtkhkKrkwntCzfOS0WLzk5UZBPseYm6qrWcUD0zJfuJdiQt95YSrDYd6o1tD0228xSs2h4syyRFvbCxJbFdAHcukqdz1wnMRU4TZ66aXrfh0MN+uVjSpdNZkj/r8CyO15nMzBe3XW9jc2de7HdMY6A0VoMkJgafhWQp20c5dtcaCuj4VNUXMV8LJebkMgxtxTJE+bLSN4ngdcell6hnT8YywW/pFvOvO7IWNhS93HVJ2Sxk0GkTm27bxWTfyMossfa3IyfFqSAWu5PLgPO20Ra6PWR2ItLqbVsvSaqe9245VYTpacqe2YN4OVyJfgG65SrUd5eI2UE/4RW9Z5kbX59az0LBVrdCznZOF9wrLWDGNws6eYYR/kTEKCqOJM8kKuky9RMR7sm3cpP6jsycE9L0LwuC5yM3kNjlWqtWhUrY62k+R/1O5eXldKezkkqKJyOZgEbs1mUY3SK1UNdC0Mm+mR9Qhl5ct4YXxNfS5HFWm8mb21qozz3gU7GjeWpCrWaMujQMZtvV80m2ZPYWd2KnqmrjoihGA99tFC4V2frMLzqnl0Ur6FqZ4JmcqHu+cDzD7Mx4cbztmKzO1ToiPNgMrBq+cdKLAsI4lc7yOpvjJn1tthx3PGy6pPJ0OiCWZLt05kSNT/TGZifkEuszMh+cpR85itGeDN8ThKjspue1cla3faMGwG+V460csNParTlVWHS2ZdjJpVGmhkCtcV1lFfRIlPSx0XpMbjky3aCt7mU0kPTtzllJchgSnalNJnP1jGrc7LQjz9R6uM7sDQXSTLnJMboydtQcX2jsDg+WLc+hEg3QK3/TJjhts2pKe/akYGuiTHdtfzb9adgN3YRYhocdxR/EtlsGgKJZAjbgR6q7mJ1t17cWD5tKj4aS9vzppMeYScArE4LZ1O3Gncz282sk91GSbbJO2S0KldoPOyIhT8FhfbS2q4K+nGhy3xbT1bqzEu4031/lYjLZrdfzDtXRWTGdGgE+EAmwgamq8va8LmATki+E3XYSShx70zh2eRp6jrPU5XzBCztH3u60W91djLa+zZxJStsDRlJ0NezONG9xc2tHrWnRvMysoEQpb10cTLcyvKz1HLDnqopzu0pY1RXv7Mje79NWGqx5wglAZUJtucZbmyj0tWqjx1ofjjMdPV9uV4YuyFnDyF47rXnnmDBXcsdy7oY5beqqyUgzwI8NcyLlbTsBpT7Me5sjZ5EzO14c/Fwd3YNH5VyxpHLY4eERSjDoWqFsZxl0PEUmSx3X6kW01N0gngf5bBp1q8k131JRv0wUb5J3TEQRigUCY1Li1VK1zQJE046z431MDb3PcdzPP798ehkPlJ/Hwv/6E9/xiO7/2Unh41Dv7YHR/VAYWO6Xu64v/wvbfv30UjohtOxxPlrFjf88RPxvp6Of/+nnDaOY/vFYdXzSdavfDtZryx9/K/QSpm5T1WX/rcri5jnDbqrxJwvVm7Uv92Um+Xi6ndUBKOH7qHv8jQQ0fnxqOs4Cfjg+uHwZf1dQA/95XPzpJQnLbFzb81nFeKA6Pqx4+eO/AHJywTVtJQAA -->
