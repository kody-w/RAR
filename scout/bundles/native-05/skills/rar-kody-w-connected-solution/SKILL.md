---
name: "rar-kody-w-connected-solution"
description: "Turn an agent stack (a folder of BasicAgent *.py files + optional metadata.json) or an explicit list of sub-agents into ONE import-ready Microsoft Copilot Studio connected-agent solution: an orchestrator plus one connected sub-agent per agent, wired with InvokeConnectedAgentTaskAction. When an agent.py carries its compiled CapIR (t2p-capir/1.0) \u2014 or one can be recompiled from its seeded data \u2014 each sub-agent ALSO gets a REAL deterministic capability topic that runs the same steps as the agent.py's perform() (trigger -> the user's real query -> filter the seeded records -> branch -> respond, plus the document for artifact capabilities); only the data is mocked, so flipping the in-topic Table() to a live Dataverse / SharePoint connector is the one-line move to production. No code deploy. Bot names are auto-capped to 42 chars and orchestrator channels default off so it imports and publishes fully headlessly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/connected_solution_agent", "rar_sha256": "2653cc11fe301bc460b4fd94cffb59bfc854f1d88fb5f35a363e3b4aba52e6ce", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.3", "author": "Kody Wildfeuer", "tags": ["copilot_studio", "connected_agents", "power_platform", "deploy", "integration", "converter"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/connected_solution_agent`. The original RAPP
agent is preserved byte-for-byte in `connected_solution_agent.py` and in the RCI capsule.

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

Connected Solution Agent — turn a set of agents into ONE Microsoft Copilot Studio
connected-agent solution (an orchestrator + one connected sub-agent per agent).

WHAT IT DOES
------------
Given an "agent stack" (a folder of BasicAgent `*.py` files + an optional
`metadata.json`) or an explicit list of sub-agents, this agent emits a single,
import-ready Copilot Studio solution `.zip` shaped as:

    orchestrator bot  +  one connected SUB-AGENT bot per agent
    wired by componenttype=9 InvokeConnectedAgentTaskAction components

Instead of cramming every capability into one base agent's instructions, each
agent becomes its own separately-registerable connected agent (the unit
OneTrust / Agent 365 govern), and a generative orchestrator routes to them.

Every bot is a GPT agent (gpt.default instructions + code interpreter); no Azure
Function / custom connector. AND — when a sub-agent's source agent.py carries its
compiled CapIR (t2p-capir/1.0), or one can be recompiled from its seeded data —
that sub-agent ALSO gets a REAL deterministic capability topic that runs the same
steps as the agent.py's perform() (OnRecognizedIntent on the agent's triggers ->
Question for the user's real input -> a Table() of the SEEDED records -> Filter by
the real query -> branch -> SendActivity, plus a document render for artifact
capabilities). The control flow is real; only the DATA is mocked, so flipping the
in-topic Table() to a live Dataverse / SharePoint connector (binding.connector) is
the one-line move to production and the same logic runs unchanged. The emitted
package uses the exact structure of a real exported Copilot Studio solution, so it
imports with no code.

PROVEN LIVE — and the two non-obvious fixes baked in
----------------------------------------------------
This was imported AND published end-to-end into a real Copilot Studio
environment. The live test surfaced two things static checks cannot, both now
handled automatically:

  1. Bot-name 42-char limit. Dataverse rejects any bot whose display name is
     longer than 42 characters (error 10004). Bot names are capped to 42 here,
     keeping a trailing "Orchestrator" intact.

  2. Orchestrator publish + channels. A headless `pac copilot publish` cannot
     do the Bot Framework / M365 channel app-registration, so an orchestrator
     that declares channels fails publish with a 409 ExternalServiceException.
     Channels are therefore OFF by default (the whole solution then imports and
     publishes fully headlessly). Set orchestrator_channels=true only if you
     will publish the orchestrator in the maker portal (where the channel
     registration + consent happens) to expose it on M365 Copilot / Teams.

USAGE (as a RAPP agent)
-----------------------
    perform(stack_dir="path/to/my_stack")              # build from a stack
    perform(subagents=[{...}, {...}], solution_name="MyPack")   # or explicit

