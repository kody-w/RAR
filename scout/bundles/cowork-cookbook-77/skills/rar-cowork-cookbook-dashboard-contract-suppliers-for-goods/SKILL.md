---
name: "rar-cowork-cookbook-dashboard-contract-suppliers-for-goods"
description: "Produces a self-contained interactive HTML dashboard for contract suppliers for goods - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_contract_suppliers_for_goods", "rar_sha256": "2630268cb5ef019db68e764b913b2b46889f9d7bbcae51658737c2eaa35f9252", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_contract_suppliers_for_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-contract-suppliers-for-goods:741e7ae3c08d7504a32ea4c3c5831b33fa1bb163dfdd31b2b35b4610ac0c7c99", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_contract_suppliers_for_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_contract_suppliers_for_goods_agent.py` is
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

Contract suppliers for goods Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for contract suppliers for goods - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-contract-suppliers-for-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_contract_suppliers_for_goods_agent.py` and embedded as the fenced Python below (sha256 2630268cb5ef019d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_contract_suppliers_for_goods_agent.py` first:

```bash
python3 dashboard_contract_suppliers_for_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_contract_suppliers_for_goods_agent.py   # or on stdin
python3 dashboard_contract_suppliers_for_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Contract suppliers for goods Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for contract suppliers for goods - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-contract-suppliers-for-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_contract_suppliers_for_goods',
    "version": '2.0.0',
    "display_name": 'Contract suppliers for goods Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for contract suppliers for goods - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-contract-suppliers-for-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-contract-suppliers-for-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5e4bbb195a700154',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/contract-suppliers-for-goods'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-contract-suppliers-for-goods', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardContractSuppliersForGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardContractSuppliersForGoods'
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
    print(DashboardContractSuppliersForGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816Z3PjVrrmX8HqfrB9qRaRg6amakmQBEhEJgCEe0pGOAhEJCJBr//7HpCSuj0ez4639sNC1RLCOW943gz0r09O20RF9fT6tAdOjghOmsYRqBAn9xG+6IsqgX+KxIX/EK/Imyp226ao6qfnJx/UXhWXTVzkcLteFX7rgRpxkBqkwZdxsRPnwEfivAGV4zVxBxDxoMiI79SRWziVjwRF9aAKHyN1W5ZpDKr6fjssCr9GviBFCfIa0oASDYhbFX0NqmckL5AFQVOI40GWNZID4ENO7oA0EUC6GPSgeoEigquTlSmon15//sfzUwzPn15/ffJSp4a3nhYfcvDvIuw/JFgVlTDyhyRSJw/h2nKAMOXwugQVFC+Dt3wQIO9XP44qPyP//d9J71Rh/dPr1xx5P74+jT+7Nr+L1hRO3UBJPad03DiNm+EFmaW9M9RIBZq2yu/4QZTz8OWx8xulokT+Pj778cHkJQTNj1+fID6VM9rg69NPCMTt61PVjucvI5Xyx59e0gKC8eNP3+jUrXsGEO+/3w318vZ+/U4WLvy2NA7uXP8OqT6s7YKvT98pNx4PuUc94c6nl3MR5z8+CJdV0YHcyT3w409/RtaLgJekcd38R3R/fhCOgONDnd4F/+n5DvI/kMm7Qp80/5xtCc36VzSByz/YPSPvQP0Z7Tv+/0Q6hZFQfyL+L8n9qw2TvyM//6lu/27DMxJ8fVqAFMZc5bgpeEV+fdvrS/7nH/xvN3/4x2+Q9P+RzL5oK+9O4S1z8jgAdfP29vMP9f32D//4+Ye2hL4GnOytrdJ/RfNf4Xrn8zsE31f9+Pu9kP8xT/Kiz5FPT0d+Lcr/Uf32ghhOGvvf7tevyPfxMh4TZFTig+kDgu9ipoayfofjT0+/wSyRQ21a7/4YRvl//ReixF5V1EXQIHuvaBsEGriJMzAKf4jiGjm8B/Uve2ktyy+Z/wsC747hDlOE06YNIlROnCIwHkaLjxoUAfLL//Tu+RVmykd+nX7mxbePnPj2mRPfYJp5u+fEX16QQwSZF1UcxrmTIruZriNOCPJmZHt3kLrNvnQj53v6vYuy49dj1qnbFPwN+eU/Y/V2p/pSDqNCX3NooUdGb0BWFpVTxemAOGPGcocGfIHJFmaVqkhT1/ESZPzVli8jSmYE8nfsPFhkwBV4bQOQtPCg+EEME/QzNH9dpLBCNCOidRKnKeLHFYSrqIZ7NYKov47EfvnlFxdK/zV/pGQCeVShegoXfAqMfPlSViBI4zBqvubAiwrkh19/+wH5X8i/23UnPvLQYYG4owbdOkU2e01FYIy2GVw21iJobce/2/DX3x7mGKXLYdmEkRUHMbhvhtS+OcSowcNGHwaCOo8ijvXuzun3uCF9BHFB4gaiBaO9fv6ajyQKuLTq4xp8gPjY/ID+w+IPPqNN6ncMoZ2Cqsjua+++OBrTKyr/BVkHyCdSUF1o12a0aFTUDXRfWHx9kHtjXXWabybMC1iuYQTVwfCMtDVUdaT8iwtJj+BkME05zS+Iwuuw4hUp/DUCdGcPdxd5PBr+3WUftyGR6gfoY/MPEi+ICiCaSOlUThlVTg3u6wLn4RGw0n3sh8Qd2AH0yFjfwWije2zfPY//d83F+p8bk8+GAPna4ihGIv//NTWjUjNB2C2F2WG5QJbqYXd6eODIcgTk0dDBzuLO8R5O37qNj8T0kbK/5mkMrVYNf3usDO5O91jzSINtBWXYzXbIh+7VnW7cQNcZfaGqRnd3vuYfteEZggUNV49pDkZ4MuaL4pPh+PRD0ghCNl5/6xOQh1eO0QL9HSlbN409JIBA3EOjiaox8N6NA/0IjEEII8WLfqcVAqlDH4H0EShEDB0a1o87dCoMINhbPaLhc3k8dl/lw9Y+AiMMvCDm6PDQaWvEBbCFGtdAFH64k0IyADGGIn4iXEdO+RBm7JjfBXRGWxSZ04DvLfD+EDrvWIQgv8/IhFQd32kglj00Agy868Oyn3K+2woKm41Rct/0e3O/64p8X8T+NkYnlPFbiYBN/lj/vwMHpvQqq+9ZClbmpIbxn4F3B4KecC/1L49q/WgHPmV5/cOY8ONfmyTu9ff4e8u9IlHTlPXrdPqokR8l8sUrsin0kbgE9bdy+eUj2r58RtsXKPqXe7T9jvoDrFfkr0n4OxLvrv2KYC/oCzo+kmMPjL77fkBA+C/z0xdyfPo134Fvln53hzH7wYwMA/ujCH0sgZUorEA4Ln4UpXqsZT0sn/dceC8qn97wHisw1ebhWEHr4rsYHnUabfsw3WfOho/ysRr4Yw8YgnFGSkfxa/D0mrdp+vyUOxn4T2ejMTdDp4U3x7EKBhDsq5oY3K8+e6zx4vej4j20YE7wi9cxwmAdhP3wM/LZ2j4jH8PGfYbLWzht/Ty21SNLuBT++Vz7OYe64AmOeM1QjtI/Jqixm3vvsv8oxBhYUOJ7ph0ryHukjhz/QASehCGo/khEu5846Xu6qBtnrJ6waL8HeQ3l9GHH9YxA+8Hgg/EE02QLN/yRDeRTgUsL67U/qvsNv29qFQ9dfrvD0DzG0F+fPtLGeP5oHh6+M46of63NG4H9KM/jYwjIKODYjN1xvjezb1DHeCzD3z0Kx57i7eGQT68w84DnpxHNKoYd+u0+fz89ZILKfGuDIQWYQ77UY1sxhfEEKcFiX46KJDD/fcdgvB379/Xjyeuf987/Nhm8MiQGGAcQHsr6DIWSDoEDh/QIj2IJzCWIwMFcF6MJP/B9eAN3CcolaQx1PNRjPI6Doow2zZx3UabYaA2oxCfk/5dd/dODCqwjOEVDMjhNoDjNei4FAhTjfJdmAUOTLocRUCqSZlku4HzGdT0HUBhNsQzBeFAXh6ACDqfwkd57R/kQ7e2je/+wzyMzQKGyLB4Fxx3HYz0GI32OcWgPEKhLeADDMZ8hAEpxRMCygIT7P7e+22g04UP70YdhMwmbmW7k8+u7zUe/pEm4UiTr9exx8FPOcJgT46qRyzF0EF7OLIty5YBmGF4DKkNBmiShXaDZLGvR41U1dlIBn9mrZVTaKTnvdXQdXJaBvebS62QvL9pDua5XTSI6OL+hgJVMb2fc8qLdqsBUAyvLXD2okIyxdxTN3FeacazS6MY2Dirx7KodXGyYTOzjhDQdINHUjePqtmM2hglsZdPfwluRRprCnuM62lIJq62A225LISDcQ5leIikNtzdhGDC5cYvrNuFOFz8+6NNpugSK3Zz39YqXxUObmZjZzauLSS4PBTgfaaAf6ikg3GHS9huN6KhJN4iZTAiKgBZDWV3LlKxk0DaEw4E9qwxWtzquuq1CoJF5pFKHZ0h7dZANS5hM/blm1dE84uMTavpYIYnziVczfO8eDWnSnnSHjUyh2VwjOCvwmdU324OgFU5EmRd7bUlVxdNGi+HqvEItRfU4mdjT6eXYKf0SHTYHZc527FUAKp5ECuMsF4YErOMy34tzTTKOZba6DBljKdi5y082XzfD3t1uVzZJTdxlbDMXi4fymKaZ4fRwiMtVad08hTG3RXsK3Gmm+oqabzRp2xBbcX6dujPzej7NGxZbVaasZ6mvLul9WwlxwFx6vNv504sqr/fKnAYwoDdoBBtShar06jLHvMbrRBO4unW7FcJeoM6gNS2rC+ilqRHe3NVcGfVNlSFjCeu6VW/opH/W1uEQtbdV4mjXnRVluBF1EdmbwCAJbS7dBHxtcThfDDYdSGJnHC9OfZwywhl6kcyFV3evnvV9dNVqOwmPVLTKcH091UBbTeza8oGReVyWGfhpYhnX8ny67db7OtpkWHs4quBgNCxeSJ3j4dW04nObyBhNR2m060+Ha76YKCK71ZSAr29bU7xM2dmp5LQuoKJJ6Im7FpxZelBnSSsQqYxmKCNdbvursg+iS+mZ0iYOzMN+LHdRthDUA1sLxXkrBEsuc1I4G2/yuSZjVqlpuz11W5Ft3BvLmb+wT3jj4fzBqoXD0pj3Kb+N9ra21E2HWN/KpS2vsSJunRo93y5l6fjmifQOuys5WAG/HrSOkEG2dQmfpzZh0u6x+LixNptTSg6cIHBK0m2p7KCwN9os+YpS+7MzXdKN63myjWdTbEoGYGssrfxyOF97ozBX01vqiZfhtuoLVCjcuXaOC1fTbbr3/OKUq9Jprs2FtpndAvV6VC1C0uj2Wm9bv1zZm6sboP2qzNaEtGHhEoOMHPlWBX16HJQ+1bIw8s87HxT97WagZUcfB051CMG9lpq5OR9r3lW3Vtll0UbvQ+it592ep7Q1W160Jos4PuvyYXE9CnkBgqO505KWSuxUztlIn54OUrNnMyXoNgZVJCkbe5MYJIvVZm1cK4cx7HmO7wI82i23eRoJbMRfW+y4a4hUs5zToVxy+M5YelhCZmZyjqkhVBt/MD1vMjjDrnCvshZ5c3nrhhOz8+NlQlAlGsMCUeTe1mXYaZVkXu7NGMUVd/PlhJsTOh2fNtPlSsElLEdPizl7ZAPa13umWuDMHlpH1O39NelL3p3o9UpcMP3ivEmWDTXwNTWcLe8gkF7E5TPzJgiDqFXBsmmXfJaXk1slXkO8PmT+xb8JN7LLK1yXS3SjNoQxvdRlrKFBElrHspzx4U6YbOWOFYJwvz8pVo/Hy/kiyeaxGaqkeXbwhjEB65uzBp1VZroijrGiavPu0hR72ZIyuyfj9fJ4Pistu+SdLJ1xebTtRH0H2rW028ASpSjCLV2bV7xtdcc0LoW/tPPcIpgpTMaUd7Tj7aE5Jm5cqV2woYwE04dGaozswEpzVNosbqzMTgRvIcldpVknS+IjXiySDj3vuInsi1OJ1cXzleXWR30ls4WTiFaVX12cms0OtaCl6mJLxUl35nkyVdr0til4ZREEV87hi2sshss2xOyBm8vBapCccnCSjeOTB2NY7jZHrPKsUBI35H5xbtcbZqc3KwkTDBXzhGRa+eYRFYldhiorG0pyE7lFJVq2PdVVPZHsFj31mZpxmZv1i4uz3iebnaCwou0BHeM6qUw4K1dLr8pjrrys/OmBPIr8Yt2Lt2wfnVZ5oOK5sjo7Zw2PTqZ6csSj2E2NhA40uRaGlPHPbpGhKJNnPCiF82VzxCflim+mXSzXmxYFy41EgJU2OdQn/lifWuWmursrPwuFTM0dhq63/Xx6SmvBk0Kn5CanLYdtb8cl3x9E+0inqu6hW//EMB2eLYloc1yK3sbYcw2qrnfb/ZpUBLmlo+mEiHjo07J1aLbtfp/Mtlt3GSUGLsyGo256K5ctawYcIyoypGN8lI+qJrd1lp4qfeaZbr0Ole1upwfDNAcs7jR8c+HXmHYNbT9xbuiVckjrsDW72MdTS1K7tRkwClbv51NCVTexcBWMyqLmLsASjTvKe0M2a8EXiEJqDklwVgkzRMOGpyyzizBZx8XQj7xUKS1X62h/udF32aahssLpTrwob7f0kg+kYnHJfLvY031CkVHbu9dVuepr096sa0lJtL2c8SGIrgnnzBfTlmrWQRbJh4U+pyeZP63X1uSKEZa2u1CklBinWdgy18rc7qaXg1bdbmJeTHBOs7pGnpF1ARxldZ0TRZpjbgwWJ9o+5d3pRBKmXBqYdyFQqrMbR459dQO4rvW9XhEPajyf32rbAkw/i6ViKy0Xfknj5Mxd271C9xPz0t/ko07ER0u+0u1wNC/rKzbM0Zm94zfohHLyDMzY/lbyZn08tdI5bm4zDzDZFSQGz9EZJQsLYyKFaUXiFxNOo5He79VQWR+6LOXk2fymRqraONg6qpKcvs5Kr70ka6/uO2OjurN9sA6P+MqWdszqslvILZqzuxNFW5Ir5NO96YYrSmHT8sDdoko87L2j68Y3bu6i7UX0/SUcinNnRfIeowWKuZaP15hM13th78mhqe7inbLi7BTVZNnhT0kjb5eb84HH17Uz12dYHmkrS5pcbE+NS9U5Tjd0faQVx7zV1HHfWcL+vBmMQObN056YJEU+udE+D4pqaRQ7L5qg3mQhD5xznXvXLLt2rn5xeWO7byeeaywaLdHJti5b1W5Ea0+bp+q6PvuDPZHKHMsBNgeTWZ2GsLGMHYnaK/tstVYOUU4G4UlZelYlGovrVqDxXdLszcMJ3zSXGSUw0aIQK31CojZ9bDJf0nNW6HyUUza76/bSVmQocFRhGoq0XjYrgSUPJ9EwZ9JizgsJlc3iwaTPkg3hENLlxV7a1BYtuBudXWQD12l2GmxqKRLWhL13E0vQYm+L70PMUzMorMWVpZSeF120HMSuqmx1Zl3XVUfwBJkKa4E+sCd8OUEb3vKoFSFvo572zKRe8uvjZOW0x6G4lr2SnA5yhjcDR56FIFFslj2gc3OrTiwYp+4xt1rIZ8uf1jbpsZg8uZwsP3Yz0YkqnIllAw1QBV3I2m2veaw+r4bpMb4d45Yp5yvc0qIynGAiva/J9UoRV6sSZTEA5Z4JfKWofa8tZsaGF3lqfj75on1JZtft7dQacjL4asW5wlq1VsR2JhWTLA0i88p7IqxNt1A6JdGyLeduFNPoYkFxAu8Xh6N1dlR0SGqgcJeTuWfXvVRLrcmcML3lY5rXbt3Fl/VYr31/axkGmxRxsU4MJsxdL71d7T7cLA7nkC4snG7hpGNSBqkznBWwQWSJBREYVNP6Q4S2BFbBtEJEPTDsKSl3Xu73ijFQcKLGTTV0BZq+ZXy8TTM3Vy6KX3KbjU/mkna+OIwymQ3UEmvcTm4BMQPg6lxEu2KryepQ74SqPR2Hqxa3QTTlueSwChduVM2KjCXErTUU3Jpcm/qiKURKhyaKAozbGz2Bb3QC0Pk8LJh6oXYnwnEzDqbZRhd3mTsx/BU1U8uI9a+3dsdkm07FYn1H0cZ06lbyNJSz1Dj6S+LSdWQ07dwBzzvfm+CVQOyUsgyCnSB0oVhCzMhYv3rcfjjIw/nUJWZ7ZXgfXWAJSmqB1QnhWpjw6Hrw2Gu3PceLPuNQd+cdb5NqTWs+5W5Ko6YIQrmu5WBX7mp/sWPamWo77LzXfBAMWQeONRopcZXsjtnJnu6IdKLaA1nXc5ufttsIbKeD4jBVq/SxJBNkzcxlyvcb3xrUyalTur2gbsJyPYX0J0PXdLPe5jerTota2DuRLKg5X5hQZjQ1D24cTOrAJ4eTQeywYHuQt/OD3aP0NCZpscn1G8BPMaNWGB6uzss96JtKsvGgcgCRXV1sS8jMeTZcO+zcqhlTMiITrO2mSIp+OfXpPENPm8l1wK0lzmOavcGW7k3gYsUqRK+Bjk3uZiGj1IGcWN61jQ2fai05FnZ0MpsoTXk7D4U5t2WaV3XQ+wIPrjIreRufwnKRCPUV36fNsiIjDGBwJMp6T9c7lj1nOhGCcibFhM/A8aM5Dz29nvVHciWHFc/BVicOt7R8cqLTNKg3K6dyk82BnNjBbn90iaV+Ulu8OQOGZuxZg2dEwtgMevRu2vnqrINUI9z0gPLlQltiA62zPMutui7Smgs2AEJrcyFo54tYXKH6povcoOj9BdljvsaLS6qb95mB4hXONVPPZDn7TOzQebqGjRNJ0/Mq9VGttX3Mag+q7hMTzEG9zZZhXKlvxPRw4YmwD3h9Nt/6S3LqSHMC9/HNciscz1NR35e2WNmLM8mtmGVmBYYyLVenU47itGiyu0W7SrSgubpNVzOhmDGVPpVolcLI3XEqsHsR6jz1pYjaaVzE6LUF6AyboIoNSJ9nQCu4XVUPV4PIp2bqWjt8umO49Da143UwdIXuMquKBlv3LAWSpsysXQhPYo0Sbjp3IvH5kdmrwp4LvNQgVwQX1AtUP2wXs3IvYj7svQ/dSVrbMeEFu4HGFn3pdmcTyPpJ7E2SRxcX9rReG4C4hXNa9PN+tjjaIg82PLGb50y+Kna0zXdbIlGagxt07t4vuIVOOdLMhLVXY0S0BXB6Oi9IoC3I5uKwC4qKqGRxUlYmv2QtPNzcwEKLpWhSNMMRm93K25E/2ZPVwl7EJ07SMh82/KEJmEhTumJvgRzfrqZTen0gZYk0SJmh/B0bL9HW8oAc2JFLCNxcYrhcuk0jZwbRMIwNrW4EWW4MzGZRXjWngBdvTJXZixufWz3JzidhtiM7zUrn8QYOj9Ga94OkWAbcMrLtJCGyHFevtigScxg6g5gLDAHaYaCJMyrioSfLGiNtZ7On56f7l+CnVwylWeL5afw88P6S/6+/Hg5vcfn2To9gCOr56f/dG8vH28OPT4H3V/7A8V/v3F//qqj/eH6qvBiK9XitXKdt+P6q8p/ez375z94cjzSGx6ft8evltfn4XtI44f31dpz7bd1Uw1tdpO395TYEvq3H/+ZSv71/aHi6K5iV968WH2y/vU9tirfSGVG+f1zOgB87DXi/DN8/BsCNA7Re7NVvBE29gaocVX3/KDVaYfwq9fTb/wbHLZHE2CcAAA== -->
