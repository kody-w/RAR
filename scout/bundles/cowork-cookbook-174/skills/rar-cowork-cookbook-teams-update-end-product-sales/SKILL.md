---
name: "rar-cowork-cookbook-teams-update-end-product-sales"
description: "Drafts a Teams channel post on end product sales status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_end_product_sales", "rar_sha256": "d1269ab87c458bf068fb22887615f9058c71a5fc8d2e7fabd9c5bba01c7f11a4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_end_product_sales_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-end-product-sales:d28562c2c8bda0d5dbe8e669fed718537d94009a3615db9b6a545a4215e1f18a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_end_product_sales`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_end_product_sales_agent.py` is
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

End product sales Teams Channel Update — Drafts a Teams channel post on end product sales status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-end-product-sales
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_end_product_sales_agent.py` and embedded as the fenced Python below (sha256 d1269ab87c458bf0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_end_product_sales_agent.py` first:

```bash
python3 teams_update_end_product_sales_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_end_product_sales_agent.py   # or on stdin
python3 teams_update_end_product_sales_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
End product sales Teams Channel Update — Drafts a Teams channel post on end product sales status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-end-product-sales
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_end_product_sales',
    "version": '2.0.0',
    "display_name": 'End product sales Teams Channel Update',
    "description": 'Drafts a Teams channel post on end product sales status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-end-product-sales',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-end-product-sales',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5feb0d5918816ca5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/end-product-sales'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-end-product-sales', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateEndProductSales(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEndProductSales'
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
    print(TeamsUpdateEndProductSales().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71aaZOi2Jr+K0zOh+oes5JVlrxxIwYREQFBVFC7OrLYQfZNgZ7+73NQM6tquvvOvRETkxVVqXDOu7/P+xyo356stgnz6un1aetZGSRYSRKFXgVZmQtx+TWvYvArj23wF3LyrKkiu23yqn56fnK92qmioonyDGyfV5bf1JAF7TwrrSEntLLMS6AirxsozyAPyCuq3G2dBqqtxKuhurGatoauURMCbVCUNV5lOU108SDWtYrbB86qXMjPK6hsIyeGgHYr8F6Abq+z0gJIeXr95dfnpwh8fnr97clJrBpcerqZsC9cq/H4zNXuarejVrA1sbIArCl64HcGvhdeBTSk4JLr+dDj20+1l/jP0H/8R3y1qqD++fVLBj1+vjyNf/Q2g5rQg5rcqhvPhRyrsOwoiZr+BWKTq9XXUOU1bZWNIamB4Vnwct/5TVJeQH8f7/10V/ISeM1PX55yYII1BvXL088QcP3LU9WOn19GKcVPP78k+dWrfvr5m5y6tc8eiCsQBqx+eXt8f4gFC78tjfyb1r8Dqff02d6Xp++cG3/udo9+gp1PL+c8yn66CwYJvHiZlTneTz//lVgn9Jw4iermn5L7y11w6Fku8Olh+M/PtyD/Ck0eDn3I/Gu1BUjrv+IJWP6u7hl6BOqvZN/i/z9EJ1EGavg94n8q7s82TP4O/fKXvv2jDc+Q/+Vp7iWgKyrLTrxX6Le3rcZzv3xyv1389OvvQPT/Kmabt5Vzk/CWWlnke3Xz9vbLp/p2+dOvv3xqC1BroIfe2ir5M5l/Ftebnh8i+Fj10497gf59Fmf5NYM+Kh36LS/+rfr9BTKsJHK/Xa9foe/7ZfyZQKMT70rvIfiuZ2pg63dx/Pnpd4AOGfAGAMB4G3T5v/87pEROlde530BbJ28bCCS4iVJvNH4XRjW0ezT1160kyvJL6n6FwNWx3QFEWG3SQEJlRckIaGPGRw9yH/r6n84NMD87D8CEmxGH3tobEL0BBHx7IODbDQG/vkC7ECjNqyiIMiuBdFbTIABwWTOquxVG3aafL6NGYE10RxydE0e0qdvE+xv09R+reLtJeyn60YEvGciIBdLkQo2XFnllVVHSQ9aIUHbfeJ8BqAIUqfIksS2AtuM/bfEyRsUMvewRKwdgtdd5Ttt4UJI7wGw/ApqeQbrrPAGY3YwRrOMoSSA3qkB48qq/jRMQ5ddR2NevX22rDr9kdwjGofsYqWGw4MNg6PPnovL8JArC5kvmOWEOffrt90/Qf0H/aNdN+KhDA4PgFi1Qxgm02qprCPRkm4JlNTQWBACcW85++/2ehtG6DMw90EmRH3m3zUDatwIYPbjn5j0xwOfRRK96aPoxbtA1BHGBogZEC3R3/fwlG0XkYGl1jWrvPYj3zffQv2f6rmfMSf2IIciTX+Xpbe2t9sZkOnnlvkCiD31ECrgL8nobw+E4eF2vADXhZU4PdlrNtxRm+TiGm6j2+2eorYGro+SvNhA9BicFsGQ1XyGF08CEyxPwzxigm3qwO8+iMfGPUr1fBkKqT6DGZu8iXqC1B6IJFVZlFWFl1d5tnW/dKwJMtvf9QLgFZd4VGue4N+bo1su3yuP/wBvu/IJ78Iv7lIe+tBiCEtD/IwkZjWMFQecFdsfPIX6904/3Shpp0ujYnVkBRnDbfGuLbyzhHVDeofZLlkQg+lX/t/tK/1Y89zV3+GorUBk6q9/kj21c3eRGDSiBMadVNZat9SV7x/RnEAeQgHqEJ9Cp8dj3+YfC8e67pSFox/H7t/kO3atrrHpQt1DR2knkQL7nubcSb8JqbKBH1EE9eGMzgYp3wh+8AhFvQK6B/DH8EUgNwP1b6NagEQAnulf1x/JoZE33DAFrQad4L5A5Fi4ovhqyPUB9xjUgCp9uoqDUAzEGJn5EuA6t4m7MSF0fBlpjLvJ0LJTvMvC4CYpwHB5A30eHAakWKCsQyytIAmig7p7ZDzsfuQLGpmO13zb9mO6Hr9D3w+dvY5cBG79BPGDb49z+LjgAmitQuSNUgIka16CPU+9RQKASbiP65T5l72P8w5bXP/D1n/41Sn+bm/sfM/cKhU1T1K8wfJ9t76PtxclTGNRIVHj1fcx9vs+gz6DHPj967POtx36Qeg/SK/SvWfaDiEdJv0LoC/KCjLfkyPHGmn38gEBwn2fHz8R490ume98y/CiDEb0Aotr9xxB5XwImSVB5wbj4PlTqcRZdwfi7YdltKHxUwaNHRpQJxglY59/17ujTmNN7yj4wF9zKRjR3R852P8sko/m19/SatUny/JRZqfe/nWFGTAVFCiIxHntAuAH/aSLv9u2DC41ffjyj3VoJYICbv44dBeYX4K3P0AcFfYbeDwW3M1bWglPRLyP9HVWCpeDXx9qPA6DtPYEjWNMXo9X3k87Iuh5s+I9GjI0ELHa8cULnH505avyDEPAhCLzqj0LU2wcrecADgPFx6oFh+2jqGtjpAob0DIG8gWYD/QNgsQUb/qgG6Kk8gO0AX0d3v8Xvm1v53Zffb2Fo7sfF357eYWL8fB/695oBG/5JWjYG9H2cvo1irXHzjTzd4nsjm2/At2gcm9/dCkYO8HYvwKdXgDDe89MYRTCbkmi4nYuf7rYAJ77RVCABYMXneqQBMOgfIAkM52J0IAY4952C8XLk3taPH17/nNv+ZdO/uhg9JTEHc2jbtRB36toe7ZEk43suhdJTnHIZAkEYCydRcI+xSWtKTC0CQ6ce6qO0BUwYc5haDxNgdIw+MP4jxP8i23667wbzAZuS42EfxUjGsmnKIaa07SMk7dsYRtMUMMhnkCntUKg19R3axTzKt2yXcaa2bSGoQ/koahGjvAfju5v09s6u3/Nx7/w3gJRpNBqMWZYzSiVchrJIx8MRG3c8FENdCveQKYP7NO0RYP/H1kdOxpTdvR5rFZA9QLUuo57fHjke648kwMolUYvs/YeDGcOyTdjWQ3lSJZOuw8kNvi/2SFXvNc/oS7Um2s1sLTTnYnHcV/TKjrdNaRHnlYPklKqsWR8x4OMBl7WBm/o6l6hYrbiIwjUnj6opedAUpF5sdizZo2s94awmRopjuo0rPIqmtbdCZH/tnDyJEgvT4Ct4AosNYdZFcjoekIWYZpIIyLySLrB2HUtoZhjNkFsRGssAtUtDTBN7ahLR1pgdaCIx92VSHvc21roHMS3RpZRcm2U+1bKBprRshcFqlpeDAX771/MipfbbaCNol5nUV42VomvTbNBTNT8sYtFUXWSn0cZRIOS0MzaNrhfteps0l+U54wqFMTcBO4/Q0pA6P1uptnpQEyepGcOQFtP9cdGbQlOJyN5OvTKp10d+XSVGsbZ36m4pLfCTUZxJzdBrEm2ECyng1tSoMoXvDSnRo1zW1kioumimJry8MqQjkpUVzYcn85KtEp+TlcPajPxqeUAD0qocPqX7ljjJA4+oMYX0CMf4kQn0hUi35jCDvl7ig9RsQ0+mGqvjTc81Oy4f1shmzji+shWue3vVqmatWc22d1aSRR8bPsZcppa4KWmUnpEc5Y6ed+immO+PnKNvshXCkpesPFSZts6k6RSZizvnejlocpW1TNicG5w1B4x2zkmAdWzUDgy1VrpsVp86YWbx6vHasIRITfpjimB97ciaAJdKuWD5icRplMUNilkcDUM726lEn2iiTVgRnzjEpl5PhuVC3ATExd30Q6Idj5oM24xrOJXUlrWmnWRVWEcufVilx2GD7PJNk5x0M0arXRYWdZSWziSVTHeXkekwoAO9rjJyuRyIoT7MaX5JsNzFJ3ld97QCVhS5YNTaLzJ4RrSh4x4oNGvcmJYwsaHFtNgSpYo1olglVmIWi24mUB1hLxaJoJz0TmrCCXq5eNPNyogL78rv2jSRpGReZVsvyP0Bl7j+yKUXZ7mVyGSxLTfhptufdJTTs4UYZ0R24rfBBjO3ahlUsbhN4v2+O2WzHJtHxkWb7k+h6/cGTZeIc2wG3dMd3uGN+OAuOok4Tia4Fym70BlWZ3oYjKY+x+u0Ovpov7YPTnVCZW3iM0dXr1eH5VknbLq5riomMboTJROOyDBVu8xt86SBopoRIsigbSyiamvaq0u4HuBZt0d3SGky00l4MRGppsu425dxeYDFzsDKcO91FekRhyN99WKzC73VYJN052lisjcJwjxI1yXTF7qNlD1eTA+UvcWKODYNo7wycbbeTfHzll9tJCYqDX0fOjEhyWi6X8DinN6cJsGUXhwWwmQwF6XbchtRU8e4HWwuljuZobM82ZzhsoFFn9M5wdA3VeUu29NuuuMzvpE5hWnZBbxKC3JiHGw7CtV4r55mTmAf9qmnnNChkKWDvd1HkwqRHOnUpbxLZmeinK9P8w7eM6cSKZHpBKDykLAUudO8Amu2R52dzPpzpUQa502KxEfX54wOU+ZYYbjB8HOMYmgx9g2S15QWNiLRY4R6wQuglsnJsDXW9Zyk9bkM70OZ1PMqY6vWxJ29tJbK8+KYVdpG1vXZadV7UcnA/DzilSHuJMeX+869bOIjvNv4qXxGUM+2XJFZbXbXjltmUYxzLAPniIfIOnKKlCqBmU0ciDripnyGIZTjtu7SPuVXdsFulVbqC7MI7JNSb/cbArm2B4Fnk24VpqR3deKgwNtAQgmUqpJ2ttWxoe+vJUrnh6rJinPcZI5pR4IXk5OJvSDdtIqGdcSdZnElWi3GwMvk2B58we1rJjs7HBdv1eS06eDJaSGQVFaq+BZRFpygJVExiecUSdLK5YIPhL4V/cl+3qWEhKGarLqduZyp+Zbig9VcSL3euZZSzpCtq68yS6gH362sra1vipaN+rlxkK8cXx+koqTEUl+s8HR9EDUeiW0DdYmSVEmTJK85hfpRvpas/jjJV1U506RBQ2cHXBdJTXVOs3KaEShnutmESfEj525RXl/nOq1xtUSIZIrNTHeF4oCXcmjcmCcmPK9oScNnV3rFMnGRgRNPpyJUwFPKySHrzZEJglOLqgdzvUovx3N3bgHdyLbCxe7d6Hpi7NWmXpL8uhCiGQoamY/0CYxe190Sr9dsTDeXejNcTWK+wgJvGZ/DYXMUKk7icdqvZWIZcDlbz48Yr563vTnDWVbpdmsXS0tLVANnv2TsEl/JiSlxXqMggLMLMLuv04WC1kLVYiE6sUuQQqXEt9Wm3Okxq1+OgsUdgpMzE+j9Kq5rctd4QPnczzfiQQ0451KeKzD7rtZxruwW16zcz+ddMHX8hQCbq1I5r2aiMcNDFV/nKxCu+ZG8xjllHJMw6KWZRA/5FuPr8FIQaBEtsJ65YHijO/Ni6llbBev5agZLZL2LvbmCmwHCNsqUmhglWS6wOS6Kl22imMf0Qrr8StPTwiXiUrrw2/2pLs7iRZsLVWkaSZSkM3UIl26YJXa8kNDFQojZoxWRSlTabLzMLUPDgtUEXy+3Wi+uos0qyJZUI1OWASMxLuZTQc6CMuhzPsH93dSc5S5noa6xiNerchdSFNzRsa1NFsN6H3foUXMDd2kOBCueC1x3G8k+tErTZFP05MoNI9jCIe+dnWQChjwlpGHuifGRbY0palwFTjoveFbWZnOF2tXJQaLNGRytNzEm2umCIKOIcbNi2C3Pwn4Fr4/7ErMB2+oSU/WkqZ5t+cbKDX5ZksluBui4NeMyI2IIssD3VdKXZ89u+tI5rhk9CWZsL9ALXLauSKwX+lVNRYu+HqK0CrVUXW7jrSwCXD6p6V5Y0dFsd1zEBV/rBa+Wk9OaDKcd0oKhodZpjbN2P53K20uX+NGq4y8rwUS21Mblj/MpUbBbb6+sDmvWVQVKd8KEz3V550a2zG5FUK9zvVZCae+aai9gqqdqp6xagKkysTKTJwyPxcP11q3LlFkWERLIFraS22utm4nrK5FRzodVtzhx7cWthks8zciNJIAm15zZJHHokzElmUA5XbTznLBn2NJdmZY4c0y1AzN3t42K7ZlsGwKhDnseU2g+8aReppLIlVI/s5fd7lJHEj+NRD1ERWUXbAWX3ah8vVstDXnYKEwMiGLnMtueaXAVc9gicAiGIofqup6VOKAfW1bpK0mBQ9ID1GrXqso2yY1arNtiXW4biWu3jRWs6aAt3RN3PgVihCxdQKOsqXL1s10eB8h8im5WBR/IqFw6dN3YMGuC8j3v11uBiHY+Nz04jbzgFNwthdn64Ctt7HQhvamt/dZYXci8Z/kCZvYJUWzMA5htnp3iw0k0EHOdZEVwTdrqrHNhIc2wxFXOjm+yQswVyTCsNrlHdNkUkfzdnmYtQsuSQ0jg/a7BTwiWS46g0NrMOiX7XL6EXOHi+WSKkiEBEhhxs9DAuGKSzRYaiwfgeIDsTDtvGsDj16AMM2brTAG2qPK6EWm5xoy+aKOOJedBjsyPyN4bcs5cuG61yBdRmPZOeuiSrXth4JmIHla4zmYsCyZzcuqkJbE8YtfVlpPig7LewXabyRHfX7gLOIzMwdgsdwa25c4pAXTlU7ueRK6PygGV2Qrte1iJXY1ZJ6lt4xcTYaMDbBdQms9seNHZBSZvd6owh0O/H1x/RjVD1V1QVVuSsKVq+oSqBmpPXeyWUszK2uHeYYYbPnxop72L8x0uJwM1HI7YorapVi3LFSe4rY/lCZZN4+QQiEdXQAZM8mbRic8SOWXaFhZp97wGQdhNU6LOjhGPOkTlcpuFC8t0g4WanghX1TwdDinDmNNV41EkyybMpMXUycrB4A6f+HvmqDC7aoJr3ZUAA5E9+7hhOtXhSGKLkAbnPXuo2EoUJoBytjMtlC8nLIANYrpcTisKps8zmq02V6ry4WEOL3c95l/c4wSrMOKqMIl3CFXxspeMKxoii2Vo7ThsNgS1d7iK+Enjs4FlVgo/z9FBqsqtzVp7T/U2516kWHp1cYTrYSHCUa+eMw8jrYOtusyg7Iv64J1ad6cT7ULN0bhMHem865GLxxNEJV+z1Iij48ln8WbN2HptHoJOYlrhkgba7nL1587JndVEVjItrwU0ZVGXeD7pW51J6tOW2w/kjNdo0WspFr2e6noRaefNId6hUzHJfcpo1aFxp5VP4nC2KENZCtpJfjZZq+5nU8UPHWeO4eDg0aR5U6IkBUhMJCpX2Y4GoWMoG6OxuVfmWOMQWrr22pzoE5TBudQnThHLXoY9dSKWHCyc2sVV2DQdJ+LH7eWwQ+SZdWawDsadXj4uOTa8ZEWLzh0+p3pfO/DiUJCzzbrWw3PUiw6Xo/1+fRGuxcAihO8eBpDBPebBzmyam8olWHuAVk6q1Rk257MpIGu5FU6QGSOuj4oNt4MiO0te74JT0AT6lUOY/nRUV7NQ2VyNpAIFxKO4QIj6DqdPGacjPM1fujUSYLDmFoD1YvTOVr00SSVFWeTNZC9blz1ssbtpHFyWpy5cwnLtBhrKCO3OnOJMjlNXcV8OzRINlJlPY1rjCVydbxR42QTKOiLnyGSaqAzjDItWc22H5zniaM8vpd7q2AZjSjw0pwqC4gHlVvp2Or/4dSnH3kEllp4cEiJNHtmZ5yPwZk3OXLQ4s1Hgsx2snHPYKmJnSdCTmDtTRVbMqIGlo+UxwznRA6d9l+yD/FK5DUMdmMsaN33URSiKSgf7euxEl7pUDCotE1bGZGK26Xxrgk4qwrjszdDB3Zm7pBjX2bnWGU+vmG9Q9IKZXEGi6Ett2i3wSkAk0dTipbvf66zqCWVLqsMSxo/lfG8bvmKUxDSiUO4STfiMPqasxW73y3IykbJsQqA62xWDgS9z87KOJ51glwgeTQ5hagGAtk+VuQqj5dVHFHk3Z7vgqsbB5tRagrJUtM1QX1F/Z8+SKwbblg/qzYmxoxcxe0AntyJV+86UTM6YdJl3V//U7PBwA19V8ertZx6xWUYkMvdAIDa6oSWrdnbez9Wlull1GbFfN+1uWW4QwOh6ZOFSNU/0k1nhkpfTwgcsbgvG62TlzVtS3l3WoX2QCzWh6oTKFrB+iuEzantH6Xw8LJUKl0o5xfkoaXawFPO5VmbDcmdptj9sHLxorqrG7qrouF6eOERS1mtstheEzL7OZwdyGw+lJqoEBhvLBTIwuOK459jJLgI/dY2O1GB2dZZdii+lDcs+PT/d3sg+vaLIFKefn8bH/I+H9f/8495giIq3hxycQqnnp/+7J5L3p4Pvr/Buj+49y329aX/9Z0389fmpciJgzv3xcJ20weMR5P943vr5Hz8BHvf291fJ41vGrnl/vwGIzO3xdJS5bd1U/VudJ+3t4TQIcFuP/42kfnu8IHi6OZQW49uG7x24v3yIguytycfnrlE1Xrq9vU09N7qvGL8Gj0f5YH0PchU59RtOTt+8qhgdfbxKGp/Nju+Snn7/bxOY1U8PJwAA -->
