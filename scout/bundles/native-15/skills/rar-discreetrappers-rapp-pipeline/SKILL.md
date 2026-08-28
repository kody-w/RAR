---
name: "rar-discreetrappers-rapp-pipeline"
description: "Unified RAPP Pipeline agent for building AI agents from discovery to deployment.\n\nRECOMMENDED: Use 'auto_process' with a project_id - just drop files into Azure storage and the agent handles everything automatically, generating professional PDF reports.\n\nAll actions:\n- AUTO: auto_process (scans inputs, processes, generates reports), generate_report\n- Discovery: prepare_discovery_call, process_transcript, generate_discovery_summary\n- MVP: generate_mvp_poke, prioritize_features, define_scope, estimate_timeline, generate_full_mvp_document\n- Code: generate_agent_code, generate_agent_metadata, generate_agent_tests, generate_deployment_config, review_code\n- Quality Gates: execute_quality_gate (gate: QG1-QG6)\n- Pipeline: get_step_guidance, get_pipeline_status, recommend_next_action, get_step_checklist, validate_step_completion"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/rapp_pipeline_agent", "rar_sha256": "feb4bd1dfa316f9aaa83bea4e4c220084794d1207ebee2ba4c3d823aa6bc7b44", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.2", "author": "Bill Whalen", "tags": ["pipeline", "rapp", "transcript-to-agent", "code-gen", "quality-gates"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/rapp_pipeline_agent`. The original RAPP
agent is preserved byte-for-byte in `rapp_pipeline_agent.py` and in the RCI capsule.

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

RAPP Agent - Unified AI Agent Production Pipeline
Purpose: Single agent for ALL RAPP Pipeline operations from discovery to deployment

This unified agent consolidates all RAPP functionality:
- AUTO-PROCESS: Drop files into Azure storage, agent automatically processes and generates reports
- Discovery: Prepare calls, process transcripts, validate discovery (QG1)
- MVP: Generate proposals, prioritize features, define scope, estimate timeline
- Code: Generate agents, metadata, tests, deployment configs, review code (QG3)
- Quality Gates: Execute QG1-QG6 validations
- Pipeline: Track progress, get guidance, recommend next steps
- REPORTS: Generate professional Microsoft-style PDF reports for any step

AUTOMATED WORKFLOW:
1. Create project folder: rapp_projects/{project_id}/
2. Drop inputs into: rapp_projects/{project_id}/inputs/
   - discovery_transcript.txt - Call transcript
   - customer_feedback.txt - Customer responses
   - code_to_review.py - Code for QG3
   - deployment_metrics.json - Metrics for QG6
3. Call auto_process with project_id
4. Reports generated in: rapp_projects/{project_id}/outputs/

Use this agent for ANY RAPP Pipeline task - it handles all 14 steps.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "The RAPP operation to perform. Use 'transcript_to_agent' for fastest transcript-to-deployable-agent workflow. Use 'auto_process' for full pipeline with PDF reports.",
      "enum": [
        "transcript_to_agent",
        "auto_process",
        "generate_report",
        "prepare_discovery_call",
        "process_transcript",
        "generate_discovery_summary",
        "generate_mvp_poke",
        "prioritize_features",
        "define_scope",
        "estimate_timeline",
        "generate_full_mvp_document",
        "generate_agent_code",
        "generate_agent_metadata",
        "generate_agent_tests",
        "generate_deployment_config",
        "review_code",
        "execute_quality_gate",
        "get_step_guidance",
        "get_pipeline_status",
        "recommend_next_action",
        "get_step_checklist",
        "validate_step_completion"
      ],
      "type": "string"
    },
    "agent_description": {
      "description": "Description of agent capabilities",
      "type": "string"
    },
    "agent_name": {
      "description": "Name for generated agent (e.g., 'InventoryOptimizer')",
      "type": "string"
    },
    "agent_priority": {
      "description": "Which agent to prioritize from transcript (e.g., 'contract', 'chargeback', 'social_media')",
      "type": "string"
    },
    "constraints": {
      "description": "Timeline, budget, or technical constraints",
      "type": "object"
    },
    "customer_name": {
      "description": "Customer/company name",
      "type": "string"
    },
    "data_sources": {
      "description": "Data sources for agent integration",
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "deploy_to_storage": {
      "description": "If true, automatically upload generated agent to Azure File Storage agents/ folder (for transcript_to_agent action)",
      "type": "boolean"
    },
    "discovery_data": {
      "description": "Structured discovery data from transcript processing",
      "type": "object"
    },
    "existing_code": {
      "description": "Existing code for review or test generation",
      "type": "string"
    },
    "features": {
      "description": "List of features/capabilities",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "gate": {
      "description": "Quality gate to execute (required for execute_quality_gate action)",
      "enum": [
        "QG1",
        "QG2",
        "QG3",
        "QG4",
        "QG5",
        "QG6"
      ],
      "type": "string"
    },
    "industry": {
      "description": "Customer industry (e.g., retail, healthcare, manufacturing)",
      "type": "string"
    },
    "input_data": {
      "description": "Input data for quality gate validation or other operations",
      "type": "object"
    },
    "problem_statement": {
      "description": "Validated problem statement",
      "type": "string"
    },
    "project_data": {
      "description": "Current project progress data",
      "type": "object"
    },
    "project_id": {
      "description": "Project ID for storing results",
      "type": "string"
    },
    "project_name": {
      "description": "Project name",
      "type": "string"
    },
    "report_type": {
      "description": "Type of report to generate (for generate_report action)",
      "enum": [
        "discovery",
        "qg1",
        "qg2",
        "qg3",
        "qg4",
        "qg5",
        "qg6",
        "mvp",
        "code",
        "deployment",
        "demo",
        "executive_summary",
        "full_pipeline"
      ],
      "type": "string"
    },
    "step": {
      "description": "Pipeline step number (1-14) for guidance/checklist/validation actions",
      "maximum": 14,
      "minimum": 1,
      "type": "integer"
    },
    "transcript": {
      "description": "Discovery call transcript to process",
      "type": "string"
    },
    "user_guid": {
      "description": "User GUID for project data access",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_pipeline_agent.py` and embedded as the fenced Python below (sha256 feb4bd1dfa316f9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_pipeline_agent.py` first:

```bash
python3 rapp_pipeline_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_pipeline_agent.py   # or on stdin
python3 rapp_pipeline_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
RAPP Agent - Unified AI Agent Production Pipeline
Purpose: Single agent for ALL RAPP Pipeline operations from discovery to deployment

This unified agent consolidates all RAPP functionality:
- AUTO-PROCESS: Drop files into Azure storage, agent automatically processes and generates reports
- Discovery: Prepare calls, process transcripts, validate discovery (QG1)
- MVP: Generate proposals, prioritize features, define scope, estimate timeline
- Code: Generate agents, metadata, tests, deployment configs, review code (QG3)
- Quality Gates: Execute QG1-QG6 validations
- Pipeline: Track progress, get guidance, recommend next steps
- REPORTS: Generate professional Microsoft-style PDF reports for any step

AUTOMATED WORKFLOW:
1. Create project folder: rapp_projects/{project_id}/
2. Drop inputs into: rapp_projects/{project_id}/inputs/
   - discovery_transcript.txt - Call transcript
   - customer_feedback.txt - Customer responses
   - code_to_review.py - Code for QG3
   - deployment_metrics.json - Metrics for QG6
3. Call auto_process with project_id
4. Reports generated in: rapp_projects/{project_id}/outputs/

Use this agent for ANY RAPP Pipeline task - it handles all 14 steps.
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/rapp_pipeline_agent",
    "version": "1.0.2",
    "display_name": "RAPP",
    "description": "Runs the full RAPP pipeline \u2014 discovery, MVP, code gen, quality gates QG1-QG6, PDF reports \u2014 using Azure OpenAI and Azure File Storage.",
    "author": "Bill Whalen",
    "tags": ["pipeline", "rapp", "transcript-to-agent", "code-gen", "quality-gates"],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": ["AZURE_OPENAI_API_VERSION", "AZURE_OPENAI_DEPLOYMENT_NAME", "AZURE_OPENAI_ENDPOINT"],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import logging
import os
import re
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
from agents.basic_agent import BasicAgent
from utils.storage_factory import get_storage_manager

try:
    from openai import AzureOpenAI
    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
    AZURE_OPENAI_AVAILABLE = True
    AZURE_OPENAI_IMPORT_ERROR = None
except ImportError as e:
    AzureOpenAI = None
    DefaultAzureCredential = None
    get_bearer_token_provider = None
    AZURE_OPENAI_AVAILABLE = False
    AZURE_OPENAI_IMPORT_ERROR = str(e)

# Import report generator (optional - handles import errors gracefully)
try:
    from utils.rapp_report_generator import RAPPReportGenerator, generate_rapp_report
    REPORT_GENERATOR_AVAILABLE = True
except Exception:
    # Catches ImportError, NameError, and other module-level errors
    REPORT_GENERATOR_AVAILABLE = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_llm_json_response(response_text: str, fallback_key: str = "raw_response") -> dict:
    """Parse JSON from LLM response, handling markdown code blocks."""
    try:
        text = response_text
        if '```json' in text:
            text = text.split('```json')[-1].split('```')[0]
        elif '```' in text:
            parts = text.split('```')
            if len(parts) >= 2:
                text = parts[1]
        json_start = text.find('{')
        json_end = text.rfind('}') + 1
        if json_start >= 0 and json_end > json_start:
            return json.loads(text[json_start:json_end])
        return {fallback_key: response_text}
    except json.JSONDecodeError:
        return {fallback_key: response_text}


class RAPPAgent(BasicAgent):
    """
    Unified RAPP Pipeline Agent - handles ALL pipeline operations.

    This is the ONLY agent needed for RAPP Pipeline work. Use this agent for:
    - Discovery call preparation and transcript processing
    - MVP document generation and scope definition
    - Agent code generation and review
    - Quality gate validations (QG1-QG6)
    - Pipeline orchestration and progress tracking

    DO NOT use individual RAPP agents - use this unified agent instead.
    """

    # Pipeline step definitions
    PIPELINE_STEPS = {
        1: {"name": "Discovery Call", "type": "manual"},
        2: {"name": "Transcript Analysis", "type": "audit", "gate": "QG1"},
        3: {"name": "Generate MVP Poke", "type": "manual"},
        4: {"name": "Customer Validation", "type": "audit", "gate": "QG2"},
        5: {"name": "Generate Agent Code", "type": "manual"},
        6: {"name": "Code Quality Review", "type": "audit", "gate": "QG3"},
        7: {"name": "Deploy Prototype", "type": "manual"},
        8: {"name": "Demo Review", "type": "audit", "gate": "QG4"},
        9: {"name": "Generate Video Demo", "type": "manual"},
        10: {"name": "Final Demo Review", "type": "audit", "gate": "QG5"},
        11: {"name": "Iteration Loop", "type": "manual"},
        12: {"name": "Production Deployment", "type": "manual"},
        13: {"name": "Post-Deployment Audit", "type": "audit", "gate": "QG6"},
        14: {"name": "Scale & Maintain", "type": "manual"}
    }

    # Quality gate configurations
    GATE_CONFIGS = {
        "QG1": {"name": "Transcript Validation", "step": 2, "decisions": ["PASS", "CLARIFY", "FAIL"]},
        "QG2": {"name": "Customer Validation", "step": 4, "decisions": ["PROCEED", "REVISE", "HOLD"]},
        "QG3": {"name": "Code Quality Review", "step": 6, "decisions": ["PASS", "FIX_REQUIRED", "FAIL"]},
        "QG4": {"name": "Demo Review", "step": 8, "decisions": ["PASS", "POLISH", "FAIL"]},
        "QG5": {"name": "Final Demo Review", "step": 10, "decisions": ["APPROVE", "MINOR_REVISIONS", "MAJOR_REVISIONS", "REJECT"]},
        "QG6": {"name": "Post-Deployment Audit", "step": 13, "decisions": ["GREEN", "YELLOW", "RED"]}
    }

    # Input file patterns for auto-detection
    INPUT_PATTERNS = {
        "discovery_transcript": ["transcript", "discovery", "call_notes", "meeting_notes"],
        "customer_feedback": ["feedback", "customer_response", "validation", "approval"],
        "code_to_review": [".py"],
        "requirements": ["requirements", "mvp_requirements", "features"],
        "demo_notes": ["demo", "presentation", "video_script"],
        "deployment_metrics": ["metrics", "telemetry", "usage", "health"],
    }

    # Report types for each step
    STEP_REPORTS = {
        1: "discovery",
        2: "qg1",
        3: "mvp",
        4: "qg2",
        5: "code",
        6: "qg3",
        7: "deployment",
        8: "qg4",
        9: "demo",
        10: "qg5",
        11: "iteration",
        12: "production",
        13: "qg6",
        14: "maintenance"
    }

    def __init__(self):
        self.name = 'RAPP'
        self.metadata = {
            "name": self.name,
            "description": """Unified RAPP Pipeline agent for building AI agents from discovery to deployment.

RECOMMENDED: Use 'auto_process' with a project_id - just drop files into Azure storage and the agent handles everything automatically, generating professional PDF reports.

All actions:
- AUTO: auto_process (scans inputs, processes, generates reports), generate_report
- Discovery: prepare_discovery_call, process_transcript, generate_discovery_summary
- MVP: generate_mvp_poke, prioritize_features, define_scope, estimate_timeline, generate_full_mvp_document
- Code: generate_agent_code, generate_agent_metadata, generate_agent_tests, generate_deployment_config, review_code
- Quality Gates: execute_quality_gate (gate: QG1-QG6)
- Pipeline: get_step_guidance, get_pipeline_status, recommend_next_action, get_step_checklist, validate_step_completion""",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "description": "The RAPP operation to perform. Use 'transcript_to_agent' for fastest transcript-to-deployable-agent workflow. Use 'auto_process' for full pipeline with PDF reports.",
                        "enum": [
                            "transcript_to_agent",
                            "auto_process",
                            "generate_report",
                            "prepare_discovery_call",
                            "process_transcript",
                            "generate_discovery_summary",
                            "generate_mvp_poke",
                            "prioritize_features",
                            "define_scope",
                            "estimate_timeline",
                            "generate_full_mvp_document",
                            "generate_agent_code",
                            "generate_agent_metadata",
                            "generate_agent_tests",
                            "generate_deployment_config",
                            "review_code",
                            "execute_quality_gate",
                            "get_step_guidance",
                            "get_pipeline_status",
                            "recommend_next_action",
                            "get_step_checklist",
                            "validate_step_completion"
                        ]
                    },
                    "report_type": {
                        "type": "string",
                        "description": "Type of report to generate (for generate_report action)",
                        "enum": ["discovery", "qg1", "qg2", "qg3", "qg4", "qg5", "qg6", "mvp", "code", "deployment", "demo", "executive_summary", "full_pipeline"]
                    },
                    "gate": {
                        "type": "string",
                        "description": "Quality gate to execute (required for execute_quality_gate action)",
                        "enum": ["QG1", "QG2", "QG3", "QG4", "QG5", "QG6"]
                    },
                    "step": {
                        "type": "integer",
                        "description": "Pipeline step number (1-14) for guidance/checklist/validation actions",
                        "minimum": 1,
                        "maximum": 14
                    },
                    "customer_name": {
                        "type": "string",
                        "description": "Customer/company name"
                    },
                    "project_name": {
                        "type": "string",
                        "description": "Project name"
                    },
                    "industry": {
                        "type": "string",
                        "description": "Customer industry (e.g., retail, healthcare, manufacturing)"
                    },
                    "transcript": {
                        "type": "string",
                        "description": "Discovery call transcript to process"
                    },
                    "problem_statement": {
                        "type": "string",
                        "description": "Validated problem statement"
                    },
                    "discovery_data": {
                        "type": "object",
                        "description": "Structured discovery data from transcript processing"
                    },
                    "input_data": {
                        "type": "object",
                        "description": "Input data for quality gate validation or other operations"
                    },
                    "agent_name": {
                        "type": "string",
                        "description": "Name for generated agent (e.g., 'InventoryOptimizer')"
                    },
                    "agent_description": {
                        "type": "string",
                        "description": "Description of agent capabilities"
                    },
                    "features": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of features/capabilities"
                    },
                    "data_sources": {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": "Data sources for agent integration"
                    },
                    "existing_code": {
                        "type": "string",
                        "description": "Existing code for review or test generation"
                    },
                    "constraints": {
                        "type": "object",
                        "description": "Timeline, budget, or technical constraints"
                    },
                    "project_data": {
                        "type": "object",
                        "description": "Current project progress data"
                    },
                    "project_id": {
                        "type": "string",
                        "description": "Project ID for storing results"
                    },
                    "user_guid": {
                        "type": "string",
                        "description": "User GUID for project data access"
                    },
                    "deploy_to_storage": {
                        "type": "boolean",
                        "description": "If true, automatically upload generated agent to Azure File Storage agents/ folder (for transcript_to_agent action)"
                    },
                    "agent_priority": {
                        "type": "string",
                        "description": "Which agent to prioritize from transcript (e.g., 'contract', 'chargeback', 'social_media')"
                    }
                },
                "required": ["action"]
            }
        }
        self.storage_manager = get_storage_manager()
        super().__init__(name=self.name, metadata=self.metadata)

    def _get_openai_client(self):
        """Initialize Azure OpenAI client with Entra ID authentication."""
        if not AZURE_OPENAI_AVAILABLE:
            raise RuntimeError(
                "Azure OpenAI support is unavailable. Install openai and "
                f"azure-identity ({AZURE_OPENAI_IMPORT_ERROR})."
            )
        token_provider = get_bearer_token_provider(
            DefaultAzureCredential(),
            "https://cognitiveservices.azure.com/.default"
        )
        return AzureOpenAI(
            azure_endpoint=os.environ.get('AZURE_OPENAI_ENDPOINT'),
            azure_ad_token_provider=token_provider,
            api_version=os.environ.get('AZURE_OPENAI_API_VERSION', '2025-01-01-preview')
        )

    def perform(self, **kwargs):
        """Execute RAPP Pipeline operations."""
        action = kwargs.get('action')
        if not action:
            return json.dumps({"status": "error", "error": "Action is required"})

        try:
            # FAST-PATH: Transcript to agent in one step
            if action == 'transcript_to_agent':
                return self._transcript_to_agent(kwargs)

            # AUTO-PROCESS actions (recommended entry points)
            elif action == 'auto_process':
                return self._auto_process(kwargs)
            elif action == 'generate_report':
                return self._generate_report(kwargs)

            # Discovery actions
            elif action == 'prepare_discovery_call':
                return self._prepare_discovery_call(kwargs)
            elif action == 'process_transcript':
                return self._process_transcript(kwargs)
            elif action == 'generate_discovery_summary':
                return self._generate_discovery_summary(kwargs)

            # MVP actions
            elif action == 'generate_mvp_poke':
                return self._generate_mvp_poke(kwargs)
            elif action == 'prioritize_features':
                return self._prioritize_features(kwargs)
            elif action == 'define_scope':
                return self._define_scope(kwargs)
            elif action == 'estimate_timeline':
                return self._estimate_timeline(kwargs)
            elif action == 'generate_full_mvp_document':
                return self._generate_full_mvp_document(kwargs)

            # Code actions
            elif action == 'generate_agent_code':
                return self._generate_agent_code(kwargs)
            elif action == 'generate_agent_metadata':
                return self._generate_agent_metadata(kwargs)
            elif action == 'generate_agent_tests':
                return self._generate_agent_tests(kwargs)
            elif action == 'generate_deployment_config':
                return self._generate_deployment_config(kwargs)
            elif action == 'review_code':
                return self._review_code(kwargs)

            # Quality gate actions
            elif action == 'execute_quality_gate':
                return self._execute_quality_gate(kwargs)

            # Pipeline orchestration actions
            elif action == 'get_step_guidance':
                return self._get_step_guidance(kwargs)
            elif action == 'get_pipeline_status':
                return self._get_pipeline_status(kwargs)
            elif action == 'recommend_next_action':
                return self._recommend_next_action(kwargs)
            elif action == 'get_step_checklist':
                return self._get_step_checklist(kwargs)
            elif action == 'validate_step_completion':
                return self._validate_step_completion(kwargs)

            else:
                return json.dumps({"status": "error", "error": f"Unknown action: {action}"})

        except Exception as e:
            logger.error(f"Error in RAPP agent: {str(e)}", exc_info=True)
            return json.dumps({"status": "error", "error": str(e), "agent": self.name})

    # =========================================================================
    # DISCOVERY METHODS
    # =========================================================================

    def _prepare_discovery_call(self, kwargs):
        """Generate discovery call preparation guide and questions."""
        customer_name = kwargs.get('customer_name', 'Customer')
        industry = kwargs.get('industry', 'technology')
        existing_context = kwargs.get('discovery_data', {})

        client = self._get_openai_client()
        prompt = f"""You are a discovery call facilitator for an AI agent development project.

CUSTOMER CONTEXT:
- Company: {customer_name}
- Industry: {industry}
{f"- Existing Notes: {json.dumps(existing_context)}" if existing_context else ""}

Generate a comprehensive discovery call preparation guide including:

1. RESEARCH CHECKLIST (before the call)
- Industry-specific pain points to investigate
- Common AI use cases in this industry
- Competitor analysis points

2. DISCOVERY QUESTIONS (prioritized)
- Opening rapport-building questions
- Problem identification questions
- Data source exploration questions
- Stakeholder mapping questions
- Success criteria questions
- Timeline and budget questions

3. RED FLAGS TO WATCH FOR
- Signs the project may not be a good fit
- Scope creep indicators
- Unrealistic expectations

4. IDEAL OUTCOMES
- What a successful discovery call produces
- Key artifacts to capture

Format as a structured guide that can be used during the call."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        return json.dumps({
            "status": "success",
            "action": "prepare_discovery_call",
            "customer_name": customer_name,
            "industry": industry,
            "discovery_guide": response.choices[0].message.content,
            "generated_at": datetime.now().isoformat()
        })

    def _process_transcript(self, kwargs):
        """Process discovery call transcript and extract structured data."""
        customer_name = kwargs.get('customer_name', 'Customer')
        transcript = kwargs.get('transcript', '')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')

        if not transcript:
            return json.dumps({"status": "error", "error": "Transcript is required"})

        client = self._get_openai_client()
        prompt = f"""Analyze this discovery call transcript and extract structured data.

