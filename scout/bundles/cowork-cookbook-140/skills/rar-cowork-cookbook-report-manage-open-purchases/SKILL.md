---
name: "rar-cowork-cookbook-report-manage-open-purchases"
description: "Builds a structured summary report of manage open purchases activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_open_purchases", "rar_sha256": "40954f247e4ebccf6c7716742bc301fa03dc5485fc031ff29b5da72574eedec3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_manage_open_purchases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-manage-open-purchases:1ba366caa5fcc4c06f76c524dd5838f7f943ca789b2fa18f46f9b84f63e74bde", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_manage_open_purchases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_manage_open_purchases_agent.py` is
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

Manage open purchases Summary Report — Builds a structured summary report of manage open purchases activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-open-purchases
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_open_purchases_agent.py` and embedded as the fenced Python below (sha256 40954f247e4ebccf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_open_purchases_agent.py` first:

```bash
python3 report_manage_open_purchases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_open_purchases_agent.py   # or on stdin
python3 report_manage_open_purchases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage open purchases Summary Report — Builds a structured summary report of manage open purchases activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-open-purchases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_open_purchases',
    "version": '2.0.0',
    "display_name": 'Manage open purchases Summary Report',
    "description": 'Builds a structured summary report of manage open purchases activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-open-purchases',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-open-purchases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd3ebb5636d58dd2c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/manage-open-purchases'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-manage-open-purchases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportManageOpenPurchases(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageOpenPurchases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportManageOpenPurchases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eXPiWJbvV9Hz/JFZjdMS2nFHRzwtSCBAAoTEUlnh1L7vElpq6rvPFWBn5kxVT3fEi4fDBqR79nN+59wr//5kNLWflU+vT6pjpJBoxHHgOyVkpDbEZW1WRuAti0zwC1lZWpeB2dRZWT09P9lOZZVBXgdZCsjZJojtCjKgqi4bq25Kx4aqJkmMsodKJ8/KGspcKDFSw3OgLHdSKG9KyzcqBxBZdXAN6h5qg9qH6qw24uoZqksntcH7qIpZOkZkZ21avQDJTmckeexUT6+//vb8FIDPT6+/P1mxUYFLT/ubtM1NkgIEbd/lAMrYSD2wJO+B0Sn4njulm5UJuGQ7LvT49rlyYvcZ+tvfotYoveqX168p9Hh9fRp/9k0K1b4DNDWqGthpGblhBjGw4AVi4tboK2AycEH68EeQei93yu+cshz6x3jv813Ii+fUn78+AceUxujRr0+/QFkJ5JXN+Pll5JJ//uUlzlqn/PzLdz5VY4aOVY/MgNYvb4/vD7Zg4felgXuT+g/A9R470/n69INx4+uu92gnoHx6CbMg/XxnnJfZ1UmN1HI+//JXbC3fsaI4qOp/ie+vd8a+Y9jApofivzzfnPwbNHkY9MHzr8XmIKz/jiVg+bu4Z+jhqL/iffP/f2MdBynI2neP/ym7PyOY/AP69S9t+2cEz5D79Yl34uAKssOMnVfo9zd1O+d+/WR/v/jptz8A6/+VjZqBcrhxeAPFGLhOVb+9/fqpul3+9Nuvn5oc5JpjJG9NGf8Zzz/z603OTx58rPr8My2Qr6VRCuoY+sh06Pcs/z/lHy+QbsSB/f169Qr9WC/jawKNRrwLvbvgh5qpgK4/+PGXpz8AOKR3PBpvgyr/j/+ANoFVZlXm1pBqZU0NgQDXQeKMyh/8oIIOj6L+pq6W6/VLYn+DwNWx3AFEGE1cQ2JpBDEE6mGM+GgBALZv/9e6oeUX64GW8B303u6I9zYi3tsH4n17gQ4+EJmVgRekRgztme0WAuvSehR2SwsAnl+uozygS3DHmz23HLGmamLn79C3fybg7cbrJe9H5b+mIBoGCJEN1U4CiIwyiHvIGNHJ7GvnC8BTgCBlFsemYUXQ+KfJX0aPHH0A1Hc/WaA9OJ1jNbUDxZkFlHYDgMHPINRVFl8BGo7eq6IgjiE7KIFrMgD9I3gDD7+OzL59+2Yalf81vcMvBt37RwWDBR8KQ1++5KXjxoHn119Tx/Iz6NPvf3yC/hP6Z1Q35qOMLegBN1+BFI4hSVVkCNRjk4BlFTQmAwCbW7x+/+MehFG7FDQ8UEWBGzg3YsDte/BHC+6ReQ8LsHlU0Skfkn72G9T6wC9QUANvgcqunr+mI4sMLC3boHLenXgnvrv+Pc53OWNMqocPQZzcMktua295NwbTykr7BVq60IenHi12jKifVTVIVZAOtpNaPaA06u8hTLMaqkC1VG7/DDUVMHXk/M0ErEfnJACSjPobtOG2oLtlMfgzOugmHlBnaTAG/pGo98uASfkJ5Bj7zuIFkh3gTSg3SiP3S5COt3Wucc8I0NXe6QFzA0qdFhpbuDPG6FbHt8zb/OmkoD4minuPh742KDLFof9vs8eoGCOK+7nIHOY8NJcP+/M9i8bZaDTqPk6N/MAkcS+J79PBO5C8Q+zXNA6A58v+7/eV7i1x7mt+MGXP7G/8xxIub3yDGoR/jGdZjilrfE3fsRyoPKZyNcISqNJorPnsQ+B4911TYL4/fv/e16F7Zo1Gg5wFPjLjwIJcx7Fv6V375Vg8D5+DXHBGr4Jst/yfrIIAd+B4wB8CSgQgKYHvbq6TQRGAWeie0R/Lg3FaAlrYjQW0BVXivEDHMWlB4lWQ6YCRZ1wDvPDpxgpKHOBjoOKHhyvfyO/KjPPqQ0HjEYsf/f+4BdJvbBlA2kdtAZ6GbdTAky0IASid7h7XDy0fkQKqJmOe34h+DvbDUujHlvP3sb6Aht+hHQzYY7f+wTUAlMukuqUa6KNRBSo4cR7pA/Lg1phf7r313rw/dHn9HyP6539vir91S+3nuL1Cfl3n1SsM3zvae0N7sbIENDUryJ3q0dy+3Evqy1hSXz5K6ieedxe9Qv+eXj+xeKTzKzR9QV6Q8dY6sJwxXx8v4AbuC3v+go93v6Z753t8gfgsAaAyur0HwPrRPN6XgA7ilY43Lr43k2rsQS1oezcMuzWDjxx41AcwM/XGzldlP9TtaNMY0XvAPrAW3EpHFLfHOc1zxu1LPKpfOU+vaRPHz0+pkTj/y7ZlhFKQocAR40YH1AoYeerAuX0zGjsYvTF+/nlLptw+GPFYTtnYEAFGBh+gedPcLoFaY/15oFU55TMEtPUADo7GtGMNjl3fBMZVAE8de9S+7vNR3fu2ZhyxPuav/6nBrYwB/tjZ61jNoG+CWfkZ+hh7n6H3jchtW5c2YCf26zhyjzaDpeDtY+3HjtN0nn77EzUeE/hfK/GAmDuoG+bYEEcT/8QmwK10igY0YHvU57uB3+Vmd2F/3PSs73vI35/eUWT8fJ8G7kkFCP6laW20973Lvo1MjZH0NlPdzL/Nn28GiP3YTX+45Y2jwds9P59eAfw4z0+AGMw0YKgebjvlp7smwITvk+uol1F+qcbpAAblBTiBnp2P6kcABH8QMF4O7Nv68cPrX4y7f44Ir1PTwEjSMgzCtSzcQkiXIi0CxW2boDHapdwZjlkGRc9M1DWmtIuT7sykcZfEHAo3bQcoUIFESIyHAvB09DxQ/cO9/9b4/XSnBW0DJUhAjCMzAndRnHJwx7Qsl7QoakpSOGpaGDJ1DQSzLQKngfIINnVddGYStkGhBIWD3uhY2MjvMQTeFXp7H7jfY3EHhTcAoUkwqosahkVb1BS3Z5RBWg6GmJjlTNGpTWEOQswwl6aBMvbTB+kjHmO47jaPWQrmPzB9XUc5vz/iO2YeiYOVC7xaMvcXB890A0Ypc++vJydk0nUw7jfUMZPX0ZGd6HShVGSzY2WxDohVm5/OkhupdWHgoWQhpalsZG5BsltUdUgTVXVBK1cHrJgvTgp7lFMbs9PLxN1uZS2a70KBWp84Ut8sT6u9Lp56LTculi5cdWptBVtFPy5W6nVAexIOyGmeFntdRVdFFZFZo6tFlU4N0jie/Wl6FXrjoE4pkNtsbZfaPl7l6WU5FfVVBHcrV9a61VHVyYTojwgu5ijtLuLJ7LqOMDvC8GaQG3jj7q5Ck2v7gI7KOL6w0/qwjFW9OWvxrjQ1LeC6tAwlyi/b4kC2UrEqI+dyyJrMkQYZE/3NTN+QlyGEFdXqtMYuiLVABplW9tlyHdUy24X+eVH4JqNPO1MryoNB9POu9+2jbphOiGiX7WIxFdzOiRvdIAZ2Iyj9MTkoKbMc+iuOtOm5EDSxukZcmLO7qkCHCG16KcNWBFo5jbWPmJ7fUQbDlCXXIYgSUUinCJOJsLyq5do5WPoKz8N9nmr8NlZzfbUm3F4rNPtICCUvDTtMbmF+vp4nlYCSRjgtWVTaNWmgJtcjf8opezJVDlN3lfuKXgeirnL2UuuTKl+F4syjD7NjTaNKmZ4sWRcGnt7gueu4JI2KU6szNmY+2R55eS4eh821onvRUuoj1iyBKmWPiTrpDqsg1y+rjq7pdc2euPJ8WHpruNT1C3dR+D2MTKWgFLcTyWur2ILn6hH1z2GvKTnBUWqHnWI1rZfHwySbTPJE93X9KKQImnJcp8DraNg4WY4jy2OvEYCasOg5UjjqpaJPl4WihNtuQh0K9cr5Sqe4PgJzUhcSeuCsdvUW9tpYkaYwvNlGAxu5KRgbdFPEjlUtRVSGLmV6meQqXigomuwXK2ItH1UpcqsFWx3Vraf75Tw/nijNqamU2ZHndaftWilXnFrqemmhHGD2mub16sgMsWBeFNna1bhJMyR/XGXBucsQzwqoar9QV22/yzrB6ubapgiSNUNqRIsri3XY6G0ZLknYCsmLPKe6MAusZS/1exkIbNqT023VSWFHnXIhigTd9xqmcVv6fBGx0yqxlTVsw355kkHVtYZydYVpKU+irFnrFzfMF6l8OTh7+RLJ+2nqcgfROiJsKV9Eb7Wcp/BucyXJdZDi5VU9zdFFRBdRp/UMMkP4OK6ibJoVJeHgsUdj6wN/7Ot5V80m8GqtSifBUShdPbCwYWXywgiGPD5hropIzUparQYcsVLBJrBQPXChPpkWpz46F1dQdINewa3t5XPvIngXfHGago3XUc5tZxVsr+xh2wnX46zddtpkspqr+b5iT9t+oc7dONa0FQUi1DeuaG1am8CXx3p5vlooNw2Iw3lWWXLkFey2DFiDrAYp5JINx7oHLZgUiGKJYpeummnXUcnsINCwG5saiWYEkU9CTTSK03qytR0NQ3hSSga6JwcxDJYwfz7Zh7NESZersZ+G6CLBMs3FmlmIL4IryeCRK5MsK5Ha3GKNC7ERj1dnE7X9DNlWdLRaKW1xiqp0PogEl3U+SwxBgaWMvLdOWXG9EuyZlRWsUqMF11xPFLJOnDPSXc5rujpE6NEQV8x2Jy53VDB3iH1S0hwWHnSRPi775kSHXsSq86BqoxnamXbtM9S8XrTMmpN1f89GRcwWSN8tTTPgOdwSInYVXHgZQdr9Zpmi5YK3GkXBpfNB2xyuG6boj4uiSfIBXRya7aYTNiQJH0ydtFOzpxSx6DsxcW1YtFVVO8cmMm2mYaXOvJ22OJXGwMzgOuPqCU6EE5Jl5pflRMMWdHdxt9eohyfzxthGUzrb+sLu3DTX7QrFc4aRKlGJ18OO8E67kz9HyErnJEwTVela44mXaOrE9JaNN9V6mnFO835dNP0q2hs2vtd7Ppfn03JzsrhBQnZEmFXSNNiqyaZQyHOPCxKt5ZG0dBMAc1bROaS22qHhMEePXbFHvZwzj4LuLFu+she0MdSJKfDE3oPN8Gg658lGKDSMC0yllhPqKJTCGZnKbkQ7h4WVduIsylPxgoVmPjBL9DwjgqXflSwzbCyqQaYaEVEOqlC9GfSXllraZ4dZ6iorBEaCC7kYhMSVhCOPXkarw6mZADBOzju6PE8OlF/4/qVZ9+h23WgBmUmINjmX562qi7xiUM2VN6IoYYNlmga+Oq3leaXq2Qy7GlO94ZheYbhY5s91ORPWnh1G8VXQBp3GWgvZeJEau5wuSjKjEawcmZbEMT4y5zu12feHfKvHuJPVhdeyO5IZJmCmyDVxEGpyk2snTmWShl/KU3FCmvUlOfdotPEFU2Fiy9GSpsxrJtnEK1TyKnXYb3KOgi9JHmqBdyUQJA+ErreK03R2cQ5L2zGIvBDyIwPrtZ2ey7neEIusE+cD2LwwpJEO/lRcuqoh2vBppgTzNGs1r2jAkgqx85gjYZdjeHPb+6sZo9V9WHtNsj6eI7IQAm4pl74ssNNLzA3eUnABnRPylD6Q+6nMJZ7QH/YTyutRfIHS5rVeLFltFjP8vp2Yl9NirTJDoaLrrNigydAjWxveYmnaYCcxZNWWWQgUGh9cRJ3jToIVmmGdwoN9ntRHgJHOIeljanNakrFNogqNFru1shIZMXRKuSbbI7vWVaaaz+HBRK+6VUrnxWQ55fZn/5odw2K1rlEnnUrORlLZuXzkI5K/xKt0g7K4T3eEIA1HhCKMw1rYr0Bd7VRfbeNE7Du8OATnMgeofIhSTgzPWijgS17J1iyy1udTkDQKADPbI71lmITiVd53/jqrVi6R80HkU/tjnomUHzMHy2MihiONDe+nWsR564OmnofrJnK3ZiXuNTsGQ8S+3GYx586tUrfP+0oUamffK5eqZP2pxEgESHTb0WluRsR6I56FdloLFKuVnM42HI9cyqIbWCzrTQQ1GG2F7x1eXMVnJTgumFqTa848tGg2gXGKWF/SHXYOgos2K5ytVfvc9rIRw9jSGm2fcbmLRIl3ymp5Y0fy9pL3cMlOYV6xds6aaL2TQi8WYdhpB55c60trTha+Xvl6ZjV9IW4UKTjDmhqUcZila8VdJGGLcHrroTSythxFPBXOYJIbRGMl4WwE/malGoHoiNYhx4381GimtQ6ixKzsPj9SqL7CFH7nginCIhJiN5fri0gO7QLrUuE0v8yUptvFGWfMa00SGDo5wtZw2XFRGwpFe7zMMtOLWZ3RduaV2OBirRkgnaOCt4VcLofOBpt/m5FIKd5dcV/nONRKpaXIoosZ4qK7PTanKHPwOMv1hdBEZ2xXTbjkMu+vkrCX6z6iN7ve8Ok6wE9W2iCzIpRZmfLqFW7wKqqKvVoYAb06HdmTLWZz45jN/MllKeg7esshKRgFLmE27214Z2RnpIlSV9L42F6mi8x2e+V0bBCHTFgKJffbAyVLgh6lFM0Z5jboO5+cCm3eLAd0vm/Ytr8mtd2cjaOMUSuP3+y7FOHn+kawa2x5FBv4gPPFkJuaYvDlZdqzzmnJBLQyCX1Nr5ITI84vCUIphactbZigVtMwNUu91NOQnWlGCKrijDmzZW1bQqmrIVzyHtq4VHbSLicweMTDpYF3l7XSb3jb6kIu8iJnOqUdBNf3CTkZ1hWisJndmha3C2oMACjfDtcuR22491tzU3gFsdq4AA6pmeLvbF4blDCZZGHPuLOr5xJLmee3eKw7JTZzz3YQIqzJLKaHdKfx7hIWJmHn0pK+XQlIUjNns6GKnsbwSxU60cJH51dW75BZtSUsZZdTyQSGs6VrSQbYHFIefAU9Vomi68JZSSRxklHQxTi3C3Yzp9iher7cMgOi8d7aIPA57llbZAW35yL1dnyVVnVFgGaM4JS1kfgDP2H6uVJIkdCK0hIO8C2PhauZxdWp0uONsMslKrosPNyaSULV+dt6cCyE6sN5EqFS40v7C7uA5dD0Qy+NCEaBCReM/whFCy2GnHamsoxO3SRsw/Ti2rbvtkKLKMcu5qQ2XW3y1HFnNiLyhV9tJFoetNMhzGYCScp2P1tMlALWF5PKtfFuJ6Rq6bT8esceLh7puixu8yiVEovDZl9v1VldAUgSqLOe95fSmMziiUPt09Mg+jbuGFvFsocNnKbWOp/5CQ7217Jap54+0JcEPzF7DlOEOcXtSXFiC8Pc2q4XsFkL+K4CG6N+tsVAiYZiU8ZGs7SKhM89kW3aHUGveNZkTVUahmrRRSk+PZNDN98u0N1JAV28npttPG8kYeHOzqCn9DMxOvsNfto19XnTw02dn5DjMvfCgTU9lrnaW8nzMo1fOCaviYtZ06Y6GG/8I7wY1rhy8KWcdCO4aqoVmDgo4SS3MVYRkkSfrEFkJlR7iScTyfe7ROesVTkMB3qC84RZBqCEDIIkEdMmI3lpUezsyHESRZ+Vrj0bk5AJSWvi4cc1vjhQQp5dmaNRd9RZlondmq0qpb5Oy4bkD8j1omN5njhdeqz7Na8pbuFPFlnluxnlcM5GpJkVH6RTeI3Y6YU6RzuGOG7xarYgduo1ohc84mmHi2xrZXNdYGv5WltLGzc4IhAHuFkrDTwQ5LSnyqu+J+wp1SNCtsVpyfIUpFkknougmeTqMCNrLlwurn3vCKjHkXK5Qckjppx2FkrKkxTfAk9dF9med+z9jhZKEswC+1a8isJ8x6fxKpzG+HWi0ja1RIuTtc/IS0Et+qs3QUoamzHIfN6utJg+beEpkvdcEICtfDXFUGzPORfe7s/U9AILddtEaEgU9P58zu1FzfvIEt9629l1pYnnZH8NBhZRKMvXNDB/WHWqoSiFIqm5OFjWsWgF39iHdkilW613Wo9WFg59nMqOwNPX88DSDGhO/laYZVyF0UMWZG4xzh2eaKNqc+DX/dXkrQRTr/nONvpZ328tqRPoDYa26XwNy1NTXfJrWJhLlF8zVT9Hm9POHjDbN68kzurxpJteJm013y22SpnKXBzqfnfBMzhWWQ0m1MuhdLfUsWcUe9rjfMrY6bLFZtlazVrkdFnuKlk5nSfMVSkOSkZ7VGjOJtaWbztr6qOrfd/Qx04lSx4xaXaxysV0aDOGYf7x9Px0e3j69DpFMAR5fhpP5h/n6//qAaw3BPnbgwtGYvTz0/+7c8L7md3787bbWbdj2K836a//moK/PT+VVgCUuR/XVnHjPY4F/9sJ6Jd/diI7Uvb3573j48Cufn8YURve7bA4SO2mqsv+rcri5nZUDFzbVOP/eVTjvwJZ4P3pZkySj0fzd2Hfjyvr7C03RncG6fh4y7EDo3YeX73Hafrzk92D4ARW9YaRxJtT5qN1j8c94yHp+Lzn6Y//AhtBIH+kJgAA -->
