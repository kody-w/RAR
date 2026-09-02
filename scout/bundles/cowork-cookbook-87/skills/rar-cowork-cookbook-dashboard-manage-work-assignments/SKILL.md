---
name: "rar-cowork-cookbook-dashboard-manage-work-assignments"
description: "Produces a self-contained interactive HTML dashboard for manage work assignments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_work_assignments", "rar_sha256": "11b608c47718763c5258a2b7f1349bf08c06c21d5f7a436a58a5e3b40bf5a807", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_work_assignments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-work-assignments:e494731c5cfd8e54db260569f671dbee805aa9f4a2ecd5f2335d8efdd91b4228", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_work_assignments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_work_assignments_agent.py` is
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

Manage work assignments Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage work assignments - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-work-assignments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_work_assignments_agent.py` and embedded as the fenced Python below (sha256 11b608c47718763c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_work_assignments_agent.py` first:

```bash
python3 dashboard_manage_work_assignments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_work_assignments_agent.py   # or on stdin
python3 dashboard_manage_work_assignments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage work assignments Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage work assignments - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-work-assignments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_work_assignments',
    "version": '2.0.0',
    "display_name": 'Manage work assignments Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage work assignments - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-work-assignments',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-work-assignments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4cee09e17b34d1a3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/manage-work-assignments'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-manage-work-assignments', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageWorkAssignments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageWorkAssignments'
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
    print(DashboardManageWorkAssignments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjVrrmX2HyfrB9lZXsILKjI0ZCSCCxSAIJkKsjzXJYJASIHTz+73OQMrPK7fbtdsR8GFVUpoBz3uV590P++uTUVZQVT69POnBSZOUkSRyBAnFSH+GzNisu8Fd2ceF/xMvSqojdusqK8un5yQelV8R5FWcp3L4tMr/2QIk4SAmS4Mu42IlT4CNxWoHC8aq4AYhoKDLiO2XkZk7hI0FWIFcndUKA3Fk5ZRmH6RWkVYl8QbIcpCXcDoXpEbfI2hIUz0iaIQuSoRHHg9xKJAXAh0zcHqkigDQxaEHxAqUDnXPNE1A+vf78j+enGH5/ev31yUsgCyjt4kME5c7dhMxn33jD7YmThnBd3kN0UnidgwIKe4W3fBAg71c/jpo+I//935fWKcLyp9evKfL++fo0/tvX6V2sKnPKCkrpObnjxklc9S/ILGmdvkQKUNVFeocNgpuGL4+d3yhlOfL38dmPDyYvIah+/PoEsSmcEfqvTz8hEMWvT0U9fn8ZqeQ//vSSZBCIH3/6Rqes3TPwqpEYlPrl7f36nSxc+G1pHNy5/h1SfRjZBV+fvlNu/DzkHvWEO59ezlmc/vggnBdZA1In9cCPP/0ZWS8C3iWJy+o/ovvzg3AEHB/q9C74T893kP+BTN4V+qT552xzaNa/oglc/sHuGXkH6s9o3/H/J9IJDIDyE/F/Se5fbZj8Hfn5T3X7nzY8I8HXpwVIYKgVjpuAV+TXN30r8D//4H+7+cM/foOk/y0ZPasL707hDYZoHICyenv7+YfyfvuHf/z8Q51DXwPO9a0ukn9F81/heufzOwTfV/34+72Q/yG9pFmbIp+ejvya5f+r+O0FOTpJ7H+7X74i38fL+JkgoxIfTB8QfBczJZT1Oxx/evoNZogUalN798cwyv/rvxAl9oqszIIK0b2srhBo4Cq+glF4I4pLxHgP6l/0jSTLL1f/FwTeHcMdpginTipkVThxgsB4GC0+apAFyC//27unVZggH2kV/UyHb49U+DY+fvsuFf7yghgR5JsVcRinToLsZ9stAlem1cjx7htlff3SjEzvCfcuxZ6XxoRT1gn4G/LLv+Xydif4kvejGl9TaJdH+q7ANc8Kp4iTHuZnmKfcvgJfYHqFuaTIksR1vAsy/qjzlxEbMwLpO2IerCigA15dASTJPCh5EMOU/AyNXmYJLAfViGN5iZME8eMCgpQV/b30QKxfR2K//PKLCwX/mj4SMYk8Sk6JwgWfAiNfvuQFCJI4jKqvKfCiDPnh199+QP4P8j/tuhMfeWwhCHfAoDMnyFrXVARGZv2oQqNbwLRzt9yvvz0sMUqXwhoJ4ykOYnDfDKl9c4NRg4d5PmwDdR5FBMU7p9/jhrQRxAWJK4gWjPHy+Ws6ksjg0qKNS/AB4mPzA/oPYz/4jDYp3zGEdgqK7Hpfe/fA0ZheVvgviBQgn0hBdaFdq9GiUVZW0GlhufVB6o2V1Km+mTDNKqSEcVMG/TNSl1DVkfIvLiQ9gnOFycmpfkEUfgvrXJbAHyNAd/Zwd5bGo+HfvfVxGxIpfoA+Nv8g8YKoAKKJ5E7h5FHhlOC+LnAeHgHr28d+SNyBNb9FxooORhvdI/ruecqfdBLSPzcgn9Uf+VoTGE4h/181L6Mqs9VqL6xmhrBABNXY2w+/G8UaYXj0bLCLuMtwD6JvncVHEvpIz1/TJIa2Kvq/PVYGd1d7rHmkvLqAMuxne+RD7eJON66gw4weUBSjkztf04868AxxguYqx5QG4/oyZonsk+H49EPSCKI1Xn/rCZCHL44xAr0cyWs3iT0kgEDcA6KKijHc3u0CvQeMoQfjw4t+pxUCqUPPgPQRKEQMIYe14g6dCsMG9lGPGPhcHo+dVv4ws4/AuAIviDm6OXTVEnEBbJfGNRCFH+6kkCuAGEMRPxEuIyd/CDMa+11AZ7RFdnUq8L0F3h9Clx0LDuT3GY+QquM7FcSyhUaA4dY9LPsp57utoLDXMTbum35v7nddke8L1t/GmIQyfqsJsI8fa/134MBEXlzLe26CVfhSwqi/gncHgp5wL+svj8r8KP2fsrz+YRL48a8NC/dae/i95V6RqKry8hVFH/Xwoxy+eNkVhT4S56D8Vhq/PALty71yfhdovyP8wOkV+WvC/Y7Eu1e/IvgL9oKNj+TYA6Pbvn8gFvyXuf2FGp9+Tffgm5HfPWFMdzAFw5j+qDofS2DpCQsQjosfVagci1cL6+U9+d2ryKcjvIcJzK1pOJbMMvsufEedRrM+rPaZpOGjdEz//tjqhWAcg5JR/BI8vaZ1kjw/pc4V/Cfjz5iIoa9CNMapCcYNbJ2qGNyvPtuo8eL3Q+A9omAq8LPXMbBg0YMt7zPy2b0+Ix/zxH1ES2s4UP08ds4jS7gU/vpc+zlhuuAJTnBVn4+SP4aksWF7b6T/KMQYT1Die4Idy8V7gI4c/0AEfglDUPyRiHb/4iTvWaKsnLFUwgr9HtsllNOHndUzAm0HY+5RC2q44Y9sIJ8C3GpYnP1R3W/4fVMre+jy2x2G6jFp/vr0kS3G749O4eE34xT6H7dzI6YfZfhtpOyM++9N1x3ie6v6BtWLx3L73aNw7B3eHn749ApzDXh+GoEsYth/D/fJ+ukhDtTjW5MLKcCs8aUc2wcUhhGkBIt6PupwgRnvOwbj7di/rx+/vP55Z/xn4f8KKI5iSdyjvcCfApryXYLBaIYLGBb3XQCmGO04XEA5BPB8OiBIkobrAt/ncJciiCmUYrTk1XmXAsVHG0D5P4H+6+3604MArBcEzUAKOO4y2NSjWBafsgzp0QQ9dQiXDXCS4twAPsIYj8CheKxDkYwDn9KAdCnMDWhnirEjvfd+8SHV20dv/mGVRxp4g5nzGo8yE47jTT0Wp3yOdRgPkJhLegCHPFgSYDRHBtMpoOD+z63vlhkN91B8dFrYKsKmpRn5/Ppu6dERGQquFKlSmj0+PModHdZk3X3kcgUD7JOFSm58uDluzZorc7hpJeXYs+viNJTL7FCUgtqvBVz1TuEJy1hTUXmRmW8JPXC9iT7L9dTR5ci15xcq9gi3JuVLQNMUe5zvl1kHpjTfzIvcnJzU1q71jMxurQpw1tw1WpkkgA+C7bVzg5I3guIorvyS4yaTk8lhcd4oV8E+YfahJ67XPi/kQ71XFlFwZb1Ngl27oSNpI4/z/Sru0kbt++OmKiRUFxI74yZAagLCnrYEs0oO8oXgDb+EiZdYHw44JosZJ65LIkhPU04j85azTa8h6QEVZIVc8U4irYcuT6hCBnWFO3OgT5XeapaHZbNTGnpV5ucNvkzbYXPVb7VPTbxIs8poHvGxjZk+nm3E+cQrWf7qHo6bSW1vnWlkrqq1H6VRLkq5sSDmZ4cR1GRzLJaL0/roWreK0PaZBhw83gS3CVZHUiIP23mlhAdZCeRAMlLjWEhnHo9Cep8m3Gwt5C2qJ4dNnrsliImB82h6xRuF7CXXg7Dgce3GREoCNnnfWPIqOeZVrVyY2x6Y3pXVcIxfX0mGowdrt6AZPT6oHjafeoGJLUuJWLiBunPwW0fTxi5a0Oot1fpGLVozcBqjF4oZEGOg9UfJoc5nzUFpZp6bMrnthvTa496UnWN5bYtFmiQkOYnUuLIUa1hR4Ox0Nb/obMK6oRsx3HSkbdr22Tnry4VNoT1W8DgRhoGM8lMn3V3thbWyqnpb6OvBvxXl4TA51pehSzqCWxbdZWD5ZbQlyk4TDrA0mBuvjwdjeUHTrXUkNaKom82wAsPAswoqZ9SBLk/SZW225eBU6xuTrAt9WF2aPMj71E4hNOqBwZpWMLp0MVHE6U5TAr4cdnvxhk5nWs5pTUBHk9gT9zWIPIbGmh6cXD3pDeeYHk+Rc12LPY5d18tLty2kvWqZ7a6PCiG/WuihribpjnWv9OFm88Gg97jELNLU0HaVJl+qo0JpUVm6prafr4vJQuDlGannm12KpbxYaK6wx2Klujjh3lJNZ08fD0SlnTVPW9+o6WndzAVXtIZUNCQ11a7TyxCV64XucS7Vc/MVJwqNRJuGNB0YM+cLWm1DKjhP62qtCSUrBnSDybdso8l7XG6oXuqLDUr31wXe7UMb02dElSX7/UEVxQtqaytMWVwjZRbPzhYIT9src7ue2ST1BBsP1Vyyri7OF+v9QeionDLELPKkeFiwfSXcuGlETtdb5aysF3krWTZmWYWgTHFvt8eCojAvx4Cr2rCYXJJSAmJ35ZxDNuX3GgbUSpIPbdzHJUM5Mr7JeiBN1J2lRTQ3Py4Zfkj2V7t2dQnl9sptKOhJp7Wphfe6xa/PTD7ZbS6hb5nJuqnafMkztFilh12/pu19I+1ubrUUtj5t+MRVYPaqf0n2onrS1kkuUbWHLSzLS1JxWySldVnTCdHWglp4HaqQdbQy3HJQDcKoF7JpeNqWA/pymDfLwV45Z57OqcX0TCxbi11vTtmxMOrGi1hva7EqioenxTRrWq9ckM3Mjr1jpForUwchJy27S7yypvms8ap9oq2Bp7bMEDp0vFiL6bGemJ0+mxgX9IQP09ZdSYaWaPT5lFkDhwrJOV5SV0xGl/qxsxwNzDTuEEZTSjoDSUgni2AmuQq/oVxzMdv3ehsJ3SqTd5VgTmXQa0m4B7OA1ePiZq5WyQxf6vg6YM+FQnnbC7/ZN7wJ9VQM6QKGsGjOVgNgLpEu+K1Z7RZ2X0MFRUO8sRp20K7KcC5YrklzwmusU7/TUSE7OYaY+tglWRlHNMduOAGLh7QpMkxW2i3KnmbKvAYU60c7sLnw00Has1PDGKYOWiwTNFmg2WG7lKeZE4lWkXYWQc9mWrnSEsXd0fGlOfP8LlHqZFhnPAVT3J7T+QzVV6FQh/gJxoeULvuNk/fOZe34lHHsRQ7WwAKzvA23xvTJOZ+umWhbLdeSsPScrbzfOsNBxWQ2M5xD7NWBYnohV4RW3NlhfsspccolPnCvLXs7UvpFilbKVFx6YItzzWZ94ayEy5UijTk/stlMtcVwpgqr03lrKbc4m23BeaFSxopcVXnfKnp/IFINBY18WOl7m6vX14HHz35SWFthhffL1cZJ6kHXINSWwNoBkC4b40hM1pwSOTsldfaX43Wxbu05tg9ZE1UTcSdTAle64cI9Unzpesy5uhmXTOzCBPQ3/OZ4p6xk9qgMVGxZ83ws1ZnvJAsrI6WLLcwxV7F8azEMx7nOL6fdASbffMcLK2PmJNElmgokAVPVdOMqeEIBO2EiYWn2s/mSswxAH1etySuM0njUbK+KgkoQk97twI3aEJQSHVxtlhC7fNvIUaEl27lDrPGNvjmYZsAqnUr3DI9ed65xkaOS9arW6Tk5W9LS9XYzVX1bL9M9vok2Rb0n1H00YyqirFLxppFXBRgr6pabDaEaGJPp3nmqQ5t7OAjF0pzdyOuhPe62cPwy7PhIz4e9fIrJeK3L60Op8wfmsBYCwdSE8Lg9rePJQiSPA7PD1fgaCqaBotWCdXcoGxUy5p2XQ4/PwmFOH3GYl0MqPSTqAT8sq8C6ZGCCalZ6dmHcJ5quLqM5mfEkgeoabzNelTY7hiR1OT9y/i1t2eZEn+QepqMJXtWc5yissYrnQlvQga/upPNGsjfCws1Igkhde98qtxY1N1QvC1s8xoI1g/tpzu1mZ/eyOu/qdrnMiT6xZDbq9DQWKtvGnaO49667kiITopM2Rwbz64O6YqlDZBxunFfjZrcMdhmY2UoUqMFUzzY77NBSpGtfwmVYBKa0lCv8MF+k1yVTrAt7ZtAKf92dZT3aFbp0CogLGYupqNPGHpsw+uDNGjm9VJtA87Y24xixagCTk9aHJafD0SU+4gq9a2Z748TSh25uXxVLyGN7Y0Qe392UHX3cuIuLf9T0VZfzhygDrHBUduzFMcLzQoblw9OEFmMgB4w2neNMZU+Yfzvp3HJvHSMp0vqJt7fioiD1nuW0UyYzlemfOExh5nLPuV1nt1cCz121tvnE29ea7R6HSrmgVFnmN+3EiabueEUxn5392Ec3eUGkAOMAWDbncAHq2NnQsbS/4pICG9iQKU9wcLlydp+Bm8SasIO98Uyw2sNmM52RnnTkCRrFifMWpi222HtojLN1mke8slkecfMyI5rKafP5iU+ykEx5d8Zs2sXOlnRMFFqB0PHDydWStY1lS2NzbvhVktb+AT85dRtYqdtto4M0rNiN4fFtjw260GPaPFKweu6QZbA+1LaPba47fOu76xsP1qI/aU10KXWwKfHPVyoljExn01lJM4IiGjcsmWV7PqXyo361Vqo2vyw2J49gS3Or2MM0j7ZpDMINs2h6ligXzoXxyUq9zYz5eQsdJfLxYcm6gPaJzOFqKiJ90efVWT+U2DndLlpn2gxliUtZTc8MPx4yx5ar3SQ3PUGP+bjHGOAUx1wPF/PlVaTsxTx0LuGi88JuuolL3Jzb2am0NlF/AjE24VJhVcRMNlseAlcv28ILtUXNcCdsqfCHsyWEVRv57ryjJuf9BlszctutJra+2ooAl+Q1EE5Lc27Jfu2KqUdyC+zWH1JxQjGMXWfFCc5COzsriFwjSDnhDei8RM3NO7uBA0E6B1VfNCjpaCwdNIGYFXk+LXGta7ujuyFvvTb01HpSBRROlouYWW3IoO52tgyI7cLf2/Lcl/fssvMr2LMqdbo6LC/int5yK2uGl7cjoQ4eKerx1gLNwb3gk4qGTb9yPqarNbVrdiYsqbutKcxvKzKLC/kUzHssaouGl2ZLcsfGHKfTS1Qm19bxaAuozjLYZj44zNacnwNiYhJs3eGwvTyhJ5NM7TlhLhjMWk2FyaHmUmfBWecLEURNgzK8yPHFLK5VFD1sp/5WdgCHD6zQYCCuDX5Cxm4OZjW5W8zxZRDTzDIw0MTEHanyHeKAZqtinbVK3QBV2MnlPN9jNHXWElEQYWhkREzR56m5x3y27w2d9fum9uPdijjDtMKszjC3ODVOLS4eU7KJCqb5qVvZS1E550rbT87NZiqRSRt5i9uS9eaNE6C94rBFrbTxRiaoyp3LtO9XldWrkwO5OuaL1aXFvCAbQu5EEmQI06AQo+nOWhjV1Nyak+s58AodledN16DmVoN1csPesm22TiSpKG0nCPalvyDYlN4ayt6vcYa1+S6eVbbJpYorklXjDrbK3NwlPoS0jTMdKQz+FD37zUUhsN2B2vg1Z3ROqaB2Z6xjdman5YWJcXoPutUa69C1lR1qAfYUQ7Ho6BWruBTUvsg76hQGeSue5bVNTzfLmOCJ6LwgS7G7pCXT02ns1lrZTrx5W5hKmi8DRZNB052nk8WcplHRA+3kMMel3DFpdMfaSeiZ4n5+3aRzSZAPrNC3gJFndpQVx4bmdpmbqbx9DYJu5Z9EA7WXk6hGHZxmS7m6zsir6w/4pezUQXXkbT4nXFomdAXVLirFBpKEUvm53E/qDCdcUuvLFQrWfC9qmH8MwwL1O+7ctctoMScpqtxfSktwUhJUNMCnnTuQJrnDZ7UZt+wmKs5quWyONH2cWJqqEhzpUEd5N+Du7VKKS7KcixkL+IUya+dLGtXVuZWfyRNmC4cFvdpOypOYHvjzZSIWWHoITip36oBlhTFrOdTOaMNKrsiDcabIQvaXKDn4SYrK/opjphs5WDjSAvWnwSTZTakzaLgzKTd276DAVbZuHam5yTEby7rdKMB0YlWKJ85qMIukUqljN5OWrkuiyScdUPJpyLbRXpjRFCwfN7ifq86Suq/sqS0f8eFIwhlqORm2bafOpquLtD3iU1/dcm0Wr4pjS5NipjTapdZOLjXF46Y1Qrlh4PxRxkfZ2s7IzCMaYa7OQ39th7J/ILzaA5F4umw4w9n1+LyZcIlMDJiGHsPbPIN1Ss4CnZ6kxnW2jajpNr5WRds0F9G0tXB2dCWj851ZA6cGQrqlfUjm7mGhnZXdKblQgjpOLBhsJVjTa+YlNyy8k7u/TKi6bLcTNDyk7erYFa1B4s6ZFtaVV2eUNRl4slYn/DFlt/A/j+1nXj+tdWxjqqbonG9nLhc2OTo9yFfSUgaRmGtN11GLaq6eI8dvnIWgqxLHzwQ2MAUJva0X/Xm9btRtqfawV0xV0et6MVixJABtz5BnTKS9VT3ptc1uNnt6frq/2316xTGGnD4/jef/76f4f+kMOBzi/O2dFMkSzPPT/7sDysdh4ccbvvuRPnD81zv3178g5T+enwovHiW6HxuXSR2+H0r+0yHsl397Mjxu7x9vp8dXkV318QakcsL7yXWc+nVZFf1bmSX1/dwaIl2X49+nlG/vrw+e7mpd8/u7iA+OT+Pfioxn/hncXGVv739Zc789vmIDfuxU4P0yfD/ph/t7aLXYK99Ihn6DaXJU9v1t03hiO75uevrt/wJ7P0yVjycAAA== -->