CUSTOMER: {customer_name}

TRANSCRIPT:
{transcript}

Extract the following in JSON format:

{{
  "callMetadata": {{
    "estimatedDuration": "estimated based on content",
    "participants": [{{"name": "", "role": "", "company": ""}}]
  }},
  "businessContext": {{
    "industry": "",
    "companySize": "small/medium/large/enterprise",
    "currentSystems": [],
    "technicalMaturity": "low/medium/high"
  }},
  "problemStatements": [
    {{
      "problem": "clear problem description",
      "verbatimQuote": "exact quote from customer if available",
      "category": "EFFICIENCY|ACCURACY|COST|COMPLIANCE|GROWTH",
      "severity": "LOW|MEDIUM|HIGH|CRITICAL",
      "currentProcess": "how they handle this today",
      "businessImpact": "quantified if possible"
    }}
  ],
  "dataSources": [
    {{
      "systemName": "",
      "dataType": "API|Database|File|Manual|SaaS",
      "accessLevel": "Full|Partial|Unknown|Blocked",
      "dataVolume": "estimated volume",
      "integrationComplexity": "LOW|MEDIUM|HIGH"
    }}
  ],
  "stakeholders": [
    {{
      "name": "",
      "role": "",
      "influenceLevel": "DECISION_MAKER|INFLUENCER|USER|TECHNICAL|BLOCKER",
      "concerns": [],
      "enthusiasm": "LOW|MEDIUM|HIGH"
    }}
  ],
  "successCriteria": [
    {{"metric": "", "currentValue": "", "targetValue": "", "measurementMethod": ""}}
  ],
  "timeline": {{
    "urgency": "LOW|MEDIUM|HIGH|CRITICAL",
    "targetLaunchDate": "",
    "budgetCycle": "",
    "keyMilestones": []
  }},
  "suggestedAgents": ["list of AI agent types that could address the problems"],
  "riskFactors": [{{"risk": "", "likelihood": "LOW|MEDIUM|HIGH", "mitigation": ""}}],
  "nextSteps": []
}}

Also provide:
1. A 3-paragraph executive summary
2. Recommended MVP scope
3. Confidence score (1-10) for data completeness"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        result = response.choices[0].message.content
        extracted_data = parse_llm_json_response(result, "raw_analysis")

        # Store discovery data if project_id provided
        stored = False
        if project_id:
            stored = self._store_discovery_data(project_id, extracted_data, user_guid)

        return json.dumps({
            "status": "success",
            "action": "process_transcript",
            "customer_name": customer_name,
            "extracted_data": extracted_data,
            "full_analysis": result,
            "stored_for_qg1": stored,
            "project_id": project_id,
            "processed_at": datetime.now().isoformat()
        })

    def _store_discovery_data(self, project_id: str, discovery_data: dict, user_guid: str = "default"):
        """Store discovery data to project storage."""
        try:
            directory = f"project_tracker/{user_guid}"
            self.storage_manager.write_file(
                directory,
                f"discovery_{project_id}.json",
                json.dumps(discovery_data, indent=2)
            )
            return True
        except Exception as e:
            logger.warning(f"Could not store discovery data: {e}")
            return False

    def _generate_discovery_summary(self, kwargs):
        """Generate executive summary from discovery data."""
        customer_name = kwargs.get('customer_name', 'Customer')
        discovery_data = kwargs.get('discovery_data', {})

        client = self._get_openai_client()
        prompt = f"""Generate a concise executive summary for this AI agent project.

CUSTOMER: {customer_name}
DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

Create:
1. ONE-PARAGRAPH EXECUTIVE SUMMARY (max 100 words)
2. THREE KEY TAKEAWAYS (bullet points)
3. RECOMMENDED NEXT STEP
4. RISK ASSESSMENT (one sentence)

Format for easy reading by executives."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        return json.dumps({
            "status": "success",
            "action": "generate_discovery_summary",
            "customer_name": customer_name,
            "executive_summary": response.choices[0].message.content,
            "generated_at": datetime.now().isoformat()
        })

    # =========================================================================
    # MVP GENERATION METHODS
    # =========================================================================

    def _generate_mvp_poke(self, kwargs):
        """Generate a lightweight MVP Poke proposal."""
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'AI Agent')
        discovery_data = kwargs.get('discovery_data', {})
        problem_statement = kwargs.get('problem_statement', '')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')

        client = self._get_openai_client()
        prompt = f"""Generate a lightweight MVP "Poke" document for an AI agent project.

