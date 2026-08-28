---
name: "rar-cowork-cookbook-bulk-update-record-production-costs"
description: "Applies a bulk field update across record production costs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_production_costs", "rar_sha256": "368d6cfbc13c88dcd00a6d6b021aa830d15ba7fb4a936214b68382336f070bf7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_record_production_costs`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_record_production_costs_agent.py` and in the RCI capsule.

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

Record production costs Bulk Field Update — Applies a bulk field update across record production costs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-record-production-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_record_production_costs_agent.py` and embedded as the fenced Python below (sha256 368d6cfbc13c88dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_record_production_costs_agent.py` first:

```bash
python3 bulk_update_record_production_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_record_production_costs_agent.py   # or on stdin
python3 bulk_update_record_production_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record production costs Bulk Field Update — Applies a bulk field update across record production costs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-record-production-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_record_production_costs',
    "version": '2.0.0',
    "display_name": 'Record production costs Bulk Field Update',
    "description": 'Applies a bulk field update across record production costs records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-record-production-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-record-production-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3ee2088fbec74f65',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/record-production-costs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-record-production-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateRecordProductionCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRecordProductionCosts'
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
    print(BulkUpdateRecordProductionCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjyLLlX2HyfajqR1aBhMRS167ZgAAJIQmJHbraqthBrGIRoJ7+7xNIyqzu17ff3B4bs1EtKSDCw/24+3GPIH99cbo2LuuXLy9K4BTQ2smyJA5qyCl8aFX2ZZ2CH2Xqgn+QVxZtnbhdW9bNy+uLHzRenVRtUhZgOl1VWRI0kAO5XZZCYRJkPtRVvtMGkOPVZdNAdeCVtQ9Vdel33jQNSGzat/sNFNZlDhaGkqLqWihLmvYV6pM2hvx6/FR3BZgZXJOgh9wgLOsAzM7zpP0MVAkGJ6+yoHn58vMvry8J+P7y5dcXL3MacOuFAQppd03k+0rHdwVW0/pgfuYUERhYjQCLAlxXQQ1WyMEtPwih59XHJsjCV+g//zPtnTpqfvrytYCen68v0x8ZqNjGAdSWTtMGPuQ5leMmWdKOnyE6651xMrXt6mJCqQFQFtHnx8wfksoK+uf07ONjkc9R0H78+lICFZxJ4a8vP0FlDdYDcIDvnycp1cefPmdlH9Qff/ohp+ncc+C1kzCg9edvz+unWDDwx9AkvK/6TyD14VI3+PryO+Omz0PvyU4w8+XzuUyKjw/BwJvXoHAKL/j401+J9eLASyd//ltyf34IjgPHBzY9Ff/p9Q7yLxD8NOhd5l8vWwG3/h1LwPC35V6hJ1B/JfuO/38RnSUFSIA3xP+luH81Af4n9PNf2vbfTXiFwq8vbJAlVxAdbhZ8gX79phy51c8f/B83P/zyGxD9fxSjlF3t3SV8y50iCYOm/fbt5w/N/faHX37+0FUg1gIn/9bV2b+S+a9wva/zBwSfoz7+cS5YXyvSouwL6D3SoV/L6n/Uv32GdCdL/B/3my/Q7/Nl+sDQZMTbog8IfpczDdD1dzj+9PIboIgCWPPggIkh/uM/oH0ykVQZtpDilYB+gIPbJA8m5dU4aSDwd8ptwEBB3SQA2Oc4EP+ThyeNyxD6/j+9O2l+8p6kiUxs+O3Bg98eRPftBwF+uxPg98+QCkSXdRIlhZNBMn08fi2cKCjaaVnAek1QXwGhuGMbfAJU9Gn6AmgS+v5vSP92F/S5Gr/fST15cJS8EiZ+aros+DzZaMRB8bTIAxQcDIHXgTWy0gMKhQng1ldge1NmV8BvEx5NmmQZ5CdgVVAPxrtsgNmXSdj3799dp4m/Fg9CxaBHoWgQMOBdHejTJ2BZmCVR3H4tAi8uoQ+//vYB+l/QfzfrLnxa4wi4/ekRoOFWkQ4QyLAuB8OAs4B7AX3cPfLrb098gZgCVDbgvyScKtU0GURoGvhvYCsb+tN8ib/VF1BHyroFLA2BKgMJIfSuL1h0ejTxeAwwhvygCgo/KLwRSHWAOe9IFmULNSAMm3B8hbomuK/63a2du4o5SHWn/Q7tV0dQNcoM/DepeR8EJpdFAuB/D4XHfSCk/tBAzJuIz9BhikmocmqnimvnuUboPPwCqsXbdCDcgYqg/1pMFTKYoLonyAMeMAgg4z1d+mny+b3CAsc2b2vfxzhTbVPvNa7+WjTP4Hfq4F7IgSojFHWJP5WEfzxDqonLLvPv+AFNJ0lPL/hPr9xjUP6L/mCq3xB/bygeZRz62s3R2QL6/9dzTOrS67XMrWmVYyHuoMrWA8apSZrgfvRVoPZDYN4jZX70A29s8kaqX4ssATFRj/94jLyD/xzzIKquBljJtHyXDzwPYJzk3gNzCrS6vgPxtXhj71eAyp2qgMkgi0GUT8H1tuD09E3TGKTqdP2jkr+hBlwPgg+qOjcDgREGge86Xgq0qqfkejoBRGkwJVofJ178B6sgIB0EA5APASUSgDpg+Dt0hxKYCfLqjv778GRyy8NTQFvQhQafIQPkxxQjDXAAaHKmMQCFD3dRUB4AjIGK7wg3sVM9lJka16eCzuSLMp+C4nceeD78EdF3XSb1gVQHhBDAsp9I1g+Gh2ff9Xz6CiibTzl4n/RHdz9thX5fZv7xtbjr+M7rILWzqUL/DhwIpFTe3Ll0YqYGsEsePAMIRMK9GH9+1NNHwX7X5cufuvWPf6+hv1dI7Y+e+wLFbVs1XxDkUdXeitpnkAUIiJGkCpp7gfv0SLpPj7j59CPbPt2z7Q+iH0h9gf6een8Q8YzrL9DsM/oZnR7tEi+YAvf5AWisPjHWp8X0dCKWH25+xsJErNkIKup7lXkbAkpNVAfRNPhRdZqpWPWgPt5pFjjia/EeCs9EASxeRFOJbMrfJfC93ALHPvz2Xg3Ao6IFa/tTixYF0/4lm9RvgpcvRZdlry+Fkwf/1r5l4nwQrgCOab8DYAc9T5sE96v3/me6+ONe7Z5UgA388suUW6/Q1Ku+Qu9t5yv0thG4b66KDuyEfp5a3mlJMBT8eB/7vhF0gxew92rHalL9sbuZOq1nB/xnJaaUAhp7wVTHy/ccnVb8kxDwJYqC+s9CpPsXJ3sSRdM6U1VO2rf0boCePuhxXiHgPJB2IJMAQXZgwp+XAevUwaUD5c+fzP2B3w+zyoctv91haB9bxF9f3gjj6YNnOwiGg8z81EwFEAGBChYE14+QAs/+bxrFpwjAcqBLATIwnPRxL3S9GeaRpO/5KOrgPu6i85njkBjqz5auQ4TuwqEwfD5buDiJkXMMw0OUQN2QAPIesfntUdaAyLnjeKRHzBY+RTi4F2Coi3nBbD7zCSxAlxQWkmSwAAi9T00BRT5tfdg2Afnes06YPE3+9cXFF2DkZtEI9OOzQijdwReEe4hdmMDD6HJGGsecbVGyMW4NnqRwmq5xZhuNql9WkWOkl8Q17VSTjcxzR5YOy1PoCfBoEkW6qywqHZVd7OyY6sgJS3ETw+FYBNSJLbcRydV8lcacWSVpkrbtPuZcY1YPHXe5DozUoqlMFmMw6tIOMzFStbEcpLjB88z6sMNy0uv2464cZ2Uds+Wm7QZX6NcjdytdiRRT4+KqqWHM5p2s75ptauiWY+CzvKyFWkNjb3e5aY6JkpuIkApVH/zjjVp64WrfmfWwpIKDduUL1eOdS80oowgaO1TSJWurlTPqIhqSNaJJSvVzMttmwXJ3arLD4qDJC63xS8QbRF3SVZTncGauOzF3ZStiCMTslqmMdVlvAt5eefy650+Wmwd5ViYHwXNQUSH9g2qO/MzRq/ZylI0GnrXrK74JnaVeFXsr01117W7pPVyLB2MwVhddZkU4SvFTumOH/XJfWbaddJQ7BB1J0pW423ipoXEsO88dtzdOV3aPm7V9O+QkSD1pQ9I3zLxkjEp6ByeLdkZ7YwintlCG9MImWQ2ay7T7PNo7lDf6y4u1KCs9nctIg3M9zie+nFni0BxvwypjjFTy5L0q9LJt3IbdbFbkI+qRBINWnbWpi6zAMDg+JK25N2/rRcjqEdYpQt0goapzdu+uG1lzqsQii9N8JRFNvm0PTb1Z3YbrJdkazbY81Uh2LsnYK5gGxut00IcNnLR8HcsMnCQoSuw9BZ4dhYUFvLR1V0XK5hTSwXnZzozAnh+rK38FcOC4I1BDmpy6ULwl5+02waltshS3+SxQ1eTaVaKfBm7SL9VaudLDkQlCNab2mzmbGgNaJ9kGYZbWorjdYC8UlkzE+bUpUfBNt0MlSAqXGcrwqNy6sir1sV3VRjIqG2LkiNtGE+yeSrQNy5R0QxfybjTmWm3v1Zs66nucvRZqd2q723mrrsourveqkVjOgvd7iz70a0uPC4dJRA0D8c7tuUO2OLeCuFzRF3s5HAx7YanMfI8VTX7ou3PvwIGjBKhLpWGJMBy+9Y7GZtwQFhxnAdcpueCnI1Ity3wejNnMIpBNAB8aQdvjqHk9I+wS4KvftFRZhHwRzuBM7Ha8HbIlx/PKNuJnF1W/qIW3GteaoTFXylFK40iqJNJ7tmS6tTysaDjdR+1uscRWZ0xeKw6pEE54IsaGqwC2hEQLG//aNyOMrHhDZgc/uAznm467FuqmuDNc2hBPU0sfLKfRiy1+0NY2oXF9PVNwbWdrkm76x4EvMcSLzNM43y7O9mJjzvanW7Kt/KAfBYRRj4NwzUdh4ENk5BV5f9iKCcL43jnoSzLaOYTuYQQVbwoeE3iFauhZJlT1XNSJU3Vm0Jwb5XVIm7J28SU7k6uBOay2SYFymWktT3CxqWQMDpSk5LLrcUOp+rr2znWxLDXcK0N7BK3Jokbxg3mlvVxPdVGbk0AskcxrImadVq/V7hiwM/xYYS7SMPRmicb9Eg8PFcMucY1LZNfGOecswPu07w8Se07O/Ylf04uc6Yl6fmLkgykvmD3qdqVgSSppnjFSmwunm3S2tjJJ3Ow5nN+27EVs5nq4Fkef9Tc3gd/QStlIXDecnB25Ho1kd20aubIkBmOEVVpwjjwX2kthqCcdQ8R9zoGAOyvJSjwdT0k6hwV8dyZWC+/EMWJ0YqU0U21R0YlQdxcudR6wvlpdyjNll3wk9lTUIHvqSuLJjAO6dddmPg8LfqQCc8kI3Co7Hzwch+cHRdGsClvWe5depBshraWr0hRnhJqfdpx77iTM8oSkYo/Zpl4sxO6aVWsRQeol2TTXUGQXMiDAzr2NrpfGtKWsNkqulx6q5nrFn8TcVIaZKZ6YLiyTy0VT+Pq072LevpGnbcMrkntJlCK+qEuU8xLaNGboWanpgN7Sm3hFS7e+cGh4JwxMmDGVsF6F2dpWaKRL9ovrZSD47X6pdGBjYJubdF9Qcz2JrnNR0E+GdEQ8hizibr73Kv821CCNuCI0t3a96aqK4pc9DeiGqQ+mlGKVxYbsml2M+ciZnLrmNEWACdJ0DdGU+J223M3hdVoagwOym+O15HRKL53uyMPVdxHMathUXvTNYaXt1GBrcMxa25ur28aViJMQefVIcEI33qr0ON857NDpJaO5AT6eRcVYbMQoyXkmHtF8L22OJGL7Iq82q/jGRdVl2WuWMWel8bQWusHplpeNic8Z5lKRhab4WqWinHTCLLFk2H4vJHmQ6LJhuLc5GbMZ02nFbEytZdeNSn2Sm2Wt3vZqvT7Q6nmDIsvrdUP4l7QVdM7NBXa3KGop3gRtBe+z1Wi3aXYSC2d+vB1nAnrztrVeKfxIUo2BNbJ/q7rAqaoqEw0WkUG/LxRre07yES3yN7PrhCI5hht3EVMrC5OVNEDx/S04b08rEYzak3KOZyseKTias65JtPMZrR3PeWTemGavtLISi9wa8BCb6mbFRcvVUSaxfIMpt4uGHNa6uEfZI+4ibH9yG5W6Sp7K9L2+d2ia8rCz4191Qsl92SgSQ40xYjFQqYsh0S1eySWVbDplH9YGuueGGbGR4AXa+pykEDC8b7KuqeYDj0qFBvNtQLGzVaFQCbPpazlsWYuLSEETuYNd31xQTNNyuQ76Y2pH1jhjr1V57Cmv23lw1cS1QAdOM1wCYi3qgY3ecu7KMU4fX7KxyxdSxvfXXUOdtGpWgu1GQVVkp5+qNlhnys3oSg2hN2u6jyXKMfPrab8tt9Uo5aghRHVa4DmtdZh+4iSw0azSyuqZYsbecgVVtcRwdssUu9QXJYyJiDhIcN5g9G5cLnfKlboyqVC5uFlampRrRkvrpM0qa60CSoWrbBFV0XjKd2dNdgnhZDCafrB1pUOTjYB3fuone1EL/dtcqN1STz3UssLIDI6Oy6ptoiFVnxxG2pJuF2K/5fVBBQ1jcdFHX7Zl1sWdJCSOFbrFq04ZApz1C8NEb4kxP+udvYva82aoMsH0ukMVX+C44G0fPXK2u13OugourYWNkRcDOJka3LGVw1W0JpPlVsitlnO5cpAYu5wP3EJhVgW1lEUGLc/rMd9364WR789Z3xb05rTLgnbpzJB1OHNvZtZygIH0zKltUjiLqIGQYpGQxBbbuAK6OGC6dMrcgN8l2TbdB5dVGA0oO0h0wEeJe/IIWl3W6E2C/dNJkU/qRj/kqeweuUu1HAf0SjL2Ret0i+cQ3jCtk1RllRUFh83NPhvZbbRtVVoI9LAG1cNzjUrrtuL16N8CB5Rjd3mcjbYJqxXXXcYGRMyGp4bAKU+n7SnQm0Ukpg5Go72872C75s+39R4RKxWnrv3apnHb2wQ6WpDUrT04VgIq9mox7+wsOw75hfLy0oCRS445a7JtyrIhGAFWLDyPd+RC3c9Ft9trplXiZcP6YjgTb5d4GwsNLBWZlq86faawPNvsQWD76+Q8etGZroecMiJDBJ316Lhrs2qFcLlNLgvpojEkLaJNc8G2akR014RibLGTS9rj/ID2JQCs4jvJ1uYre2FS2aHFt7E8rIHW+F4hgqbCxTVBbNbYKSHdK9sUzjm+4Dh6LVPuNFtvPRNwBe+u4dm6IMhsKRdHgZ/7awVTChkLBTIUfLgned8P27zGa5OadwfiuIE9CRZBkdj4RIp0UnLFdo2Lj1hzPprmXl9ctqLqd5RcDpe8QQsjtmRvsyD3tse6Y2XKmHT2Wo+m/BOlN6q9LAxO17ZrW9LUPl+VA7K+RWEy1HvJjHU9R2H2uKz5jhHo6HAzekua7XJsxwyik1z5yDkhxjmX3I1MDHsXlhMsNojjui9mhQ8CsY142wrr0t6V5jIh5lR5nNkSbcMwjCBWGWo7WhNxDKE0ZEDR7EJg5rEHlR8X7WZL5FssWzAERffnk4DwyGzfMyFD7dczE+m3haZ5FGg7Wq2v6chauIHCqTeeYrZcsTwsImmbK0fkKI/+Yryap3rZex3TxoYc2GuGmG+CeTLTzyJzoubLq2T5SzlhFZXDTk3ZRAQccweyNwmiiUIzabvFKa3JDWLOzZM7F1KzHRKSLWzX9+PwRo363BgymmmLi8hecYvy0TVb2k2zPWM3zVTVlOIX+IEdqQ0sXa4aQlkIEcdq7u91KkqMSElGBoURViPwtjjepLmVEIcam8f8mZPbyMD4/FATczNbeOvWPFxmWLQ8ofgA9gEUiZz9a8rN+5O2kIDr1cFKOIRbqsJpEVmFlYSygZZX67xeWEix6yqJi1bAl1scLqzStTI5qOMl4UZh1W9i0Ofuw1UzYLSBJSiJM568hWew1ni+P4AN903Z82ALAoMAjuXqRunssCBDNvHVFt1cIkm2LzuXsMXlUThHCbtyIxTsVtu5bR2kgC1b+LJjYcxSLpdZF6bheZmRvK1uPFBFXL91Ix+bzcXYTbZXGzur5WWZe3yCnjBxmWA7Omwqq1TNY4n0uxtpxDCHz3fh9ubjuGUHC04S93XRqMgWRYZ0iQ9dSZDH+VY1kHh/jq8Y6IELzyFJPSbCns2iFh81vyEPfYMjoQKPl1k1rzsqVJqR3ehdEyfS7uqtrnJKcp01o2njitPNjtpd8KPKJdFxO8D1UZ47kewVwhhwQbLZ1pe1i51I7uYQ5ooNOKZs53DlHVesHV6vcBAemo5wS+xqzgxkkBUSxo5HtjKxA42VdT+nzvB+WyOLpg931OocdGs32ix1qyNwrOZ2Hg5jiyNCJo2NEjhJwPTcTNvwOtDjqV3IVUI75EG2Zj5uwAp13gjzy4mUS3x7AdF8jeHZjnSMyFmtLP7iwLsNRpEaw8oX38A2jdcd94hS+4PtDu7OVeWQzURWB7rACnfEN0w59OHJ2oHOfHtxduYmZ0t/bouXrr0Zy1pq2wPWVh0l4ZtFq50JVjtLeHGTgoqjzszCls6L6uKQq+VyWKasJXB1LHo71eKW1ziTszDUcjQ7nMmFl2np+pg5c2e5DzLzVDi3DM+KZnE77xZVjV1dYY0EfSp6fOGJJE/t53UwjI5ZN0de8PqWqL0IbCmtMSUtyuOGjiwF074IvOrlCNowp6t+zINLGhpEcfRuVRYdj7Rfb3tHnPHLk+XsSkEwVoXbXxkTk4XCMmJ/qJDZfIfWWeek89xH97N1NeIzNXIROhi3g1CN4ommX15fpqPn5wHy33k7PB3o/T87V3wcAb69TrofHgeO/+W+1pe/pdUvry+1lwCdHieooP2MnoeN/+X89NO/8R5iEjA+XrtO776G9u3AvXWi6XeHXpLC75q2Hr81ZdbdD3FfAYjN9GsMzbfnYfXL3bS8au/P3k15Ho1/a8unNdOdpJhe6AR+8hgwXUbPQ+XXF38Ebkq85huGL78FdTXZ+nyzMR3ETq82Xn7732bJ/TGhJQAA -->
