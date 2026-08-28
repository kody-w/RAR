---
name: "rar-cowork-cookbook-audit-analyze-product-profitability"
description: "Audits analyze product profitability records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_product_profitability", "rar_sha256": "9986b320a3c586268f3d22f5d9cca468edd7a68bfcbe4ffcea53cd7e03b8d947", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_product_profitability`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_product_profitability_agent.py` and in the RCI capsule.

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

Analyze product profitability Completeness Audit — Audits analyze product profitability records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-product-profitability
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_product_profitability_agent.py` and embedded as the fenced Python below (sha256 9986b320a3c58626…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_product_profitability_agent.py` first:

```bash
python3 audit_analyze_product_profitability_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_product_profitability_agent.py   # or on stdin
python3 audit_analyze_product_profitability_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze product profitability Completeness Audit — Audits analyze product profitability records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-product-profitability
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_product_profitability',
    "version": '2.0.0',
    "display_name": 'Analyze product profitability Completeness Audit',
    "description": 'Audits analyze product profitability records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-analyze-product-profitability',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-product-profitability',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '96fc385f54bd78d6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/analyze-product-profitability'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-analyze-product-profitability', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditAnalyzeProductProfitability(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeProductProfitability'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(AuditAnalyzeProductProfitability().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716a5ei2JL2X3FyPnT3WJVyk0udddYaREARUUEQ6OpVzR3kfpNLv/3f342aWVVzus+cnjVrrMpUZO+I2E9EPBF7k7+9WG0T5tXLpxfFs7IZbyVJFHrVzMrcGZN3eRWDtzy2wc/MybOmiuy2yav65cOL69VOFRVNlGdgOt26UVODeVYyjN6sqHK3dZrp3Y8ay46SqBlmlefklVvP/LwC0tIi8Rov8+r6rq7Ik8gZHt9HVuZ4MyuwoqxuZlWbeB9tq/bcmRN6Tly/AvVeb00C6pdPP//y4SUCn18+/fbiJFZdv5lDP4w5Pmw5fmsKEJBYWQBGFgMAIAPXhVcBu1Lwlev5s+fVj7WX+B9m//EfcWdVQf3Tp8/Z7Pn6/DL9k9ts1oTerMmtupkMtIqnitcZnXTWUINVN22VgUXOaoBfFrw+Zn6VlBezv0/3fnwoeQ285sfPLzkwwZrQ/fzy0wwA9vmlaqfPr5OU4sefXpO886off/oqp27tqwdAB8KA1a9fntdPsWDg16GRf9f6dyD14Ufb+/zyzeKm18PuaZ1g5svrNY+yHx+CgVdvXjb56Mef/kzs3VNJVDf/ktyfH4JDz3LBmp6G//ThDvIvs/lzQe8y/1xtAdz6V1YChr+p+zB7AvVnsu/4/xfRSQQC+B3xPxT3RxPmf5/9/Kdr+2cTPsz8zy9rL4luIDrsxPs0++2LcmSZn39wv375wy+/A9H/rRglbyvnLuFLamWR79XNly8//1Dfv/7hl59/aAsQa56Vfmmr5I9k/hGudz3fIfgc9eP3c4F+NYuzvMtm75E++y0v/q36/XWmWUnkfv2+/jT7Nl+m13w2LeJN6QOCb3KmBrZ+g+NPL78DjgBcUgEimG6DLP/3f5/tI6fK69xvZoqTtxPRZE2UepPx5zCqZ+D/lNuVB3CtIwDscxyI/8nDk8W5P/v1P507U350nky5sCb2+fLkwi9PLvzyHRf++jo7A9F5FQURGDeT6ePxc2YFXtZMaovKq73qBgjFHhrvI6Cij9OHWZTNfv0XpH+5C3othl/v1Bo9OEpmthM/1YBOX6c1XkIve67IAeTv9Z7TAh1J7gCD/AiQ6wew9jpPboDfJjzqOEqSmRsBHgdFYLjLBph9moT9+uuvgKLDz9mDUNHZozrUCzDg3ZzZx49gZX4SBWHzOfOcMJ/98NvvP8z+3+yfzboLn3QcAbk/PQIsFJSDNAMZ1qZgGHAWcC+gj7tHfvv9iS8Qk4FyBvwX+ZH3mAwiNPbcN7CVDf0RWeIz2wMgA4DTIq8awNKzqHmdbf3Zu71A6XRr4vEwB1XJ9Qovc70M1KwmtMBy3pHM8mZWgzCs/eHDrK29u9Zf7epezbwUpLrV/DrbM0dQNfIE/JrMvA8Ck/MsAvC/h8LjeyCk+qGerd5EvM6kKSZnhVVZRVhZTx2+9fALqBZv04Fwa5Z53edsKpHeBNU9QR7wgEEAGefp0o+Tz6cCDNjArd9038dYU20732tc9Tmrn8FvVd69pgNThlnQRu5UEv72DKk6zNvEveMHLJ0kPb3gPr1yj0H6nzYMzLdNwr2mzz63CARjs//bfuNuKc/LLE+f2fWMlc6y8UBwaoompB991KR0UnbPlq+twBuRvPHp5yyJQDhUw98eI++4P8c8OKqtgHKZlu/ygVUAwUnuPSanGKuqKZqtz9kbcX8Abr6zFHALSGAQ4FNcvSmc7r5ZGoIsna6/FvEnThMqIO5mRWsDZGa+57m25cTAqmrKqyfwIEC9Kce6MHLC71Y1A9JBHAD5M2DE5B1A7nfopBwsE6SUX+Xp1+HR1Bo9HAesBV2n9zq7gNSYwqMG+Qj6m2kMQOGHu6hZ6gGMgYnvCNehVTyMmRrVp4HWxNeR132L//PW11C+WzIZD2RartUAJLuJXV2vf/j13cqnp4DQdIqO+6Tvnf1c6ezb+vK3z9ndwndCBzmdTKX5G2hmIJfSRyxOlFQDWkm9Z/iAOLhX4ddHIX1U6ndbPv1Db/7jX2vf76VR/d5vn2Zh0xT1p8XiUc7eqtkryJAFiJCo8OpHZfv4zLqPz6z7+F3WfSf6gdSn2V8z7zsRz6j+NINfoVdouiVGjjeF7fMF0GA+royP2HT3cyZ7X90M1Ocp4LsJ/QGU0vfy8jYE1Jig8oJp8KPc1FOV6kBhvPMrcMTn7D0UnmkC6DsLptpY59+k773OAsc+/PZeBsCtrAG63ak3C7xp55JM5tfey6esTZIPL5mVev/ajmViexCvAI9pqwNAB91OE3n3K7AucCOyps/f78wO9w9W8ojrugGGWtWdHZ558qS9D1OrmwFmmbYVU0l70D/YDFlt0kyGN0MxWfrYxUwd1Xu79Y9a74kMdLj5pymfP8ym1vjD7L3L/TB723fcN3NZCzZeP08d9rROMBS8vY9932za3ssvf2DGs+H+EyOiiUsm9nks13O/EsXdcYXVAD5UZRGYlDv3ZmIqoPVwL7T/uGygsPLKFlRMdzL5KwZfTcsf9vx+X0rz2FX+9vJGNU/nPTtIMBzk9Md6qpkLEOJAIbh+BCO49z/pLZ8iADuCxgbIoCgSt1EEslBnSeIITvqoiyD+0qUcx8Jw0nNdwsJJ23dsD/N9x7OWqOMSHoTapEthBJD3iOovU28QTWYhluWQDgFjLgWmOh4K2ajjwQjsEqgHLSnUJ0kPAwi9T40BuT7X+ljbBOR7mzth8lzyby82joGRG6ze0o8Xs6A0C0dFWwrteYX7dH0l46bfaXojNru2dQ8lbo/qYJtFDx16WO+wbSwwfKrQRpDjgTcuTuE8l6n4Bh3EqhccU2yIGoMwyhhouXOyfYPegn3JbEX54uDjQpkziVVscVyJ0KExSS1M66YcSUSwzXKrtC4D0uhSVNL1dlss0yOS8QQ8VDK3yzVR0nLtqiTOcUwEjROKA+Ury2UWXHkYHtM23ZVjfaqXSRmLUrpdcuUmpzZmDnk6hy0OWUKRvYJ7R3FB7i/no9TtRAeKan43r84WlytUWSLxVWKTJS75Kz10ErhU6mS+sdRBC/tGpwIBX8bCrVPPe7qw8osrkmR71aNcEE7yDm9PRwsLLkxcOFtbTlp3EPQTbJoDxcaVuE1dM9b6q6upEELxOYwe15Rhz0PQPkVu5yBNuRXXIkOOJa+64S5an9PhrEFBflb5dXdzgKWc2zSmKBaZ4a4AbmebNriBuXFi7gtZeMJ0YpnuYK1GyBgrZfGiu6txuzxtkRNpnxP7KBkNp7V9vs6xhZSLhlYzCG4FfSURHZQWSsm3Vz73WQ0W6/ZqZUukxi4Ldof0gabwzhYb0tucDzbpHDTpPEoh/DXT6cPqguVcjds3fePM5YJjxlyUKeMgQ8ZwGxybp+CMN4gIbk5eFUqV1e2b2C9Rs2iCHTegnQfzlbxfpdc1NG76huPigHao9QiagQMpz+3jak+a2LwLjTN83Z9DbrND44xzObX0Twcb9VWyQXZWqVSIMfaHcb/ZVKf2zGyObKDgmyxbCfXyJlTTD1y3tyqVq4LWiOP8grNJx4rUdYPZaLeJrXlspAGz0RfGNhsRZ++bSyp0NqfiAggCR0RxByUXlJCwEVUik8uK1iQV0tes6KxJ13w4uty1ZZ3A6Es7Djj2TDOYGwfoEYaEI2Ymh6QR+kFYXHR9NWaho0H9dbdDBlfJQ7vDoJXKQ6p8xhY5Frl1UcsbRTydhFOz7o1aFbvahCz3oGLO+QBjY+Uw+Xx/qy5Nil79y2a5GeX5mWR9ndzrxpAxmjAybqwsSDKxq/18TQwe0d3ItTmE4qVD5scFQ2oeIzddc1wQodn7+oKH+7as9hcmCG9HNFbwIQU5nVVCr/ONgBf8il0MqbmIMFG54f0OgpFVdIkPNVnmxTZS8/LkUPG5jFs1TzASnd9Ywzw4VbmZXy5RDpGLW08KmoHr55JlScrjkOYgH9LaCrXFJWM6U9N2hkFKFjJWt5ZDhGTUIEjYbHVqIyQ5QigBnw+9pK713PPZNJQwVzMv4rjVV+cjsjqm5PZUF5QLG6ESaUrux8Zhy7hqaa3cG75dEiPWHQx17zg7JN6qKp6oS1gxWre4SlfOAaR02w95X6WWyma7VCmHArpc9sq6rmxR3K4g5gRnV0pvzAgxUHMucFJVclh6PS2yuXEy+j0ip7a+sw5bdy4l7vIAnXGr9yCiQGnpcsWp+ZzQbzTVsO6huPbOyRnHnbIPuNBm0Hh7vAqHfSvvNjdpE1VbcbXcr3sUQ3LusN/6omJJyxO3P2/n54SYM8e1EFlmPGzh2D822NwLDfUyl4obflRugy1S9LhlCQ5QNblSYNkSSbo+d72LbzHzwtGrQTmFQo8HkiyNF7x024uDXi16IyqRVAhXSQ6AvKWAClfCwWopZnanYJ1ZirEtuXDUbuENPW58PhZL5BhKNDFe1tUtXY7IYmwPdXRwIfgWo1eSvGXXgdgKbHDGLpfD4TY/LqXdPqrmbR2JhMGzW5TjwiVBzD1WXMsMQZwjZN2z6lZfEL6gkfNap2AfPWI35abjit9Cqz7CtrztoDt4qQqMQqsEGxVrHpkvi/iyEmRQZQQhU7iAw7w8zTaqJlMda8tWzbhBubqacKguJUWUDnNhV+yY2DpBzIit6T0kBNEcYsklW0ZxeSyV3rAESuudfjUntuPVqDaQlo0B2Z2tWJUZVXHRJaIpc8mJSnubYGKfJ1KFchEsQqjVSJd88HhF65uxow8JGqjqlr2u7WNhmWHsEqnldNyRc9N+x8i39b5ilySpVzJ/vmwkPNVG92qXUYfIOH+F6UoFoT0kp1q9JS1H9QdEhiLhkMH7DLRtzCUGVXEv7ExEDstQ5evxsuC0pXpEaeiId4Zakjk0h2tY3bDdQRY4SjQvrRlk0ajvtITQTl63E3bWmteIEpPjmreL4MzyUV+v1eNxrJk1Srtt55eJdQ7CgaFo2BHG9SoXNrf9PiEywPvCiTjpO/aQjHv6lsFap5ObNGvsPWLvWXYl73VlkXq17xZ1mDMY5vQn8xCX2U3e+LZ+3V6yA+ihiYRZQpvWTR0EpUcclGB0bSSiVGJbaWEMzSGxFe0gao4WLCBTLwehT5ubbNFKyBDHC71Lr2iIgg5VQUTuzG2a3XWP5gMbRG2div42Po3BiRjwTui8klW9oL4O5zLS7VVeM4G2602OBc1iFJmWydQYs9EoJF2jyrnVFw2vxrxFZ9Lh1pEsT7EL+5axUF0DRSc6MEpNGsYsF3aw4GoIAwVgGyAv5p5vO5IP8Qq3hebhCi2kBr4qPJNTfnO+1o1tjxsomt8i9LRASETihkMVozvk6IVLXi+8ng4xeHlE3JyWGXbPMasWWloWB8eCwTuGLzKQIrJHl4F8ucYdfUmd9asYM5F/6Mx10w/JWYQHONoyGSqvqPOuSIVCqMS17WZXYj7A5yTDrvqQzbHb+VAo89N4OCm0do73aZ4oqZlTl6pQOAZwk6W4Y8wZZaQYmWUQZ7pTE1nAA1lZGXse3e7CvdCFiyLf83rp8A4fwFF7jUPKol3JK3detr5ioRoGTJaZXbCwrja9hxk9X3NkRB0CypVIYilQIYVKkHFZals2syApsvl6DYxykA2URObuPHo4R0FQFWsbQtmHjHsdx+VV1AU1UmTfU0smH20IGzBqsNem7meZMo/LeYZIhglxt31WqKBjGEe5MWPu7G12UBUeOmJIrWKMCIe0iV5YZRyowxWNSBpb3a4X7jTWVwkpiC2+2C+gcER6q9s0y6G4LNPNTpcsgkvH3fJ0w8IO9VIOc5eDpW/NALN5EoY29pyGoKhslVRxWSoeTBeuq5rbXyGec9hivgD6h4SzCCTRWHrAzzDZnpACYmjEWLdd2ATqRdz5uDfPraO4z0KM8xtO1UvZa7N12WQLVG5uF9gNWG+pttRmM/Ab226PNWV2hq3OQdAbpLnjNq5qm7WahnIrSwPdU4WzOAbWsVxTNS4yTJqclwixpvk6xvSOESKnhU/WcWGvDHwOaYymR9vopHunjlXYHTuYQqXJ66BMl6awV7CzlBziA3YOuNLS0uDAwo0Cg2gF0RdnZ8Xd3nB1WedmweCkgnEW3XBHkxK2i27F7nzFuPo9qhO6zB117ZifVrAAQuvUUVEYDZuBY4lFdLmg4ZAQeSvt+Cue7G06clUqPe0GpZQxAUNJh6YDjET6E7HbWU1qrtYH7rjdXIv6xKCh2JWc3gtNGPL7MExIXQoIOJDJCCq7pZXGJpSgzWjKBWVqiR0j2jV0YCua78FUDh8jSRP3VIDrx/hCHdkus+DYMuLNqjgVCiLBqmei4dmob2CDJ5XCclDgpdGksZZ7qlwEaKcaXKOWfZ7LXRohSGUWy5NluzDCjVTLt3GxNC/HFhmGOLFLDoXXhhhArbfI2fUQuiDbNhFiefWmOZ+gBilAh4xkdeZV81vY4Dm8sfEKlUYIwfhFwreb8+K2BvwEEyTqaxu4O2hgCwwFhnhAjmv3ZELspd9Rw5JLM7bs0bNwWQX6ijqueesKM3tihwYZnB9B3ylly1s3JllkGly6ObW7mOgJA/G2cwlKhZXYRaksVf0CNyzak13xLEYrd10vrEpnDd1yMsnJzpTi50TtbW7swcNKcdR110BWYbI5XfTMlrOdhJuHcy04gZReCVXHBidCQYOwACFAdbegqxr/Np4Xm3NwOmYS65MV6uYoetpweXjUsZpyL9G520Pc/tTHelEcdtWaym4pWxcxGyD2CrudipvF2JcDGxYxGZD52eG7U7b10zETRkAyrD/uKy4wGnl3KTWE2sgYzx6Xo8XQ2Oi25phuPHXvCVLk5op6OWmLsWsQo7vi8GmdJIQ3F9RswZ5GVD9p8/i0IZcKNHTMQBBKFYsp4Zl8vN9p60BFLfjIm1SLbTixh2oOAp6zz2eVsjFcWg2NuNhbC35BGSQlB9f5ysHG4KKCitaHRUPyAnS0ET929/0GokQY6bnAvF1OwWWZ7e3N2NzEjpR2pbuE0WC5hfCeYMf53OtbdGBtQ6RdTkspRTDqfGHAShEQtJHtYzzS6lK4bAmvPg6FDUMhtg+cLbTwwnbgFZE57xCWXfCX2CO3S8figna9C6466hzOtMZmJWxGaF+0e4duPVmpnF0WCppjCQcfr26of4vjkd4TJ6cUr+wWKemmID1npXqspI7U+RRf1plsrOMjh0uUtOPmTpiM/GiTuzHc4dyavfVpr6P+BpjfDil5Ng9eGqcCZIqC7+Z87xH92AmFGtyOOduLMHwBvRSOh7d4eQN8yeukvI7OHCYJVdCu0n1GI3tp41/BpjjqnNXFaWCS3wtOHpHmlTBULqFrfhjMxqYwwJLnyjc1GyIUPdKhig+vpQ50H8SqXOn56DHn/fFEc8ni3DCbnEALzGDV9ZIXl7Q8mkUoDM5VwpXd1ku9uL+pIagk483ZrrAT0qLVXh5Jg8sWVncRzSRDG/fi4otBXzVBcGzHscO19XiS8M1F9uhlbDc3HLXjUTwzcysyjqY7gu1si6wMS6NunbsgV3WAaWvPRUHMqzefSmlSbjC5iGiLFE5W35r4mKFg1xGqG0XgT5QPclYs+ib1w9JaNgPfihmBYSq3Ko5W1+QG4dYSnrRonteIFV4wBr1AcWOYnsyxHpnTh5AwSfoIr5QuY66r8rK+6p25r/QLRLa+jYLtFNW489xutWDPbJvMXS8SMZ43HY0dsr7TYEphGzImxrCjGdxkALYnTrhe057TPNWj1hagaSG97uuM7skSkeaJrFyoWFT9oxP4G5CTfuN6heivUEDuK7GuCcENbkaE8Ah/Prt2R4ZilqCyAZHXFnHCfXpCQSuOSkwygM2eCssLsK1Qj4hojkKTzW8cvTngS2fVBxtzqPmxWSkaH5fLEyNdiwHKOq6HlWWyiTPemi/X3BJf6AfFC8a2yQr4YF8G7+rX+mm7kuqCpum/v3x4mc5Pn8fXf+Wh9HQo+L92Nvk4Rnx7lHU/RPYs99Nd16e/ZNUvH14qJwI2PU5h66QNngeW/+UM9uO/8BRkEjA8nvZOz9365u24v7GC6W+WXqLMbeumGr7UedLeD4I/vNhgfzk9n5wsdMD7y31paTGdgN91Pk7CoyD70uRfKq+JKu9l+sOG6UmS50ZW83YZPM+kwfgBeChy6i8ovvziVcW0zOcjlekcd3qm8vL7/wcp0EibCCYAAA== -->