CUSTOMER: {customer_name}
PROJECT: {project_name}
PROBLEM: {problem_statement}

DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

Create a concise MVP Poke with:
1. EXECUTIVE SUMMARY (2-3 sentences)
2. PROBLEM STATEMENT with Current State, Impact, Root Cause
3. PROPOSED SOLUTION with Agent Name and Core Capability
4. MVP FEATURES table (P0, P1, P2 priorities)
5. OUT OF SCOPE items (Phase 2)
6. DATA REQUIREMENTS table
7. SUCCESS METRICS table
8. TECHNICAL APPROACH (brief)
9. RISKS AND MITIGATIONS table
10. TIMELINE ESTIMATE
11. APPROVAL SECTION

Format as clean Markdown suitable for customer presentation.

Return JSON:
{{
  "status": "success",
  "document": "full markdown document",
  "features": {{"p0": [], "p1": [], "p2": []}},
  "outOfScope": [],
  "successMetrics": [{{"metric": "", "current": "", "target": ""}}],
  "estimatedDays": 0
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        result = response.choices[0].message.content
        parsed = parse_llm_json_response(result, "document")
        parsed["customer_name"] = customer_name
        parsed["project_name"] = project_name
        parsed["generated_at"] = datetime.now().isoformat()
        parsed["status"] = "success"
        parsed["action"] = "generate_mvp_poke"

        if project_id:
            self._update_project_with_mvp(project_id, parsed, user_guid)
            parsed["project_updated"] = True

        return json.dumps(parsed)

    def _update_project_with_mvp(self, project_id: str, mvp_data: dict, user_guid: str = "default"):
        """Update project with MVP document."""
        try:
            directory = f"project_tracker/{user_guid}"
            project_file = f"project_{project_id}.json"
            project_content = self.storage_manager.read_file(directory, project_file)
            if project_content:
                project = json.loads(project_content)
                project["mvp_document"] = mvp_data
                project["updated_at"] = datetime.now().isoformat()
                self.storage_manager.write_file(directory, project_file, json.dumps(project, indent=2))
                return True
            return False
        except Exception as e:
            logger.warning(f"Could not update project with MVP: {e}")
            return False

    def _prioritize_features(self, kwargs):
        """Prioritize features using P0/P1/P2 method."""
        discovery_data = kwargs.get('discovery_data', {})
        features = kwargs.get('features', [])
        constraints = kwargs.get('constraints', {})

        client = self._get_openai_client()
        prompt = f"""Prioritize AI agent features for MVP development.

DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

SUGGESTED FEATURES: {json.dumps(features) if features else 'Derive from discovery'}

CONSTRAINTS:
{json.dumps(constraints, indent=2) if constraints else 'None specified'}

Prioritize using P0/P1/P2 framework:
- P0: MUST have for MVP (blocks launch if missing)
- P1: SHOULD have (significant value, low risk)
- P2: COULD have (nice-to-have, defer if needed)
- DEFERRED: Phase 2 or later

Return JSON:
{{
  "features": [
    {{"name": "", "description": "", "priority": "P0|P1|P2|DEFERRED", "effort": "S|M|L", "businessValue": 0, "technicalRisk": "LOW|MEDIUM|HIGH", "rationale": ""}}
  ],
  "mvpCoreFeatures": [],
  "deferredFeatures": [],
  "totalEffort": "S|M|L|XL"
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_analysis")
        parsed["status"] = "success"
        parsed["action"] = "prioritize_features"
        parsed["analyzed_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    def _define_scope(self, kwargs):
        """Define clear scope boundaries for MVP."""
        customer_name = kwargs.get('customer_name', 'Customer')
        discovery_data = kwargs.get('discovery_data', {})
        problem_statement = kwargs.get('problem_statement', '')

        client = self._get_openai_client()
        prompt = f"""Define clear scope boundaries for this AI agent MVP.

CUSTOMER: {customer_name}
PROBLEM: {problem_statement}
DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

Create explicit scope definition with:
1. IN SCOPE (What we WILL build)
2. OUT OF SCOPE (What we WON'T build in MVP)
3. ASSUMPTIONS
4. DEPENDENCIES
5. CONSTRAINTS
6. SCOPE CREEP INDICATORS

Return JSON:
{{
  "scope": {{
    "inScope": [{{"item": "", "description": "", "priority": "P0|P1|P2"}}],
    "outOfScope": [{{"item": "", "reason": "", "phase": "2|3|future"}}],
    "assumptions": [{{"category": "TECHNICAL|BUSINESS|DATA", "assumption": ""}}],
    "dependencies": [{{"type": "SYSTEM|STAKEHOLDER|DATA", "dependency": "", "risk": "LOW|MEDIUM|HIGH"}}],
    "constraints": [],
    "scopeCreepIndicators": []
  }},
  "scopeStatement": "One paragraph scope statement"
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_scope")
        parsed["status"] = "success"
        parsed["action"] = "define_scope"
        parsed["customer_name"] = customer_name
        parsed["defined_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    def _estimate_timeline(self, kwargs):
        """Estimate MVP development timeline."""
        discovery_data = kwargs.get('discovery_data', {})
        constraints = kwargs.get('constraints', {})

        client = self._get_openai_client()
        prompt = f"""Estimate MVP development timeline for this AI agent project.

DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

CONSTRAINTS:
{json.dumps(constraints, indent=2) if constraints else 'None specified'}

Provide realistic timeline with phases, milestones, and risk buffers.

Return JSON:
{{
  "timeline": {{
    "phases": [{{"name": "", "estimatedDays": 0, "dependencies": [], "deliverables": []}}],
    "totalDays": 0,
    "milestones": [{{"name": "", "targetDay": 0, "description": ""}}],
    "criticalPath": [],
    "riskBuffer": {{"days": 0, "reason": ""}}
  }},
  "confidenceLevel": "LOW|MEDIUM|HIGH"
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_estimate")
        parsed["status"] = "success"
        parsed["action"] = "estimate_timeline"
        parsed["estimated_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    def _generate_full_mvp_document(self, kwargs):
        """Generate a complete MVP Poke document ready for customer presentation."""
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'AI Agent MVP')
        discovery_data = kwargs.get('discovery_data', {})
        problem_statement = kwargs.get('problem_statement', '')

        client = self._get_openai_client()
        prompt = f"""Generate a complete, professional MVP Poke document.

CUSTOMER: {customer_name}
PROJECT: {project_name}
PROBLEM: {problem_statement}

DISCOVERY DATA:
{json.dumps(discovery_data, indent=2)}

Create a comprehensive document in clean Markdown with:
- Executive Summary
- Problem Statement (Current State, Impact, Root Cause)
- Proposed Solution (Agent Name, Core Capability, How It Works)
- MVP Features (P0/P1/P2 priority table)
- Out of Scope (Phase 2+)
- Data Requirements table
- Integration Points
- Success Metrics table
- Technical Approach
- Assumptions & Dependencies
- Risks & Mitigations table
- Timeline
- Investment & ROI
- Approval section with signature lines

End with scope lock notice."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        return json.dumps({
            "status": "success",
            "action": "generate_full_mvp_document",
            "customer_name": customer_name,
            "project_name": project_name,
            "document": response.choices[0].message.content,
            "format": "markdown",
            "ready_for_customer": True,
            "generated_at": datetime.now().isoformat()
        })

    # =========================================================================
    # CODE GENERATION METHODS
    # =========================================================================

    def _generate_agent_code(self, kwargs):
        """Generate complete Python agent code."""
        agent_name = kwargs.get('agent_name', 'CustomAgent')
        agent_description = kwargs.get('agent_description', 'A custom AI agent')
        features = kwargs.get('features', [])
        data_sources = kwargs.get('data_sources', [])
        customer_name = kwargs.get('customer_name', 'Customer')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')

        # Create class name
        class_name = ''.join(word.capitalize() for word in agent_name.replace('-', '_').replace(' ', '_').split('_'))
        if not class_name.endswith('Agent'):
            class_name += 'Agent'
        snake_name = agent_name.lower().replace('-', '_').replace(' ', '_')
        if not snake_name.endswith('_agent'):
            snake_name += '_agent'

        client = self._get_openai_client()
        prompt = f"""Generate a complete, production-ready Python agent following the BasicAgent pattern.

AGENT SPECIFICATIONS:
- Agent Name: {agent_name}
- Class Name: {class_name}
- Description: {agent_description}
- Features: {json.dumps(features)}
- Data Sources: {json.dumps(data_sources)}
- Customer: {customer_name}

REQUIREMENTS:
1. Follow the BasicAgent pattern exactly
2. Include complete JSON Schema metadata for all parameters
3. The perform() method must return JSON string (never dict or exception)
4. Wrap all external calls in try/except
5. Use logging, not print statements
6. No hardcoded credentials - use os.environ
7. Include usage example in __main__
8. Include comprehensive docstrings
9. Handle all edge cases gracefully

Generate the complete Python code."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        code = response.choices[0].message.content
        if '```python' in code:
            code_start = code.find('```python') + 9
            code_end = code.rfind('```')
            if code_end > code_start:
                code = code[code_start:code_end].strip()

        result = {
            "status": "success",
            "action": "generate_agent_code",
            "agent_name": agent_name,
            "class_name": class_name,
            "file_name": f"{snake_name}.py",
            "code": code,
            "features_implemented": features,
            "generated_at": datetime.now().isoformat()
        }

        if project_id:
            self._update_project_with_code(project_id, result, user_guid)
            result["project_updated"] = True

        return json.dumps(result)

    def _update_project_with_code(self, project_id: str, code_data: dict, user_guid: str = "default"):
        """Update project with generated code."""
        try:
            directory = f"project_tracker/{user_guid}"
            project_file = f"project_{project_id}.json"
            project_content = self.storage_manager.read_file(directory, project_file)
            if project_content:
                project = json.loads(project_content)
                project["generated_code"] = code_data
                project["updated_at"] = datetime.now().isoformat()
                self.storage_manager.write_file(directory, project_file, json.dumps(project, indent=2))
                return True
            return False
        except Exception as e:
            logger.warning(f"Could not update project with code: {e}")
            return False

    def _generate_agent_metadata(self, kwargs):
        """Generate metadata schema for an agent."""
        agent_name = kwargs.get('agent_name', 'CustomAgent')
        agent_description = kwargs.get('agent_description', 'A custom AI agent')
        features = kwargs.get('features', [])

        client = self._get_openai_client()
        prompt = f"""Generate a complete JSON Schema metadata definition for an AI agent.

AGENT: {agent_name}
DESCRIPTION: {agent_description}
FEATURES: {json.dumps(features)}

Create a complete metadata object with name, description, and parameters schema.

Return valid JSON:
{{
  "name": "{agent_name}",
  "description": "...",
  "parameters": {{"type": "object", "properties": {{}}, "required": []}}
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_metadata")
        return json.dumps({
            "status": "success",
            "action": "generate_agent_metadata",
            "agent_name": agent_name,
            "metadata": parsed,
            "generated_at": datetime.now().isoformat()
        })

    def _generate_agent_tests(self, kwargs):
        """Generate unit test stubs for an agent."""
        agent_name = kwargs.get('agent_name', 'CustomAgent')
        existing_code = kwargs.get('existing_code', '')
        features = kwargs.get('features', [])

        class_name = ''.join(word.capitalize() for word in agent_name.replace('-', '_').replace(' ', '_').split('_'))
        if not class_name.endswith('Agent'):
            class_name += 'Agent'
        snake_name = agent_name.lower().replace('-', '_').replace(' ', '_')
        if not snake_name.endswith('_agent'):
            snake_name += '_agent'

        client = self._get_openai_client()
        prompt = f"""Generate comprehensive pytest unit tests for this agent.

AGENT: {agent_name}
CLASS: {class_name}
FEATURES: {json.dumps(features)}
{f'CODE:{chr(10)}{existing_code}' if existing_code else ''}

Generate pytest-style tests covering initialization, metadata validation, perform() with valid/invalid inputs, error handling, and edge cases. Use mocking appropriately."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        test_code = response.choices[0].message.content
        if '```python' in test_code:
            code_start = test_code.find('```python') + 9
            code_end = test_code.rfind('```')
            if code_end > code_start:
                test_code = test_code[code_start:code_end].strip()

        return json.dumps({
            "status": "success",
            "action": "generate_agent_tests",
            "agent_name": agent_name,
            "test_file_name": f"test_{snake_name}.py",
            "test_code": test_code,
            "generated_at": datetime.now().isoformat()
        })

    def _generate_deployment_config(self, kwargs):
        """Generate deployment configuration."""
        agent_name = kwargs.get('agent_name', 'CustomAgent')
        customer_name = kwargs.get('customer_name', 'Customer')
        snake_name = agent_name.lower().replace('-', '_').replace(' ', '_')

        deployment_config = {
            "agent_name": agent_name,
            "file_name": f"{snake_name}_agent.py",
            "deployment_steps": [
                {"step": 1, "action": "Upload agent to Azure File Storage", "command": f"az storage file upload --share-name agents --source {snake_name}_agent.py"},
                {"step": 2, "action": "Verify agent loads", "command": "func start --verbose"},
                {"step": 3, "action": "Test agent endpoint", "command": f'curl -X POST http://localhost:7071/api/businessinsightbot_function -H "Content-Type: application/json" -d \'{{"user_input": "test {agent_name}"}}\''},
                {"step": 4, "action": "Deploy to Azure", "command": "func azure functionapp publish <FUNCTION_APP_NAME> --build remote"}
            ],
            "environment_variables": ["AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT_NAME", "AZURE_OPENAI_API_VERSION"],
            "azure_file_storage_path": f"agents/{snake_name}_agent.py"
        }

        return json.dumps({
            "status": "success",
            "action": "generate_deployment_config",
            "agent_name": agent_name,
            "customer_name": customer_name,
            "deployment_config": deployment_config,
            "generated_at": datetime.now().isoformat()
        })

    def _review_code(self, kwargs):
        """Review existing code for issues."""
        existing_code = kwargs.get('existing_code', '')
        agent_name = kwargs.get('agent_name', 'Agent')

        if not existing_code:
            return json.dumps({"status": "error", "error": "No code provided for review"})

        client = self._get_openai_client()
        prompt = f"""Review this Python agent code for quality and security.

AGENT: {agent_name}
CODE:
```python
{existing_code}
```

Review for:
1. PATTERN VALIDATION - BasicAgent pattern, metadata schema, perform() returns JSON
2. SECURITY AUDIT - No hardcoded creds, input validation, injection vulnerabilities
3. LOGIC CORRECTNESS - Error handling, edge cases
4. CODE QUALITY - Naming, logging, complexity

Return JSON:
{{
  "overallScore": 0,
  "passesReview": true|false,
  "categories": {{
    "patternValidation": {{"score": 0, "passed": true|false, "issues": []}},
    "securityAudit": {{"score": 0, "passed": true|false, "issues": []}},
    "logicCorrectness": {{"score": 0, "passed": true|false, "issues": []}},
    "codeQuality": {{"score": 0, "passed": true|false, "issues": []}}
  }},
  "criticalIssues": [],
  "fixes": [{{"location": "", "issue": "", "fix": ""}}]
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_review")
        parsed["status"] = "success"
        parsed["action"] = "review_code"
        parsed["agent_name"] = agent_name
        parsed["reviewed_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    # =========================================================================
    # QUALITY GATE METHODS
    # =========================================================================

    def _execute_quality_gate(self, kwargs):
        """Execute a quality gate validation."""
        gate = kwargs.get('gate')
        if not gate:
            return json.dumps({"status": "error", "error": "Gate identifier (QG1-QG6) is required"})
        if gate not in self.GATE_CONFIGS:
            return json.dumps({"status": "error", "error": f"Invalid gate: {gate}. Use QG1-QG6."})

        input_data = kwargs.get('input_data') or kwargs.get('discovery_data', {})
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'Project')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')

        # Retrieve discovery data from storage if needed
        if not input_data and project_id:
            input_data = self._get_discovery_data_from_storage(project_id, user_guid)

        client = self._get_openai_client()

        if gate == "QG1":
            result = self._execute_qg1(client, input_data, customer_name)
        elif gate == "QG2":
            result = self._execute_qg2(client, input_data, customer_name, project_name)
        elif gate == "QG3":
            result = self._execute_qg3(client, input_data, customer_name, project_name)
        elif gate == "QG4":
            result = self._execute_qg4(client, input_data, customer_name, project_name)
        elif gate == "QG5":
            result = self._execute_qg5(client, input_data, customer_name, project_name)
        elif gate == "QG6":
            result = self._execute_qg6(client, input_data, customer_name, project_name)

        # Store result in project
        if project_id:
            try:
                parsed_result = json.loads(result)
                self._update_project_with_qg_result(project_id, gate, parsed_result, user_guid)
            except json.JSONDecodeError:
                pass

        return result

    def _get_discovery_data_from_storage(self, project_id: str, user_guid: str) -> dict:
        """Retrieve discovery data from storage."""
        try:
            directory = f"project_tracker/{user_guid}"
            content = self.storage_manager.read_file(directory, f"discovery_{project_id}.json")
            if content:
                return json.loads(content)
            return {}
        except Exception:
            return {}

    def _update_project_with_qg_result(self, project_id: str, gate: str, qg_result: dict, user_guid: str):
        """Update project with quality gate result."""
        try:
            directory = f"project_tracker/{user_guid}"
            project_file = f"project_{project_id}.json"
            content = self.storage_manager.read_file(directory, project_file)
            if content:
                project = json.loads(content)
                if "qg_results" not in project:
                    project["qg_results"] = {}
                project["qg_results"][gate] = qg_result
                project["updated_at"] = datetime.now().isoformat()
                self.storage_manager.write_file(directory, project_file, json.dumps(project, indent=2))
        except Exception as e:
            logger.warning(f"Could not update project with QG result: {e}")

    def _execute_qg1(self, client, input_data, customer_name):
        """QG1: Transcript/Discovery Validation."""
        prompt = f"""You are Quality Gate #1 (QG1) - Transcript Validation.

CUSTOMER: {customer_name}
DISCOVERY DATA:
{json.dumps(input_data, indent=2)}

Score each criterion 1-10:
1. PROBLEM CLARITY: Is the problem specific, measurable, with quantified pain points?
2. DATA AVAILABILITY: Are data sources identified with feasible access?
3. STAKEHOLDER ALIGNMENT: Clear decision-maker? Agreement on problem?
4. SUCCESS CRITERIA: Metrics defined with realistic targets?
5. SCOPE BOUNDARIES: MVP scope appropriate? Clear exclusions?

DECISION: Average >= 8: PASS, 6-7: CLARIFY, < 6: FAIL

Return ONLY valid JSON with gate, gateName, decision, overallScore, scores, validatedProblemStatement, strengths, concerns, clarifyingQuestions, recommendations, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG1")

    def _execute_qg2(self, client, input_data, customer_name, project_name):
        """QG2: Customer Validation (Scope Lock)."""
        prompt = f"""You are Quality Gate #2 (QG2) - Customer Validation.

CUSTOMER: {customer_name}
PROJECT: {project_name}
MVP PROPOSAL & FEEDBACK:
{json.dumps(input_data, indent=2)}

Validate: SCOPE AGREEMENT, DATA ACCESS, STAKEHOLDER BUY-IN, TIMELINE ACCEPTANCE
DECISION: All confirmed: PROCEED (SCOPE LOCKED), Minor issues: REVISE, Major: HOLD

Return ONLY valid JSON with gate, gateName, decision, scopeLocked, scores, lockedFeatures, deferredToPhase2, concerns, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG2")

    def _execute_qg3(self, client, input_data, customer_name, project_name):
        """QG3: Code Quality Review."""
        prompt = f"""You are Quality Gate #3 (QG3) - Code Quality Review.

CUSTOMER: {customer_name}
PROJECT: {project_name}
CODE & SPECIFICATION:
{json.dumps(input_data, indent=2)}

Review: PATTERN VALIDATION, SECURITY AUDIT, LOGIC CORRECTNESS, INTEGRATION COMPATIBILITY, CODE QUALITY
DECISION: All pass: PASS, Fixable: FIX_REQUIRED, Major problems: FAIL

Return ONLY valid JSON with gate, gateName, decision, securityScore, scores, criticalIssues, fixes, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG3")

    def _execute_qg4(self, client, input_data, customer_name, project_name):
        """QG4: Demo Review (Waiter Pattern)."""
        prompt = f"""You are Quality Gate #4 (QG4) - Demo Review using "Waiter Pattern".

CUSTOMER: {customer_name}
PROJECT: {project_name}
DEMO DATA:
{json.dumps(input_data, indent=2)}

Waiter Pattern: "Would you confidently serve this to the customer?"
Score 1-10: RESPONSE QUALITY, CONVERSATION FLOW, VISUAL PRESENTATION, BUSINESS VALUE, EDGE CASES
DECISION: Average >= 8: PASS, 6-7: POLISH, < 6: FAIL

Return ONLY valid JSON with gate, gateName, decision, waiterScore, scores, strengths, polishItems, blockers, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG4")

    def _execute_qg5(self, client, input_data, customer_name, project_name):
        """QG5: Final Demo Review (Executive Readiness)."""
        prompt = f"""You are Quality Gate #5 (QG5) - Final Demo Review for Executive Presentation.

CUSTOMER: {customer_name}
PROJECT: {project_name}
DEMO DATA:
{json.dumps(input_data, indent=2)}

Score 1-10: OPENING HOOK, PROBLEM ILLUSTRATION, SOLUTION WOW, METRICS CLARITY, INDUSTRY ACCURACY, CLOSING STRENGTH, TECHNICAL POLISH, MVP ALIGNMENT
DECISION: >= 8.5: APPROVE, 7-8.4: MINOR_REVISIONS, 5-6.9: MAJOR_REVISIONS, < 5: REJECT

Return ONLY valid JSON with gate, gateName, decision, executiveReadinessScore, scores, feedback, strengths, approvalReady, nextStep."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG5")

    def _execute_qg6(self, client, input_data, customer_name, project_name):
        """QG6: Post-Deployment Audit."""
        prompt = f"""You are Quality Gate #6 (QG6) - Post-Deployment Audit.

CUSTOMER: {customer_name}
PROJECT: {project_name}
DEPLOYMENT METRICS:
{json.dumps(input_data, indent=2)}

Score: SYSTEM HEALTH (25%), USAGE ADOPTION (25%), BUSINESS VALUE (30%), CUSTOMER SATISFACTION (20%)
STATUS: GREEN (all meeting targets), YELLOW (some below but trending up), RED (critical failing)

Return ONLY valid JSON with gate, gateName, decision, auditDate, scores, roiValidation, recommendations, optimizations, nextAuditDate."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )
        return self._parse_gate_response(response.choices[0].message.content, "QG6")

    def _parse_gate_response(self, response_text, gate):
        """Parse and validate gate response."""
        parsed = parse_llm_json_response(response_text, "raw_response")
        parsed["status"] = "success"
        parsed["gate"] = gate
        parsed["evaluatedAt"] = datetime.now().isoformat()
        return json.dumps(parsed)

    # =========================================================================
    # PIPELINE ORCHESTRATION METHODS
    # =========================================================================

    def _get_step_guidance(self, kwargs):
        """Get detailed guidance for a specific pipeline step."""
        step = kwargs.get('step', 1)
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'Project')
        project_data = kwargs.get('project_data', {})

        if step not in self.PIPELINE_STEPS:
            return json.dumps({"status": "error", "error": f"Invalid step: {step}. Use 1-14."})

        step_info = self.PIPELINE_STEPS[step]
        client = self._get_openai_client()

        prompt = f"""Provide detailed guidance for RAPP Pipeline Step {step}: {step_info['name']}

CUSTOMER: {customer_name}
PROJECT: {project_name}
STEP TYPE: {step_info['type']}

CURRENT PROJECT DATA:
{json.dumps(project_data, indent=2) if project_data else 'No data yet'}

Provide:
1. STEP OVERVIEW - Purpose and objectives
2. INPUTS REQUIRED - What you need before starting
3. KEY ACTIVITIES - Specific tasks and best practices
4. OUTPUTS EXPECTED - Deliverables and quality criteria
5. COMMON PITFALLS - What to avoid
6. RAPP AGENT ACTIONS - Which action to use (e.g., process_transcript, execute_quality_gate with gate=QG1)
7. SUCCESS CRITERIA - How to know you're done"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        return json.dumps({
            "status": "success",
            "action": "get_step_guidance",
            "step": step,
            "step_name": step_info['name'],
            "step_type": step_info['type'],
            "guidance": response.choices[0].message.content,
            "related_gate": step_info.get('gate'),
            "generated_at": datetime.now().isoformat()
        })

    def _get_pipeline_status(self, kwargs):
        """Get overall pipeline status for a project."""
        project_data = kwargs.get('project_data', {})
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'Project')

        completed_steps = project_data.get('completed_steps', [])
        current_step = project_data.get('current_step', 1)
        step_decisions = project_data.get('step_decisions', {})

        progress_percent = len(completed_steps) / 14 * 100

        # Build step status
        step_status = []
        for step_id, step_info in self.PIPELINE_STEPS.items():
            status = "completed" if step_id in completed_steps else "pending"
            if step_id == current_step:
                status = "in_progress"
            if str(step_id) in step_decisions:
                status = f"{status} ({step_decisions[str(step_id)]})"
            step_status.append({
                "step": step_id,
                "name": step_info['name'],
                "type": step_info['type'],
                "status": status
            })

        return json.dumps({
            "status": "success",
            "action": "get_pipeline_status",
            "customer_name": customer_name,
            "project_name": project_name,
            "progress_percent": round(progress_percent, 1),
            "current_step": current_step,
            "current_step_name": self.PIPELINE_STEPS[current_step]['name'],
            "completed_count": len(completed_steps),
            "total_steps": 14,
            "step_status": step_status,
            "generated_at": datetime.now().isoformat()
        })

    def _recommend_next_action(self, kwargs):
        """Recommend the next action based on current state."""
        project_data = kwargs.get('project_data', {})
        current_step = project_data.get('current_step', 1)
        step_decisions = project_data.get('step_decisions', {})

        step_info = self.PIPELINE_STEPS[current_step]
        client = self._get_openai_client()

        prompt = f"""Based on current RAPP Pipeline state, recommend the best next action.

CURRENT STEP: {current_step} - {step_info['name']} ({step_info['type']})
STEP DECISIONS: {json.dumps(step_decisions, indent=2)}

Provide:
1. IMMEDIATE NEXT ACTION - What to do now
2. RAPP AGENT ACTION - The exact action to call (e.g., process_transcript, execute_quality_gate)
3. REQUIRED INPUTS - What parameters are needed
4. BLOCKERS - Any issues to resolve first

Return JSON:
{{
  "recommended_action": "description",
  "rapp_action": "action name from RAPP agent",
  "required_parameters": {{}},
  "blockers": [],
  "priority": "HIGH|MEDIUM|LOW",
  "rationale": "why this is recommended"
}}"""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        parsed = parse_llm_json_response(response.choices[0].message.content, "raw_recommendation")
        parsed["status"] = "success"
        parsed["action"] = "recommend_next_action"
        parsed["current_step"] = current_step
        parsed["current_step_name"] = step_info['name']
        parsed["generated_at"] = datetime.now().isoformat()
        return json.dumps(parsed)

    def _get_step_checklist(self, kwargs):
        """Get the completion checklist for a step."""
        step = kwargs.get('step', 1)

        if step not in self.PIPELINE_STEPS:
            return json.dumps({"status": "error", "error": f"Invalid step: {step}"})

        step_info = self.PIPELINE_STEPS[step]

        checklists = {
            1: ["Scheduled discovery call", "Prepared questions", "Recorded call", "Captured problem statements", "Identified data sources", "Mapped stakeholders", "Documented success criteria"],
            2: ["Reviewed transcript clarity", "Verified data access", "Confirmed stakeholder alignment", "Validated measurable criteria", "Assessed MVP scope", "Made PASS/FAIL/CLARIFY decision"],
            3: ["Created executive summary", "Defined MVP features (P0/P1/P2)", "Listed out-of-scope items", "Documented data requirements", "Set success metrics", "Added approval section"],
            4: ["Presented MVP to customer", "Received feature approval", "Confirmed out-of-scope accepted", "Got decision-maker sign-off", "LOCKED scope"],
            5: ["Generated BasicAgent code", "Defined metadata schema", "Implemented perform() method", "Added input validation", "Integrated Azure OpenAI", "Added error handling", "No hardcoded credentials"],
            6: ["Validated pattern compliance", "Completed security audit", "Verified logic matches MVP", "Checked Azure integration", "Made PASS/FIX/FAIL decision"],
            7: ["Validated Azure infrastructure", "Deployed Function App", "Uploaded agent code", "Configured environment", "Tested endpoint"],
            8: ["Tested all MVP features", "Verified response quality", "Checked conversation flow", "Applied waiter pattern", "Made PASS/POLISH/FAIL decision"],
            9: ["Created narrative arc", "Wrote narration script", "Designed demo steps", "Included metrics", "Generated demo JSON"],
            10: ["Reviewed opening hook", "Validated problem illustration", "Confirmed wow moment", "Checked metrics", "Made APPROVE/REVISE/REJECT decision"],
            11: ["Collected feedback", "Classified items (bug/polish/feature/creep)", "Deferred scope creep", "Created iteration plan"],
            12: ["Completed security hardening", "Deployed production infra", "Configured Key Vault", "Set up monitoring", "Created documentation"],
            13: ["Collected health metrics", "Analyzed usage patterns", "Measured business value", "Gathered customer feedback", "Generated audit report"],
            14: ["Reviewed audit results", "Prioritized optimization backlog", "Identified scaling opportunities", "Documented lessons learned"]
        }

        return json.dumps({
            "status": "success",
            "action": "get_step_checklist",
            "step": step,
            "step_name": step_info['name'],
            "step_type": step_info['type'],
            "checklist": checklists.get(step, []),
            "generated_at": datetime.now().isoformat()
        })

    def _validate_step_completion(self, kwargs):
        """Validate if a step is ready for completion."""
        step = kwargs.get('step', 1)
        project_data = kwargs.get('project_data', {})

        if step not in self.PIPELINE_STEPS:
            return json.dumps({"status": "error", "error": f"Invalid step: {step}"})

        step_info = self.PIPELINE_STEPS[step]
        step_checklists = project_data.get('step_checklists', {})
        step_decisions = project_data.get('step_decisions', {})

        checklist_data = step_checklists.get(str(step), {})
        checklist_complete = all(checklist_data.values()) if checklist_data else False

        gate_decision = step_decisions.get(str(step))
        gate_passed = gate_decision in ['PASS', 'PROCEED', 'APPROVE', 'GREEN'] if gate_decision else None

        if step_info['type'] == 'audit':
            is_valid = checklist_complete and gate_decision is not None
            can_proceed = gate_passed
        else:
            is_valid = checklist_complete
            can_proceed = is_valid

        return json.dumps({
            "status": "success",
            "action": "validate_step_completion",
            "step": step,
            "step_name": step_info['name'],
            "step_type": step_info['type'],
            "validation": {
                "checklist_complete": checklist_complete,
                "gate_decision": gate_decision,
                "gate_passed": gate_passed,
                "is_valid": is_valid,
                "can_proceed": can_proceed
            },
            "next_step": step + 1 if can_proceed and step < 14 else None,
            "message": f"Step {step} {'ready to proceed' if can_proceed else 'not yet complete'}",
            "generated_at": datetime.now().isoformat()
        })

    # =========================================================================
    # AUTO-PROCESS AND REPORT GENERATION METHODS
    # =========================================================================

    def _auto_process(self, kwargs):
        """
        Automatically process a project based on available inputs.

        Scans the project folder for input files, determines the appropriate
        pipeline step, processes the inputs, and generates professional PDF reports.

        Folder structure expected:
            rapp_projects/{project_id}/
                inputs/
                    discovery_transcript.txt
                    customer_feedback.txt
                    code_to_review.py
                    etc.
                outputs/
                    (reports generated here)
                project_state.json
        """
        project_id = kwargs.get('project_id')
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'AI Agent Project')
        user_guid = kwargs.get('user_guid', 'default')

        if not project_id:
            return json.dumps({"status": "error", "error": "project_id is required for auto_process"})

        try:
            # Scan inputs
            inputs = self._scan_project_inputs(project_id, user_guid)
            if not inputs['files']:
                return json.dumps({
                    "status": "error",
                    "error": "No input files found",
                    "expected_location": f"rapp_projects/{project_id}/inputs/",
                    "supported_files": list(self.INPUT_PATTERNS.keys())
                })

            # Load or create project state
            project_state = self._load_project_state(project_id, user_guid)
            project_state['customer_name'] = customer_name
            project_state['project_name'] = project_name

            # Determine what to process based on inputs and current state
            actions_taken = []
            reports_generated = []

            # Process discovery transcript if present
            if inputs.get('discovery_transcript'):
                logger.info(f"Processing discovery transcript for project {project_id}")
                transcript_content = inputs['discovery_transcript']['content']

                # Process transcript
                result = json.loads(self._process_transcript({
                    'customer_name': customer_name,
                    'transcript': transcript_content,
                    'project_id': project_id,
                    'user_guid': user_guid
                }))

                if result.get('status') == 'success':
                    actions_taken.append("Processed discovery transcript")
                    project_state['discovery_data'] = result.get('extracted_data', {})
                    project_state['current_step'] = 2

                    # Generate discovery report
                    report_path = self._generate_and_save_report(
                        "discovery", result, customer_name, project_name, project_id, user_guid
                    )
                    if report_path:
                        reports_generated.append({"type": "discovery", "path": report_path})

                    # Execute QG1
                    qg1_result = json.loads(self._execute_quality_gate({
                        'gate': 'QG1',
                        'customer_name': customer_name,
                        'project_name': project_name,
                        'input_data': result.get('extracted_data', {}),
                        'project_id': project_id,
                        'user_guid': user_guid
                    }))

                    if qg1_result.get('status') == 'success':
                        actions_taken.append(f"Executed QG1: {qg1_result.get('decision', 'N/A')}")
                        project_state['qg1_result'] = qg1_result
                        if qg1_result.get('decision') == 'PASS':
                            project_state['completed_steps'] = project_state.get('completed_steps', []) + [1, 2]
                            project_state['current_step'] = 3

                        # Generate QG1 report
                        report_path = self._generate_and_save_report(
                            "qg1", qg1_result, customer_name, project_name, project_id, user_guid
                        )
                        if report_path:
                            reports_generated.append({"type": "qg1", "path": report_path})

            # Process customer feedback for QG2 if present
            if inputs.get('customer_feedback') and project_state.get('current_step', 1) >= 3:
                logger.info(f"Processing customer feedback for project {project_id}")
                feedback_content = inputs['customer_feedback']['content']

                # First generate MVP if not done
                if not project_state.get('mvp_document'):
                    mvp_result = json.loads(self._generate_full_mvp_document({
                        'customer_name': customer_name,
                        'project_name': project_name,
                        'discovery_data': project_state.get('discovery_data', {}),
                        'problem_statement': project_state.get('discovery_data', {}).get('problemStatements', [{}])[0].get('problem', '')
                    }))

                    if mvp_result.get('status') == 'success':
                        actions_taken.append("Generated MVP document")
                        project_state['mvp_document'] = mvp_result

                        report_path = self._generate_and_save_report(
                            "mvp", mvp_result, customer_name, project_name, project_id, user_guid
                        )
                        if report_path:
                            reports_generated.append({"type": "mvp", "path": report_path})

                # Execute QG2 with customer feedback
                qg2_input = {
                    'mvp_document': project_state.get('mvp_document', {}),
                    'customer_feedback': feedback_content
                }
                qg2_result = json.loads(self._execute_quality_gate({
                    'gate': 'QG2',
                    'customer_name': customer_name,
                    'project_name': project_name,
                    'input_data': qg2_input,
                    'project_id': project_id,
                    'user_guid': user_guid
                }))

                if qg2_result.get('status') == 'success':
                    actions_taken.append(f"Executed QG2: {qg2_result.get('decision', 'N/A')}")
                    project_state['qg2_result'] = qg2_result
                    if qg2_result.get('decision') == 'PROCEED':
                        project_state['scope_locked'] = True
                        project_state['completed_steps'] = list(set(project_state.get('completed_steps', []) + [3, 4]))
                        project_state['current_step'] = 5

                    report_path = self._generate_and_save_report(
                        "qg2", qg2_result, customer_name, project_name, project_id, user_guid
                    )
                    if report_path:
                        reports_generated.append({"type": "qg2", "path": report_path})

            # Process code for review if present
            if inputs.get('code_to_review') and project_state.get('current_step', 1) >= 5:
                logger.info(f"Processing code review for project {project_id}")
                code_content = inputs['code_to_review']['content']

                # First generate agent code if not done
                if not project_state.get('generated_code'):
                    discovery_data = project_state.get('discovery_data', {})
                    suggested_agents = discovery_data.get('suggestedAgents', ['CustomAgent'])
                    agent_name = suggested_agents[0] if suggested_agents else 'CustomAgent'

                    code_result = json.loads(self._generate_agent_code({
                        'agent_name': agent_name,
                        'agent_description': project_state.get('mvp_document', {}).get('document', '')[:500],
                        'features': [p.get('problem', '') for p in discovery_data.get('problemStatements', [])],
                        'customer_name': customer_name,
                        'project_id': project_id,
                        'user_guid': user_guid
                    }))

                    if code_result.get('status') == 'success':
                        actions_taken.append("Generated agent code")
                        project_state['generated_code'] = code_result

                        report_path = self._generate_and_save_report(
                            "code", code_result, customer_name, project_name, project_id, user_guid
                        )
                        if report_path:
                            reports_generated.append({"type": "code", "path": report_path})

                # Execute QG3 code review
                qg3_result = json.loads(self._execute_quality_gate({
                    'gate': 'QG3',
                    'customer_name': customer_name,
                    'project_name': project_name,
                    'input_data': {
                        'code': code_content,
                        'features': project_state.get('mvp_document', {}).get('features', {})
                    },
                    'project_id': project_id,
                    'user_guid': user_guid
                }))

                if qg3_result.get('status') == 'success':
                    actions_taken.append(f"Executed QG3: {qg3_result.get('decision', 'N/A')}")
                    project_state['qg3_result'] = qg3_result
                    if qg3_result.get('decision') == 'PASS':
                        project_state['completed_steps'] = list(set(project_state.get('completed_steps', []) + [5, 6]))
                        project_state['current_step'] = 7

                    report_path = self._generate_and_save_report(
                        "qg3", qg3_result, customer_name, project_name, project_id, user_guid
                    )
                    if report_path:
                        reports_generated.append({"type": "qg3", "path": report_path})

            # Process deployment metrics for QG6 if present
            if inputs.get('deployment_metrics') and project_state.get('current_step', 1) >= 12:
                logger.info(f"Processing deployment metrics for project {project_id}")
                try:
                    metrics_content = json.loads(inputs['deployment_metrics']['content'])
                except json.JSONDecodeError:
                    metrics_content = {"raw_metrics": inputs['deployment_metrics']['content']}

                qg6_result = json.loads(self._execute_quality_gate({
                    'gate': 'QG6',
                    'customer_name': customer_name,
                    'project_name': project_name,
                    'input_data': metrics_content,
                    'project_id': project_id,
                    'user_guid': user_guid
                }))

                if qg6_result.get('status') == 'success':
                    actions_taken.append(f"Executed QG6: {qg6_result.get('decision', 'N/A')}")
                    project_state['qg6_result'] = qg6_result
                    project_state['completed_steps'] = list(set(project_state.get('completed_steps', []) + [13]))
                    project_state['current_step'] = 14

                    report_path = self._generate_and_save_report(
                        "qg6", qg6_result, customer_name, project_name, project_id, user_guid
                    )
                    if report_path:
                        reports_generated.append({"type": "qg6", "path": report_path})

            # Generate executive summary report
            exec_summary = self._generate_executive_summary_data(project_state, customer_name, project_name)
            report_path = self._generate_and_save_report(
                "executive_summary", exec_summary, customer_name, project_name, project_id, user_guid
            )
            if report_path:
                reports_generated.append({"type": "executive_summary", "path": report_path})

            # Save project state
            self._save_project_state(project_id, project_state, user_guid)

            return json.dumps({
                "status": "success",
                "action": "auto_process",
                "project_id": project_id,
                "customer_name": customer_name,
                "project_name": project_name,
                "inputs_detected": list(inputs['files'].keys()),
                "actions_taken": actions_taken,
                "reports_generated": reports_generated,
                "current_step": project_state.get('current_step', 1),
                "completed_steps": project_state.get('completed_steps', []),
                "progress_percent": len(project_state.get('completed_steps', [])) / 14 * 100,
                "processed_at": datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"Error in auto_process: {str(e)}", exc_info=True)
            return json.dumps({
                "status": "error",
                "error": str(e),
                "project_id": project_id
            })

    def _scan_project_inputs(self, project_id: str, user_guid: str) -> Dict[str, Any]:
        """Scan project inputs folder for files."""
        inputs = {'files': {}}
        input_directory = f"rapp_projects/{project_id}/inputs"

        try:
            files = self.storage_manager.list_files(input_directory)
            if not files:
                return inputs

            for file_info in files:
                filename = file_info.name if hasattr(file_info, 'name') else str(file_info)
                filename_lower = filename.lower()

                # Determine file type
                file_type = None
                for input_type, patterns in self.INPUT_PATTERNS.items():
                    for pattern in patterns:
                        if pattern in filename_lower:
                            file_type = input_type
                            break
                    if file_type:
                        break

                if file_type:
                    content = self.storage_manager.read_file(input_directory, filename)
                    if content:
                        inputs['files'][filename] = {
                            'type': file_type,
                            'size': len(content)
                        }
                        inputs[file_type] = {
                            'filename': filename,
                            'content': content
                        }

        except Exception as e:
            logger.warning(f"Error scanning inputs for project {project_id}: {e}")

        return inputs

    def _load_project_state(self, project_id: str, user_guid: str) -> Dict[str, Any]:
        """Load or create project state."""
        state_directory = f"rapp_projects/{project_id}"
        state_file = "project_state.json"

        try:
            content = self.storage_manager.read_file(state_directory, state_file)
            if content:
                return json.loads(content)
        except Exception:
            pass

        return {
            'project_id': project_id,
            'current_step': 1,
            'completed_steps': [],
            'created_at': datetime.now().isoformat()
        }

    def _save_project_state(self, project_id: str, state: Dict[str, Any], user_guid: str):
        """Save project state."""
        state_directory = f"rapp_projects/{project_id}"
        state_file = "project_state.json"
        state['updated_at'] = datetime.now().isoformat()

        try:
            self.storage_manager.write_file(state_directory, state_file, json.dumps(state, indent=2))
        except Exception as e:
            logger.warning(f"Could not save project state: {e}")

    def _generate_and_save_report(
        self,
        report_type: str,
        data: Dict[str, Any],
        customer_name: str,
        project_name: str,
        project_id: str,
        user_guid: str
    ) -> Optional[str]:
        """Generate a PDF report and save it to the outputs folder."""
        if not REPORT_GENERATOR_AVAILABLE:
            logger.warning("Report generator not available. Install reportlab.")
            return None

        try:
            generator = RAPPReportGenerator()
            pdf_bytes = generator.generate_report(
                report_type=report_type,
                data=data,
                customer_name=customer_name,
                project_name=project_name
            )

            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{report_type}_report_{timestamp}.pdf"
            output_directory = f"rapp_projects/{project_id}/outputs"

            # Save to storage
            self.storage_manager.write_file(output_directory, filename, pdf_bytes)
            logger.info(f"Generated report: {output_directory}/{filename}")

            return f"{output_directory}/{filename}"

        except Exception as e:
            logger.error(f"Error generating report: {e}")
            return None

    def _generate_executive_summary_data(
        self,
        project_state: Dict[str, Any],
        customer_name: str,
        project_name: str
    ) -> Dict[str, Any]:
        """Generate data for executive summary report."""
        completed_steps = project_state.get('completed_steps', [])
        current_step = project_state.get('current_step', 1)

        qg_decisions = []
        for gate in ['qg1', 'qg2', 'qg3', 'qg4', 'qg5', 'qg6']:
            result = project_state.get(f'{gate}_result', {})
            if result.get('decision'):
                qg_decisions.append(f"{gate.upper()}: {result['decision']}")

        return {
            'summary': f"RAPP Pipeline progress for {project_name} ({customer_name}). "
                      f"Currently at Step {current_step} ({self.PIPELINE_STEPS[current_step]['name']}). "
                      f"Completed {len(completed_steps)} of 14 steps.",
            'metrics': {
                'progress_percent': round(len(completed_steps) / 14 * 100, 1),
                'completed_steps': len(completed_steps),
                'current_step': current_step
            },
            'progress_percent': round(len(completed_steps) / 14 * 100, 1),
            'current_step': current_step,
            'current_step_name': self.PIPELINE_STEPS[current_step]['name'],
            'quality_gate_decisions': qg_decisions,
            'scope_locked': project_state.get('scope_locked', False),
            'discovery_data': project_state.get('discovery_data', {}),
            'generated_at': datetime.now().isoformat()
        }

    def _generate_report(self, kwargs):
        """Generate a professional PDF report for a specific report type."""
        report_type = kwargs.get('report_type')
        customer_name = kwargs.get('customer_name', 'Customer')
        project_name = kwargs.get('project_name', 'AI Agent Project')
        project_id = kwargs.get('project_id')
        user_guid = kwargs.get('user_guid', 'default')
        data = kwargs.get('input_data') or kwargs.get('data', {})

        if not report_type:
            return json.dumps({"status": "error", "error": "report_type is required"})

        if not REPORT_GENERATOR_AVAILABLE:
            return json.dumps({
                "status": "error",
                "error": "Report generator not available. Install reportlab: pip install reportlab"
            })

        try:
            generator = RAPPReportGenerator()
            pdf_bytes = generator.generate_report(
                report_type=report_type,
                data=data,
                customer_name=customer_name,
                project_name=project_name
            )

            # Save if project_id provided
            output_path = None
            if project_id:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{report_type}_report_{timestamp}.pdf"
                output_directory = f"rapp_projects/{project_id}/outputs"
                self.storage_manager.write_file(output_directory, filename, pdf_bytes)
                output_path = f"{output_directory}/{filename}"

            return json.dumps({
                "status": "success",
                "action": "generate_report",
                "report_type": report_type,
                "customer_name": customer_name,
                "project_name": project_name,
                "output_path": output_path,
                "pdf_size_bytes": len(pdf_bytes),
                "generated_at": datetime.now().isoformat()
            })

        except Exception as e:
            logger.error(f"Error generating report: {e}", exc_info=True)
            return json.dumps({
                "status": "error",
                "error": str(e)
            })

    # =========================================================================
    # TRANSCRIPT TO AGENT - FAST PATH FOR QUICK ITERATION
    # =========================================================================

    def _transcript_to_agent(self, kwargs):
        """
        FASTEST PATH: Transcript → Deployable Agent + Demo in one step.

        This method:
        1. Reads transcript from Azure storage or inline
        2. Analyzes transcript to extract agent requirements
        3. Generates complete agent Python code (BasicAgent pattern)
        4. Generates demo JSON for ScriptedDemoAgent
        5. Auto-deploys both to agents/ and demos/ folders

        User workflow:
        1. Drop transcript in rapp_projects/{project_id}/inputs/ OR pass inline
        2. Call this action
        3. Agent and demo are ready to use immediately

        Args:
            project_id: Project ID (reads transcript from rapp_projects/{project_id}/inputs/)
            transcript: Inline transcript text (alternative to project_id)
            customer_name: Customer/company name
            agent_priority: Which agent to prioritize (e.g., 'contract', 'chargeback')
            deploy_to_storage: If True, auto-deploy to agents/ and demos/ folders
            user_guid: User GUID for storage access
        """
        project_id = kwargs.get('project_id')
        transcript = kwargs.get('transcript', '')
        customer_name = kwargs.get('customer_name', 'Customer')
        agent_priority = kwargs.get('agent_priority', '')
        deploy_to_storage = kwargs.get('deploy_to_storage', True)
        user_guid = kwargs.get('user_guid', 'default')

        try:
            # Step 1: Get transcript content
            if not transcript and project_id:
                transcript = self._get_transcript_from_storage(project_id, user_guid)

            if not transcript:
                return json.dumps({
                    "status": "error",
                    "error": "No transcript provided. Either pass 'transcript' parameter or ensure transcript file exists in rapp_projects/{project_id}/inputs/",
                    "expected_patterns": self.INPUT_PATTERNS.get('discovery_transcript', [])
                })

            # Step 2: Analyze transcript to extract agent requirements
            logger.info(f"Analyzing transcript for {customer_name}...")
            agent_spec = self._analyze_transcript_for_agent(transcript, customer_name, agent_priority)

            if agent_spec.get('status') == 'error':
                return json.dumps(agent_spec)

            # Step 3: Generate complete agent Python code
            logger.info(f"Generating agent code for {agent_spec.get('agent_name')}...")
            agent_code = self._generate_complete_agent_code(agent_spec, customer_name)

            # Step 4: Generate demo JSON
            logger.info(f"Generating demo JSON...")
            demo_json = self._generate_demo_json(agent_spec, customer_name)

            # Step 5: Generate HTML tester
            logger.info(f"Generating HTML tester...")
            html_tester = self._generate_agent_tester_html(agent_spec, demo_json, customer_name)

            # Step 6: Deploy everything to project folder (and optionally to main folders)
            deployment_results = {}
            if deploy_to_storage:
                deployment_results = self._deploy_project_outputs(
                    project_id=project_id or agent_spec.get('agent_id'),
                    agent_spec=agent_spec,
                    agent_code=agent_code,
                    demo_json=demo_json,
                    html_tester=html_tester,
                    deploy_to_main_folders=kwargs.get('deploy_to_main_folders', True),
                    user_guid=user_guid
                )

            agent_id = agent_spec.get('agent_id')
            project_folder = project_id or agent_id

            # Build response
            result = {
                "status": "success",
                "action": "transcript_to_agent",
                "customer_name": customer_name,
                "project_id": project_folder,
                "agent_spec": {
                    "agent_name": agent_spec.get('agent_name'),
                    "agent_id": agent_id,
                    "class_name": agent_spec.get('class_name'),
                    "description": agent_spec.get('description'),
                    "category": agent_spec.get('category'),
                    "actions": [a.get('name') for a in agent_spec.get('actions', [])],
                    "use_cases": agent_spec.get('use_cases', []),
                    "data_sources": agent_spec.get('data_sources', [])
                },
                "files_generated": {
                    "agent_file": f"{agent_id}_agent.py",
                    "demo_file": f"{agent_id}_demo.json",
                    "tester_file": "agent_tester.html",
                    "agent_code_length": len(agent_code),
                    "demo_json_length": len(json.dumps(demo_json)),
                    "html_tester_length": len(html_tester)
                },
                "project_folder": f"rapp_projects/{project_folder}/outputs/",
                "deployment": deployment_results,
                "agent_code": agent_code,
                "demo_json": demo_json,
                "html_tester": html_tester,
                "next_steps": [
                    f"All files in: rapp_projects/{project_folder}/outputs/",
                    f"Open agent_tester.html to test the agent and demo",
                    f"Agent also deployed to: agents/{agent_id}_agent.py" if deployment_results.get('main_agent_deployed') else f"To deploy: copy {agent_id}_agent.py to agents/",
                    "Restart function app to load the new agent"
                ],
                "generated_at": datetime.now().isoformat()
            }

            return json.dumps(result)

        except Exception as e:
            logger.error(f"Error in transcript_to_agent: {str(e)}", exc_info=True)
            return json.dumps({
                "status": "error",
                "error": str(e),
                "action": "transcript_to_agent"
            })

    def _get_transcript_from_storage(self, project_id: str, user_guid: str) -> str:
        """Read transcript from project inputs folder."""
        input_directory = f"rapp_projects/{project_id}/inputs"

        try:
            files = self.storage_manager.list_files(input_directory)
            if not files:
                return ""

            for file_info in files:
                filename = file_info.name if hasattr(file_info, 'name') else str(file_info)
                filename_lower = filename.lower()

                # Check for transcript patterns
                for pattern in self.INPUT_PATTERNS.get('discovery_transcript', []):
                    if pattern in filename_lower:
                        content = self.storage_manager.read_file(input_directory, filename)
                        if content:
                            logger.info(f"Found transcript: {filename}")
                            return content

            return ""
        except Exception as e:
            logger.warning(f"Error reading transcript from storage: {e}")
            return ""

    def _analyze_transcript_for_agent(self, transcript: str, customer_name: str, agent_priority: str = "") -> Dict[str, Any]:
        """Analyze transcript to extract agent specification."""
        client = self._get_openai_client()

        priority_instruction = ""
        if agent_priority:
            priority_instruction = f"\n\nIMPORTANT: The user wants to prioritize building an agent related to: {agent_priority}. Focus on this area if mentioned in the transcript."

        prompt = f"""Analyze this discovery call transcript and design a production-ready AI agent.

CUSTOMER: {customer_name}
{priority_instruction}

TRANSCRIPT:
{transcript}

Based on the transcript, design ONE specific AI agent that addresses their highest-priority need.

Return ONLY valid JSON (no markdown):
{{
  "agent_name": "Human readable name (e.g., 'Artist Contract Analyzer')",
  "agent_id": "snake_case_agent (e.g., 'artist_contract_analyzer_agent')",
  "class_name": "PascalCaseAgent (e.g., 'ArtistContractAnalyzerAgent')",
  "description": "2-3 sentence description of what the agent does and its value proposition",
  "category": "legal|finance|operations|sales|hr|analytics|communications",
  "problem_statement": "The specific problem this agent solves",
  "target_users": ["list of user roles who will use this"],
  "data_sources": [
    {{"name": "source name", "type": "API|Database|File|Manual", "description": "what data it provides"}}
  ],
  "actions": [
    {{
      "name": "action_name",
      "description": "What this action does",
      "parameters": ["param1", "param2"],
      "example_input": {{"action": "action_name", "param1": "value"}},
      "example_output": "Example response text"
    }}
  ],
  "use_cases": ["list of 4-6 specific use cases"],
  "integrations": ["list of systems this would integrate with"],
  "success_metrics": ["how success is measured"],
  "demo_conversation": [
    {{"role": "user", "content": "Example user message"}},
    {{"role": "agent", "content": "Example agent response with **markdown** formatting"}}
  ],
  "sample_scenarios": [
    {{
      "name": "Scenario Name",
      "description": "What this scenario demonstrates",
      "prompts": ["prompt 1", "prompt 2", "prompt 3"]
    }}
  ]
}}

Design 4-6 actions that cover the main capabilities. Make the demo_conversation show a realistic interaction that demonstrates the agent's value. Include at least 2-3 sample scenarios."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        result = parse_llm_json_response(response.choices[0].message.content, "raw_spec")

        # Validate required fields
        required = ['agent_name', 'agent_id', 'class_name', 'description', 'actions']
        missing = [f for f in required if not result.get(f)]
        if missing:
            result['status'] = 'error'
            result['error'] = f"Missing required fields: {missing}"
        else:
            result['status'] = 'success'

        return result

    def _generate_complete_agent_code(self, agent_spec: Dict[str, Any], customer_name: str) -> str:
        """Generate complete, production-ready agent Python code."""
        client = self._get_openai_client()

        prompt = f"""Generate a complete, production-ready Python agent following the BasicAgent pattern.

AGENT SPECIFICATION:
{json.dumps(agent_spec, indent=2)}

CUSTOMER: {customer_name}

REQUIREMENTS:
1. Follow the BasicAgent pattern EXACTLY:
   - Import from agents.basic_agent import BasicAgent
   - Class inherits from BasicAgent
   - __init__ sets self.name, self.metadata with full JSON Schema, calls super().__init__()
   - perform(**kwargs) method that routes to action handlers and ALWAYS returns json.dumps()

2. Metadata must include:
   - name: {agent_spec.get('agent_name', 'Agent')}
   - description: Full description with all actions listed
   - parameters: Complete JSON Schema with all action parameters

3. Code quality:
   - Use logging, not print
   - No hardcoded credentials - use os.environ
   - Wrap external calls in try/except
   - Return JSON strings from perform() - NEVER raw dicts or exceptions
   - Include docstrings

4. Action handlers:
   - Create a _handle_{{action_name}} method for each action
   - Each handler returns a dict that gets json.dumps() in perform()
   - Include realistic mock data that demonstrates the agent's capabilities

5. Include:
   - Module docstring with agent purpose and usage
   - Usage example in if __name__ == "__main__" block
   - All necessary imports at the top

Generate the complete Python code - no placeholders, no TODOs. The agent should work immediately when dropped into the agents/ folder."""

        response = client.chat.completions.create(
            model=os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),
            messages=[{"role": "user", "content": prompt}],
        )

        code = response.choices[0].message.content

        # Extract code from markdown if present
        if '```python' in code:
            code_start = code.find('```python') + 9
            code_end = code.rfind('```')
            if code_end > code_start:
                code = code[code_start:code_end].strip()
        elif '```' in code:
            parts = code.split('```')
            if len(parts) >= 2:
                code = parts[1].strip()

        return code

    def _generate_demo_json(self, agent_spec: Dict[str, Any], customer_name: str) -> Dict[str, Any]:
        """Generate demo JSON in the ScriptedDemoAgent format."""

        # Build actions list from spec
        actions = []
        for action in agent_spec.get('actions', []):
            actions.append({
                "name": action.get('name'),
                "description": action.get('description'),
                "parameters": action.get('parameters', []),
                "example": {
                    "input": action.get('example_input', {}),
                    "output": action.get('example_output', '')
                }
            })

        # Build metadata
        parameters_properties = {
            "action": {
                "type": "string",
                "enum": [a.get('name') for a in agent_spec.get('actions', [])],
                "description": "The action to perform"
            }
        }

        # Add common parameters based on actions
        param_set = set()
        for action in agent_spec.get('actions', []):
            for param in action.get('parameters', []):
                param_set.add(param)

        for param in param_set:
            if param != 'action':
                parameters_properties[param] = {
                    "type": "string",
                    "description": f"{param.replace('_', ' ').title()} parameter"
                }

        demo_json = {
            "agent": {
                "id": agent_spec.get('agent_id'),
                "name": agent_spec.get('agent_name'),
                "version": "1.0.0",
                "category": agent_spec.get('category', 'general'),
                "icon": self._get_category_icon(agent_spec.get('category', 'general')),
                "description": agent_spec.get('description'),
                "tokens": 750,
                "author": f"RAPP Pipeline - {customer_name}",
                "created": datetime.now().strftime("%Y-%m-%d"),
                "updated": datetime.now().strftime("%Y-%m-%d")
            },
            "metadata": {
                "name": agent_spec.get('class_name', '').replace('Agent', ''),
                "description": agent_spec.get('description'),
                "parameters": {
                    "type": "object",
                    "properties": parameters_properties,
                    "required": ["action"]
                }
            },
            "actions": actions,
            "useCases": agent_spec.get('use_cases', []),
            "integrations": agent_spec.get('integrations', []),
            "demoConversation": agent_spec.get('demo_conversation', []),
            "sampleScenarios": agent_spec.get('sample_scenarios', [])
        }

        return demo_json

    def _get_category_icon(self, category: str) -> str:
        """Get FontAwesome icon for category."""
        icons = {
            "legal": "fa-gavel",
            "finance": "fa-chart-line",
            "operations": "fa-cogs",
            "sales": "fa-handshake",
            "hr": "fa-users",
            "analytics": "fa-chart-bar",
            "communications": "fa-comments",
            "general": "fa-robot"
        }
        return icons.get(category, "fa-robot")

    def _deploy_project_outputs(self, project_id: str, agent_spec: Dict, agent_code: str,
                                  demo_json: Dict, html_tester: str, deploy_to_main_folders: bool,
                                  user_guid: str) -> Dict:
        """Deploy all generated files to project folder and optionally to main folders."""
        results = {
            "project_deployed": False,
            "main_agent_deployed": False,
            "main_demo_deployed": False,
            "project_path": None,
            "files": [],
            "errors": []
        }

        agent_id = agent_spec.get('agent_id', 'generated_agent')
        output_dir = f"rapp_projects/{project_id}/outputs"

        # Ensure output directory exists
        try:
            self.storage_manager.ensure_directory_exists(output_dir)
        except Exception as e:
            logger.warning(f"Could not ensure directory exists: {e}")

        # Deploy to project folder
        try:
            # Agent code
            agent_filename = f"{agent_id}_agent.py"
            self.storage_manager.write_file(output_dir, agent_filename, agent_code)
            results['files'].append(f"{output_dir}/{agent_filename}")
            logger.info(f"Saved agent to: {output_dir}/{agent_filename}")

            # Demo JSON
            demo_filename = f"{agent_id}_demo.json"
            self.storage_manager.write_file(output_dir, demo_filename, json.dumps(demo_json, indent=2))
            results['files'].append(f"{output_dir}/{demo_filename}")
            logger.info(f"Saved demo to: {output_dir}/{demo_filename}")

            # HTML Tester
            self.storage_manager.write_file(output_dir, "agent_tester.html", html_tester)
            results['files'].append(f"{output_dir}/agent_tester.html")
            logger.info(f"Saved tester to: {output_dir}/agent_tester.html")

            # Result JSON (without the large code/html fields)
            result_summary = {
                "agent_id": agent_id,
                "agent_name": agent_spec.get('agent_name'),
                "customer_name": agent_spec.get('customer_name', 'Unknown'),
                "category": agent_spec.get('category'),
                "actions": [a.get('name') for a in agent_spec.get('actions', [])],
                "generated_at": datetime.now().isoformat(),
                "files": [agent_filename, demo_filename, "agent_tester.html"]
            }
            self.storage_manager.write_file(output_dir, "result.json", json.dumps(result_summary, indent=2))
            results['files'].append(f"{output_dir}/result.json")

            results['project_deployed'] = True
            results['project_path'] = output_dir
            logger.info(f"All project files saved to: {output_dir}")

        except Exception as e:
            results['errors'].append(f"Project deployment failed: {str(e)}")
            logger.error(f"Failed to deploy to project folder: {e}")

        # Optionally deploy to main agents/ and demos/ folders
        if deploy_to_main_folders:
            try:
                agent_path = f"{agent_id}_agent.py"
                self.storage_manager.write_file('agents', agent_path, agent_code)
                results['main_agent_deployed'] = True
                logger.info(f"Deployed agent to: agents/{agent_path}")
            except Exception as e:
                results['errors'].append(f"Main agent deployment failed: {str(e)}")
                logger.error(f"Failed to deploy to agents/: {e}")

            try:
                demo_path = f"{agent_id}_demo.json"
                self.storage_manager.write_file('demos', demo_path, json.dumps(demo_json, indent=2))
                results['main_demo_deployed'] = True
                logger.info(f"Deployed demo to: demos/{demo_path}")
            except Exception as e:
                results['errors'].append(f"Main demo deployment failed: {str(e)}")
                logger.error(f"Failed to deploy to demos/: {e}")

        return results

    def _generate_agent_tester_html(self, agent_spec: Dict, demo_json: Dict, customer_name: str) -> str:
        """Generate a self-contained HTML page to test both the real agent and demo."""
        agent_id = agent_spec.get('agent_id', 'agent')
        agent_name = agent_spec.get('agent_name', 'Agent')
        description = agent_spec.get('description', '')
        actions = agent_spec.get('actions', [])
        demo_conversation = demo_json.get('demoConversation', [])
        sample_scenarios = demo_json.get('sampleScenarios', [])

        # Build action buttons HTML
        action_buttons = ""
        for action in actions:
            action_buttons += f'''
            <button class="action-btn" onclick="testAction('{action.get('name')}')">
                <span class="action-name">{action.get('name')}</span>
                <span class="action-desc">{action.get('description', '')[:50]}...</span>
            </button>'''

        # Build demo conversation HTML
        demo_steps = ""
        for i, msg in enumerate(demo_conversation):
            role = msg.get('role', 'user')
            content = msg.get('content', '').replace('`', '\\`').replace('${', '\\${')
            demo_steps += f'''
            <div class="demo-step" data-step="{i}">
                <div class="step-role {role}">{role.upper()}</div>
                <div class="step-content">{content}</div>
            </div>'''

        # Build sample prompts
        sample_prompts = ""
        for scenario in sample_scenarios:
            for prompt in scenario.get('prompts', []):
                sample_prompts += f'<button class="sample-prompt" onclick="sendMessage(`{prompt}`)">{prompt}</button>'

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{agent_name} - Agent Tester</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #e0e0e0;
            min-height: 100vh;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}

        /* Header */
        .header {{
            background: rgba(0, 212, 255, 0.1);
            border: 1px solid #0f3460;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
        }}
        .header h1 {{ color: #00d4ff; margin-bottom: 8px; }}
        .header p {{ color: #888; font-size: 14px; }}
        .header .customer {{ color: #00ff88; font-size: 12px; margin-top: 8px; }}

        /* Config Panel */
        .config-panel {{
            background: #0a0a1a;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 20px;
            display: grid;
            grid-template-columns: 1fr 1fr auto;
            gap: 12px;
            align-items: end;
        }}
        .config-panel label {{ display: block; font-size: 12px; color: #888; margin-bottom: 4px; }}
        .config-panel input {{
            width: 100%;
            padding: 10px;
            background: #16213e;
            border: 1px solid #0f3460;
            border-radius: 6px;
            color: #fff;
            font-size: 13px;
        }}
        .config-panel input:focus {{ outline: none; border-color: #00d4ff; }}
        .save-config {{
            padding: 10px 20px;
            background: #00d4ff;
            color: #1a1a2e;
            border: none;
            border-radius: 6px;
            font-weight: bold;
            cursor: pointer;
        }}

        /* Tabs */
        .tabs {{
            display: flex;
            gap: 8px;
            margin-bottom: 20px;
        }}
        .tab {{
            padding: 12px 24px;
            background: #16213e;
            border: 2px solid #0f3460;
            border-radius: 8px;
            color: #888;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .tab:hover {{ border-color: #00d4ff; }}
        .tab.active {{
            background: #00d4ff;
            color: #1a1a2e;
            border-color: #00d4ff;
            font-weight: bold;
        }}

        /* Main Content Grid */
        .main-grid {{
            display: grid;
            grid-template-columns: 300px 1fr;
            gap: 20px;
        }}

        /* Sidebar */
        .sidebar {{
            background: #0f0f1a;
            border-radius: 12px;
            padding: 16px;
        }}
        .sidebar h3 {{
            color: #00d4ff;
            font-size: 14px;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 1px solid #1a4a7a;
        }}
        .action-btn {{
            display: block;
            width: 100%;
            padding: 12px;
            margin-bottom: 8px;
            background: #16213e;
            border: 1px solid #0f3460;
            border-radius: 8px;
            color: #fff;
            text-align: left;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .action-btn:hover {{
            background: #1a5a9a;
            border-color: #00d4ff;
            transform: translateX(4px);
        }}
        .action-name {{ display: block; font-weight: bold; margin-bottom: 4px; }}
        .action-desc {{ display: block; font-size: 11px; color: #666; }}

        .sample-prompts {{ margin-top: 16px; }}
        .sample-prompt {{
            display: block;
            width: 100%;
            padding: 8px 12px;
            margin-bottom: 6px;
            background: #0a0a1a;
            border: 1px solid #1a4a7a;
            border-radius: 6px;
            color: #aaa;
            font-size: 12px;
            text-align: left;
            cursor: pointer;
        }}
        .sample-prompt:hover {{ background: #16213e; color: #fff; }}

        /* Chat Area */
        .chat-area {{
            background: #0f0f1a;
            border-radius: 12px;
            display: flex;
            flex-direction: column;
            height: 600px;
        }}
        .chat-messages {{
            flex: 1;
            overflow-y: auto;
            padding: 16px;
        }}
        .message {{
            margin-bottom: 16px;
            padding: 12px 16px;
            border-radius: 12px;
            max-width: 85%;
        }}
        .message.user {{
            background: #00d4ff;
            color: #1a1a2e;
            margin-left: auto;
        }}
        .message.agent {{
            background: #16213e;
            border: 1px solid #0f3460;
        }}
        .message pre {{
            background: #0a0a1a;
            padding: 12px;
            border-radius: 6px;
            overflow-x: auto;
            margin-top: 8px;
            font-size: 12px;
        }}

        .chat-input {{
            padding: 16px;
            border-top: 1px solid #1a4a7a;
            display: flex;
            gap: 12px;
        }}
        .chat-input input {{
            flex: 1;
            padding: 12px 16px;
            background: #16213e;
            border: 1px solid #0f3460;
            border-radius: 8px;
            color: #fff;
            font-size: 14px;
        }}
        .chat-input input:focus {{ outline: none; border-color: #00d4ff; }}
        .chat-input button {{
            padding: 12px 24px;
            background: #00d4ff;
            color: #1a1a2e;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
        }}
        .chat-input button:hover {{ background: #00ffff; }}
        .chat-input button:disabled {{ background: #333; color: #666; cursor: not-allowed; }}

        /* Demo Panel */
        .demo-panel {{ display: none; }}
        .demo-panel.active {{ display: block; }}
        .demo-step {{
            background: #16213e;
            border-radius: 8px;
            margin-bottom: 12px;
            overflow: hidden;
        }}
        .step-role {{
            padding: 8px 16px;
            font-size: 11px;
            font-weight: bold;
            background: #0a0a1a;
        }}
        .step-role.user {{ color: #00ff88; }}
        .step-role.agent {{ color: #00d4ff; }}
        .step-content {{
            padding: 16px;
            white-space: pre-wrap;
            line-height: 1.6;
        }}

        .demo-controls {{
            display: flex;
            gap: 12px;
            margin-top: 16px;
        }}
        .demo-btn {{
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }}
        .demo-btn.play {{ background: #00ff88; color: #1a1a2e; }}
        .demo-btn.reset {{ background: #ff6b6b; color: #fff; }}

        /* Status */
        .status {{
            padding: 8px 16px;
            background: #0a0a1a;
            border-radius: 6px;
            font-size: 12px;
            color: #666;
            margin-top: 12px;
        }}
        .status.success {{ color: #00ff88; }}
        .status.error {{ color: #ff6b6b; }}
        .status.loading {{ color: #00d4ff; }}

        /* Responsive */
        @media (max-width: 900px) {{
            .main-grid {{ grid-template-columns: 1fr; }}
            .config-panel {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{agent_name}</h1>
            <p>{description}</p>
            <div class="customer">Customer: {customer_name}</div>
        </div>

        <div class="config-panel">
            <div>
                <label>API Endpoint</label>
                <input type="text" id="apiEndpoint" value="http://localhost:7071/api/businessinsightbot_function" placeholder="API URL">
            </div>
            <div>
                <label>Function Key (optional)</label>
                <input type="text" id="apiKey" placeholder="Function key for Azure deployment">
            </div>
            <button class="save-config" onclick="saveConfig()">Save</button>
        </div>

        <div class="tabs">
            <button class="tab active" onclick="switchTab('chat')">Real Agent</button>
            <button class="tab" onclick="switchTab('demo')">Demo Mode</button>
        </div>

        <div class="main-grid">
            <div class="sidebar">
                <h3>Agent Actions</h3>
                {action_buttons}

                <div class="sample-prompts">
                    <h3>Sample Prompts</h3>
                    {sample_prompts}
                </div>
            </div>

            <div id="chatPanel" class="chat-area">
                <div class="chat-messages" id="chatMessages"></div>
                <div class="chat-input">
                    <input type="text" id="messageInput" placeholder="Type a message..." onkeypress="if(event.key==='Enter')sendMessage()">
                    <button onclick="sendMessage()" id="sendBtn">Send</button>
                </div>
                <div class="status" id="status">Ready</div>
            </div>

            <div id="demoPanel" class="demo-panel chat-area">
                <div class="chat-messages">
                    {demo_steps}
                </div>
                <div class="demo-controls" style="padding: 16px;">
                    <button class="demo-btn play" onclick="playDemo()">Play Demo</button>
                    <button class="demo-btn reset" onclick="resetDemo()">Reset</button>
                </div>
                <div class="status" id="demoStatus">Click "Play Demo" to start</div>
            </div>
        </div>
    </div>

    <script>
        // Configuration
        let config = {{
            endpoint: localStorage.getItem('agentTesterEndpoint') || 'http://localhost:7071/api/businessinsightbot_function',
            key: localStorage.getItem('agentTesterKey') || ''
        }};

        // Demo JSON data (embedded)
        const demoJson = {json.dumps(demo_json)};
        const agentId = '{agent_id}';

        // Initialize
        document.getElementById('apiEndpoint').value = config.endpoint;
        document.getElementById('apiKey').value = config.key;

        let conversationHistory = [];
        let currentDemoStep = 0;

        function saveConfig() {{
            config.endpoint = document.getElementById('apiEndpoint').value;
            config.key = document.getElementById('apiKey').value;
            localStorage.setItem('agentTesterEndpoint', config.endpoint);
            localStorage.setItem('agentTesterKey', config.key);
            setStatus('Configuration saved!', 'success');
        }}

        function switchTab(tab) {{
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            event.target.classList.add('active');

            document.getElementById('chatPanel').style.display = tab === 'chat' ? 'flex' : 'none';
            document.getElementById('demoPanel').style.display = tab === 'demo' ? 'flex' : 'none';
            document.getElementById('demoPanel').classList.toggle('active', tab === 'demo');
        }}

        function setStatus(message, type = '') {{
            const status = document.getElementById('status');
            status.textContent = message;
            status.className = 'status ' + type;
        }}

        function addMessage(content, role) {{
            const messages = document.getElementById('chatMessages');
            const div = document.createElement('div');
            div.className = 'message ' + role;

            // Handle markdown-like formatting
            let formatted = content
                .replace(/\\*\\*(.+?)\\*\\*/g, '<strong>$1</strong>')
                .replace(/\\n/g, '<br>')
                .replace(/`([^`]+)`/g, '<code>$1</code>');

            div.innerHTML = formatted;
            messages.appendChild(div);
            messages.scrollTop = messages.scrollHeight;
        }}

        async function sendMessage(text) {{
            const input = document.getElementById('messageInput');
            const message = text || input.value.trim();
            if (!message) return;

            input.value = '';
            addMessage(message, 'user');
            setStatus('Sending...', 'loading');
            document.getElementById('sendBtn').disabled = true;

            conversationHistory.push({{ role: 'user', content: message }});

            try {{
                let url = config.endpoint;
                if (config.key) {{
                    url += (url.includes('?') ? '&' : '?') + 'code=' + config.key;
                }}

                const response = await fetch(url, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{
                        user_input: message,
                        conversation_history: conversationHistory
                    }})
                }});

                const data = await response.json();
                const assistantResponse = data.assistant_response || data.error || 'No response';

                addMessage(assistantResponse, 'agent');
                conversationHistory.push({{ role: 'assistant', content: assistantResponse }});
                setStatus('Ready', 'success');

            }} catch (err) {{
                setStatus('Error: ' + err.message, 'error');
                addMessage('Error: ' + err.message, 'agent');
            }}

            document.getElementById('sendBtn').disabled = false;
        }}

        function testAction(actionName) {{
            const prompt = `Test the ${{actionName}} action`;
            sendMessage(prompt);
        }}

        // Demo functions
        function playDemo() {{
            const steps = document.querySelectorAll('.demo-step');
            let i = 0;

            function showNext() {{
                if (i < steps.length) {{
                    steps[i].style.display = 'block';
                    steps[i].scrollIntoView({{ behavior: 'smooth' }});
                    i++;
                    document.getElementById('demoStatus').textContent = `Step ${{i}} of ${{steps.length}}`;
                    setTimeout(showNext, 2000);
                }} else {{
                    document.getElementById('demoStatus').textContent = 'Demo complete!';
                }}
            }}

            // Hide all first
            steps.forEach(s => s.style.display = 'none');
            showNext();
        }}

        function resetDemo() {{
            document.querySelectorAll('.demo-step').forEach(s => s.style.display = 'block');
            document.getElementById('demoStatus').textContent = 'Click "Play Demo" to start';
        }}
    </script>
</body>
</html>'''
        return html


# Usage example
if __name__ == "__main__":
    agent = RAPPAgent()

    # Test discovery preparation
    result = agent.perform(
        action="prepare_discovery_call",
        customer_name="Acme Corp",
        industry="manufacturing"
    )
    print("Prepare Discovery:", json.loads(result)["status"])

    # Test MVP generation
    result = agent.perform(
        action="generate_mvp_poke",
        customer_name="Acme Corp",
        project_name="Inventory Optimizer",
        problem_statement="Manual inventory counts take 4 hours daily"
    )
    print("MVP Poke:", json.loads(result)["status"])

    # Test quality gate
    result = agent.perform(
        action="execute_quality_gate",
        gate="QG1",
        customer_name="Acme Corp",
        input_data={"problemStatements": [{"problem": "Manual data entry"}]}
    )
    print("QG1:", json.loads(result).get("decision", "N/A"))

    # Test pipeline status
    result = agent.perform(
        action="get_pipeline_status",
        customer_name="Acme Corp",
        project_data={"current_step": 3, "completed_steps": [1, 2]}
    )
    print("Status:", json.loads(result)["progress_percent"], "% complete")
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
