---
name: "rar-cowork-cookbook-dashboard-manage-service-truck-inventory"
description: "Produces a self-contained interactive HTML dashboard for manage service truck inventory - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_service_truck_inventory", "rar_sha256": "87a1fc6dc850ac840fa891b988f370569167fb3dd101c1ecac0a33b839823003", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_service_truck_inventory`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_service_truck_inventory_agent.py` and in the RCI capsule.

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

Manage service truck inventory Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage service truck inventory - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-service-truck-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_service_truck_inventory_agent.py` and embedded as the fenced Python below (sha256 87a1fc6dc850ac84…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_service_truck_inventory_agent.py` first:

```bash
python3 dashboard_manage_service_truck_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_service_truck_inventory_agent.py   # or on stdin
python3 dashboard_manage_service_truck_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service truck inventory Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage service truck inventory - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-service-truck-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_service_truck_inventory',
    "version": '2.0.0',
    "display_name": 'Manage service truck inventory Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage service truck inventory - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-service-truck-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-service-truck-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '34dba2330dd432c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/manage-service-truck-inventory'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-manage-service-truck-inventory', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageServiceTruckInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageServiceTruckInventory'
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
    print(DashboardManageServiceTruckInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZPiSNLmX9Hm+6GqX1Uluo8aG7MVEgiBDg6ddLVV6ZbQiS4Qvf3fNwRkVvf0zOz02n5Y0jIToQh3j8fdH/cI8euL23dJ1bx8eTmEbgmJbp6nSdhAbhlAfHWpmgz8qzIP/EJ+VXZN6vVd1bQvn16CsPWbtO7SqgTTt00V9H7YQi7Uhnn0eRrspmUYQGnZhY3rd+kQQitdkaHAbROvcpsAiqoGKtzSjUMwqRlSP4S6pvczMGcIS6BnhD5DVR2WLfgE2DRCXlNdwNBPUFlBAk6RkOsDpS1UhmEAdHkj1CUhNKThJWxegZHh1S3qPGxfvvz8y6eXFLx/+fLri5+7LfjoRXizRLkbcXjYoE8mSG8WACG5W8ZgdD0CqEpwXYcNsLwAHwVhBD2vPk7L/gT9939nF7eJ25++fC2h5+vry/Sz78u7cV3lth2w1Xdr10vztBtfIS6/uGMLNWHXN+UdQ4B0Gb8+Zv6QVNXQ36d7Hx9KXuOw+/j1BSDUuJMfvr78BAFIv740/fT+dZJSf/zpNa8AHB9/+iGn7b1T6HeTMGD167fn9VMsGPhjaBrdtf4dSH143Au/vvxucdPrYfe0TjDz5fVUpeXHh+C6qQCObumHH3/6V2L9JPSzPG27/0juzw/BSegGYE1Pw3/6dAf5Fwh+Luhd5r9WWwO3/pWVgOFv6j5BT6D+lew7/v8gOgfZ0L4j/k/F/bMJ8N+hn//l2v7dhE9Q9PVFCHOQd43r5eEX6Ndvh+2C//lD8OPDD7/8BkT/H8Ucqr7x7xK+gXxNo7Dtvn37+UN7//jDLz9/6GsQa6FbfOub/J/J/Ge43vX8AcHnqI9/nAv0G2VWVpcSeo906Neq/h/Nb6+Q6eZp8OPz9gv0+3yZXjA0LeJN6QOC3+VMC2z9HY4/vfwGeKJsJx663wZZ/l//BSmp31RtFXXQwa/6DgIO7tIinIzXkxTQU3vP7SYEuLYpAPY5DsT/5OHJ4iqCvv9P/86pgB0fnDp758JvDx789uTBb3ce/PbOg99fIR3Ir5o0Tks3h/bcdvt1mlB2k+66CaeJdwbsws+Ajz5PbybW/P6fqvh2l/Zaj9/v7J8+2GrPSxNTtX0evk6rtZKwfK7NBwUjvIZ+DxTllQ+silJAtZ8ACm2VA7bvJmTaLM1zKEgbAMNE6JNsgN6XSdj37989YN3X8kGtOPSoKO0MDHg3B/r8GSwvytM46b6WoZ9U0Idff/sA/S/o3826C590bAHVP30DLFwfNBUCudYXYNhUVQAVu8HdN7/+9gQZiClBCQSeTKM0fEwGsZqFwRvihxX3GSMpyAsB0gDloq6aDvA1lHavkBRB7/YCpdOtidGTqu2gIATFLAhLf6pTLljOO5Jl1UEtCMg2Gj9BfRvetX73GvduYgGS3u2+Qwq/BfWjysGfycz7IDC5KlMA/3s8PD4HQpoPLTR/E/EKqVN0QrXbuHXSuE8dkfvwC6gbb9OBcBdU1MvXciqY4QTVPVUe8IBBABn/6dLPk89Ba1CA4AraN933Me5U5fR7tWu+lu0zDdxmcoUPygJQGvdpMBWHvz1Dqk2qPg/u+AFL76X84YXg6ZV7DCr/vmWQ/rHheC/z0NceQ1AC+v+xWZkWxonifiFy+kKAFqq+dx6AT9ZNjnm0aqBfuJtyT64fPcQbA70R8dcyT0H0NOPfHiPvbnqOeZBb3wAb9tweelt9c5d7D+EpJJtmCn73a/nG+J8AXHd6A14E+Q7yYQrDN4XT3TdLEwDadP2j+t9dDkAEQQLCFKp7LwchFAEgPBdA2CXNlIZP94B4DqeUvCSpn/xhVRCQDnAG8iFgRAoSC1SFO3RqBZYJMjBqquLH8HTqqeqHtwMINLbhK2SBTJqiqQXpCxqjaQxA4cNdFFSEAGNg4jvCbeLWD2OmXvhpoDv5oipAgP/eA8+bP2L/bstkPpDqBm4HsLxMnByE14dn3+18+goYW0zZep/0R3c/1wr9vjT97Wt5t/G9DAASyKeq/jtwIBDPRXtn3YnDWsBDRfgMIBAJ9wL++qjBjyL/bsuXP20APv61PcK9qhp/9NwXKOm6uv0ymz0q4VshfAUMMgMxktZh+6Mofn7k2+dnvn2+59vn93z7g/wHXF+gv2bjH0Q8g/sLhL4ir8h0SwZap+h9vgAk/Oe585mY7n4t9+EPXz8DYuLhfJxS+60ovQ0BlSluwnga/ChS7VTbLqCc3lkZeONr+R4Pz2wBpF/GU0Vtq99l8b06A+8+nPdePMCtsgO6g6m3i8Np95NP5rfhy5eyz/NPL6VbhP/5rmeqEyBwASbTlgkkEeiYujS8X713T9PFHzeC9/QCvBBUX6Ys+wRNne4n6L1p/QS9bSPu+7OyB/uon6eGeVIJhoJ/72Pfd5le+AK2b91YT/Y/9kZTn/bsn/9sxJRcwOI7207V7Jmtk8Y/CQFv4jhs/ixEu79x8ydltJ07VfK0e0v0FtgZgL7oExROqEGP+tCDCX9WA/Q04bkHJTOYlvsDvx/Lqh5r+e0OQ/fYYP768kYdTx88m0kwHOTo53YqmjMQrUAhuH7EFbj3f91mPuUA0gPtDRDE0C4a+VTgMyTi+gyBRC7Doh7LMBFOIyTFohQdeXgQoAjqo6Hv+oiL4x6DswyGIwgO5D2i9NvUIaSTbZgLBPk0SgQs7VJ+iCMe7ocohgY0HiIki0cMExIApvepGWDM54IfC5zQfO94J2Ce6/71xaMIMHJFtBL3ePEz1nQpXPbUxIMbKuLaE5t114257nHYUB06OKKywmqZGPR0aVBnx1gcsnyuzzltFzS78DbbJXC1Z7MB0eR0v9wY9KE84sebl6I6x63mcDSWIcyl53XFrjd2xFvOIqrdYyWbfVv0BT8OezNrBssYxrwG1GOPViMMcs7CN5K8tAhhoreSJugowqy+Y1JHT8qltFl7ur420JyyJcnaXBSRseXaLIpZj5f62kwDOebDbZ6fTRe3hHOytjZbu0RQijneaL52XGOnRcdNR11DHne6q4PvGCtB4OFGwsG2rEnwh+bLZqS3EdEc185xrRJJOWxK+9B2lHu1apTdXE5Ln8l3BntBmexM5Uqzs6MTdz66Zwo/sfiiPlwXhbiWKK/ZG5rAsOtxWWFtY3bONUSXQqu6h5uw5ePQPBSrijdQRPbc3dlyxXFDjb3ptcFp57DojXNmJlrPve1lUXgHKVcuEj+7LY4E7h4Wt67aqUZMN6jVSb5I1ECaYzUbr/NvlgYHScbd6N3JFbhGFhuyPawB5fkyOV6PR9fzmrW2yaw8Uq+37sin5IntNQdFLpifETWPB5y/WrHt3BPVWMRvhtU5LeyaCKLXG6p117O+EVx2icMV0ibSZVXTpR6XB7FfE7eihftqZY7oyPgk2bLRVouPkleoFHkMQnZW7UGQXZYtOawkqvWImLW6jhj4mubbI7oUpTXuMKcdttEYpRg7tZVX/G0cxBpZWxJ25Wf91bR07VbvWKrOD+ZYwg7i23EdtRoAsl3Dpra+8kLnj4lZIJrjKRF8o9yWtgITO8LWaGGOdbSvQemeVGGvJJtiWXi2qdmWqUXg17MCBQO7J7CxtAtaVRB6MVxi/VrajLMlYt+B96RnnAUqugkrLNK9kjpGjj1H5FO1ha/p7ritOtKdrbvN9axcOn3RkK7rieno5GguFY0cSscLmxqDMD9XzLzce15BGmeHD276AXUo4VSa8G6E5awzFUJL2taztGi+bmBB5pcxcag3uzoreb07dSlH7AtrVGGpKWR1w5zPR6vc59pqAVhEyXDuvD155HVWt8t5aSoHktQX2mhd9Sx3a2JkJREk+2DtgCkhya6NecAUjqvMTkHR7bRVS+sRbSP6tdpUstHJI8JISLOZkWMhoMVtdamQFefNtVNaHbVtTV38oHJKVXPm/HzVd9wNhJih2vhGo/srKD90Hh7SSuaTmj1yIrmU92JDhITBsYN8k+1LoZDbuJfKHWqfEhTQdnQxPMRfUi56RvGb68eCWNcev9pT5FAk6+0l3nX46XjgSU1i6kbrsCTgyW15WGyMlV2FkaHONaQns2Mp10qynTnjuaOYVomGZU4iWY6kKZwEmUCv1+a1cenjcVFi8NbTnbSjx4tgAb6zvU2tkYfVqVNqJM1o7pz2h9G/yYf93qCIAuvJRtQi73Y0K+8mb6++KO9vMUiZ/rrZef5M0Qu9E+hQj8MVG46b9Zydjw4Wpvy6I4Rhhi4vOrXeHCuziTpHF4iKVFQ6GhtkxY7F/JZHbCqs9LSSbhJ2Mx3hysFKthvpXPJn2VllL6qXjyvREaLWcKQW7uAU93bewS+95RBhsnPlj3hdSt5uZCNbcS1HMlKPKDlzbS+Diq64C6ofODVOOyI+RsRS4or24jRJ5yiL1XrDL64Lb9dtkKtH5JxEwfMtMS87bdPXC0CtQmXKRl72B+V2vVo7qRY364CUjKvi7mcan4YaKGX+zkh1q/ePsVpuHLZsPSUkW3q/o5ybpg0DDFJSN6/B9nDYE4WwOcy2p7Jeb5SiYfU6aNqDHu/slV5ZxziaYRV3xH32ClP83LClippxu4SBw2EX32iWYgWBxuJwY18PKCV29nDuugPHN84i2LjF6XaaB+JC1DekuS70nVgV8OzkMst9gWy5dTA/33JqTovrDGH1DJV2CE0UTSaNh7oxnS1nWPqlkFeBo9N84J6Ds3I2RmR0tYILHXtwckPviJsHH2fJ7HJrL7OMYDZUHkoVH5rxds4aK50NvbH31CXauSeNIAbLTWKiZtWVxK0ysTupdpueqkiOTgKIvYIWO1m8KAylY9gGjrarLcaLR9a/DUWeOzRq9WG1ErLz4ozKJpyxMzTs1/0lRPYS0tcdc1gceSQ+9rQgefxSFTabRLFBW9O21F5jQbez4Aqqmds3rzBE1vCvc55Z4Jgu1rp+0xal1i5AnvHeJStTRVy0tY+5W17azBeWKCzx+Z6bqcQuSiJhuWBANAxXIeNE1jkugnnS5TJ6mhe3tRfimRRKlmsqGa9urdQrNzXGXy7lvqBHac4j/h4PGkIfzKKJGy8+LNWW4O2jk8FtH3aKwSwbp8xqFJt3pHidHdP1TYx2OIJx7qIOu8gwe9qyjuiiWxusNR4zPY3PpLY/SERAbff8Qi6DM740pp3IeFiMBpYDuodrIyxZcZfhhZWegbm+uuSrOcvWFV/ptCmmmJRrRoDwsNOtNDMd9/LO3ZVulO2UZUzy2RFGmBXu31xzpvJWIYYCwYrdrFVsNqOI1cpBfUbdbUTuYAcw3lR8h65PpmrubQMmtVU03HpWXUeSGWfjvu0kjeRoePR0Tl/pPcNQnr2i9kd5oPMDbB8phVZDfX3VsK7DGpwtqDWzl8Z50tBnep45hDA3Yk8VMgz3fF5bZtYKvtii6SSdZJ/IjYwis+1ZAE3sBRWXNFezW8s4k16luXMmbQ4L1ar3iL3M5X5OBBdYyLV66aHbQ68tZcOcCzbdGS1sI6IRL0BEXexIbXiLFBV4iWDU2kjF/rBtFnyOEec4ud141s7Mlqv9Yq5L+7JGY7vOFgN98K6C3jR+XbQckhfEPNS3a9eY+YR7RZByKWJEO7tYM/mcbu39Ij8fsSTkysOtHPOURxWnXx8WSVvyxDI2bPRGLEbQV/RB1p0ObTXbLUWlqZJBQvC5KK4otGqpuhrWfD3o5XFt8Ch7OmDHfMMHVLfmVXt9gP29nTYNfhhpVgNtK3Go9n7CIgt6TlOMN0e9izhiPb0EnVPt70Pe9dBbpyxw6swkZ60ml9YYBnST8yc1DWabvMJiGFvC1nJACT7UehdeF6DuXTeKniRxXFk+gZSsRNXhlEypkp9dLBQTtRPhoCU4an4+4UOAuZlMlvvTkRYa3Nzqo+8b7gmUZbUNN2quHwpOnpudtoA51MzmMecEtWbFkp/01eHsyQf0tN8UOzE01E1kpDV1xoI11m9x2OOlIFVFtyRNMq5WjJY5y1Agu+MsH7zD2B0vzUVXEoyiME9fLg4bWiUG+GjGc62CxaBTOsEvcM30x8Ui0sr5Wd4v4uW2NpqldFYoZy5ZyoUMmvCqcdeyXq2ircRwlj8P0Fl/tFAJ9UrPRaScF93Flg2Zs6iCFo3NscoCvWSOB1LOqVf+0i6GciswDrOl+Nbkmr4x9GBVnl1p3h20fOtnbszzFEZph9rMw1SYz7OV4wjzOCzi09WP55mcMqQ1d6pjW4rJWE8bALJcYENMVZJogAgbdk0UwULrqld82fLGacUl3S6JgN8JWNhvkHUvXRpt5hw26ipk1/IRECt64GzPbD2c9vNAXBI4bO/BQubbI46uTcMew9OGO4+2BnavC3ub2wqfBfxWgOvQ42cHIfdyO7F7Exau1zEmVw02bLtZb2rsRQyCXlGzYJWPOXuYMXh/0eTKaQKYVuZxRzuMii4Tf2l02xYXU4RAdzBlkXvLClbZDDn6QjvWuGNrjR/sJDYQWLPXddBE7rfXzG3Ja6QtzjwN44yMJZy964pFOxbezdW56NwgJ+7qchp9igw4CGEVttGltdga+azLJB/TTn0s4Wxg1n3DXF3+AgeY2ZHoxcxiOF9dZ0utkQcHu+AWQS5Lspwxs6SDd7KxaQQdvs1guUTJIqRYeihRNKboNStsfFcDAjhYRcxVRlLrIbX2R2znFH6BWTNnp0lVK4Ly5y4vwGTyipGSvipWxCLzowxPY+rUFhEarK6304YM+KEMR0KkBZcKNtrp4isB2JHJZasldH4NGZIEl+ha0QN+TMfTQC0yHK3DmehwGNHTCFdmEQGL8AjEKkkKa5IWW7CNg0LD5H5B0wqSnPYOtcso1thawbUlREHeOycCWSIIrVmglM+cbj8b5DZZzewIJhzmwFTD0EhoLFZtHAZDHQTCiJTHIVKuaoJStC0kKdgmiGju4wraRWAJHVvRNXnZmSF+TvCVENzY27XPR/iiG7t5BDLpRilLmNiwluEqeLheoFmJ2J0mW9ItbGdXlJrHCaFw/gaZhddwtPq1ZW/GMCSNBQXazTFNlYivPZLrGienEYEYdex6TG/Xba+1F9ifXxpLKWsVVzRZGwoyjISY8BXi1CGrc6zV3fqA4xfcY1o+5Zi1MteJNTJ44VxqV1o6ipUlo/QYGGeRFKxeLgci1xT6LLfazLcPg8ewiNcVPF54wQ3N2qt6U115W88xj0wxV+W0TCXoSJJm8PHU7gE1oJiHa1QrzsI1P640JDLjuJkVV/Z0vSwTYY4TTLvPWntxLPGoY0Lcv3o33ML3Ktdb6YXeJE3WtcvBI0kTtjVVRQL8TJjy7oZ650u7kvEjH+0xZsE78wu/ufVZIwz7vr+1V6kSRiUizTHaVEt7zWy3NVf1o0fFFnuZzRGsRy8pnnDuKhzOK+EyWBaNX0anYwbKI/De3oN88tR5JJ9KGOlXRRYhUuvCsbywLbqLSm+Fb1Sd9/oUu9Fk4NuBe8KwWwsPOCXMGBDsDGA8ARc9G0l8TFzA+4DY1SnnMKZxRDpMhqlru6qwKlLMM0WeaXQzpPBxYHCVQxYZIRsoY2+3LNOk4sm+DPiqcgYVgTeiRyB4OsP4WG4XNU8M6VIwt/Gs8q3TCmxc4mC9i+Vup/qhEyb4Mdt0urfjSWEI0VLGUHwxnK8md5EO2BzZkj6skzi3ioloddVttNptR31QVhwnd9maAHtEq1A0b2Ha5EFGuvO+3BWOMo4+vxpL50IZyzWNGd2cYUeBCY77DKZCBtHgbW+XO96+esgBX4U1mamt32eU3d8EXFvDPNqQW3MgeSMQfH4cDtnGVgv52LgNXGViNWszubCj7c0eOS1CR0IANeaWu8HW5Repuu5AMaO3uikNqSykpbzeLrUWhRFte65gsjlp4h7t2X49UrMT4jHz4HbxNVWpOY77+8unl+lg+nm8/JefN08nff/PDhwfZ4Nvj53uR8uhG3y56/ry10375dNL46fAsMcha5v38fMo8h+OWD//pw8tJinj45Hu9LTs2r2dznduPH1N6SUtg77tgBFtlff3w95PL17fTl+WaL89D7Vf7oss6vsJ+ZviSfLbeqpvzy95vEzfZpieAYVB6nbh8zJ+nj6D2SNwW+q333CK/BY29bTi53OQ6bB2ehDy8tv/BgyuLWInJgAA -->