DEPLOY THE RESULT
-----------------
    Autonomous (built in — PURE Web API, stdlib only):
      perform(stack_dir="my_stack", deploy=true)
      Imports the solution into your Microsoft Copilot Studio (Dataverse)
      environment via the Web API ImportSolution action, then publishes every bot
      via PvaPublish (SUB-AGENTS FIRST, ORCHESTRATOR LAST — a connected-agent root
      409s if its children are not published yet). NO pac CLI, NO subprocess, NO
      binary — the IDENTICAL code runs in a local brainstem AND an
      Azure-Function-hosted brainstem. App-registration credentials are read ONLY
      from env (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET /
      DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file
      (credentials_path=, ~/.rapp_deploy_settings.json, RAPP_DEPLOY_SETTINGS, or
      ./local.settings.json) — the secret NEVER travels through chat.

    M365 Copilot / Teams exposure:
      regenerate with orchestrator_channels=true, import, then open the
      orchestrator in Copilot Studio and Publish (handles channel registration).

Self-contained: standard library only. Drop into any RAPP agents/ directory.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "capir_mode": {
      "description": "How to build the deterministic per-capability topic inside each sub-agent (the topic that runs the agent.py's perform() logic on STATIC synthetic stand-in data): 'auto' (default) uses an embedded CapIR, else real seeded data, else SYNTHESIZES static stand-in records from the agent's inferred data shape \u2014 so EVERY agent.py maps to a self-documented topic; 'static' uses only real seeded data (no synthetic stand-in); 'embedded' uses only an embedded CapIR; 'off' emits instructions-only sub-agents. Synthetic data is the swap-for-live seam (Table() -> connector).",
      "type": "string"
    },
    "credentials_path": {
      "description": "Path to a local.settings.json-style file holding DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE (under a top-level 'Values' object or at the root). Used only for deploy; the secret is never echoed back. If omitted, env vars / ~/.rapp_deploy_settings.json / ./local.settings.json are tried.",
      "type": "string"
    },
    "deploy": {
      "description": "When true, AUTONOMOUSLY import the solution into your Microsoft Copilot Studio (Dataverse) environment and publish every bot (sub-agents first, orchestrator last) \u2014 no pac CLI needed, stdlib only. App-registration credentials are read ONLY from env vars (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file \u2014 NEVER from chat. Default false (package only).",
      "type": "boolean"
    },
    "environment_url": {
      "description": "Optional override for the target Dataverse environment URL (e.g. https://yourorg.crm.dynamics.com). Defaults to DYNAMICS_365_RESOURCE from the creds.",
      "type": "string"
    },
    "orchestrator_channels": {
      "description": "Declare MsTeams + M365 Copilot channels on the orchestrator. Default false (headlessly publishable). True requires a maker-portal publish.",
      "type": "boolean"
    },
    "orchestrator_name": {
      "description": "Orchestrator display name (auto-capped to 42 chars, 'Orchestrator' kept).",
      "type": "string"
    },
    "output_path": {
      "description": "Where to write the .zip. Defaults to <SolutionName>_connected_solution.zip.",
      "type": "string"
    },
    "publish": {
      "description": "When deploy=true, also publish the bots after import (default true). false imports without publishing.",
      "type": "boolean"
    },
    "publisher_display": {
      "description": "Solution publisher friendly name (default 'Default Publisher').",
      "type": "string"
    },
    "publisher_name": {
      "description": "Solution publisher unique name (default 'DefaultPublisher'). Pair a fresh publisher_name with a fresh publisher_prefix to create a brand-new publisher.",
      "type": "string"
    },
    "publisher_prefix": {
      "description": "Customization prefix for the bot schema names (2-8 lowercase alphanumerics, default 'rapp'). Use a FRESH prefix to mint brand-new, isolated bots + a distinct solution instead of updating ones that already exist.",
      "type": "string"
    },
    "solution_display_name": {
      "description": "Solution friendly name.",
      "type": "string"
    },
    "solution_name": {
      "description": "Solution unique name (alphanumeric). Defaults from metadata.json id / stack folder name.",
      "type": "string"
    },
    "stack_dir": {
      "description": "Path to an agent stack folder. Each BasicAgent *.py under it (or its agents/ subfolder) becomes one connected sub-agent; metadata.json (name/description/features/starters) shapes the orchestrator.",
      "type": "string"
    },
    "subagents": {
      "description": "Alternative to stack_dir: explicit sub-agents, each an object with agent_name, display_name, description, instructions.",
      "type": "array"
    },
    "version": {
      "description": "Solution version, e.g. 1.0.0.0.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `connected_solution_agent.py` and embedded as the fenced Python below (sha256 2653cc11fe301bc4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `connected_solution_agent.py` first:

```bash
python3 connected_solution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 connected_solution_agent.py   # or on stdin
python3 connected_solution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/connected_solution_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/connected_solution_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/connected_solution_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Connected Solution Agent — turn a set of agents into ONE Microsoft Copilot Studio
connected-agent solution (an orchestrator + one connected sub-agent per agent).

WHAT IT DOES
------------
Given an "agent stack" (a folder of BasicAgent `*.py` files + an optional
`metadata.json`) or an explicit list of sub-agents, this agent emits a single,
import-ready Copilot Studio solution `.zip` shaped as:

    orchestrator bot  +  one connected SUB-AGENT bot per agent
    wired by componenttype=9 InvokeConnectedAgentTaskAction components

Instead of cramming every capability into one base agent's instructions, each
agent becomes its own separately-registerable connected agent (the unit
OneTrust / Agent 365 govern), and a generative orchestrator routes to them.

Every bot is a GPT agent (gpt.default instructions + code interpreter); no Azure
Function / custom connector. AND — when a sub-agent's source agent.py carries its
compiled CapIR (t2p-capir/1.0), or one can be recompiled from its seeded data —
that sub-agent ALSO gets a REAL deterministic capability topic that runs the same
steps as the agent.py's perform() (OnRecognizedIntent on the agent's triggers ->
Question for the user's real input -> a Table() of the SEEDED records -> Filter by
the real query -> branch -> SendActivity, plus a document render for artifact
capabilities). The control flow is real; only the DATA is mocked, so flipping the
in-topic Table() to a live Dataverse / SharePoint connector (binding.connector) is
the one-line move to production and the same logic runs unchanged. The emitted
package uses the exact structure of a real exported Copilot Studio solution, so it
imports with no code.

PROVEN LIVE — and the two non-obvious fixes baked in
----------------------------------------------------
This was imported AND published end-to-end into a real Copilot Studio
environment. The live test surfaced two things static checks cannot, both now
handled automatically:

  1. Bot-name 42-char limit. Dataverse rejects any bot whose display name is
     longer than 42 characters (error 10004). Bot names are capped to 42 here,
     keeping a trailing "Orchestrator" intact.

  2. Orchestrator publish + channels. A headless `pac copilot publish` cannot
     do the Bot Framework / M365 channel app-registration, so an orchestrator
     that declares channels fails publish with a 409 ExternalServiceException.
     Channels are therefore OFF by default (the whole solution then imports and
     publishes fully headlessly). Set orchestrator_channels=true only if you
     will publish the orchestrator in the maker portal (where the channel
     registration + consent happens) to expose it on M365 Copilot / Teams.

USAGE (as a RAPP agent)
-----------------------
    perform(stack_dir="path/to/my_stack")              # build from a stack
    perform(subagents=[{...}, {...}], solution_name="MyPack")   # or explicit

DEPLOY THE RESULT
-----------------
    Autonomous (built in — PURE Web API, stdlib only):
      perform(stack_dir="my_stack", deploy=true)
      Imports the solution into your Microsoft Copilot Studio (Dataverse)
      environment via the Web API ImportSolution action, then publishes every bot
      via PvaPublish (SUB-AGENTS FIRST, ORCHESTRATOR LAST — a connected-agent root
      409s if its children are not published yet). NO pac CLI, NO subprocess, NO
      binary — the IDENTICAL code runs in a local brainstem AND an
      Azure-Function-hosted brainstem. App-registration credentials are read ONLY
      from env (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET /
      DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file
      (credentials_path=, ~/.rapp_deploy_settings.json, RAPP_DEPLOY_SETTINGS, or
      ./local.settings.json) — the secret NEVER travels through chat.

    M365 Copilot / Teams exposure:
      regenerate with orchestrator_channels=true, import, then open the
      orchestrator in Copilot Studio and Publish (handles channel registration).

Self-contained: standard library only. Drop into any RAPP agents/ directory.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/connected_solution_agent",
    "version": "1.0.3",
    "display_name": "ConnectedSolution",
    "description": "Packages a BasicAgent stack into an import-ready Copilot Studio connected-agents solution zip, optionally publishing via the Dataverse Web API.",
    "author": "Kody Wildfeuer",
    "tags": ["copilot_studio", "connected_agents", "power_platform", "deploy", "integration", "converter"],
    "category": "integrations",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import io
import os
import re
import sys
import json
import ast
import base64
import uuid
import zipfile
import logging
import urllib.request
import urllib.parse
import urllib.error
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

# PUBLISHER PREFIX. Kody, 2026-08-27: "make it aibast for now."
#
# Env-overridable rather than hardcoded, because this repo is public: a bare "aibast"
# default would stamp every stranger's generated solution with a publisher that is not
# theirs, and a solution carrying the wrong publisher is a real problem for them to unpick
# in a tenant. Setting RAPP_PUBLISHER_PREFIX overrides it; unset, it is aibast.
_DEFAULT_PUBLISHER_PREFIX = os.getenv("RAPP_PUBLISHER_PREFIX", "aibast")

logger = logging.getLogger("connected_solution_agent")

# BasicAgent base — use the RAPP runtime's when present, else a minimal shim so
# this file also runs standalone (python connected_solution_agent.py <stack_dir>).
try:  # the RAPP runtime's base when hosted; a minimal shim when standalone
    from agents.basic_agent import BasicAgent  # type: ignore
except ImportError:
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        class BasicAgent:  # minimal fallback
            def __init__(self, name=None, metadata=None):
                self.name = name or getattr(self, "name", self.__class__.__name__)
                self.metadata = metadata or getattr(self, "metadata", {})

# ============================================================================
# Embedded Copilot Studio solution templates (verbatim from the proven packager)
# ============================================================================

DEFAULT_ICON_BASE64 = (
    "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"
)

SOLUTION_XML_NATIVE = """\
<ImportExportXml version="9.2.26023.151" SolutionPackageVersion="9.2" languagecode="1033" generatedBy="CrmLive" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" OrganizationVersion="9.2.26023.151" OrganizationSchemaType="Standard" CRMServerServiceabilityVersion="9.2.26024.00146">
  <SolutionManifest>
    <UniqueName>{solution_unique_name}</UniqueName>
    <LocalizedNames>
      <LocalizedName description="{solution_display_name}" languagecode="1033" />
    </LocalizedNames>
    <Descriptions />
    <Version>{solution_version}</Version>
    <Managed>{managed_flag}</Managed>
    <Publisher>
      <UniqueName>{publisher_unique_name}</UniqueName>
      <LocalizedNames>
        <LocalizedName description="{publisher_display_name}" languagecode="1033" />
      </LocalizedNames>
      <Descriptions>
        <Description description="Auto-generated publisher" languagecode="1033" />
      </Descriptions>
      <EMailAddress xsi:nil="true"></EMailAddress>
      <SupportingWebsiteUrl xsi:nil="true"></SupportingWebsiteUrl>
      <CustomizationPrefix>{publisher_prefix}</CustomizationPrefix>
      <CustomizationOptionValuePrefix>10000</CustomizationOptionValuePrefix>
      <Addresses>
        <Address>
          <AddressNumber>1</AddressNumber>
          <AddressTypeCode xsi:nil="true"></AddressTypeCode>
          <City xsi:nil="true"></City>
          <County xsi:nil="true"></County>
          <Country xsi:nil="true"></Country>
          <Fax xsi:nil="true"></Fax>
          <FreightTermsCode xsi:nil="true"></FreightTermsCode>
          <ImportSequenceNumber xsi:nil="true"></ImportSequenceNumber>
          <Latitude xsi:nil="true"></Latitude>
          <Line1 xsi:nil="true"></Line1>
          <Line2 xsi:nil="true"></Line2>
          <Line3 xsi:nil="true"></Line3>
          <Longitude xsi:nil="true"></Longitude>
          <Name xsi:nil="true"></Name>
          <PostalCode xsi:nil="true"></PostalCode>
          <PostOfficeBox xsi:nil="true"></PostOfficeBox>
          <PrimaryContactName xsi:nil="true"></PrimaryContactName>
          <ShippingMethodCode xsi:nil="true"></ShippingMethodCode>
          <StateOrProvince xsi:nil="true"></StateOrProvince>
          <Telephone1 xsi:nil="true"></Telephone1>
          <Telephone2 xsi:nil="true"></Telephone2>
          <Telephone3 xsi:nil="true"></Telephone3>
          <TimeZoneRuleVersionNumber xsi:nil="true"></TimeZoneRuleVersionNumber>
          <UPSZone xsi:nil="true"></UPSZone>
          <UTCOffset xsi:nil="true"></UTCOffset>
          <UTCConversionTimeZoneCode xsi:nil="true"></UTCConversionTimeZoneCode>
        </Address>
        <Address>
          <AddressNumber>2</AddressNumber>
          <AddressTypeCode xsi:nil="true"></AddressTypeCode>
          <City xsi:nil="true"></City>
          <County xsi:nil="true"></County>
          <Country xsi:nil="true"></Country>
          <Fax xsi:nil="true"></Fax>
          <FreightTermsCode xsi:nil="true"></FreightTermsCode>
          <ImportSequenceNumber xsi:nil="true"></ImportSequenceNumber>
          <Latitude xsi:nil="true"></Latitude>
          <Line1 xsi:nil="true"></Line1>
          <Line2 xsi:nil="true"></Line2>
          <Line3 xsi:nil="true"></Line3>
          <Longitude xsi:nil="true"></Longitude>
          <Name xsi:nil="true"></Name>
          <PostalCode xsi:nil="true"></PostalCode>
          <PostOfficeBox xsi:nil="true"></PostOfficeBox>
          <PrimaryContactName xsi:nil="true"></PrimaryContactName>
          <ShippingMethodCode xsi:nil="true"></ShippingMethodCode>
          <StateOrProvince xsi:nil="true"></StateOrProvince>
          <Telephone1 xsi:nil="true"></Telephone1>
          <Telephone2 xsi:nil="true"></Telephone2>
          <Telephone3 xsi:nil="true"></Telephone3>
          <TimeZoneRuleVersionNumber xsi:nil="true"></TimeZoneRuleVersionNumber>
          <UPSZone xsi:nil="true"></UPSZone>
          <UTCOffset xsi:nil="true"></UTCOffset>
          <UTCConversionTimeZoneCode xsi:nil="true"></UTCConversionTimeZoneCode>
        </Address>
      </Addresses>
    </Publisher>
    <RootComponents />
    <MissingDependencies />
  </SolutionManifest>
</ImportExportXml>"""

CUSTOMIZATIONS_XML_NATIVE = """\
<ImportExportXml xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" OrganizationVersion="9.2.26023.151" OrganizationSchemaType="Standard" CRMServerServiceabilityVersion="9.2.26024.00146">
  <Entities></Entities>
  <Roles></Roles>
  <Workflows></Workflows>
  <FieldSecurityProfiles></FieldSecurityProfiles>
  <Templates />
  <EntityMaps />
  <EntityRelationships />
  <OrganizationSettings />
  <optionsets />
  <CustomControls />
  <EntityDataProviders />
  <connectionreferences>
{connection_references}
  </connectionreferences>
  <Languages>
    <Language>1033</Language>
  </Languages>
</ImportExportXml>"""

CONTENT_TYPES_XML_NATIVE = '<?xml version="1.0" encoding="utf-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="xml" ContentType="application/octet-stream" /><Default Extension="json" ContentType="application/octet-stream" />{overrides}</Types>'

CONTENT_TYPE_OVERRIDE = '<Override PartName="/{part_name}" ContentType="application/octet-stream" />'

BOT_XML = """\
<bot schemaname="{bot_schema}">
  <authenticationmode>2</authenticationmode>
  <authenticationtrigger>1</authenticationtrigger>
  <iconbase64>{icon_base64}</iconbase64>
  <iscustomizable>0</iscustomizable>
  <language>1033</language>
  <name>{bot_display_name}</name>
  <runtimeprovider>0</runtimeprovider>
  <template>default-2.1.0</template>
</bot>"""

BOT_CONFIGURATION_JSON_NATIVE = """{{
  "$kind": "BotConfiguration",
  "settings": {{
    "GenerativeActionsEnabled": true
  }},
  "isAgentConnectable": true,
  "gPTSettings": {{
    "$kind": "GPTSettings",
    "defaultSchemaName": "{gpt_schema}"
  }},
  "aISettings": {{
    "$kind": "AISettings",
    "useModelKnowledge": true,
    "isFileAnalysisEnabled": true,
    "isSemanticSearchEnabled": true,
    "contentModeration": "Low",
    "optInUseLatestModels": false
  }},
  "recognizer": {{
    "$kind": "GenerativeAIRecognizer"
  }}
}}"""

ORCHESTRATOR_CHANNELS_BLOCK = """
  "channels": [
    {
      "$kind": "ChannelDefinition",
      "channelId": "MsTeams"
    },
    {
      "$kind": "ChannelDefinition",
      "channelId": "Microsoft365Copilot"
    }
  ],"""

ORCHESTRATOR_CONFIGURATION_JSON = """{{
  "$kind": "BotConfiguration",{channels_block}
  "settings": {{
    "GenerativeActionsEnabled": true
  }},
  "isAgentConnectable": true,{publish_on_import_line}
  "gPTSettings": {{
    "$kind": "GPTSettings",
    "defaultSchemaName": "{gpt_schema}"
  }},
  "isLightweightBot": false,
  "aISettings": {{
    "$kind": "AISettings",
    "useModelKnowledge": true,
    "isFileAnalysisEnabled": true,
    "isSemanticSearchEnabled": true,
    "contentModeration": "Low",
    "optInUseLatestModels": true
  }},
  "recognizer": {{
    "$kind": "GenerativeAIRecognizer"
  }}
}}"""

GPT_BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>15</componenttype>
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{bot_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

GPT_DATA_YAML = """\
kind: GptComponentMetadata
displayName: {display_name}
instructions: |-
{instructions_indented}
gptCapabilities:
  webBrowsing: true
  codeInterpreter: true

aISettings:
  model:
    modelNameHint: GPT5Chat

  extensionData:
    lastUsedCustomModel: {{}}

declarativeSkillsMetadata:"""

BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>{component_type}</componenttype>{description_element}
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{bot_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

CONN_REF_SET_XML = """\
<botcomponent_connectionreferenceset>
{entries}
</botcomponent_connectionreferenceset>"""

INVOKE_CONNECTED_AGENT_BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>9</componenttype>
  <description>{description}</description>
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{orchestrator_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

INVOKE_CONNECTED_AGENT_DATA = """\
kind: TaskDialog
modelDisplayName: {display_name}
modelDescription: |-
{description_indented}{inputs_block}
action:
  kind: InvokeConnectedAgentTaskAction{input_type_block}
  botSchemaName: {child_schema}
  historyType:
    kind: ConversationHistory"""


def _connected_inputs_yaml(params):
    """The orchestrator-side typed inputs for a connected agent, from the source
    agent.py's perform() params. Per the Copilot Studio connected-agent schema:
    `inputs` (AutomaticTaskInput list) sits at the TaskDialog root and `inputType`
    sits INSIDE the action block. These populate the connected agent's Inputs
    panel and let the orchestrator pass the params when it delegates. Returns
    (inputs_block, input_type_block) — both '' when there are no params."""
    params = params or []
    if not params:
        return "", ""
    inlines, props = [], []
    for entry in params:
        pn = entry[0] if isinstance(entry, (list, tuple)) else entry
        required = bool(entry[2]) if isinstance(entry, (list, tuple)) and len(entry) > 2 else False
        name = re.sub(r"[^A-Za-z0-9_]", "", str(pn)) or "input"
        inlines.append("  - kind: AutomaticTaskInput\n    propertyName: " + name)
        props.append("      " + name + ":\n"
                     "        displayName: " + name + "\n"
                     "        isRequired: " + ("true" if required else "false") + "\n"
                     "        type: String")
    return ("\ninputs:\n" + "\n".join(inlines),
            "\n  inputType:\n    properties:\n" + "\n".join(props))

INVOKE_CONNECTED_AGENT_DEPENDENCIES = '[{{"type":"bot","schemaName":"{child_schema}"}}]'

SYSTEM_TOPICS = {
    "ConversationStart": {
        "display_name": "Conversation Start",
        "description": "This system topic triggers when the agent receives an Activity indicating the beginning of a new conversation. If you do not want the agent to initiate the conversation, disable this topic.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnConversationStart
  id: main
  actions:
    - kind: SendActivity
      id: sendMessage_M0LuhV
      activity:
        text:
          - Hello, I'm {{System.Bot.Name}}. How can I help?
        speak:
          - Hello and thank you for calling {{System.Bot.Name}}. Please note that some responses are generated by AI and may require verification for accuracy. How may I help you today?"""
    },
    "EndofConversation": {
        "display_name": "End of Conversation",
        "description": "This system topic is only triggered by a redirect action,\nand guides the user through rating their conversation with the agent.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnSystemRedirect
  id: main
  actions:
    - kind: Question
      id: 41d42054-d4cb-4e90-b922-2b16b37fe379
      conversationOutcome: ResolvedImplied
      alwaysPrompt: true
      variable: init:Topic.SurveyResponse
      prompt: Did that answer your question?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: condition-0
      conditions:
        - id: condition-0-item-0
          condition: =Topic.SurveyResponse = true
          actions:
            - kind: CSATQuestion
              id: csat_1
              conversationOutcome: ResolvedConfirmed

            - kind: SendActivity
              id: sendMessage_8r29O0
              activity: Thanks for your feedback.

            - kind: Question
              id: question_1
              alwaysPrompt: true
              variable: init:Topic.Continue
              prompt: Can I help with anything else?
              entity: BooleanPrebuiltEntity

            - kind: ConditionGroup
              id: condition-1
              conditions:
                - id: condition-1-item-0
                  condition: =Topic.Continue = true
                  actions:
                    - kind: SendActivity
                      id: sendMessage_4eOE6h
                      activity: Go ahead. I'm listening.

              elseActions:
                - kind: SendActivity
                  id: yHBz55
                  activity: Ok, goodbye.

                - kind: EndConversation
                  id: jh1GMT

      elseActions:
        - kind: Question
          id: PM68ot
          alwaysPrompt: true
          variable: init:Topic.TryAgain
          prompt: Sorry I wasn't able to help better. Would you like to try again?
          entity: BooleanPrebuiltEntity

        - kind: ConditionGroup
          id: KNxYBf
          conditions:
            - id: DPveFP
              condition: =Topic.TryAgain = false
              actions:
                - kind: BeginDialog
                  id: cngqi4
                  dialog: {bot_schema}.topic.Escalate

          elseActions:
            - kind: SendActivity
              id: GrVHEW
              activity: Go ahead. I'm listening."""
    },
    "Escalate": {
        "display_name": "Escalate",
        "description": "This system topic is triggered when the user indicates they would like to speak to a representative.\nYou can configure how the agent will handle human hand-off scenarios in the agent settings..\nIf your agent does not handle escalations, this topic should be disabled.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnEscalate
  id: main
  intent:
    displayName: Escalate
    includeInOnSelectIntent: false
    triggerQueries:
      - Talk to agent
      - Talk to a person
      - Talk to someone
      - Call back
      - Call customer service
      - Call me please
      - Call support
      - Call technical support
      - Can an agent call me
      - Can I call
      - Can I get in touch with someone else
      - Can I get real agent support
      - Can I get transferred to a person to call
      - Can I have a call in number Or can I be called
      - Can I have a representative call me
      - Can I schedule a call
      - Can I speak to a representative
      - Can I talk to a human
      - Can I talk to a human assistant
      - Can someone call me
      - Chat with a human
      - Chat with a representative
      - Chat with agent
      - Chat with someone please
      - Connect me to a live agent
      - Connect me to a person
      - Could some one contact me by phone
      - Customer agent
      - Customer representative
      - Customer service
      - I need a manager to contact me
      - I need customer service
      - I need help from a person
      - I need to speak with a live argent
      - I need to talk to a specialist please
      - I want to talk to customer service
      - I want to proceed with live support
      - I want to speak with a consultant
      - I want to speak with a live tech
      - I would like to speak with an associate
      - I would like to talk to a technician
      - Talk with tech support member

  actions:
    - kind: SendActivity
      id: sendMessage_s39DCt
      conversationOutcome: Escalated
      activity: |-
        Escalating to a representative is not currently configured for this agent, however this is where the agent could provide information about how to get in touch with someone another way.

        Is there anything else I can help you with?"""
    },
    "Fallback": {
        "display_name": "Fallback",
        "description": "This system topic triggers when the user's utterance does not match any existing topics.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnUnknownIntent
  id: main
  actions:
    - kind: ConditionGroup
      id: conditionGroup_LktzXw
      conditions:
        - id: conditionItem_tlGIVo
          condition: =System.FallbackCount < 3
          actions:
            - kind: SendActivity
              id: sendMessage_QZreqo
              activity: I'm sorry, I'm not sure how to help with that. Can you try rephrasing?

      elseActions:
        - kind: BeginDialog
          id: 5aXj5M
          dialog: {bot_schema}.topic.Escalate"""
    },
    "Goodbye": {
        "display_name": "Goodbye",
        "description": "This topic triggers when the user says goodbye. By default, it does not end the conversation. If you would like to end the conversation when the user says goodbye, you can add an \"End of Conversation\" action to this topic, or redirect to the \"End of Conversation\" system topic.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Goodbye
    includeInOnSelectIntent: false
    triggerQueries:
      - Bye
      - Bye for now
      - Bye now
      - Good bye
      - No thank you. Goodbye.
      - See you later

  actions:
    - kind: Question
      id: question_zf2HhP
      variable: Topic.EndConversation
      prompt: Would you like to end our conversation?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: condition_DGc1Wy
      conditions:
        - id: condition_DGc1Wy-item-0
          condition: =Topic.EndConversation = true
          actions:
            - kind: BeginDialog
              id: dn94DC
              dialog: {bot_schema}.topic.EndofConversation

        - id: condition_DGc1Wy-item-1
          condition: =Topic.EndConversation = false
          actions:
            - kind: SendActivity
              id: sendMessage_LdLhmf
              activity: Go ahead. I'm listening."""
    },
    "Greeting": {
        "display_name": "Greeting",
        "description": "This topic is triggered when the user greets the agent.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Greeting
    includeInOnSelectIntent: false
    triggerQueries:
      - Good afternoon
      - Good morning
      - Hello
      - Hey
      - Hi

  actions:
    - kind: SendActivity
      id: sendMessage_abmysR
      activity:
        text:
          - Hello, how can I help you today?
        speak:
          - Hello, <break strength="medium" /> how can I help?

    - kind: CancelAllDialogs
      id: cancelAllDialogs_01At22"""
    },
    "MultipleTopicsMatched": {
        "display_name": "Multiple Topics Matched",
        "description": "This system topic triggers when the agent matches multiple Topics with the incoming message and needs to clarify which one should be triggered.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnSelectIntent
  id: main
  triggerBehavior: Always
  actions:
    - kind: SetVariable
      id: setVariable_M6434i
      variable: init:Topic.IntentOptions
      value: =System.Recognizer.IntentOptions

    - kind: SetTextVariable
      id: setTextVariable_0
      variable: Topic.NoneOfTheseDisplayName
      value: None of these

    - kind: EditTable
      id: sendMessage_g5Ls09
      changeType: Add
      itemsVariable: Topic.IntentOptions
      value: "={{ DisplayName: Topic.NoneOfTheseDisplayName, TopicId: \\"NoTopic\\", TriggerId: \\"NoTrigger\\", Score: 1.0 }}"

    - kind: Question
      id: question_zf2HhP
      interruptionPolicy:
        allowInterruption: false

      alwaysPrompt: true
      variable: System.Recognizer.SelectedIntent
      prompt: "To clarify, did you mean:"
      entity:
        kind: DynamicClosedListEntity
        items: =Topic.IntentOptions

    - kind: ConditionGroup
      id: conditionGroup_60PuXb
      conditions:
        - id: conditionItem_rs7GgM
          condition: =System.Recognizer.SelectedIntent.TopicId = "NoTopic"
          actions:
            - kind: ReplaceDialog
              id: YZXRDb
              dialog: {bot_schema}.topic.Fallback"""
    },
    "OnError": {
        "display_name": "On Error",
        "description": "This system topic triggers when the agent encounters an error. When using the test chat pane, the full error description is displayed.",
        "data": """\
kind: AdaptiveDialog
startBehavior: UseLatestPublishedContentAndCancelOtherTopics
beginDialog:
  kind: OnError
  id: main
  actions:
    - kind: SetVariable
      id: setVariable_timestamp
      variable: init:Topic.CurrentTime
      value: =Text(Now(), DateTimeFormat.UTC)

    - kind: ConditionGroup
      id: condition_1
      conditions:
        - id: bL4wmY
          condition: =System.Conversation.InTestMode = true
          actions:
            - kind: SendActivity
              id: sendMessage_XJBYMo
              activity: |-
                Error Message: {{System.Error.Message}}
                Error Code: {{System.Error.Code}}
                Conversation Id: {{System.Conversation.Id}}
                Time (UTC): {{Topic.CurrentTime}}

      elseActions:
        - kind: SendActivity
          id: sendMessage_dZ0gaF
          activity:
            text:
              - |-
                An error has occurred.
                Error code: {{System.Error.Code}}
                Conversation Id: {{System.Conversation.Id}}
                Time (UTC): {{Topic.CurrentTime}}.
            speak:
              - An error has occurred, please try again.

    - kind: LogCustomTelemetryEvent
      id: 9KwEAn
      eventName: OnErrorLog
      properties: "={{ErrorMessage: System.Error.Message, ErrorCode: System.Error.Code, TimeUTC: Topic.CurrentTime, ConversationId: System.Conversation.Id}}"

    - kind: CancelAllDialogs
      id: NW7NyY"""
    },
    "ResetConversation": {
        "display_name": "Reset Conversation",
        "description": None,
        "data": """\
kind: AdaptiveDialog
startBehavior: UseLatestPublishedContentAndCancelOtherTopics
beginDialog:
  kind: OnSystemRedirect
  id: main
  actions:
    - kind: SendActivity
      id: sendMessage_OPsT1O
      activity: What can I help you with?

    - kind: ClearAllVariables
      id: clearAllVariables_73bTFR
      variables: ConversationScopedVariables

    - kind: CancelAllDialogs
      id: cancelAllDialogs_12Gt21"""
    },
    "Search": {
        "display_name": "Conversational boosting",
        "description": "Create generative answers from knowledge sources.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnUnknownIntent
  id: main
  priority: -1
  actions:
    - kind: SearchAndSummarizeContent
      id: search-content
      variable: Topic.Answer
      userInput: =System.Activity.Text

    - kind: ConditionGroup
      id: has-answer-conditions
      conditions:
        - id: has-answer
          condition: =!IsBlank(Topic.Answer)
          actions:
            - kind: EndDialog
              id: end-topic
              clearTopicQueue: true"""
    },
    "Signin": {
        "display_name": "Sign in ",
        "description": "This system topic triggers when the agent needs to sign in the user or require the user to sign in",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnSignIn
  id: main
  actions:
    - kind: ConditionGroup
      id: conditionGroup_ypjGKL
      conditions:
        - id: conditionItem_7XYIIR
          condition: =System.SignInReason = SignInReason.SignInRequired
          actions:
            - kind: SendActivity
              id: sendMessage_1jHUNO
              activity: Hello! To be able to help you, I'll need you to sign in.

    - kind: OAuthInput
      id: gOjhZA
      title: Login
      text: To continue, please login"""
    },
    "StartOver": {
        "display_name": "Start Over",
        "description": None,
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Start Over
    includeInOnSelectIntent: false
    triggerQueries:
      - let's begin again
      - start over
      - start again
      - restart

  actions:
    - kind: Question
      id: question_zguoVV
      alwaysPrompt: false
      variable: init:Topic.Confirm
      prompt: Are you sure you want to restart the conversation?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: conditionGroup_lvx2zV
      conditions:
        - id: conditionItem_sVQtHa
          condition: =Topic.Confirm = true
          actions:
            - kind: BeginDialog
              id: 0YKYsy
              dialog: {bot_schema}.topic.ResetConversation

      elseActions:
        - kind: SendActivity
          id: sendMessage_lk2CyQ
          activity: Ok. Let's carry on."""
    },
    "ThankYou": {
        "display_name": "Thank you",
        "description": "This topic triggers when the user says thank you.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Thank you
    includeInOnSelectIntent: false
    triggerQueries:
      - thanks
      - thank you
      - thanks so much
      - ty

  actions:
    - kind: SendActivity
      id: sendMessage_9iz6v7
      activity: You're welcome."""
    },
}


# ============================================================================
# Packager: orchestrator + connected sub-agents, with the 42-char name cap,
# 100-char schema cap, and optional channels (default off = headless-publishable)
# ============================================================================

MAX_SCHEMA = 100


_CONNECTED_INFIX = ".InvokeConnectedAgentTaskAction."   # 32 chars (incl. both dots)


_MIN_ACTION_BUDGET = 26   # always leave at least this many chars for the action suffix


MAX_BOT_NAME = 42


def _cap_bot_name(name: str, preserve_suffix: Optional[str] = None) -> str:
    """Truncate a bot display name to the 42-char limit, keeping a trailing word
    like 'Orchestrator' intact when present."""
    name = (name or "").strip()
    if len(name) <= MAX_BOT_NAME:
        return name
    if preserve_suffix and name.endswith(preserve_suffix):
        budget = MAX_BOT_NAME - len(preserve_suffix) - 1
        head = name[: -len(preserve_suffix)].rstrip()[:budget].rstrip()
        return f"{head} {preserve_suffix}"
    return name[:MAX_BOT_NAME].rstrip()


def _sanitize_schema(name: str) -> str:
    """Lowercase alphanumeric fragment for a bot schema name."""
    return re.sub(r"[^a-zA-Z0-9]", "", name or "").lower()


def _pascal(name: str) -> str:
    """PascalCase alphanumeric fragment for a connected-action schema name."""
    parts = re.split(r"[^a-zA-Z0-9]+", name or "")
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def _xml_escape(text: str) -> str:
    return (
        (text or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _indent(text: str, spaces: int = 2) -> str:
    pad = " " * spaces
    return "\n".join(f"{pad}{line}" for line in (text or "").split("\n"))


def _yaml_display_safe(text: str) -> str:
    """Make a one-line value safe as a bare YAML scalar (no colons/quotes/newlines)."""
    clean = re.sub(r"\s+", " ", (text or "").replace(":", " -")).strip()
    return clean.replace('"', "").replace("'", "")


# ============================================================================
# CapIR -> deterministic capability topic (the 1:1 conversion)
#
# A converted agent.py compiles its perform() to a CapIR (t2p-capir/1.0). When a
# sub-agent carries that CapIR, the packager emits a REAL Copilot Studio topic
# that runs the SAME steps perform() runs: OnRecognizedIntent (the agent's real
# triggers) -> Question (the user's real input) -> SetVariable Table() of the
# SEEDED records -> Filter by the real query -> branch -> SendActivity, plus a
# document render for artifact-producing capabilities. The control flow is real;
# only the DATA is mocked. Flipping the in-topic Table() to a Dataverse /
# SharePoint connector (binding.connector) is the one-line move to live data, and
# the same filter/respond/document logic runs unchanged. This is the opposite of
# an actions:[]+modelDescription "gamed" topic.
# ============================================================================

def _yaml_dq(text) -> str:
    """A YAML double-quoted scalar: robust for Power Fx expressions and message
    text (escapes backslash/quote, encodes newlines)."""
    s = (str(text).replace("\\", "\\\\").replace('"', '\\"')
         .replace("\n", "\\n").replace("\t", "\\t").replace("\r", ""))
    return '"' + s + '"'


def _pfx_str(value) -> str:
    """A Power Fx double-quoted string literal (internal quotes doubled)."""
    return '"' + str(value).replace('"', '""') + '"'


def _pfx_safe_text(text) -> str:
    """Strip literal braces from message text so Copilot Studio does not parse
    them as variable bindings (unparseable {...} fails publish). Template tokens
    like {Topic.X} are added AFTER this, so they survive."""
    return str(text).replace("{", "(").replace("}", ")")


def _capir_topic_fields(records):
    """Stable union of record field names (the Table()/filter columns) when the
    binding omits an explicit field list (recovered / recompiled CapIRs)."""
    fields = []
    for r in records or []:
        if isinstance(r, dict):
            for k in r.keys():
                if k not in fields:
                    fields.append(k)
    return fields


def _numeric_metric_field(records, fields, hint=None):
    """Pick the field numeric-threshold queries compare against (e.g. "assets
    above a 30% failure probability" -> a real `Value(field) >= 0.30`). A field
    qualifies only if it parses as a number in EVERY record (so Power Fx Value()
    never errors). Prefers probability/score-like names and 0..1-ranged fields;
    honors an explicit binding `metric_field` hint."""
    if hint and hint in (fields or []):
        return hint
    if not records:
        return None
    numeric, ratio = [], []
    for f in fields:
        vals, ok = [], True
        for r in records:
            if not isinstance(r, dict) or f not in r or str(r.get(f)).strip() == "":
                ok = False; break
            try:
                vals.append(float(str(r.get(f)).strip()))
            except (TypeError, ValueError):
                ok = False; break
        if ok and vals:
            numeric.append(f)
            if all(0.0 <= v <= 1.0 for v in vals):
                ratio.append(f)
    pool = ratio or numeric
    if not pool:
        return None
    for pat in (r"p_?fail|prob|likeli|risk", r"score|rate|ratio|pct|percent|conf"):
        for f in pool:
            if re.search(pat, f, re.I):
                return f
    return pool[0]


# The load-bearing perform() constants (t2p-capir/1.0 CAPIR_CONSTS). The topic
# reads these off the CapIR when present so it mirrors the agent.py's numbers.
_CAPIR_TOPIC_CONSTS = {
    "example_take": 2, "fallback_take": 2, "pdf_records": 3,
    "pdf_prepared": "Prepared for {customer}",
    "pdf_footer": "Synthetic demo data - no customer data was needed.",
}


def capir_topic_action_name(capir: dict) -> str:
    """The custom-topic schema suffix for a capability: Handle<Pascal(key)>."""
    key = (capir or {}).get("key") or "capability"
    return "Handle" + (_pascal(key) or "Capability")


def capir_topic_data_yaml(display_name: str, capir: dict) -> str:
    """Render a capability's CapIR into a REAL deterministic Copilot Studio topic
    'data' YAML that goes INSIDE the sub-agent: OnRecognizedIntent triggers ->
    Question (slot) -> SetVariable Table() of the SEEDED records -> Filter by the
    real query -> ConditionGroup on the match count -> SendActivity, plus (for an
    artifact capability) a SetVariable that renders the document from the matched
    (or fallback) records exactly like perform()'s artifact step. The synthetic
    records live IN the topic and the control flow runs deterministically; only
    the DATA is mocked. Structural 1:1 with the generated agent.py's perform()."""
    capir = capir or {}
    consts = dict(_CAPIR_TOPIC_CONSTS)
    consts.update(capir.get("consts") or {})
    binding = capir.get("binding") or {}
    fields = binding.get("fields") or _capir_topic_fields(binding.get("records"))
    table = binding.get("table") or "records"
    records = binding.get("records") or []
    customer = str(capir.get("customer") or "the customer")
    response = _pfx_safe_text(capir.get("response") or f"Here is how I handle {display_name}.")
    # triggers + grounding facts + the artifact doc come straight from the steps
    triggers, facts, doc = [], [], None
    for step in capir.get("steps") or []:
        op = step.get("op")
        if op == "trigger_match":
            triggers = step.get("queries") or []
        elif op == "knowledge_lookup":
            facts = step.get("facts") or []
        elif op == "artifact":
            doc = step.get("doc")
    prompt = None
    for slot in capir.get("slots") or []:
        prompt = slot.get("prompt"); break
    prompt = prompt or f"What would you like help with for {display_name}?"

    # Power Fx: a real Table() of the seeded records, a real query Filter, a real
    # count, then a real branch -- the exact perform() path.
    recs = []
    for r in records:
        if isinstance(r, dict):
            cells = ", ".join("%s: %s" % (f, _pfx_str(r.get(f, ""))) for f in fields)
            recs.append("{" + cells + "}")
    table_pfx = "=Table(" + ", ".join(recs) + ")" if recs else "=Blank()"
    conds = " || ".join("(Lower(ThisRecord.%s) in Lower(Topic.Query))" % f for f in fields)
    text_clause = "(%s)" % (conds or "false")

    # numeric-threshold support: a query like "assets above a 30% failure
    # probability" sets Topic.Threshold (number, %-aware) + Topic.Direction
    # (ge/le) and the Filter does a REAL Value()-comparison on the metric field,
    # not just text containment. Falls back to text match when no number is asked.
    metric_field = _numeric_metric_field(records, fields, (binding.get("metric_field")))
    threshold_actions, filter_inner = "", text_clause
    if metric_field:
        num_re = r"\d+\.?\d*"
        thr_pfx = ('=If(IsMatch(Topic.Query, "\\d"), '
                   'Value(First(MatchAll(Topic.Query, "' + num_re + '")).FullMatch) '
                   '/ If(IsMatch(Topic.Query, "%"), 100, 1), Blank())')
        dir_pfx = ('=If(IsMatch(Lower(Topic.Query), "above|over|greater|more than|exceed|at least|higher|>"), "ge", '
                   'If(IsMatch(Lower(Topic.Query), "below|under|less|fewer|within|at most|lower|<"), "le", "ge"))')
        threshold_actions = (
            "    - kind: SetVariable\n"
            "      id: setThreshold\n"
            "      variable: Topic.Threshold\n"
            "      value: " + _yaml_dq(thr_pfx) + "\n"
            "    - kind: SetVariable\n"
            "      id: setDirection\n"
            "      variable: Topic.Direction\n"
            "      value: " + _yaml_dq(dir_pfx) + "\n")
        num_clause = ('(!IsBlank(Topic.Threshold) && If(Topic.Direction = "le", '
                      'Value(ThisRecord.' + metric_field + ') <= Topic.Threshold, '
                      'Value(ThisRecord.' + metric_field + ') >= Topic.Threshold))')
        filter_inner = "(" + text_clause + " || " + num_clause + ")"
    filter_pfx = "=Filter(Topic.Records, !IsBlank(Topic.Query) && " + filter_inner + ")"

    grounding = "\n".join("- " + _pfx_safe_text(f) for f in facts)
    ground_block = ("\n\nGrounded in what you told us:\n" + grounding) if grounding else ""

    # artifact (op==artifact): render the document from the matched-or-fallback
    # records, exactly like perform()'s artifact step (hits[:pdf_records] with a
    # data[:fallback_take] fallback). Materializing the real downloadable file is
    # the live-data flip -- a Create-file / Convert-to-PDF flow over these records.
    doc_actions, doc_block = "", ""
    if doc and fields:
        cells_pfx = ' & " | " & '.join('"%s: " & Text(ThisRecord.%s)' % (f, f) for f in fields)
        source = ("If(Topic.MatchCount > 0, Topic.Matches, FirstN(Topic.Records, %d))"
                  % consts["fallback_take"])
        document_pfx = ("=Concat(FirstN(%s, %d), %s & Char(10))"
                        % (source, consts["pdf_records"], cells_pfx))
        doc_actions = (
            "    - kind: SetVariable\n"
            "      id: setDocument\n"
            "      variable: Topic.Document\n"
            "      value: " + _yaml_dq(document_pfx) + "\n")
        prepared = _pfx_safe_text(consts["pdf_prepared"].replace("{customer}", customer))
        footer = _pfx_safe_text(consts["pdf_footer"])
        safe_doc = _pfx_safe_text(str(doc))
        doc_block = ("\n\n[" + safe_doc + "] " + prepared + ":\n"
                     + "{Topic.Document}\n" + footer
                     + "\n(In production, a Create-file / Convert-to-PDF flow over these "
                       "records delivers the real " + safe_doc + ".)")

    hit_msg = (response + ground_block
               + "\n\nI found {Topic.MatchCount} matching record(s) in the "
               + table + " data (synthetic demo data - no customer data needed)."
               + doc_block)
    miss_msg = (response + ground_block
                + "\n\nNo matching record in the " + table
                + " data; here are reference examples to ground the answer."
                + doc_block)
    trig = "\n".join("      - " + _yaml_dq(t) for t in triggers) or ("      - " + _yaml_dq(display_name))

    # intake: ask for the value to filter on. We intentionally do NOT read an
    # orchestrator-passed `Global.<param>` here. A connected agent can only
    # reference a global it has DECLARED as external-settable, and the solution
    # package format gives no reliable way to emit that declaration — referencing
    # an undeclared Global makes Copilot Studio's topic checker throw a
    # PowerFxError ("Identifier not recognized"), which blocks publish. The
    # orchestrator still DECLARES + PASSES the typed inputs (see the connected
    # action's inputType); the agent's generative layer receives them, and this
    # deterministic topic captures the value it filters on via the Question.
    intake_actions = (
        "    - kind: Question\n"
        "      id: question_query\n"
        "      variable: Topic.Query\n"
        "      prompt: " + _yaml_dq(prompt) + "\n"
        "      entity: StringPrebuiltEntity\n")

    return (
        "kind: AdaptiveDialog\n"
        "beginDialog:\n"
        "  kind: OnRecognizedIntent\n"
        "  id: main\n"
        "  intent:\n"
        "    displayName: " + _yaml_dq(display_name) + "\n"
        "    includeInOnSelectIntent: false\n"
        "    triggerQueries:\n" + trig + "\n"
        "  actions:\n"
        + intake_actions +
        "    - kind: SetVariable\n"
        "      id: setRecords\n"
        "      variable: Topic.Records\n"
        "      value: " + _yaml_dq(table_pfx) + "\n"
        + threshold_actions +
        "    - kind: SetVariable\n"
        "      id: setMatches\n"
        "      variable: Topic.Matches\n"
        "      value: " + _yaml_dq(filter_pfx) + "\n"
        "    - kind: SetVariable\n"
        "      id: setCount\n"
        "      variable: Topic.MatchCount\n"
        "      value: " + _yaml_dq("=CountRows(Topic.Matches)") + "\n"
        + doc_actions +
        "    - kind: ConditionGroup\n"
        "      id: hasMatches\n"
        "      conditions:\n"
        "        - id: hasMatches_hit\n"
        "          condition: " + _yaml_dq("=Topic.MatchCount > 0") + "\n"
        "          actions:\n"
        "            - kind: SendActivity\n"
        "              id: replyHit\n"
        "              activity: " + _yaml_dq(hit_msg) + "\n"
        "      elseActions:\n"
        "        - kind: SendActivity\n"
        "          id: replyMiss\n"
        "          activity: " + _yaml_dq(miss_msg) + "\n"
    )


@dataclass
class SubAgentSpec:
    """One connected sub-agent (one agent.py promoted to its own bot)."""
    agent_name: str           # e.g. "loanoriginationassistant"
    display_name: str         # e.g. "Loan Origination Assistant"
    description: str          # routing description the orchestrator selects on
    instructions: str         # the sub-agent's gpt.default instruction blob
    # The capability's compiled CapIR (t2p-capir/1.0), records already injected.
    # When present, the packager emits a REAL deterministic topic INSIDE this
    # sub-agent that runs the same steps as the converted agent.py's perform(),
    # instead of leaving the behavior to the gpt.default instruction blob. The
    # instructions remain as the persona/router fallback.
    capir: Optional[dict] = None
    # The source agent.py's perform() params [(name, description, required), ...],
    # declared as typed INPUTS on the orchestrator's connected-agent action so the
    # Copilot Studio orchestrator passes them when it delegates (the agent's
    # "Inputs" panel) — the contract, structurally, not just in the description.
    params: Optional[list] = None


@dataclass
class ConnectedSolutionSpec:
    """A single solution bundling an orchestrator + N connected sub-agents."""
    solution_unique_name: str
    solution_display_name: str
    orchestrator_display_name: str
    subagents: List[SubAgentSpec]
    orchestrator_instructions: str = ""   # synthesized if empty
    publisher_prefix: str = _DEFAULT_PUBLISHER_PREFIX
    publisher_unique_name: str = "DefaultPublisher"
    publisher_display_name: str = "Default Publisher"
    solution_version: str = "1.0.0.0"
    managed: bool = False
    orchestrator_schema_suffix: str = "orchestrator"
    # When True the orchestrator auto-publishes on import. Leave False so the
    # import itself never depends on the (slower, fail-prone) publish step.
    orchestrator_publish_on_import: bool = False
    # When True the orchestrator declares MsTeams + M365 Copilot channels. This
    # requires a maker-portal publish (headless `pac copilot publish` 409s on the
    # channel registration). Default False = fully headlessly publishable.
    orchestrator_channels: bool = False


class ConnectedSolutionPackager:
    """Assembles a multi-bot connected-agent solution zip from a spec."""

    def __init__(self, spec: ConnectedSolutionSpec):
        self.spec = spec
        # publisher_prefix is the one untamed length input feeding the schema caps
        # below; bound it to Dataverse's 8-char prefix limit so no schema exceeds
        # MAX_SCHEMA for ANY direct caller (perform() already caps it). Mutate the
        # spec too so the CustomizationPrefix stays consistent with the schemas.
        spec.publisher_prefix = spec.publisher_prefix[:8]
        prefix = spec.publisher_prefix

        # Connected-agent components are named
        #   {orch_schema}.InvokeConnectedAgentTaskAction.{Action}
        # and the full schema name must stay within Dataverse's 100-char limit.
        # Cap the orchestrator schema (reserving room for the action suffix) so a
        # long stack name can never push a component name over the limit.
        suffix = spec.orchestrator_schema_suffix
        base = re.sub(r"stack$", "", _sanitize_schema(spec.solution_unique_name)) or "agents"
        orch = f"{prefix}_{base}{suffix}"
        max_orch = MAX_SCHEMA - len(_CONNECTED_INFIX) - _MIN_ACTION_BUDGET   # 42
        if len(orch) > max_orch:
            keep = max(4, max_orch - len(prefix) - 1 - len(suffix))
            orch = f"{prefix}_{base[:keep]}{suffix}"
        self.orch_schema = orch
        # Whatever room is left after the (capped) orchestrator schema + infix.
        self._action_budget = MAX_SCHEMA - len(_CONNECTED_INFIX) - len(self.orch_schema)

        # Assign a unique schema name + connected-action name to each sub-agent.
        self._children = []  # list of (SubAgentSpec, child_schema, action_name)
        seen_schemas = {self.orch_schema}
        seen_actions = set()
        # Children need room for a ".topic.<Name>" suffix within MAX_SCHEMA. The
        # orchestrator schema is capped above; children were NOT, so a long
        # solution + capability name overflowed the Dataverse 100-char limit.
        child_base_max = max(4, MAX_SCHEMA - 35 - len(prefix) - 1)
        for sub in spec.subagents:
            base = (_sanitize_schema(sub.agent_name) or "agent")[:child_base_max]
            child_schema = f"{prefix}_{base}"
            n = 2
            while child_schema in seen_schemas:
                child_schema = f"{prefix}_{base}{n}"
                n += 1
            seen_schemas.add(child_schema)

            pascal = _pascal(sub.display_name or sub.agent_name) or "Agent"
            action = pascal[: self._action_budget]
            n = 2
            while action in seen_actions:
                tag = str(n)
                action = pascal[: max(1, self._action_budget - len(tag))] + tag
                n += 1
            seen_actions.add(action)

            self._children.append((sub, child_schema, action))

    # -- public ----------------------------------------------------------

    def package(self, output_path: Optional[Path] = None) -> bytes:
        buf = io.BytesIO()
        overrides: List[str] = []  # /data parts for [Content_Types].xml

        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
            # 1. solution + customizations (connector-less, empty RootComponents)
            zf.writestr("solution.xml", self._solution_xml())
            zf.writestr(
                "customizations.xml",
                CUSTOMIZATIONS_XML_NATIVE.format(connection_references=""),
            )

            # 2. Orchestrator bot (router) — instructions list the sub-agents
            self._write_bot(
                zf,
                bot_schema=self.orch_schema,
                display_name=self.spec.orchestrator_display_name,
                instructions=self._orchestrator_instructions(),
                overrides=overrides,
                is_orchestrator=True,
            )

            # 3. Connected-agent delegation components (under the orchestrator)
            for sub, child_schema, action in self._children:
                self._write_connected_action(
                    zf, sub, child_schema, action, overrides
                )

            # 4. Each sub-agent as its own connectable bot — now carrying the REAL
            #    deterministic capability topic (1:1 with its agent.py) when a
            #    CapIR is present.
            for sub, child_schema, _action in self._children:
                self._write_bot(
                    zf,
                    bot_schema=child_schema,
                    display_name=sub.display_name,
                    instructions=sub.instructions,
                    overrides=overrides,
                    capir=sub.capir,
                )

            # 5. Empty connection reference set (no connectors in this topology)
            zf.writestr(
                "Assets/botcomponent_connectionreferenceset.xml",
                CONN_REF_SET_XML.format(entries=""),
            )

            # 6. [Content_Types].xml — every extensionless /data part listed
            zf.writestr(
                "[Content_Types].xml",
                CONTENT_TYPES_XML_NATIVE.format(overrides="".join(overrides)),
            )

        data = buf.getvalue()
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(data)
        return data

    @property
    def bot_schemas(self) -> List[str]:
        return [self.orch_schema] + [c[1] for c in self._children]

    # -- bot writers -----------------------------------------------------

    def _write_bot(
        self,
        zf: zipfile.ZipFile,
        bot_schema: str,
        display_name: str,
        instructions: str,
        overrides: List[str],
        is_orchestrator: bool = False,
        capir: Optional[dict] = None,
    ) -> None:
        """Write a complete bot: bot.xml, configuration.json, gpt.default, system
        topics, and (for a sub-agent carrying a CapIR) the REAL deterministic
        capability topic that runs the same steps as the converted agent.py."""
        # Copilot Studio caps the bot name at 42 chars; keep "Orchestrator" intact.
        display_name = _cap_bot_name(
            display_name, preserve_suffix="Orchestrator" if is_orchestrator else None
        )
        # bot.xml + configuration.json
        zf.writestr(
            f"bots/{bot_schema}/bot.xml",
            BOT_XML.format(
                bot_schema=bot_schema,
                bot_display_name=display_name,
                icon_base64=DEFAULT_ICON_BASE64,
            ),
        )
        gpt_schema = f"{bot_schema}.gpt.default"
        if is_orchestrator:
            # The connected-agent root needs the channels + isLightweightBot config
            # or its post-publish provisioning fails with a 409 ExternalServiceException.
            poi = '\n  "publishOnImport": true,' if self.spec.orchestrator_publish_on_import else ""
            channels = ORCHESTRATOR_CHANNELS_BLOCK if self.spec.orchestrator_channels else ""
            config_json = ORCHESTRATOR_CONFIGURATION_JSON.format(
                gpt_schema=gpt_schema, publish_on_import_line=poi, channels_block=channels
            )
        else:
            config_json = BOT_CONFIGURATION_JSON_NATIVE.format(gpt_schema=gpt_schema)
        zf.writestr(f"bots/{bot_schema}/configuration.json", config_json)

        # gpt.default component (instructions)
        gpt_folder = f"botcomponents/{gpt_schema}"
        zf.writestr(
            f"{gpt_folder}/botcomponent.xml",
            GPT_BOTCOMPONENT_XML.format(
                schema_name=gpt_schema,
                display_name=display_name,
                bot_schema=bot_schema,
            ),
        )
        instr = instructions or f"You are {display_name}. Help the user with their request."
        zf.writestr(
            f"{gpt_folder}/data",
            GPT_DATA_YAML.format(
                display_name=display_name,
                instructions_indented=_indent(instr, 2),
            ),
        )
        overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{gpt_folder}/data"))

        # system topics (one set per bot)
        for topic_key, topic_data in SYSTEM_TOPICS.items():
            schema_name = f"{bot_schema}.topic.{topic_key}"
            folder = f"botcomponents/{schema_name}"
            zf.writestr(
                f"{folder}/botcomponent.xml",
                self._topic_botcomponent_xml(bot_schema, topic_key, topic_data),
            )
            zf.writestr(
                f"{folder}/data",
                topic_data["data"].format(bot_schema=bot_schema),
            )
            overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

        # custom per-capability topic: the REAL deterministic behavior, INSIDE
        # this sub-agent (1:1 with the converted agent.py's CapIR steps). The
        # orchestrator stays a pure router and never carries one.
        if capir and not is_orchestrator:
            action = capir_topic_action_name(capir)
            # keep "{bot_schema}.topic.{action}" within the 100-char schema limit
            action = action[: max(4, MAX_SCHEMA - len(bot_schema) - len(".topic."))]
            schema_name = f"{bot_schema}.topic.{action}"
            folder = f"botcomponents/{schema_name}"
            zf.writestr(
                f"{folder}/botcomponent.xml",
                self._topic_botcomponent_xml(
                    bot_schema, action,
                    {"display_name": _xml_escape(display_name),
                     "description": f"Deterministic handler for {display_name} "
                                    "(seeded records + the real user query, 1:1 with the agent.py)."}),
            )
            zf.writestr(f"{folder}/data", capir_topic_data_yaml(display_name, capir))
            overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

    def _write_connected_action(
        self,
        zf: zipfile.ZipFile,
        sub: SubAgentSpec,
        child_schema: str,
        action: str,
        overrides: List[str],
    ) -> None:
        """Write the orchestrator's delegation component for one sub-agent."""
        schema_name = f"{self.orch_schema}.InvokeConnectedAgentTaskAction.{action}"
        folder = f"botcomponents/{schema_name}"
        description = sub.description or f"Delegate to {sub.display_name}."

        zf.writestr(
            f"{folder}/botcomponent.xml",
            INVOKE_CONNECTED_AGENT_BOTCOMPONENT_XML.format(
                schema_name=schema_name,
                description=_xml_escape(description),
                display_name=_xml_escape(sub.display_name),
                orchestrator_schema=self.orch_schema,
            ),
        )
        zf.writestr(
            f"{folder}/dependencies.json",
            INVOKE_CONNECTED_AGENT_DEPENDENCIES.format(child_schema=child_schema),
        )
        inputs_block, input_type_block = _connected_inputs_yaml(getattr(sub, "params", None))
        zf.writestr(
            f"{folder}/data",
            INVOKE_CONNECTED_AGENT_DATA.format(
                display_name=_yaml_display_safe(sub.display_name),
                description_indented=_indent(description, 2),
                child_schema=child_schema,
                inputs_block=inputs_block,
                input_type_block=input_type_block,
            ),
        )
        overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

    # -- xml helpers -----------------------------------------------------

    def _topic_botcomponent_xml(self, bot_schema, topic_key, topic_data) -> str:
        schema_name = f"{bot_schema}.topic.{topic_key}"
        desc = topic_data.get("description")
        desc_element = ""
        if desc:
            desc_element = f"\n  <description>{_xml_escape(desc)}</description>"
        return BOTCOMPONENT_XML.format(
            schema_name=schema_name,
            component_type=9,
            display_name=topic_data["display_name"],
            bot_schema=bot_schema,
            description_element=desc_element,
        )

    def _solution_xml(self) -> str:
        return SOLUTION_XML_NATIVE.format(
            solution_unique_name=self.spec.solution_unique_name,
            solution_display_name=self.spec.solution_display_name,
            publisher_unique_name=self.spec.publisher_unique_name,
            publisher_display_name=self.spec.publisher_display_name,
            publisher_prefix=self.spec.publisher_prefix,
            solution_version=self.spec.solution_version,
            managed_flag="1" if self.spec.managed else "0",
        )

    # -- orchestrator instructions --------------------------------------

    def _orchestrator_instructions(self) -> str:
        if self.spec.orchestrator_instructions:
            return self.spec.orchestrator_instructions
        lines = [
            f"You are {self.spec.orchestrator_display_name}, the orchestrator for the "
            f"{self.spec.solution_display_name} workflow. You route each user request to the "
            "right connected sub-agent and never answer specialized questions yourself.",
            "",
            "Connected sub-agents you can delegate to:",
        ]
        for sub, _schema, _action in self._children:
            one_line = re.sub(r"\s+", " ", (sub.description or sub.display_name)).strip()
            lines.append(f"- {sub.display_name}: {one_line}")
        lines += [
            "",
            "Routing rules:",
            "- Read the user's request, pick the single best-matching sub-agent from the list, and delegate to it.",
            "- Pass each sub-agent only the inputs it needs; do not paraphrase or pre-answer its work.",
            "- If the request spans several sub-agents, handle one sub-agent per turn and confirm before moving on.",
            "- If no sub-agent fits, say so and ask a clarifying question rather than inventing an answer.",
        ]
        return "\n".join(lines)


def generate_connected_solution(
    spec: ConnectedSolutionSpec,
    output_path: Optional[Path] = None,
) -> bytes:
    """Build a connected (multi-bot) solution zip from a ConnectedSolutionSpec."""
    return ConnectedSolutionPackager(spec).package(output_path=output_path)


# ============================================================================
# Build sub-agents from an agent stack (agents/*.py + metadata.json) and validate
# ============================================================================

def _humanize(name: str) -> str:
    name = re.sub(r"_stacks$", "", name or "")
    name = name.replace("_", " ").replace("-", " ").strip()
    name = re.sub(r"([a-z])([A-Z])", r"\1 \2", name)
    return " ".join(w[:1].upper() + w[1:] for w in name.split())


def _humanize_class(name: str) -> str:
    name = re.sub(r"Agent$", "", name or "")
    name = re.sub(r"_agent$", "", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    name = name.replace("_", " ").strip()
    return " ".join(w[:1].upper() + w[1:] for w in name.split())


def _safe_literal(node):
    try:
        return ast.literal_eval(node)
    except Exception:
        return None


# Class-body literals a converted agent.py embeds. CAPIR is the compiled CapIR
# (perform()'s spec); SYNTHETIC_DATA holds the seeded records (the build keeps
# them OUT of the CapIR binding, so we re-inject them); the rest let us recompile
# a CapIR when one was not embedded.
_RECOVERED_ATTRS = {"CAPIR", "SYNTHETIC_DATA", "KNOWLEDGE", "RESPONSE",
                    "DOC_NAME", "CUSTOMER", "TRIGGERS"}


def _parse_basic_agent(py_path: Path):
    """AST-extract (display_name, agent_name, description, module_doc, params,
    recovered) from a BasicAgent .py — `recovered` carries any embedded CapIR /
    seeded records used to build the deterministic capability topic."""
    src = py_path.read_text(encoding="utf-8", errors="replace")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    module_doc = (ast.get_docstring(tree) or "").strip()

    cls = None
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and any(
            isinstance(b, ast.Name) and b.id == "BasicAgent" for b in node.bases
        ):
            cls = node
            break
    if cls is None:
        return None

    self_name = None
    description = ""
    params = []  # (name, description, required)
    recovered = {}  # class-level CAPIR / SYNTHETIC_DATA / ... for deterministic topics
    for sub in ast.walk(cls):
        if not isinstance(sub, ast.Assign):
            continue
        for tgt in sub.targets:
            # class-body literals the build stage embeds (CAPIR = {...},
            # SYNTHETIC_DATA = [...], KNOWLEDGE / RESPONSE / DOC_NAME / CUSTOMER / TRIGGERS)
            if isinstance(tgt, ast.Name) and tgt.id in _RECOVERED_ATTRS:
                val = _safe_literal(sub.value)
                if val is not None:
                    recovered[tgt.id] = val
                continue
            if not (isinstance(tgt, ast.Attribute) and isinstance(tgt.value, ast.Name)
                    and tgt.value.id == "self"):
                continue
            if tgt.attr == "name" and isinstance(sub.value, ast.Constant) and isinstance(sub.value.value, str):
                self_name = sub.value.value
            elif tgt.attr == "metadata" and isinstance(sub.value, ast.Dict):
                # Walk the dict node key-by-key: the metadata literal contains a
                # non-literal value ("name": self.name), so literal_eval on the
                # whole dict fails — pull the literal keys we care about directly.
                for k, v in zip(sub.value.keys, sub.value.values):
                    key = k.value if isinstance(k, ast.Constant) else None
                    if key == "description":
                        dv = _safe_literal(v)
                        if isinstance(dv, str):
                            description = dv.strip()
                    elif key == "parameters":
                        pv = _safe_literal(v)
                        if isinstance(pv, dict):
                            props = pv.get("properties") or {}
                            req = set(pv.get("required") or [])
                            for pn, pinfo in props.items():
                                pdesc = (pinfo.get("description") if isinstance(pinfo, dict) else "") or pn
                                params.append((pn, pdesc, pn in req))

    stem_name = re.sub(r"_agent$", "", py_path.stem)
    agent_name = stem_name
    display = _humanize_class(self_name or stem_name)
    if not description:
        # First paragraph of the module docstring.
        description = re.sub(r"\s+", " ", module_doc.split("\n\n")[0]).strip()
    # Statically infer the SHAPE of the data this agent works with (the dict keys
    # its perform()/helpers read & write) so we can synthesize matching static
    # stand-in records — no execution, no domain rules.
    recovered["INFERRED_FIELDS"] = _infer_record_fields(tree, exclude=[p[0] for p in params])
    return display, agent_name, description, module_doc, params, recovered


def _stack_subagent_instructions(display, description, module_doc, params) -> str:
    """The sub-agent's brain: self-documents the agent.py end-to-end — its purpose
    and its FULL input contract (what the orchestrator passes to delegate). Generic
    for ANY agent.py; no domain assumptions."""
    lines = [f"You are the {display} agent.", "", "# Purpose"]
    lines.append(module_doc.strip() if module_doc else (description or f"Handle {display} requests."))
    lines += ["", "# Inputs the orchestrator passes you"]
    if params:
        for pn, pdesc, required in params:
            tag = "required" if required else "optional"
            clean = re.sub(r"\s+", " ", pdesc).strip()
            lines.append(f"- {pn} ({tag}): {clean}")
    else:
        lines.append("- No structured inputs are required; use the user's request directly.")
    lines += ["", "# How you answer",
              "- Run your deterministic capability topic and ground every answer in its seeded records.",
              "- That seeded data is SYNTHETIC stand-in data for your real source system, so you load "
              "and run end-to-end with no live connection. Swapping the topic's Table() for the live "
              "connector takes you to production with no change to the logic.",
              "- Stay in your lane: if the request belongs to another connected agent, say so and let "
              "the orchestrator route it."]
    return "\n".join(lines)


def _contract_description(description, params, limit=850):
    """The orchestrator-facing routing description: the agent's purpose PLUS its
    input contract, so the Copilot Studio agent knows what to pass when it
    delegates. Self-documenting, generic, length-capped for the component."""
    base = re.sub(r"\s+", " ", description or "").strip()
    if params:
        ins = "; ".join("%s (%s)" % (pn, "required" if req else "optional")
                        for pn, _pd, req in params)
        base = (base + " Inputs to pass: " + ins + ".").strip()
    return base[:limit]


# t2p-capir/1.0 — the load-bearing perform() constants, mirrored so a recompiled
# CapIR carries the same numbers the agent.py uses.
_CAPIR_SCHEMA = "t2p-capir/1.0"
_RECOMPILE_CONSTS = {
    "word_min_len": 3, "example_take": 2, "fallback_take": 2, "pdf_records": 3,
    "pdf_prepared": "Prepared for {customer}",
    "pdf_footer": "Synthetic demo data - no customer data was needed.",
}


# Envelope / structural dict keys that are NOT data columns, so schema inference
# never mistakes the result wrapper for record fields.
_ENVELOPE_KEYS = {"status", "agent", "data", "parameters", "properties",
                  "required", "type", "name", "description", "items", "enum",
                  "error", "result", "results", "success", "ok", "count", "as_of_utc"}
# Objects whose `.get("x")` calls are NOT record reads (input kwargs, env, etc.).
_SKIP_GET_OBJS = {"kwargs", "self", "metadata", "os", "sys", "environ", "params", "config"}


def _flatten_record(r):
    """Flatten one record to top-level scalar fields (the Table()/filter columns):
    a nested dict is merged up one level; lists/dicts are json-encoded to strings."""
    if not isinstance(r, dict):
        return {}
    out = {}
    for k, v in r.items():
        if isinstance(v, dict):
            for kk, vv in v.items():
                out[str(kk)] = vv if not isinstance(vv, (list, dict)) else json.dumps(vv, ensure_ascii=False)
        elif isinstance(v, list):
            out[str(k)] = json.dumps(v, ensure_ascii=False)
        else:
            out[str(k)] = v
    return out


def _infer_record_fields(tree, exclude=None, max_fields=14):
    """Infer the SHAPE of the data an agent.py works with by statically scanning
    its code for the dict keys it reads/writes: `rec.get("field")`, `rec["field"]`
    and `{"field": ...}` literals. Excludes input-param names + envelope keys so
    only genuine data columns remain. 100% static — no execution, no domain rules."""
    exclude = set(exclude or []) | _ENVELOPE_KEYS
    keys = []

    def add(k):
        if (isinstance(k, str) and k and k.isidentifier()
                and k not in exclude and k not in keys):
            keys.append(k)

    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == "get" and node.args):
            obj = node.func.value
            if isinstance(obj, ast.Name) and obj.id in _SKIP_GET_OBJS:
                continue
            a = node.args[0]
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                add(a.value)
        elif isinstance(node, ast.Subscript):
            sl = node.slice
            if isinstance(sl, ast.Constant) and isinstance(sl.value, str):
                add(sl.value)
        elif isinstance(node, ast.Dict):
            klits = [k.value for k in node.keys
                     if isinstance(k, ast.Constant) and isinstance(k.value, str)]
            if "status" in klits and "data" in klits:
                continue  # a result-envelope literal, not a data record
            for k in klits:
                add(k)
    return keys[:max_fields]


def _synthesize_value(field, i):
    """A clearly-synthetic, generic value for `field` on row i — typed by the field
    NAME's TOKENS only (token-matched, so "age" never fires inside "message"). No
    domain knowledge. Deterministic (index-based, no RNG)."""
    f = field.lower()
    toks = set(t for t in re.split(r"[^a-z0-9]+", f) if t)
    if toks & {"prob", "probability", "score", "rate", "ratio", "pct", "percent",
               "confidence", "likelihood", "fail", "risk"}:
        return round(0.15 + 0.7 * (((i - 1) % 5) / 4.0), 2)   # 0.15 .. 0.85
    if f.startswith(("is_", "has_")) or toks & {"enabled", "active", "flag", "bool"}:
        return (i % 2 == 0)
    if toks & {"date", "time", "utc", "timestamp", "datetime", "created", "updated"}:
        return "2026-01-%02dT00:00:00Z" % min(i, 28)
    if toks & {"id", "guid", "uuid", "code", "ref"}:
        return "%s-%04d" % ((re.sub(r"[^A-Za-z]", "", field).upper()[:4] or "REC"), i)
    if toks & {"count", "qty", "quantity", "amount", "price", "cost", "value", "age",
               "days", "years", "hours", "num", "number", "level", "index", "size",
               "total", "kv", "voltage", "pct"}:
        return i * 10
    return "synthetic %s %d" % (f.replace("_", " "), i)


def _synthesize_records(fields, n=5):
    """Generate n self-documenting STATIC stand-in records over `fields` — the
    synthetic data that lets the topic load and run end-to-end with no live
    connection. Generic for any field set; swap the Table() for the live connector."""
    fields = [f for f in (fields or []) if f] or ["id", "label", "detail"]
    return [{f: _synthesize_value(f, i) for f in fields} for i in range(1, n + 1)]


def _resolve_capir(recovered, display, agent_name, description, params, capir_mode):
    """Decide the CapIR a sub-agent's deterministic topic is built from — the
    topic that IS this agent.py's perform() running on STATIC stand-in data, so
    the Copilot Studio orchestrator gets the same result it would by chatting the
    brainstem and invoking the agent.py.

    Policy (capir_mode):
      off       -> never emit a topic (instructions-blob only)
      embedded  -> only when the agent.py embeds a CAPIR literal
      static    -> embedded, else recompile ONLY from real seeded data
                   (SYNTHETIC_DATA); do not synthesize a stand-in
      auto      -> (default) embedded, else recompile from SYNTHETIC_DATA, else
                   SYNTHESIZE static stand-in data from the agent's inferred data
                   shape. Maps EVERY agent.py to a self-documented topic."""
    mode = (capir_mode or "auto").lower()
    if mode in ("capture", "always", "run"):
        mode = "auto"
    if mode == "off":
        return None
    synth = recovered.get("SYNTHETIC_DATA") or []
    embedded = recovered.get("CAPIR")
    if isinstance(embedded, dict) and embedded.get("steps"):
        binding = dict(embedded.get("binding") or {})
        if not binding.get("records"):
            binding["records"] = synth
        if not binding.get("fields"):
            binding["fields"] = _capir_topic_fields(binding.get("records"))
        out = {**embedded, "binding": binding}
        out.setdefault("customer", recovered.get("CUSTOMER") or "the customer")
        return out
    if mode == "embedded":
        return None
    if mode == "static":
        return _recompile_capir_from_meta(recovered, display, agent_name, description,
                                          params, records=synth) if synth else None
    # auto: always map — real seeded data if present, else a STATIC stand-in
    # synthesized from the agent's inferred data shape (its perform() field reads).
    records = synth
    if not records:
        fields = recovered.get("INFERRED_FIELDS") or [p[0] for p in (params or [])]
        records = _synthesize_records(fields)
    return _recompile_capir_from_meta(recovered, display, agent_name, description,
                                      params, records=records)


def _recompile_capir_from_meta(recovered, display, agent_name, description, params, records=None):
    """Build a CapIR for an agent.py with no embedded CAPIR — mirrors T2P's
    _compile_capir shape from its records (real or synthesized), KNOWLEDGE,
    RESPONSE, DOC_NAME, TRIGGERS plus the parsed metadata. Same structure and
    perform()-parity constants as the generated path; only the source differs."""
    records = [_flatten_record(r) for r in (records if records is not None
               else (recovered.get("SYNTHETIC_DATA") or []))][:10]
    knowledge = list(recovered.get("KNOWLEDGE") or [])
    triggers = list(recovered.get("TRIGGERS") or [])
    if not triggers:
        triggers = [display] + ([re.sub(r"\s+", " ", description).strip()[:60]]
                                if description else [])
    response = recovered.get("RESPONSE") or description or f"Here is how I handle {display}."
    doc = recovered.get("DOC_NAME") or None
    key = re.sub(r"[^a-z0-9_]", "", (agent_name or display).lower().replace(" ", "_")) or "capability"
    fields = _capir_topic_fields(records)
    prompt = f"What would you like to ask the {display} agent? (a keyword, id, or value to filter on)"
    binding = {
        "connector": "table",
        "table": "rec_" + key,
        "library": display + " Library",
        "fields": fields,
        "key_field": fields[0] if fields else "id",
        "row_count": len(records),
        "records": records,
    }
    steps = [
        {"id": "trigger", "op": "trigger_match", "queries": triggers},
        {"id": "slot_query", "op": "slot_fill", "slot": "query"},
        {"id": "ground", "op": "knowledge_lookup", "facts": knowledge, "into": "Grounding"},
        {"id": "lookup", "op": "record_lookup", "source": "binding", "from": "query",
         "into": "Matches", "take": _RECOMPILE_CONSTS["example_take"],
         "fallback_take": _RECOMPILE_CONSTS["fallback_take"]},
        {"id": "respond", "op": "respond", "template_kind": "standard"},
    ]
    if doc:
        steps.append({"id": "artifact", "op": "artifact", "doc": doc,
                      "from": ["Grounding", "Matches"]})
    return {
        "schema": _CAPIR_SCHEMA,
        "key": key,
        "response": response,
        "customer": recovered.get("CUSTOMER") or "the customer",
        "binding": binding,
        "slots": [{"name": "query", "entity": "StringPrebuiltEntity",
                   "prompt": prompt, "required": True}],
        "consts": dict(_RECOMPILE_CONSTS),
        "steps": steps,
        "expect": list(triggers),
        "triggers_owned": True,
    }


def _subagents_from_stack(stack_dir: Path, capir_mode: str = "auto") -> List[SubAgentSpec]:
    agents_dir = stack_dir / "agents"
    if not agents_dir.is_dir():
        agents_dir = stack_dir
    subs: List[SubAgentSpec] = []
    for py in sorted(agents_dir.glob("*.py")):
        if py.name.startswith("_") or py.name == "basic_agent.py":
            continue
        parsed = _parse_basic_agent(py)
        if not parsed:
            logger.warning("  - %s: no BasicAgent subclass, skipping", py.name)
            continue
        display, agent_name, description, module_doc, params, recovered = parsed
        capir = _resolve_capir(recovered, display, agent_name, description, params, capir_mode)
        subs.append(SubAgentSpec(
            agent_name=agent_name,
            display_name=display,
            # description carries the input contract so the orchestrator knows what
            # to pass when it delegates (self-documented, like the agent.py).
            description=_contract_description(description, params) or f"Handle {display} requests.",
            instructions=_stack_subagent_instructions(display, description, module_doc, params),
            capir=capir,
            params=params,
        ))
        logger.info("  + %s%s", display, "  [deterministic topic]" if capir else "")
    return subs


def _load_stack_metadata(stack_dir: Path) -> dict:
    mpath = stack_dir / "metadata.json"
    if mpath.is_file():
        try:
            return json.loads(mpath.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def _orchestrator_instructions_from_metadata(meta: dict, subs: List[SubAgentSpec]) -> str:
    name = meta.get("name", "the agent stack")
    desc = meta.get("description", "")
    lines = [f"You are the orchestrator for {name}.", ""]
    if desc:
        lines += [desc, ""]
    lines.append("You route each user request to the right connected sub-agent and never do their specialized work yourself.")
    features = meta.get("features") or []
    if features:
        lines += ["", "End-to-end flow this stack supports, in order:"]
        lines += [f"- {f}" for f in features]
    lines += ["", "Connected sub-agents you can delegate to:"]
    for sub in subs:
        lines.append(f"- {sub.display_name}: {sub.description}")
    starters = meta.get("starters") or []
    if starters:
        lines += ["", "Example requests you should expect:"]
        lines += [f"- {s}" for s in starters]
    lines += [
        "",
        "Routing rules:",
        "- Pick the single best-matching connected agent for the request and delegate to it; pass it the inputs named in its description.",
        "- Calling a connected agent gives you the SAME result you would get by chatting the source brainstem and letting it invoke that agent.py — each connected agent's topic runs the agent's deterministic logic on its seeded sample data.",
        "- If a request spans several connected agents, handle one per turn, show its result, then continue to the next.",
        "- If a required input is missing, ask for it. The seeded data is synthetic stand-in data; do not invent records beyond it.",
        "- If no connected agent fits, say so and ask a clarifying question.",
    ]
    return "\n".join(lines)


def validate_connected_solution(zip_path: Path) -> bool:
    """Structural checks that the connected solution is import-shaped."""
    ok = True
    with zipfile.ZipFile(zip_path, "r") as zf:
        names = set(zf.namelist())

        for required in ("[Content_Types].xml", "solution.xml", "customizations.xml"):
            if required not in names:
                logger.error("  X missing %s", required)
                ok = False

        bots = sorted({n.split("/")[1] for n in names if n.startswith("bots/")})
        logger.info("  bots: %d (%s)", len(bots), ", ".join(bots))

        # Every connected-action must reference an existing child bot.
        actions = [n for n in names if ".InvokeConnectedAgentTaskAction." in n and n.endswith("/dependencies.json")]
        logger.info("  connected-agent actions: %d", len(actions))
        for dep in actions:
            child = json.loads(zf.read(dep).decode("utf-8"))[0]["schemaName"]
            if f"bots/{child}/bot.xml" not in names:
                logger.error("  X action %s -> missing child bot %s", dep, child)
                ok = False
            data_path = dep.rsplit("/", 1)[0] + "/data"
            if data_path in names:
                data_text = zf.read(data_path).decode("utf-8")
                if f"botSchemaName: {child}" not in data_text:
                    logger.error("  X %s data does not invoke %s", data_path, child)
                    ok = False

        # Every extensionless /data part must be declared in [Content_Types].xml.
        ct = zf.read("[Content_Types].xml").decode("utf-8")
        data_parts = [n for n in names if n.endswith("/data")]
        missing = [p for p in data_parts if f'PartName="/{p}"' not in ct]
        if missing:
            logger.error("  X %d /data parts missing from [Content_Types].xml (e.g. %s)",
                         len(missing), missing[0])
            ok = False
        else:
            logger.info("  content-types: all %d /data parts declared", len(data_parts))

        # Each bot needs gpt.default + the system-topic set.
        for bot in bots:
            if f"botcomponents/{bot}.gpt.default/data" not in names:
                logger.error("  X bot %s missing gpt.default", bot)
                ok = False

        # No botcomponent schema name may exceed the Dataverse 100-char limit.
        schemas = {n.split("/")[1] for n in names if n.startswith("botcomponents/")}
        longest = max(schemas, key=len) if schemas else ""
        if len(longest) > 100:
            logger.error("  X schema name too long (%d > 100): %s", len(longest), longest)
            ok = False
        else:
            logger.info("  schema lengths: max %d/100 (%s)", len(longest), longest)

        # Copilot Studio rejects bot display names longer than 42 chars.
        worst_name, worst_len = "", 0
        for bot in bots:
            bx = zf.read(f"bots/{bot}/bot.xml").decode("utf-8")
            m = re.search(r"<name>(.*?)</name>", bx, re.DOTALL)
            nm = (m.group(1).strip() if m else "")
            if len(nm) > worst_len:
                worst_name, worst_len = nm, len(nm)
        if worst_len > 42:
            logger.error("  X bot name too long (%d > 42): %s", worst_len, worst_name)
            ok = False
        else:
            logger.info("  bot names: max %d/42 (%s)", worst_len, worst_name)
    return ok


# ===========================================================================
# Autonomous deploy to Microsoft Copilot Studio (Dataverse Web API, stdlib only)
#
# Self-contained so this one file, dropped into any brainstem, can BOTH package a
# connected-agents solution AND import + publish it into a real Copilot Studio
# environment — no pac CLI, no third-party packages. App-registration credentials
# come ONLY from env vars or a settings file, never from chat, and the secret is
# never echoed back. Same proven path as the T2P deploy agent: service-principal
# token -> ImportSolution -> PvaPublish (children first, orchestrator last).
# ===========================================================================

_DEPLOY_AUTH = "https://login.microsoftonline.com"


def _http(url, data=None, headers=None, method=None, timeout=300):
    """Minimal stdlib HTTP: dict data -> form-encoded (OAuth), else JSON bytes."""
    if isinstance(data, dict):
        data = urllib.parse.urlencode(data).encode()
    elif data is not None and not isinstance(data, (bytes, bytearray)):
        data = json.dumps(data).encode()
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read().decode("utf-8", "replace")
            return r.status, (json.loads(body) if body[:1] in ("{", "[") else body)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, body
    except Exception as e:  # network / DNS / timeout
        return 0, str(e)


def _extract_dyn_creds(creds):
    """From a settings dict ({IsEncrypted,Values} or bare), a Values dict, or a
    JSON string -> {client_id, client_secret, tenant_id, resource} or None."""
    if isinstance(creds, str):
        try:
            creds = json.loads(creds)
        except Exception:
            return None
    if not isinstance(creds, dict):
        return None
    vals = creds.get("Values", creds)
    cid, sec = vals.get("DYNAMICS_365_CLIENT_ID"), vals.get("DYNAMICS_365_CLIENT_SECRET")
    ten, res = vals.get("DYNAMICS_365_TENANT_ID"), vals.get("DYNAMICS_365_RESOURCE")
    if not all([cid, sec, ten, res]):
        return None
    return {"client_id": cid, "client_secret": sec, "tenant_id": ten, "resource": str(res).rstrip("/")}


def _deploy_creds(kwargs):
    """Resolve app-registration creds for deploy — env / settings file ONLY, never
    from chat. Returns (creds_dict, source_label) or (None, None)."""
    candidates = [
        os.path.expanduser(kwargs["credentials_path"]) if kwargs.get("credentials_path") else None,
        os.environ.get("RAPP_DEPLOY_SETTINGS"),
        os.path.expanduser("~/.rapp_deploy_settings.json"),
        "local.settings.json",
    ]
    for cand in candidates:
        if cand and os.path.isfile(cand):
            try:
                c = _extract_dyn_creds(json.load(open(cand)))
                if c:
                    return c, cand
            except Exception:
                pass
    c = _extract_dyn_creds({"Values": dict(os.environ)})
    if c:
        return c, "process env"
    return None, None


def _sp_token(client_id, secret, tenant, resource):
    """Service-principal (client-credentials) token for the Dataverse env."""
    code, t = _http(f"{_DEPLOY_AUTH}/{tenant}/oauth2/v2.0/token",
                    data={"grant_type": "client_credentials", "client_id": client_id,
                          "client_secret": secret, "scope": resource.rstrip("/") + "/.default"},
                    headers={"Content-Type": "application/x-www-form-urlencoded"})
    if code != 200 or not isinstance(t, dict) or "access_token" not in t:
        raise RuntimeError("service-principal auth failed: " + str(t)[:200])
    return t["access_token"]


def _dataverse_action(resource, token, action, body=None, method="POST"):
    data = json.dumps(body).encode() if body is not None else None
    return _http(resource.rstrip("/") + "/api/data/v9.2/" + action, data=data, method=method,
                 headers={"Authorization": "Bearer " + token, "Content-Type": "application/json",
                          "Accept": "application/json", "OData-MaxVersion": "4.0",
                          "OData-Version": "4.0"})


def _import_solution(resource, token, zip_bytes):
    """ImportSolution (unmanaged, overwrite) then PublishAllXml."""
    code, r = _dataverse_action(resource, token, "ImportSolution", {
        "OverwriteUnmanagedCustomizations": True, "PublishWorkflows": True,
        "ImportJobId": str(uuid.uuid4()),
        "CustomizationFile": base64.b64encode(zip_bytes).decode()})
    if code not in (200, 204):
        raise RuntimeError("ImportSolution failed (%s): %s" % (code, str(r)[:400]))
    _dataverse_action(resource, token, "PublishAllXml")


def _find_botid(resource, token, schema):
    qs = urllib.parse.urlencode({"$select": "botid,schemaname",
                                 "$filter": "schemaname eq '%s'" % schema,
                                 "$orderby": "createdon desc", "$top": "1"})
    code, r = _http(resource.rstrip("/") + "/api/data/v9.2/bots?" + qs,
                    headers={"Authorization": "Bearer " + token, "Accept": "application/json"})
    rows = (r.get("value") if isinstance(r, dict) else None) or []
    return rows[0]["botid"] if rows else None


def _publish_botid(botid, resource, token):
    """Publish ONE bot via the Dataverse PvaPublish Web API action. PURE HTTPS —
    no pac/CLI/subprocess — so this agent.py runs identically in a local brainstem
    AND inside an Azure-Function-hosted brainstem (no binary to ship)."""
    code, r = _dataverse_action(resource, token,
                                "bots(%s)/Microsoft.Dynamics.CRM.PvaPublish" % botid, {})
    if code in (200, 204):
        return {"bot_id": botid, "status": "publish_requested", "via": "PvaPublish"}
    return {"bot_id": botid, "status": "publish_failed", "via": "PvaPublish", "error": str(r)[:160]}


def _publish_connected(bot_schemas, resource, token):
    """Publish every bot — CHILDREN first, ORCHESTRATOR last (a connected-agent
    root cannot publish until its invoked sub-agents are published)."""
    if not bot_schemas:
        return []
    orch = bot_schemas[0]
    order = list(bot_schemas[1:]) + [orch]
    out = []
    for schema in order:
        botid = _find_botid(resource, token, schema)
        if not botid:
            out.append({"schema": schema, "status": "not_found"})
            continue
        out.append({"schema": schema, **_publish_botid(botid, resource, token)})
    return out


def _run_deploy(zip_bytes, bot_schemas, orch_display, kwargs):
    """Import + (optionally) publish the connected solution into Copilot Studio.
    Returns a result dict with a human `summary`; never includes the secret."""
    creds, src = _deploy_creds(kwargs)
    if creds and kwargs.get("environment_url"):
        creds = {**creds, "resource": str(kwargs["environment_url"]).rstrip("/")}
    if not creds:
        return {"status": "creds_missing",
                "summary": "NOT deployed — no app-registration credentials found.",
                "how_to": ("Set env DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / "
                           "DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE, or pass "
                           "credentials_path=<local.settings.json>, or place "
                           "~/.rapp_deploy_settings.json. Secrets never travel through chat.")}
    publish = bool(kwargs.get("publish", True))
    try:
        token = _sp_token(creds["client_id"], creds["client_secret"],
                          creds["tenant_id"], creds["resource"])
    except Exception as e:
        return {"status": "auth_failed", "summary": "NOT deployed — service-principal auth failed.",
                "error": str(e)[:300], "creds_source": src, "environment": creds["resource"]}
    try:
        _import_solution(creds["resource"], token, zip_bytes)
    except Exception as e:
        return {"status": "import_failed", "summary": "Import FAILED.", "error": str(e)[:400],
                "environment": creds["resource"], "creds_source": src}
    published = _publish_connected(bot_schemas, creds["resource"], token) if publish else []
    npub = sum(1 for p in published if p.get("status") in ("published", "publish_requested"))
    summary = ("Imported into " + creds["resource"] + " and "
               + (("published %d/%d bots. " % (npub, len(published))) if publish else "skipped publish. ")
               + "Open Copilot Studio, select that environment, open '"
               + orch_display[:42] + "' and use the Test pane.")
    return {"status": "deployed", "summary": summary, "environment": creds["resource"],
            "orchestrator": orch_display[:42], "publish_enabled": publish,
            "published": published, "creds_source": src,
            "test_in_studio": "https://copilotstudio.microsoft.com"}


# ---------------------------------------------------------------------------
# RAPP agent wrapper
# ---------------------------------------------------------------------------

class ConnectedSolutionAgent(BasicAgent):
    """Generate a connected-agent (orchestrator + sub-agents) Copilot Studio solution."""

    def __init__(self):
        self.name = "ConnectedSolutionAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Turn an agent stack (a folder of BasicAgent *.py files + optional "
                "metadata.json) or an explicit list of sub-agents into ONE import-ready "
                "Microsoft Copilot Studio connected-agent solution: an orchestrator plus "
                "one connected sub-agent per agent, wired with InvokeConnectedAgentTaskAction. "
                "When an agent.py carries its compiled CapIR (t2p-capir/1.0) — or one can be "
                "recompiled from its seeded data — each sub-agent ALSO gets a REAL "
                "deterministic capability topic that runs the same steps as the agent.py's "
                "perform() (trigger -> the user's real query -> filter the seeded records -> "
                "branch -> respond, plus the document for artifact capabilities); only the "
                "data is mocked, so flipping the in-topic Table() to a live Dataverse / "
                "SharePoint connector is the one-line move to production. No code deploy. Bot "
                "names are auto-capped to 42 chars and orchestrator channels default off so it "
                "imports and publishes fully headlessly."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "stack_dir": {
                        "type": "string",
                        "description": "Path to an agent stack folder. Each BasicAgent *.py under it "
                                       "(or its agents/ subfolder) becomes one connected sub-agent; "
                                       "metadata.json (name/description/features/starters) shapes the orchestrator.",
                    },
                    "subagents": {
                        "type": "array",
                        "description": "Alternative to stack_dir: explicit sub-agents, each an object with "
                                       "agent_name, display_name, description, instructions.",
                    },
                    "solution_name": {
                        "type": "string",
                        "description": "Solution unique name (alphanumeric). Defaults from metadata.json id / stack folder name.",
                    },
                    "solution_display_name": {"type": "string", "description": "Solution friendly name."},
                    "orchestrator_name": {
                        "type": "string",
                        "description": "Orchestrator display name (auto-capped to 42 chars, 'Orchestrator' kept).",
                    },
                    "orchestrator_channels": {
                        "type": "boolean",
                        "description": "Declare MsTeams + M365 Copilot channels on the orchestrator. Default false "
                                       "(headlessly publishable). True requires a maker-portal publish.",
                    },
                    "capir_mode": {
                        "type": "string",
                        "description": "How to build the deterministic per-capability topic inside each "
                                       "sub-agent (the topic that runs the agent.py's perform() logic on STATIC "
                                       "synthetic stand-in data): 'auto' (default) uses an embedded CapIR, else "
                                       "real seeded data, else SYNTHESIZES static stand-in records from the "
                                       "agent's inferred data shape — so EVERY agent.py maps to a self-documented "
                                       "topic; 'static' uses only real seeded data (no synthetic stand-in); "
                                       "'embedded' uses only an embedded CapIR; 'off' emits instructions-only "
                                       "sub-agents. Synthetic data is the swap-for-live seam (Table() -> connector).",
                    },
                    "version": {"type": "string", "description": "Solution version, e.g. 1.0.0.0."},
                    "output_path": {
                        "type": "string",
                        "description": "Where to write the .zip. Defaults to <SolutionName>_connected_solution.zip.",
                    },
                    "deploy": {
                        "type": "boolean",
                        "description": "When true, AUTONOMOUSLY import the solution into your Microsoft Copilot "
                                       "Studio (Dataverse) environment and publish every bot (sub-agents first, "
                                       "orchestrator last) — no pac CLI needed, stdlib only. App-registration "
                                       "credentials are read ONLY from env vars (DYNAMICS_365_CLIENT_ID / "
                                       "DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) "
                                       "or a settings file — NEVER from chat. Default false (package only).",
                    },
                    "publish": {
                        "type": "boolean",
                        "description": "When deploy=true, also publish the bots after import (default true). "
                                       "false imports without publishing.",
                    },
                    "credentials_path": {
                        "type": "string",
                        "description": "Path to a local.settings.json-style file holding DYNAMICS_365_CLIENT_ID / "
                                       "DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE "
                                       "(under a top-level 'Values' object or at the root). Used only for deploy; "
                                       "the secret is never echoed back. If omitted, env vars / "
                                       "~/.rapp_deploy_settings.json / ./local.settings.json are tried.",
                    },
                    "environment_url": {
                        "type": "string",
                        "description": "Optional override for the target Dataverse environment URL (e.g. "
                                       "https://yourorg.crm.dynamics.com). Defaults to DYNAMICS_365_RESOURCE from the creds.",
                    },
                    "publisher_prefix": {
                        "type": "string",
                        "description": "Customization prefix for the bot schema names (2-8 lowercase alphanumerics, "
                                       "default 'rapp'). Use a FRESH prefix to mint brand-new, isolated bots + a "
                                       "distinct solution instead of updating ones that already exist.",
                    },
                    "publisher_name": {
                        "type": "string",
                        "description": "Solution publisher unique name (default 'DefaultPublisher'). Pair a fresh "
                                       "publisher_name with a fresh publisher_prefix to create a brand-new publisher.",
                    },
                    "publisher_display": {
                        "type": "string",
                        "description": "Solution publisher friendly name (default 'Default Publisher').",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        stack_dir = kwargs.get("stack_dir")
        subagents_in = kwargs.get("subagents")
        if not stack_dir and not subagents_in:
            return {
                "status": "needs_input",
                "agent": self.name,
                "message": "Provide 'stack_dir' (a folder of BasicAgent *.py + optional metadata.json) "
                           "or 'subagents' (a list of {agent_name, display_name, description, instructions}).",
            }

        meta: Dict[str, Any] = {}
        if stack_dir:
            sd = Path(stack_dir)
            if not sd.exists():
                return {"status": "error", "agent": self.name, "message": f"stack_dir not found: {sd}"}
            subs = _subagents_from_stack(sd, capir_mode=str(kwargs.get("capir_mode") or "auto"))
            meta = _load_stack_metadata(sd)
            fallback = _humanize(sd.name)
        else:
            subs = []
            for s in subagents_in:
                dn = s.get("display_name") or s.get("agent_name") or "Agent"
                subs.append(SubAgentSpec(
                    agent_name=s.get("agent_name") or dn,
                    display_name=dn,
                    description=(s.get("description") or "").strip() or f"Handle {dn} requests.",
                    instructions=s.get("instructions") or "",
                    capir=s.get("capir") if isinstance(s.get("capir"), dict) else None,
                ))
            fallback = kwargs.get("solution_name") or "Connected Agents"

        if not subs:
            return {"status": "error", "agent": self.name, "message": "No sub-agents found to bundle."}

        short = re.sub(r"\b(Agent\s+Stack|Agent|Stack)\b", "", meta.get("name", "")).strip()
        unique = re.sub(r"[^A-Za-z0-9]", "",
                        kwargs.get("solution_name") or meta.get("id", "") or fallback.replace(" ", ""))
        display = kwargs.get("solution_display_name") or meta.get("name") or f"{fallback} Agents"
        orch_name = kwargs.get("orchestrator_name") or f"{short or fallback} Orchestrator"
        orch_instructions = _orchestrator_instructions_from_metadata(meta, subs) if meta else ""

        spec = ConnectedSolutionSpec(
            solution_unique_name=unique or "ConnectedAgents",
            solution_display_name=display,
            orchestrator_display_name=orch_name,
            subagents=subs,
            orchestrator_instructions=orch_instructions,
            orchestrator_channels=bool(kwargs.get("orchestrator_channels", False)),
            solution_version=kwargs.get("version", "1.0.0.0"),
            # publisher controls — a fresh publisher_prefix mints brand-new bot
            # schema names (an isolated, clearly-distinct solution), instead of
            # updating bots that already exist under the default 'rapp' prefix.
            publisher_prefix=re.sub(r"[^a-z0-9]", "", str(kwargs.get("publisher_prefix") or _DEFAULT_PUBLISHER_PREFIX).lower())[:8] or _DEFAULT_PUBLISHER_PREFIX,
            publisher_unique_name=kwargs.get("publisher_name") or "DefaultPublisher",
            publisher_display_name=kwargs.get("publisher_display") or "Default Publisher",
        )
        packager = ConnectedSolutionPackager(spec)
        out = Path(kwargs.get("output_path") or f"{spec.solution_unique_name}_connected_solution.zip")
        data = packager.package(output_path=out)
        ok = validate_connected_solution(out)

        # autonomous deploy: import into Copilot Studio + publish the bots
        # (children first, orchestrator last). Creds come ONLY from env / a
        # settings file — never from chat.
        deploy_result = _run_deploy(data, list(packager.bot_schemas), display, kwargs) \
            if kwargs.get("deploy") else None

        capir_topics = sum(1 for s in subs if getattr(s, "capir", None))
        msg = (f"Generated '{out.name}' — {len(packager.bot_schemas)} bots "
               f"(1 orchestrator + {len(subs)} connected sub-agents, "
               f"{capir_topics} with a deterministic capability topic), "
               f"{round(len(data)/1024,1)} KB. Validation: {'pass' if ok else 'fail'}.")
        if deploy_result:
            msg += " " + deploy_result.get("summary", "")

        data_block = {
            "solution_path": str(out),
            "size_kb": round(len(data) / 1024, 1),
            "orchestrator_schema": packager.orch_schema,
            "sub_agents": [s.display_name for s in subs],
            "capir_topics": capir_topics,
            "deterministic_topics": [s.display_name for s in subs if getattr(s, "capir", None)],
            "validation": "pass" if ok else "fail",
        }
        status = "success" if ok else "error"
        if deploy_result:
            data_block["deploy"] = deploy_result
            if deploy_result.get("status") not in ("deployed",):
                status = "partial"
        else:
            data_block["deploy_hint"] = ("Pass deploy=true to import + publish into your Copilot Studio "
                                         "environment automatically (creds from env DYNAMICS_365_CLIENT_ID/"
                                         "SECRET/TENANT_ID/RESOURCE or a settings file via credentials_path).")
            data_block["m365_exposure"] = ("Set orchestrator_channels=true and publish the orchestrator "
                                           "in the maker portal for M365/Teams exposure.")
        return {"status": status, "agent": self.name, "message": msg, "data": data_block}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    target = sys.argv[1] if len(sys.argv) > 1 else None
    if not target:
        print("usage: python connected_solution_agent.py <stack_dir> [output.zip]")
        sys.exit(1)
    out_path = sys.argv[2] if len(sys.argv) > 2 else None
    result = ConnectedSolutionAgent().perform(stack_dir=target, output_path=out_path)
    print(json.dumps(result, indent=2))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
