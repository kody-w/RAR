---
name: "rar-cowork-cookbook-adaptive-card-scrap-defective-inventory"
description: "Produces a reusable Adaptive Card JSON snapshot of scrap defective inventory status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_scrap_defective_inventory", "rar_sha256": "dd28e860014771fc62293bd17bcd04b9e2abb8b8e7bb0fa0429dbd5ad5d3a2d7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_scrap_defective_inventory`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_scrap_defective_inventory_agent.py` and in the RCI capsule.

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

Scrap defective inventory Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of scrap defective inventory status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-scrap-defective-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_scrap_defective_inventory_agent.py` and embedded as the fenced Python below (sha256 dd28e860014771fc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_scrap_defective_inventory_agent.py` first:

```bash
python3 adaptive_card_scrap_defective_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_scrap_defective_inventory_agent.py   # or on stdin
python3 adaptive_card_scrap_defective_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap defective inventory Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of scrap defective inventory status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-scrap-defective-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_scrap_defective_inventory',
    "version": '2.0.1',
    "display_name": 'Scrap defective inventory Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of scrap defective inventory status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-scrap-defective-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-scrap-defective-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a1f2bd2a12b6e657',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/scrap-defective-inventory'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-scrap-defective-inventory', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardScrapDefectiveInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardScrapDefectiveInventory'
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
    print(AdaptiveCardScrapDefectiveInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6e7OiyJbvV3H2/FHdY9UGAUHqREdcQFREQOUldHVU80gUeb+Fvv3db6LuXV3Tp2dOT0zEpR4Kmbne67dWJv724jT1JStfPr+owEknayeOwwsoJ07qT7isy8oIfmSRC/9NvCyty9Bt6qysXj6++KDyyjCvwyyFy/dl5jceqCbOpARN5bgxmDC+A4dbMOGc0p9sVUWeVKmTV5esnmTBBC538okPAuDdZ4VpC1JIvJ9UtVM31STIyglIXOD7YXqGwxPfqS5uBolVH+GAE8bwE87RgJNUr1AkcHOSPAbVy+eff/n4EsLvL59/e/Fip4KPXt7EGaVRR97LN9bCG2dII3bSM5yc99AuKbzPQQnlSOAjKOnkefdDBeLg4+Q//iPqnPJc/fj5Szp5Xl9exj/HJp3UFzCpM6eqgT/xnNxxwzis+9cJE3dOX0Ez1U2ZjgaroFnT8+tj5TdKWT75aRz74cHk9QzqH768ZFAEZzT6l5cfR+W/vJTN+P11pJL/8ONrnHWg/OHHb3Sqxr1CPUdiUOrXr8/7J1k48dvUMLhz/QlSfbjXBV9e/qDceD3kHvWEK19er1mY/vAgnJcZtKOTeuCHH/+KrHcBXhSHVf0v0f35QfgCHB/q9BT8x493I/8ymT4Veqf512xz6Na/owmc/sbu4+RpqL+ifbf/fyIdhynMhTeL/1Ny/2zB9KfJz3+p23+14OMk+PKyBDEM5nLMvc+T376qe577+YP/7eGHX36HpP9bMmrWlN6dwtfEScMAVPXXrz9/qO6PP/zy84cmh7EGc+5rU8b/jOY/s+udz3cWfM764fu1kL+eRmnWpZP3SJ/8luX/Vv7+OjGcOPS/Pa8+T/6YL+M1nYxKvDF9mOAPOVNBWf9gxx9ffocwkUJtGu8+DLP83/99IoVemVVZUE9UL2vqCXRwHSZgFF67hNUE/h1zuwTQrlU4It1jHoz/0cOjxBDefv0/3h1AP3lPAEWcJwB99SACfb3D39d3+Pv6Dn+/vk40SD4rw3OYOvHkyOz3X1LnDEdH1nkJKlC2EFTcvgafIBx9Gr+M+Pjrv8jh653Ya97/egf68IFVR04YcapqYvA66mpeQPrUzIO1AdyA10A+ceZBoYIQ4uxHaIMqiyF216NdqiiM44kflpDfCOMjbWi7zyOxX3/91YXo/SV9ACs+eRSPCoET3sWZfPoEtQvi8Hypv6TAu2STD7/9/mHyfyf/1ao78ZHHHuL80zNQwnu9gZnWJHAadBp0M4SRu2d++/1pY0gmhdUO+jEMQvBYDCM1Av6bwdUN8wmbkxMXQENDIyd5Vtb3clS/ToRg8i4vZDoOjXh+yaoa1rUcpD5IvR5SdaA675ZMYfmrYDhWQf9x0lTgzvVXt3TuIiYw5Z3614nE7WH1yGL43yjmfRJcnKUhNP97ODyeQyLlh2rCvpF4nchjbE5yBwbApXSePALn4RdYNd6WQ+LOJAXdl3SslmA01T1RHuaBk6BlvKdLP40+h11AAlHBr9543+c4Y43T7rWu/JJWzyRwytEVHiwKkOm5Cf2xNPzjGVKwC2hi/24/KOlI6ekF/+mVewyqf9kjqI8e4fse40uDoTNi8v+/GRllZ9brI79mNH454WXtaD1sOnZRo+0fjRdsCO6U7/nzrUl4g5g3pP2SxiEMkLL/x2Pm3RPPOQ/0akpouCNzvNOHYQBtOtK9R+kYdWU5xrfzJX2D9I/QOHf8go6CKQ1Dfoy0N4bj6JukF6joeP+tvN+9Cq0I4wBG4iRv3BhGSQCA7zpeBKUqx0x7OgOGLBgt3F1C7/KdVhNIHRoY0p9AIUKYOxD276aTM6gmNHNQZsm36eHYNOUP3/oT2KaC14kJk2UMmApmKOx8xjnQCh/upCYJgDaGIr5buLo4+UOYsbN9CuiMvsgSGMN/9MBz8Ft432UZxYdUIc7W0JbdGCc+uD08+y7n01dQ2GRMyPui79391HXyx9rzjy/pXcZ3oId5Ht9D95txJjC/kuoOrCNMVRBqEvAMIBgJ9wr9+iiyjyr+LsvnP7XzP/y9jv9eNvXvPfd5cqnrvPqMII9S91bpXiFIIDBGwhxU71Xv01iTPt3z7NN7nn16z7PvyD+s9Xny90T8jsQztj9PZq/oKzoO7UIPjMH7vKBFuE+s9YkYR7+kR/DN1c94GJE27mGZfS87b1Ng7TmX4DxOfpShaqxeHSyYd9yFzviSvofDM1kgrKfnsWZW2R+S+F5/oXMfvnsvD3AorSFvf+zdzmDc3MSj+BV4+Zw2cfzxJXUS8C9vasZCAMMWmmTcEMEUgg1RHYL73XtzNN58v6m7JxdEBT/7PObYx8nYyH6cvPekHydvu4T77itt4Dbp57EfHlnCqfDjfe77jtEFL3BzVvf5KP5j6zO2Yc/2+M9CjKkFJYZwXo2yvOXqyPFPROCX8xmUfyai3L848RMwIKaPpTqs39K8gnL6sPGBUD5abQRyCJQNXPBnNpBPCYoG1kR/VPeb/b6plT10+f1uhvqxf/zt5Q04nj549opwOsxQmBiwKiIwWCFDeP8IKzj2P+0in2Qg4sH2Zdy9+tgCLEgUaktRs8AjMYzGXX9GuZ6PEi4NMMd1F+4CUK6LBg5KYLTv+nPHn/u4g/kUpPeI0a9jBxCOogE0ADg9wzwfJ7H5nKBnFObQvkNQjuOjiwWFUoEPi8K3pRGEy6e+D/1GY743tKNdnmr/9uKSBJy5ISqBeVwcQhsOZRLu7XaiBxJYbjo/qNFV9PNKz8QqDMOe2iW7TSR367O+rWwcbOa8tkuDk1ImR5Pfcpue3SfqCUaoH+/1UvSz8BKK7Hom4ft0aFGCpm82G/Fdk513iVXzO8PwyKSK/Y1TV7Wgm/jq2JdiT4TqUbGmXh8KxxahFiF+0RJRFeOjoa7Eopei0rBkN9hRc2pndolHVViusTsLIP7Nzf24sA7ORcm38sbmKimMTpa/PoQD392EFAj4vLwZXiKnGb3ZhrcgtXtawXOC5jHQ4nMKkVi5naElvw2ri7EIi9O25uJZY5okOVu5G8l2jhrIHESN+saLK5Nf+qJvaILVtrpm3IqN5O8761Dsiprbgt1ivh1W6hzLz9Wp8EIbxBfWW20LSfJLQeOmxk71umGnF+XSsVV+trj4JqxNzhU1yr18mG+DKVidtVm0CmtLXjpdJvUqb89PupNfK+NQhOZxwdroudOiizSPwp4mK98dmlT3Genc7bCDIJKsiLhX0aJ2J3ZqLj3b5DHKVL16xc0X2DmcFflBQja0mTthsRRKITed9bxYEgRtR/I5w5aWLVvOzJlHlKbfbjcn31YlYver7azUiavYna7EKQ1jjoOeJJIqV69rohCPuxmeJgMMWJKNziE37JKYms2RQ3HDqGxnU750JHv7ZK9PWJDnfbqzTN7RCzm3pKuG9WLfmnYhL1ppOeRhHrJOtfU8Plijp4SotU7Xp3JjlV06hIS+FLQdxa0u7cwiUkZU3OHAezcV4/cCwgeBgSu3XdV6QzZVrJiwprg5YOte4VmeNBBbmF5UV2hgoJmBXktJ5tjy8QRSRd/sb84hx7bBmUizdlOhYDjernOjAiKUATkPhpLTyELaoxobBWmRmt2yW8lxPRUdvjpk+726qQ3tUMbOysxXEbrHojkem8RhuJR8rpgbnRVWewiAdTXXOX511XpDJ5dtqjeHvhmuIjM62kh2JStbuZGyMbM7uBdz7ecmn12rUx0yxBHbhPKCKRMhY4+LPik94qCxNwlPq0TumivhTAFwABbcYK84VY9RSqiyttitt5jU3maNdlxi7P6InIabXC9mx6bDi0Dr9vExy3u5tShkT1+a2JUuKh9QW4mrjHnQ56cVWVU3Rtxy6vq2dGhRHK4JCDcr3TS5vlZXh6UEZjTTBTIeb1M8A9k5kBNvp3YrL79YPqVl3JnPMKHc00AwlvSuisyhhsQChJjZ4CK2u1sXVicLIUSiuRCpZsqLZlGowfkUx8WNs5dq0pfLCM+5zJ8bTcxghhzN0tPu2CzlEyMdqiPccc8Xm9Nqe9tE7oH0L5E2FZNA11OMNQ8J0pilOr9kW76dw4TZVoUrcNj1VOLdtJzP+1m43rQ7RraltdyauVWLibxxbG3L3xasv4k827INLZe5FakdQmSXeItSi6KMQnYSqysanV6ndXHVc3Y2LFDFV/j9zEuwhULSSozyEmXH9kqN5YBh44aoiylxwErDQalQufjkVFpiCB0eOMSfe0p1ZVW/BzErp6bpZGtywK9bXmppjUS23FX1loe5Fw97tgoLSVdhm2jJub6u0i0pujgkLBy0/dLaHmmujDE6HcRdoVaUESRF7y/rDcWsLsutwLSiawnrzfR63Kp6J5kCWm244RzBNAnrw1zAZhqaVxl1jUVtueXsY63Kt+i8miVuv9PXVkXNOrDmt00hFOpsuyI406kW4oYgiL1xY9Uj6CgOZV2gdZTS4HM6vIja6cjbA07SzSnHQLOTbsK2SszKboe5Zmy3xzANksWt8kOtClWUpFc8HSCOxtpX3z8O7qXLFNoLdtvZpj8u51M+xeK2LfthmB8QUTwfTBZMXSqKGFbtLFJH62XS6H0tVEu9J02luB0ZmaZXs5kaMrXHrlCxbE5n+Zg1R80wVR3dqy0nNcc+L5LaOi+OR2HP6ZGfXvYouzBv+RGj+GKlzf3ccazZwC1InUwyfFlpblUxlYmrmoZJGxoL4nOL7TIDRjPgF0eGujWY5+X1gJRqXERpctrapU0d6CRFUTXizpcjXsf6XFOatFYEtxzWriTrjmQ5hbD0mSvrW3bhutgczCypMJJ+IcUCxOlzvDW8CLtKw1Clu2YLeI7fnk9BfpyqlcXpldWYiViX5P4sDD0VVUW/nF7lZlNxsXrljKuPn1ZzXXVZNtKH4XRRsVRSd0f/sGnF2Kg4jUgYcU2uIstIyoZPGGphyyfP0E8LnOWqXMpPxuqAambEHgJrPXDu2TIgRhliVFVw32aDzX7JZMYuVjr33PRheTxeBmOrXISTdGBybBk2QxnARKg0PXfV9aGVW05NGP5gmySFRtdt1FzAlqlRSTniAeaErrZBa3rvyNyhObVVj/vhTvWtUjP2cnVRu4BUSn2+sgZ6lsnC7qA4dBzuT2jrydJFpqI8vK5kRMsuW1Ka7Wtr7hgEa4iO2Krh0GEMXXQZup12WwUIfrVeHNSYr7sLm191YkqsDPIoKIfGDGTxMsUkMg6GY3y8ysxCSU9UwmrLjHKRVEK9aqWtI0Y7ySRWZooy26a6kSZAh8Jv2nLq9n6LBDrboSOSliHdanJbrXhvr5HzKElli8TMfTmL9QRD59WVTnaZzxUL9+STNrEBa43n7NYhW9M7sBJ9YDxhvdRInIitfEvsaeEoaNYtKoik009lN1fIE3C4bofuOiefFiBNRQOz6eUwKNHW1TdiEVzJSGMXgFDYMDVCnygynC/jvojtco4Wnm3Q14RgD/16scJ3Todzx+v+Ass8KqQ7XtaToJK4OCGy8w0ZdIOJdgrPK+5GiAQaIwQWVQcb0cEUdlcYRjIh58dGzSDxTZ2e63S9nStiPRd68mDlywYWFHuliQZ6yQVbzZbd3NyvJSHZqiiqp2rH45ERDwse3ViwJ4q2odRbsa8DqbTClcAjpbTYdeKwRLnjDOsLF53f1DlzONlonaxCpyvKOFFnTi3lFQH3WauTQkd7Uu+zlGzIg7rBD1q1aa/bcrNtOVceem+5sEXDO9rC2rxWjVA6YqCvqQwIPaZdS9/z9Vt3bec6vUYp6gx3MAlinrfEqj8dZRjCGEQ4nkGjmUqFFk+166O+j/kK0y+Xm6yiXaRVC7uTcW6r9cD1fQHHt9c1hW42RK3gGUlYF+6AeJYtKe4hBzoDg31maQO7Ovv5Tceb8uBRjGaX+qBgvnBQ7YO4MfYgWgktT+ZF36PtQvFbPlkFV4niVdfS1ts4F86SLCztqxkP/cU+KZZMbBOdWnuumevNVmz3HtyP6/zZzfe30NKmbs43eV96NLdZ5jfHOR+Ei0YYBWwVryLOoN1RaoBdrpfDWkJES5vPU4Kbnmmp8UtxpvmAwpKY2fZtRFocrnmh1Uz5IjFBWCZ4sZdrT0UsbnXSsrT3SYaeg11hpMerjYUhvSfNSEwRzptnpCXsSjebr1aXMj6ahxtDLRlQbY7nfAF7xK7orNSArfUl6T2z6GPnpFGJoxXKsogZ+0D7G1WspyahDNk8rXYWn7MNy9y6wnfZGzG96iK648qZtuEsdb3fgF5cR21mr0z2tDPb5FipMkX0YKZrne2hyyVdiGRVRzyjzsQVmG9RXPZo05NErUEPfuwunJOzaXZe4Ql+13ZTTkY3AtIUCxJv/dzHF9JsEQY04fEzswUNRcFBNmyoFeYvjzZ2y9xyzeoGX++x3TVxPLUAvjjLMPnE2htvnQrkQvRRf8DQ3YDtT+bScPXu0AFOIPmrkjpb4oB6J2RNcyBki16xLoaRoNMl0EqzmWaMBJEXsSjy2glI2cBKUHTCNMFnmUevabyu3DVi6S2xKrDbQubs1DZwV2fNZDPvFKVZNVlDByUDrteuRRDzlCL8MsuNMA8MBAnnUyVL6xZQNl3rMghdVz0xYWUEzN49rlhiHYQkEaOrVKH09pyEw/SyJy7LsyUhRpGsLH6ZbtzzRVp0yIEJl4uEPpwYQsCRhCUAbZ/K3Kjm+IkZDqVVSleLWC/xRqgNqz/re79xh2QDdCtEo5uM7sSdoCAZtwyksJluhCVGFFTDzEWErWQ6Rtd0yK4WnhUwc8zAT9ZpsfdyOq7sA6PPyevWplPk5LNncu3uOGu5mK1QgtwfgXI9ee0RuRblbI+Y+ylhSfNUiwOLhe3l0WamILh43jLB03kaSEf5atB0BqwbX1qr+mZfnSkdzwHFlsbg1D6hmLJS+TcJaVPPrRdnE+W4ltVq2GfvpMOJSAWb26x3PBXhW3AIt5hwa5JgnlB5cBEY2puFoM2brYltzVNBAiAQG9JjCfsCdz0X1aK7nXNT9sr5xKtBGCS7zSbwTg7roQhrnu023MSE7nmIkS3A/hT1yQL3WDJbRqbLYVNs1Wi9YAmLLiFk+Vzu/ASDHeSB3FlO2CE1xhdF60bbEzG1AxY2mTgf9Biumf3Gp/0wM4mri/kESoqNnbJWzct949R9RyzFROSNOb2Zbr1LSM+6TWDUXl278pRQYc/mnacty24Q/Eptlmd3vV62N8K6ylbD3BRsCObBRrq5w2Dily3TmFxHiWwd2dUqdch5iW/LpLXWJUavLsVGCY6nJWrqLbpt2b25AsyM7bSYbjI5cCgrOjK2uq/mU2k4E45ggU3WLaK+IPNTLe6WHkyOA4mHDOD9tjW5cxCYvotoFbcwfZuOEO3ctHnd3q78BW+mDa5mQGdbGwnr5YouaXeBdpSXzSS2IUVyD5sHYk1iKa6UKHKkFvEMCRIGj4MDwBdGSRaZc+ADUZGY0/EsBuuitZVhQ98sjNYpdbs+0IGXG4SCz4PQR/faYcnk6mbmI/thSC1RcAtsivgXvDwlKl6FNW06N5ynhpXKzICrC9EU6c8MufHTjlnq9g629HmjbhRc2Ryu0WDQrpXEuElTptXCHsSjMeW4vnBmUm/oZB8t/INAKZueMGY3jR+IyB3ogeFu3SVg0UyNuungXYtWPIKrkq992Lpou223b0U/wdXW3jW2OqMGRGBus2g90Lk7HF2imQGf2Qar823n1eQ1OWC3ntRyQEk7j0h4uOXvlTLo+XPPE3bs2ZleaRXYmfPNIjuI16loKH4tIXUgMBAcdmdFZyjFCFE6E1QBxU5wu1TRIhpOhUopXKmjeepKzQgvkG71ANaV1uRJhSmnUwauSLe8QsPRZR8xDPPTTy8fX8aj6OeB8t99hTwe7v2vnTE+jgPfXjPdD5OB43++8/r8tyX75eNL6YVQrsepahU35+fh4386U/30L76jGIn0j3e047uxW/12GF875/FHRy9h6jdVDWWosri5H+5+fHGbavztQ/X1eYj9clcxyccT8e9Uehl/i/CmRJ19ff5y4/54fO8D/NCpwfP2/Dxz/vji99BzoVd9xcn5V1Dmo9rPlx9QW+wVfZ29/P7/AIYziDzpJQAA -->
