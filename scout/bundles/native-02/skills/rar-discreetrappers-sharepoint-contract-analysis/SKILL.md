---
name: "rar-discreetrappers-sharepoint-contract-analysis"
description: "Analyzes recording and entertainment contracts FROM THE LABEL'S PERSPECTIVE. Identifies risks to the label, flags artist-favorable terms, extracts clauses, and generates executive summaries for label decision-makers. Supports PDF, DOCX, and TXT formats."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/sharepoint_contract_analysis_agent", "rar_sha256": "6bfac36ced9e10e89b7a35b6e3a7464d3cc66e4f8832feedbbde899852aa3893", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.2", "author": "Bill Whalen", "tags": ["integrations", "sharepoint", "contracts", "analysis", "legal"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/sharepoint_contract_analysis_agent`. The original RAPP
agent is preserved byte-for-byte in `sharepoint_contract_analysis_agent.py` and in the RCI capsule.

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

Agent: ContractAnalysisAgent
Purpose: Analyze, interpret, and summarize contracts stored in Azure File Storage
Data Sources: Azure File Storage (contracts/ folder), Azure OpenAI for analysis
Production Ready: Reads real documents, extracts text, performs AI-powered analysis

Supported formats: PDF, DOCX, TXT
Storage path: contracts/ folder in Azure File Storage

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Action to perform. Use 'full_workup' when user says 'work on' a contract to run comprehensive analysis.",
      "enum": [
        "list_contracts",
        "full_workup",
        "analyze_contract",
        "extract_clauses",
        "summarize_contract",
        "identify_risks",
        "compare_contracts"
      ],
      "type": "string"
    },
    "audience": {
      "description": "Target audience for summary: legal, business, executive",
      "enum": [
        "legal",
        "business",
        "executive"
      ],
      "type": "string"
    },
    "clause_types": {
      "description": "Specific clause types to extract: financial, rights, obligations, termination, exclusivity, territory, duration",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "contract_name": {
      "description": "Name of the contract file in Azure storage (e.g., 'artist_agreement_2026.pdf')",
      "type": "string"
    },
    "contract_name_b": {
      "description": "Second contract name for comparison (used with compare_contracts action)",
      "type": "string"
    },
    "summary_type": {
      "description": "Type of summary: executive (brief), detailed, or legal",
      "enum": [
        "executive",
        "detailed",
        "legal"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sharepoint_contract_analysis_agent.py` and embedded as the fenced Python below (sha256 6bfac36ced9e10e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sharepoint_contract_analysis_agent.py` first:

```bash
python3 sharepoint_contract_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sharepoint_contract_analysis_agent.py   # or on stdin
python3 sharepoint_contract_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/sharepoint_contract_analysis_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/sharepoint_contract_analysis_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/sharepoint_contract_analysis_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Agent: ContractAnalysisAgent
Purpose: Analyze, interpret, and summarize contracts stored in Azure File Storage
Data Sources: Azure File Storage (contracts/ folder), Azure OpenAI for analysis
Production Ready: Reads real documents, extracts text, performs AI-powered analysis

Supported formats: PDF, DOCX, TXT
Storage path: contracts/ folder in Azure File Storage
"""

from __future__ import annotations

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/sharepoint_contract_analysis_agent",
    "version": "1.0.2",
    "display_name": "ContractAnalysis",
    "description": "Analyzes contract documents in Azure File Storage with Azure OpenAI \u2014 clause extraction, risk flagging, and comparison.",
    "author": "Bill Whalen",
    "tags": ["integrations", "sharepoint", "contracts", "analysis", "legal"],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": ["AZURE_FILES_SHARE_NAME", "AZURE_OPENAI_API_VERSION", "AZURE_OPENAI_DEPLOYMENT_NAME", "AZURE_OPENAI_ENDPOINT", "AZURE_STORAGE_ACCOUNT_NAME"],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import logging
import os
import io
import re
from datetime import datetime
from typing import Optional, Dict, List, Any
from agents.basic_agent import BasicAgent

# Document processing imports
# Note: Auto-installation of missing packages is handled globally by function_app.py
# These imports will trigger auto-install if the packages are missing

# PDF support - try pypdf (modern) first, then PyPDF2 (legacy)
PDF_SUPPORT = False
pypdf_module = None

try:
    import pypdf
    pypdf_module = pypdf
    PDF_SUPPORT = True
except ImportError:
    try:
        import PyPDF2
        pypdf_module = PyPDF2
        PDF_SUPPORT = True
    except ImportError:
        logging.warning("PDF support disabled - pypdf/PyPDF2 not available")

# PDF generation support (reportlab)
PDF_GENERATION = False
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
    PDF_GENERATION = True
except ImportError:
    logging.warning("PDF generation disabled - reportlab not available")

# DOCX support
DOCX_SUPPORT = False
DocxDocument = None

try:
    from docx import Document as DocxDocument
    DOCX_SUPPORT = True
except ImportError:
    logging.warning("DOCX support disabled - python-docx not available")

# Azure imports
try:
    from azure.identity import DefaultAzureCredential
    from azure.storage.fileshare import ShareFileClient, ShareDirectoryClient, ShareServiceClient
    from openai import AzureOpenAI
    from azure.identity import get_bearer_token_provider
    AZURE_SUPPORT = True
except ImportError as e:
    AZURE_SUPPORT = False
    logging.warning(f"Azure SDK not fully installed: {e}")


class ContractAnalysisAgent(BasicAgent):
    """
    Production contract analysis agent that reads documents from Azure File Storage
    and uses Azure OpenAI to extract clauses, generate summaries, and identify risks.

    Storage Structure:
        contracts/           - Root folder for all contracts
        contracts/templates/ - Standard contract templates for comparison
        contracts/analysis/  - Stored analysis results (optional)

    Supported Actions:
        - list_contracts: List available contracts in storage
        - analyze_contract: Full analysis with all extractions
        - extract_clauses: Extract specific clause categories
        - summarize_contract: Generate executive summary
        - identify_risks: Compare against standard terms
        - compare_contracts: Compare two contracts side-by-side
    """

    def __init__(self):
        self.name = 'ContractAnalysis'
        self.metadata = {
            "name": self.name,
            "description": "Analyzes recording and entertainment contracts FROM THE LABEL'S PERSPECTIVE. Identifies risks to the label, flags artist-favorable terms, extracts clauses, and generates executive summaries for label decision-makers. Supports PDF, DOCX, and TXT formats.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "description": "Action to perform. Use 'full_workup' when user says 'work on' a contract to run comprehensive analysis.",
                        "enum": [
                            "list_contracts",
                            "full_workup",
                            "analyze_contract",
                            "extract_clauses",
                            "summarize_contract",
                            "identify_risks",
                            "compare_contracts"
                        ]
                    },
                    "contract_name": {
                        "type": "string",
                        "description": "Name of the contract file in Azure storage (e.g., 'artist_agreement_2026.pdf')"
                    },
                    "contract_name_b": {
                        "type": "string",
                        "description": "Second contract name for comparison (used with compare_contracts action)"
                    },
                    "clause_types": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Specific clause types to extract: financial, rights, obligations, termination, exclusivity, territory, duration"
                    },
                    "summary_type": {
                        "type": "string",
                        "description": "Type of summary: executive (brief), detailed, or legal",
                        "enum": ["executive", "detailed", "legal"]
                    },
                    "audience": {
                        "type": "string",
                        "description": "Target audience for summary: legal, business, executive",
                        "enum": ["legal", "business", "executive"]
                    }
                },
                "required": ["action"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)

        # Initialize Azure clients
        self.storage_account = os.environ.get('AZURE_STORAGE_ACCOUNT_NAME', 'stov4bzgynnlvii')
        self.share_name = os.environ.get('AZURE_FILES_SHARE_NAME', 'azfrapp-ov4bzgynnlviiov4bzgynnlvii')
        self.contracts_folder = 'contracts'

        # Initialize OpenAI client
        self.openai_client = None
        self.deployment_name = os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-5.1-chat')
        self._init_openai_client()

    def _init_openai_client(self):
        """Initialize Azure OpenAI client with managed identity."""
        try:
            endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
            if not endpoint:
                logging.warning("AZURE_OPENAI_ENDPOINT not set")
                return

            credential = DefaultAzureCredential()
            token_provider = get_bearer_token_provider(
                credential,
                "https://cognitiveservices.azure.com/.default"
            )

            self.openai_client = AzureOpenAI(
                azure_endpoint=endpoint,
                azure_ad_token_provider=token_provider,
                api_version=os.environ.get('AZURE_OPENAI_API_VERSION', '2025-01-01-preview')
            )
            logging.info("ContractAnalysisAgent: OpenAI client initialized")
        except Exception as e:
            logging.error(f"Failed to initialize OpenAI client: {e}")

    def _get_share_service_client(self) -> Optional[ShareServiceClient]:
        """Get Azure File Share service client."""
        try:
            credential = DefaultAzureCredential()
            account_url = f"https://{self.storage_account}.file.core.windows.net"
            return ShareServiceClient(
                account_url=account_url,
                credential=credential,
                token_intent="backup"  # Required for token-based auth
            )
        except Exception as e:
            logging.error(f"Failed to create share service client: {e}")
            return None

    def _list_files_in_folder(self, folder_path: str = None) -> List[Dict]:
        """List all files in the contracts folder."""
        try:
            service_client = self._get_share_service_client()
            if not service_client:
                return []

            share_client = service_client.get_share_client(self.share_name)
            target_folder = folder_path or self.contracts_folder

            try:
                directory_client = share_client.get_directory_client(target_folder)
                files = []

                for item in directory_client.list_directories_and_files():
                    if not item.get('is_directory', False):
                        file_name = item['name']
                        # Get file properties
                        file_client = directory_client.get_file_client(file_name)
                        props = file_client.get_file_properties()

                        files.append({
                            "name": file_name,
                            "size_kb": round(props.size / 1024, 2),
                            "last_modified": props.last_modified.isoformat() if props.last_modified else None,
                            "path": f"{target_folder}/{file_name}"
                        })

                return files
            except Exception as e:
                if "ResourceNotFound" in str(e):
                    logging.info(f"Folder {target_folder} does not exist, will be created on first upload")
                    return []
                raise

        except Exception as e:
            logging.error(f"Error listing files: {e}")
            return []

    def _read_file_content(self, file_path: str) -> Optional[bytes]:
        """Read file content from Azure File Storage."""
        try:
            service_client = self._get_share_service_client()
            if not service_client:
                return None

            share_client = service_client.get_share_client(self.share_name)
            file_client = share_client.get_file_client(file_path)

            download = file_client.download_file()
            return download.readall()

        except Exception as e:
            logging.error(f"Error reading file {file_path}: {e}")
            return None

    def _write_file_content(self, file_path: str, content: str) -> bool:
        """Write content to Azure File Storage."""
        try:
            service_client = self._get_share_service_client()
            if not service_client:
                return False

            share_client = service_client.get_share_client(self.share_name)

            # Ensure directory exists
            dir_path = '/'.join(file_path.split('/')[:-1])
            if dir_path:
                try:
                    dir_client = share_client.get_directory_client(dir_path)
                    dir_client.create_directory()
                except Exception:
                    pass  # Directory may already exist

            file_client = share_client.get_file_client(file_path)
            content_bytes = content.encode('utf-8')
            file_client.upload_file(content_bytes)

            logging.info(f"Successfully wrote file: {file_path}")
            return True

        except Exception as e:
            logging.error(f"Error writing file {file_path}: {e}")
            return False

    def _generate_download_url(self, file_path: str) -> str:
        """Generate a download URL for the file.

        Note: This storage account uses Entra ID authentication only (shared key access disabled).
        The returned URL requires authentication to access. Users can:
        1. Open in Azure Portal to download
        2. Use Azure Storage Explorer with their credentials
        3. Access via authenticated API calls
        """
        account_url = f"https://{self.storage_account}.file.core.windows.net"
        file_url = f"{account_url}/{self.share_name}/{file_path}"
        return file_url

    def _save_analysis_report(self, contract_name: str, analysis_data: Dict) -> Dict:
        """Save analysis report as professional PDF and return download info."""
        try:
            # Generate report filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_name = contract_name.rsplit('.', 1)[0]  # Remove extension
            report_name = f"{base_name}_analysis_{timestamp}.pdf"
            report_path = f"contracts/analysis/{report_name}"

            # Generate PDF report
            if PDF_GENERATION:
                pdf_bytes = self._generate_pdf_report(contract_name, analysis_data)
                if pdf_bytes:
                    # Write PDF to storage
                    if self._write_file_bytes(report_path, pdf_bytes):
                        download_url = self._generate_download_url(report_path)
                        return {
                            "saved": True,
                            "format": "PDF",
                            "report_name": report_name,
                            "report_path": report_path,
                            "download_url": download_url,
                            "size_kb": round(len(pdf_bytes) / 1024, 2)
                        }

            # Fallback to JSON if PDF generation fails
            report_name = f"{base_name}_analysis_{timestamp}.json"
            report_path = f"contracts/analysis/{report_name}"
            report_content = json.dumps(analysis_data, indent=2, default=str)

            if self._write_file_content(report_path, report_content):
                download_url = self._generate_download_url(report_path)
                return {
                    "saved": True,
                    "format": "JSON",
                    "report_name": report_name,
                    "report_path": report_path,
                    "download_url": download_url,
                    "size_kb": round(len(report_content) / 1024, 2)
                }
            else:
                return {"saved": False, "error": "Failed to write file"}

        except Exception as e:
            logging.error(f"Error saving analysis report: {e}")
            return {"saved": False, "error": str(e)}

    def _write_file_bytes(self, file_path: str, content: bytes) -> bool:
        """Write binary content to Azure File Storage."""
        try:
            service_client = self._get_share_service_client()
            if not service_client:
                return False

            share_client = service_client.get_share_client(self.share_name)

            # Ensure directory exists
            dir_path = '/'.join(file_path.split('/')[:-1])
            if dir_path:
                try:
                    dir_client = share_client.get_directory_client(dir_path)
                    dir_client.create_directory()
                except Exception:
                    pass  # Directory may already exist

            file_client = share_client.get_file_client(file_path)
            file_client.upload_file(content)

            logging.info(f"Successfully wrote binary file: {file_path}")
            return True

        except Exception as e:
            logging.error(f"Error writing binary file {file_path}: {e}")
            return False

    def _generate_pdf_report(self, contract_name: str, analysis_data: Dict) -> Optional[bytes]:
        """Generate a professional PDF analysis report."""
        if not PDF_GENERATION:
            return None

        try:
            # === DEBUG LOGGING: Dump structure of all data sections ===
            logging.info("=" * 60)
            logging.info("PDF GENERATION - DATA STRUCTURE ANALYSIS")
            logging.info("=" * 60)

            # Check executive_summary
            exec_summary = analysis_data.get('executive_summary', {})
            if isinstance(exec_summary, dict):
                logging.info(f"executive_summary keys: {list(exec_summary.keys())}")
                if exec_summary.get('parse_error'):
                    logging.error(f"executive_summary has PARSE ERROR")
                logging.info(f"  - summary length: {len(exec_summary.get('summary', ''))}")
                logging.info(f"  - risk_level: {exec_summary.get('risk_level', 'MISSING')}")
                logging.info(f"  - key_points count: {len(exec_summary.get('key_points', []))}")
            else:
                logging.error(f"executive_summary is NOT a dict: {type(exec_summary)}")

            # Check risk_assessment
            risk_assessment = analysis_data.get('risk_assessment', {})
            if isinstance(risk_assessment, dict):
                logging.info(f"risk_assessment keys: {list(risk_assessment.keys())}")
                if risk_assessment.get('parse_error'):
                    logging.error(f"risk_assessment has PARSE ERROR - raw: {risk_assessment.get('raw_analysis', '')[:500]}")
                logging.info(f"  - overall_risk_level: {risk_assessment.get('overall_risk_level', 'MISSING')}")
                logging.info(f"  - risk_score: {risk_assessment.get('risk_score', 'MISSING')}")
                logging.info(f"  - risks count: {len(risk_assessment.get('risks', []))}")
                logging.info(f"  - summary length: {len(risk_assessment.get('summary', ''))}")
            else:
                logging.error(f"risk_assessment is NOT a dict: {type(risk_assessment)}")

            # Check full_analysis
            full_analysis = analysis_data.get('full_analysis', {})
            if isinstance(full_analysis, dict):
                logging.info(f"full_analysis keys: {list(full_analysis.keys())}")
                if full_analysis.get('parse_error'):
                    logging.error(f"full_analysis has PARSE ERROR - raw: {full_analysis.get('raw_analysis', '')[:500]}")
                logging.info(f"  - contract_type: {full_analysis.get('contract_type', 'MISSING')}")
                logging.info(f"  - parties count: {len(full_analysis.get('parties', []))}")
                logging.info(f"  - financial_terms keys: {list(full_analysis.get('financial_terms', {}).keys()) if isinstance(full_analysis.get('financial_terms'), dict) else 'NOT DICT'}")
            else:
                logging.error(f"full_analysis is NOT a dict: {type(full_analysis)}")

            # Check extracted_clauses
            extracted_clauses = analysis_data.get('extracted_clauses', {})
            if isinstance(extracted_clauses, dict):
                logging.info(f"extracted_clauses keys: {list(extracted_clauses.keys())}")
                if extracted_clauses.get('parse_error'):
                    logging.error(f"extracted_clauses has PARSE ERROR")

            logging.info("=" * 60)

            # Create PDF in memory
            buffer = io.BytesIO()
            doc = SimpleDocTemplate(
                buffer,
                pagesize=letter,
                leftMargin=0.75*inch,
                rightMargin=0.75*inch,
                topMargin=0.75*inch,
                bottomMargin=0.75*inch
            )

            # Define styles
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=20,
                spaceAfter=20,
                alignment=TA_CENTER,
                textColor=colors.HexColor('#1a365d')
            )
            heading_style = ParagraphStyle(
                'CustomHeading',
                parent=styles['Heading2'],
                fontSize=14,
                spaceBefore=20,
                spaceAfter=10,
                textColor=colors.HexColor('#2c5282')
            )
            subheading_style = ParagraphStyle(
                'CustomSubHeading',
                parent=styles['Heading3'],
                fontSize=12,
                spaceBefore=12,
                spaceAfter=6,
                textColor=colors.HexColor('#4a5568')
            )
            body_style = ParagraphStyle(
                'CustomBody',
                parent=styles['Normal'],
                fontSize=10,
                spaceAfter=8,
                leading=14,
                alignment=TA_JUSTIFY
            )
            bullet_style = ParagraphStyle(
                'CustomBullet',
                parent=styles['Normal'],
                fontSize=10,
                spaceAfter=4,
                leftIndent=20,
                bulletIndent=10
            )
            risk_high = ParagraphStyle(
                'RiskHigh',
                parent=styles['Normal'],
                fontSize=12,
                textColor=colors.HexColor('#c53030'),
                spaceAfter=8
            )
            risk_medium = ParagraphStyle(
                'RiskMedium',
                parent=styles['Normal'],
                fontSize=12,
                textColor=colors.HexColor('#dd6b20'),
                spaceAfter=8
            )
            risk_low = ParagraphStyle(
                'RiskLow',
                parent=styles['Normal'],
                fontSize=12,
                textColor=colors.HexColor('#38a169'),
                spaceAfter=8
            )

            story = []

            # Title
            story.append(Paragraph("CONTRACT ANALYSIS REPORT", title_style))
            story.append(Spacer(1, 0.1*inch))

            # Contract info header
            story.append(Paragraph(f"<b>Contract:</b> {contract_name}", body_style))
            story.append(Paragraph(f"<b>Analysis Date:</b> {analysis_data.get('analyzed_at', datetime.now().isoformat())}", body_style))
            story.append(Spacer(1, 0.2*inch))

            # Horizontal line
            story.append(Table([['']], colWidths=[7*inch], rowHeights=[2]))
            story[-1].setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2c5282'))]))
            story.append(Spacer(1, 0.2*inch))

            # Executive Summary Section
            exec_summary = analysis_data.get('executive_summary', {})
            if exec_summary:
                story.append(Paragraph("EXECUTIVE SUMMARY", heading_style))

                if isinstance(exec_summary, dict):
                    summary_text = exec_summary.get('summary', '')
                    if summary_text:
                        # Use larger max_length for executive summary - don't truncate
                        story.append(Paragraph(self._clean_text(summary_text, max_length=2000), body_style))

                    # Risk Level Box
                    risk_level = exec_summary.get('risk_level', 'unknown').upper()
                    risk_style = risk_high if risk_level == 'HIGH' else (risk_medium if risk_level == 'MEDIUM' else risk_low)
                    story.append(Spacer(1, 0.1*inch))
                    story.append(Paragraph(f"<b>Overall Risk Level: {risk_level}</b>", risk_style))

                    # Key Points
                    key_points = exec_summary.get('key_points', [])
                    if key_points:
                        story.append(Paragraph("<b>Key Points:</b>", subheading_style))
                        for point in key_points[:10]:  # Limit to 10 points
                            if isinstance(point, dict):
                                # Format dict with point and clickable ref
                                point_text = point.get('point', '')
                                point_ref = point.get('ref', '')
                                clickable_ref = self._format_clickable_ref(point_ref, analysis_data.get('_contract_text', '')) if point_ref else ""
                                formatted = f"{self._clean_text(point_text, max_length=300)} {clickable_ref}"
                            else:
                                formatted = self._clean_text(str(point), max_length=300)
                            story.append(Paragraph(f"* {formatted}", bullet_style))

                    # Recommendation
                    recommendation = exec_summary.get('recommendation', '')
                    if recommendation:
                        story.append(Spacer(1, 0.1*inch))
                        story.append(Paragraph(f"<b>Recommendation:</b> {self._clean_text(recommendation, max_length=1000)}", body_style))

            story.append(PageBreak())

            # Risk Assessment Section
            risk_assessment = analysis_data.get('risk_assessment', {})
            story.append(Paragraph("RISK ASSESSMENT", heading_style))

            if isinstance(risk_assessment, dict):
                # Check for parse error
                if risk_assessment.get('parse_error'):
                    story.append(Paragraph(
                        "<b><font color='red'>Warning: Risk assessment data extraction encountered issues.</font></b>",
                        body_style
                    ))
                    # Show raw analysis if available
                    raw_analysis = risk_assessment.get('raw_analysis', '')
                    if raw_analysis and len(raw_analysis) > 50:
                        story.append(Paragraph("<b>Raw Analysis Output:</b>", subheading_style))
                        # Show first 2000 chars of raw analysis
                        story.append(Paragraph(self._clean_text(raw_analysis[:2000], max_length=2000), body_style))
                else:
                    # Overall risk
                    overall_risk = risk_assessment.get('overall_risk_level', 'Unknown').upper()
                    risk_score = risk_assessment.get('risk_score', 'N/A')
                    risk_style = risk_high if overall_risk == 'HIGH' else (risk_medium if overall_risk == 'MEDIUM' else risk_low)
                    story.append(Paragraph(f"<b>Risk Level: {overall_risk} | Score: {risk_score}/100</b>", risk_style))

                    # Summary
                    risk_summary = risk_assessment.get('summary', '')
                    if risk_summary:
                        story.append(Paragraph(self._clean_text(risk_summary, max_length=1000), body_style))
                    else:
                        story.append(Paragraph("<i>No risk summary available.</i>", body_style))

                    # Individual risks
                    risks = risk_assessment.get('risks', [])
                    if risks:
                        story.append(Paragraph("<b>Identified Risks:</b>", subheading_style))

                        # Create table cell style for wrapping text
                        cell_style = ParagraphStyle(
                            'CellStyle',
                            parent=styles['Normal'],
                            fontSize=8,
                            leading=10,
                            spaceAfter=0
                        )
                        header_cell_style = ParagraphStyle(
                            'HeaderCellStyle',
                            parent=styles['Normal'],
                            fontSize=9,
                            leading=11,
                            textColor=colors.white,
                            fontName='Helvetica-Bold'
                        )

                        # Build header row with Paragraphs
                        risk_data = [[
                            Paragraph('Category', header_cell_style),
                            Paragraph('Severity', header_cell_style),
                            Paragraph('Description', header_cell_style)
                        ]]

                        for risk in risks[:10]:  # Limit to 10 risks
                            if isinstance(risk, dict):
                                desc_text = self._clean_text(risk.get('description', 'N/A'), max_length=300)
                                risk_data.append([
                                    Paragraph(risk.get('category', 'N/A'), cell_style),
                                    Paragraph(risk.get('severity', 'N/A').upper(), cell_style),
                                    Paragraph(desc_text, cell_style)
                                ])

                        if len(risk_data) > 1:
                            # Adjusted widths: Category 1", Severity 0.7", Description 5"
                            risk_table = Table(risk_data, colWidths=[1*inch, 0.7*inch, 5*inch])
                            risk_table.setStyle(TableStyle([
                                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5282')),
                                ('FONTSIZE', (0, 0), (-1, -1), 8),
                                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
                                ('TOPPADDING', (0, 0), (-1, -1), 4),
                                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                                ('LEFTPADDING', (0, 0), (-1, -1), 4),
                                ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                            ]))
                            story.append(risk_table)
                    else:
                        story.append(Paragraph("<i>No individual risks identified.</i>", body_style))

                    # Artist-favorable terms from risk assessment
                    artist_favorable = risk_assessment.get('artist_favorable_terms', [])
                    if artist_favorable:
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph("<b>Artist-Favorable Terms (Label Concerns):</b>", subheading_style))
                        for term in artist_favorable[:6]:
                            if isinstance(term, dict):
                                term_text = term.get('term', 'N/A')
                                label_impact = term.get('label_impact', '')
                                ref = term.get('ref', '')
                                impact_text = f" - {label_impact}" if label_impact else ""
                                ref_text = f" (Ref: {ref})" if ref else ""
                                story.append(Paragraph(f"* {self._clean_text(str(term_text))}{impact_text}{ref_text}", bullet_style))

                    # Negotiation points
                    negotiation = risk_assessment.get('negotiation_points', risk_assessment.get('negotiation_priorities', []))
                    if negotiation:
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph("<b>Recommended Negotiation Points:</b>", subheading_style))
                        for point in negotiation[:8]:
                            if isinstance(point, dict):
                                priority_text = point.get('priority', point.get('point', str(point)))
                                ref = point.get('ref', '')
                                ref_text = f" (Ref: {ref})" if ref else ""
                                story.append(Paragraph(f"* {self._clean_text(str(priority_text))}{ref_text}", bullet_style))
                            else:
                                story.append(Paragraph(f"* {self._clean_text(str(point))}", bullet_style))

                    # Deal breakers
                    deal_breakers = risk_assessment.get('deal_breakers', [])
                    if deal_breakers:
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph("<b>Potential Deal Breakers:</b>", subheading_style))
                        for item in deal_breakers[:5]:
                            if isinstance(item, dict):
                                issue = item.get('issue', 'N/A')
                                ref = item.get('ref', '')
                                ref_text = f" (Ref: {ref})" if ref else ""
                                story.append(Paragraph(f"* {self._clean_text(str(issue))}{ref_text}", bullet_style))
                            else:
                                story.append(Paragraph(f"* {self._clean_text(str(item))}", bullet_style))
            else:
                story.append(Paragraph("<i>Risk assessment data not available.</i>", body_style))

            story.append(PageBreak())

            # Full Analysis Section
            full_analysis = analysis_data.get('full_analysis', {})
            logging.info(f"PDF Generation - full_analysis keys: {list(full_analysis.keys()) if isinstance(full_analysis, dict) else 'NOT DICT'}")

            story.append(Paragraph("DETAILED CONTRACT ANALYSIS", heading_style))

            if isinstance(full_analysis, dict):
                # Check for parse error
                if full_analysis.get('parse_error'):
                    story.append(Paragraph(
                        "<b><font color='red'>Warning: Detailed analysis data extraction encountered issues.</font></b>",
                        body_style
                    ))
                    # Show raw analysis if available
                    raw_analysis = full_analysis.get('raw_analysis', '')
                    if raw_analysis and len(raw_analysis) > 50:
                        story.append(Paragraph("<b>Raw Analysis Output:</b>", subheading_style))
                        # Show first 3000 chars of raw analysis
                        story.append(Paragraph(self._clean_text(raw_analysis[:3000], max_length=3000), body_style))
                else:
                    # Contract Type
                    contract_type = full_analysis.get('contract_type', 'Not identified')
                    logging.info(f"PDF Generation - contract_type: {contract_type}")
                    story.append(Paragraph(f"<b>Contract Type:</b> {contract_type}", body_style))

                    # Get contract text for snippets
                    contract_text = analysis_data.get('_contract_text', '')
                    logging.info(f"PDF Generation - contract_text length: {len(contract_text) if contract_text else 0}")

                    # Parties
                    parties = full_analysis.get('parties', [])
                    logging.info(f"PDF Generation - parties count: {len(parties) if parties else 0}")
                    if parties:
                        story.append(Paragraph("<b>Parties:</b>", subheading_style))
                        for party in parties:
                            if isinstance(party, dict):
                                try:
                                    party_ref = party.get('ref', '')
                                    clickable_ref = self._format_clickable_ref(party_ref, contract_text) if party_ref else ""
                                    story.append(Paragraph(f"* {party.get('name', 'N/A')} - {party.get('role', 'N/A')} {clickable_ref}", bullet_style))
                                except Exception as e:
                                    logging.error(f"Error rendering party: {e}")
                                    story.append(Paragraph(f"* {party.get('name', 'N/A')} - {party.get('role', 'N/A')}", bullet_style))

                    # Term - handle both string and dict formats
                    term = full_analysis.get('term_duration', '')
                    if term:
                        if isinstance(term, dict):
                            term_val = term.get('value', 'N/A')
                            term_ref = term.get('ref', '')
                            clickable_ref = self._format_clickable_ref(term_ref, contract_text) if term_ref else ""
                            story.append(Paragraph(f"<b>Term:</b> {self._clean_text(str(term_val))} {clickable_ref}", body_style))
                        else:
                            story.append(Paragraph(f"<b>Term:</b> {self._clean_text(str(term))}", body_style))

                    # Effective Date
                    effective_date = full_analysis.get('effective_date', {})
                    if effective_date and isinstance(effective_date, dict):
                        date_val = effective_date.get('value', '')
                        if date_val:
                            date_ref = effective_date.get('ref', '')
                            clickable_ref = self._format_clickable_ref(date_ref, contract_text) if date_ref else ""
                            story.append(Paragraph(f"<b>Effective Date:</b> {self._clean_text(str(date_val))} {clickable_ref}", body_style))

                    # Financial Terms
                    financial = full_analysis.get('financial_terms', {})
                    if financial and isinstance(financial, dict):
                        story.append(Paragraph("<b>Financial Terms:</b>", subheading_style))
                        # Use the formatter for complex nested values
                        if financial.get('advances'):
                            formatted_advances = self._format_value_for_pdf(financial.get('advances'))
                            story.append(Paragraph(f"* Advances: {formatted_advances}", bullet_style))
                        if financial.get('royalty_rates'):
                            formatted_royalties = self._format_value_for_pdf(financial.get('royalty_rates'))
                            story.append(Paragraph(f"* Royalty Rates: {formatted_royalties}", bullet_style))
                        if financial.get('payment_schedule'):
                            formatted_schedule = self._format_value_for_pdf(financial.get('payment_schedule'))
                            story.append(Paragraph(f"* Payment Schedule: {formatted_schedule}", bullet_style))
                        if financial.get('label_investment'):
                            formatted_investment = self._format_value_for_pdf(financial.get('label_investment'))
                            story.append(Paragraph(f"* Label Investment: {formatted_investment}", bullet_style))
                        if financial.get('recoupment_terms'):
                            formatted_recoup = self._format_value_for_pdf(financial.get('recoupment_terms'))
                            story.append(Paragraph(f"* Recoupment: {formatted_recoup}", bullet_style))

                    # Rights Secured (AI returns 'rights_secured' not 'rights_granted')
                    rights = full_analysis.get('rights_secured', []) or full_analysis.get('rights_granted', [])
                    if rights:
                        story.append(Paragraph("<b>Rights Secured:</b>", subheading_style))
                        for right in rights[:8]:
                            if isinstance(right, dict):
                                exclusivity = "Exclusive" if right.get('exclusivity') else "Non-exclusive"
                                right_desc = right.get('right', '') or right.get('description', 'N/A')
                                scope = right.get('scope', '')
                                duration = right.get('duration', '')
                                ref = right.get('ref', '')

                                details = [f"{exclusivity}"]
                                if scope:
                                    details.append(f"Territory: {scope}")
                                if duration:
                                    details.append(f"Duration: {duration}")

                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(right_desc))} ({', '.join(details)}) {clickable_ref}",
                                    bullet_style
                                ))

                    # Artist Obligations
                    artist_obligations = full_analysis.get('artist_obligations', [])
                    if artist_obligations:
                        story.append(Paragraph("<b>Artist Obligations:</b>", subheading_style))
                        for obligation in artist_obligations[:6]:
                            if isinstance(obligation, dict):
                                obl_text = obligation.get('obligation', 'N/A')
                                deadline = obligation.get('deadline', '')
                                ref = obligation.get('ref', '')

                                deadline_text = f" (Deadline: {deadline})" if deadline else ""
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(obl_text))}{deadline_text} {clickable_ref}",
                                    bullet_style
                                ))

                    # Label Obligations
                    label_obligations = full_analysis.get('label_obligations', [])
                    if label_obligations:
                        story.append(Paragraph("<b>Label Obligations:</b>", subheading_style))
                        for obligation in label_obligations[:6]:
                            if isinstance(obligation, dict):
                                obl_text = obligation.get('obligation', 'N/A')
                                impact = obligation.get('financial_impact', '')
                                ref = obligation.get('ref', '')

                                impact_text = f" (Cost: {impact})" if impact else ""
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(obl_text))}{impact_text} {clickable_ref}",
                                    bullet_style
                                ))

                    # Label Protections
                    protections = full_analysis.get('label_protections', [])
                    if protections:
                        story.append(Paragraph("<b>Label Protections:</b>", subheading_style))
                        for protection in protections[:6]:
                            if isinstance(protection, dict):
                                clause = protection.get('clause', 'N/A')
                                ref = protection.get('ref', '')
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(f"* {self._clean_text(str(clause))} {clickable_ref}", bullet_style))

                    # Termination Clauses
                    termination = full_analysis.get('termination_clauses', [])
                    if termination:
                        story.append(Paragraph("<b>Termination Provisions:</b>", subheading_style))
                        for term_clause in termination[:6]:
                            if isinstance(term_clause, dict):
                                trigger = term_clause.get('trigger', 'N/A')
                                who = term_clause.get('who_can_trigger', '')
                                impact = term_clause.get('label_impact', '')
                                ref = term_clause.get('ref', '')

                                who_text = f" (By: {who})" if who else ""
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(trigger))}{who_text} {clickable_ref}",
                                    bullet_style
                                ))

                    # Artist-Favorable Terms (risks to label)
                    artist_favorable = full_analysis.get('artist_favorable_terms', [])
                    if artist_favorable:
                        story.append(Paragraph("<b>Artist-Favorable Terms (Label Concerns):</b>", subheading_style))
                        for term in artist_favorable[:5]:
                            if isinstance(term, dict):
                                term_desc = term.get('term', 'N/A')
                                concern = term.get('concern', '')
                                ref = term.get('ref', '')

                                concern_text = f" - {concern}" if concern else ""
                                clickable_ref = self._format_clickable_ref(ref, contract_text) if ref else ""
                                story.append(Paragraph(
                                    f"* {self._clean_text(str(term_desc))}{concern_text} {clickable_ref}",
                                    bullet_style
                                ))

                    # Overall Assessment
                    assessment = full_analysis.get('overall_assessment', '')
                    if assessment:
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph("<b>Overall Assessment:</b>", subheading_style))
                        story.append(Paragraph(self._clean_text(str(assessment)), body_style))
            else:
                story.append(Paragraph("<i>Detailed analysis data not available or could not be parsed.</i>", body_style))

            # SOURCE CONTRACT SECTION - Appended with page anchors for clickable references
            contract_text = analysis_data.get('_contract_text', '')
            if contract_text:
                story.append(PageBreak())
                story.append(Paragraph("SOURCE CONTRACT", heading_style))
                story.append(Paragraph(
                    "<i>The original contract text is included below. Click any page reference in the analysis above to jump directly to that location.</i>",
                    body_style
                ))
                story.append(Spacer(1, 0.2*inch))

                # Style for contract text (smaller, monospace-like)
                contract_style = ParagraphStyle(
                    'ContractText',
                    parent=styles['Normal'],
                    fontSize=9,
                    spaceAfter=6,
                    leading=12,
                    leftIndent=10,
                    rightIndent=10
                )

                # Split contract by page markers and create anchors
                # Look for [PAGE N] markers in the text
                page_pattern = re.compile(r'\[PAGE\s*(\d+)\]', re.IGNORECASE)

                # Split text by page markers, keeping the markers
                parts = page_pattern.split(contract_text)

                if len(parts) > 1:
                    # We have page markers
                    current_page = None
                    for i, part in enumerate(parts):
                        if i % 2 == 1:  # This is a page number
                            current_page = part
                            # Create anchor for this page
                            anchor_name = f"contract_page_{current_page}"
                            story.append(Spacer(1, 0.15*inch))
                            # Page header with anchor
                            story.append(Paragraph(
                                f'<a name="{anchor_name}"/><b>--- PAGE {current_page} ---</b>',
                                subheading_style
                            ))
                        else:
                            # This is content
                            if part.strip():
                                # Clean and split into paragraphs
                                paragraphs = part.strip().split('\n\n')
                                for para in paragraphs:
                                    if para.strip():
                                        clean_para = self._clean_text(para.strip(), max_length=2000)
                                        if clean_para:
                                            story.append(Paragraph(clean_para, contract_style))
                else:
                    # No page markers - create anchors for every ~2000 chars as "pages"
                    chunk_size = 2000
                    chunks = [contract_text[i:i+chunk_size] for i in range(0, len(contract_text), chunk_size)]
                    for page_num, chunk in enumerate(chunks, 1):
                        anchor_name = f"contract_page_{page_num}"
                        story.append(Spacer(1, 0.15*inch))
                        story.append(Paragraph(
                            f'<a name="{anchor_name}"/><b>--- PAGE {page_num} ---</b>',
                            subheading_style
                        ))
                        clean_chunk = self._clean_text(chunk.strip(), max_length=2500)
                        if clean_chunk:
                            story.append(Paragraph(clean_chunk, contract_style))

            # Footer
            story.append(Spacer(1, 0.5*inch))
            story.append(Table([['']], colWidths=[7*inch], rowHeights=[2]))
            story[-1].setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2c5282'))]))
            story.append(Spacer(1, 0.1*inch))

            footer_style = ParagraphStyle(
                'Footer',
                parent=styles['Normal'],
                fontSize=8,
                textColor=colors.grey,
                alignment=TA_CENTER
            )
            story.append(Paragraph(
                f"Generated by ContractAnalysis Agent | {datetime.now().strftime('%B %d, %Y at %I:%M %p')}",
                footer_style
            ))
            story.append(Paragraph(
                "This analysis is for informational purposes only and does not constitute legal advice.",
                footer_style
            ))

            # Build PDF
            doc.build(story)
            pdf_bytes = buffer.getvalue()
            buffer.close()

            logging.info(f"Generated PDF report: {len(pdf_bytes)} bytes")
            return pdf_bytes

        except Exception as e:
            logging.error(f"Error generating PDF report: {e}")
            return None

    def _clean_text(self, text: str, max_length: int = 500) -> str:
        """Clean text for PDF rendering - escape special characters and normalize Unicode."""
        if not text:
            return ""
        text = str(text)

        # Normalize Unicode characters that don't render in standard PDF fonts
        unicode_replacements = {
            '\u2011': '-',   # Non-breaking hyphen → regular hyphen
            '\u2010': '-',   # Hyphen → regular hyphen
            '\u2012': '-',   # Figure dash → regular hyphen
            '\u2013': '-',   # En-dash → regular hyphen
            '\u2014': '-',   # Em-dash → regular hyphen
            '\u2015': '-',   # Horizontal bar → regular hyphen
            '\u2018': "'",   # Left single quote → apostrophe
            '\u2019': "'",   # Right single quote → apostrophe
            '\u201a': "'",   # Single low quote → apostrophe
            '\u201b': "'",   # Single high-reversed quote → apostrophe
            '\u201c': '"',   # Left double quote → regular quote
            '\u201d': '"',   # Right double quote → regular quote
            '\u201e': '"',   # Double low quote → regular quote
            '\u201f': '"',   # Double high-reversed quote → regular quote
            '\u2022': '*',   # Bullet → asterisk
            '\u2023': '>',   # Triangular bullet → greater than
            '\u2024': '.',   # One dot leader → period
            '\u2025': '..',  # Two dot leader → two periods
            '\u2026': '...', # Ellipsis → three periods
            '\u2027': '-',   # Hyphenation point → hyphen
            '\u2032': "'",   # Prime → apostrophe
            '\u2033': '"',   # Double prime → quote
            '\u2039': '<',   # Single left angle quote
            '\u203a': '>',   # Single right angle quote
            '\u00ab': '<<',  # Left double angle quote
            '\u00bb': '>>',  # Right double angle quote
            '\u00a0': ' ',   # Non-breaking space → regular space
            '\u200b': '',    # Zero-width space → remove
            '\u200c': '',    # Zero-width non-joiner → remove
            '\u200d': '',    # Zero-width joiner → remove
            '\ufeff': '',    # BOM → remove
            '\u00b7': '*',   # Middle dot → asterisk
            '\u2212': '-',   # Minus sign → hyphen
            '\u00d7': 'x',   # Multiplication sign → x
            '\u00f7': '/',   # Division sign → slash
            '\u2248': '~',   # Almost equal → tilde
            '\u2260': '!=',  # Not equal → !=
            '\u2264': '<=',  # Less than or equal
            '\u2265': '>=',  # Greater than or equal
            '\u00b0': ' deg', # Degree symbol
            '\u00a9': '(c)', # Copyright
            '\u00ae': '(R)', # Registered
            '\u2122': '(TM)', # Trademark
        }

        for unicode_char, replacement in unicode_replacements.items():
            text = text.replace(unicode_char, replacement)

        # Replace any remaining non-ASCII characters that might cause issues
        # Keep basic extended ASCII (accented letters) but remove other oddities
        cleaned_chars = []
        for char in text:
            if ord(char) < 128:  # Standard ASCII
                cleaned_chars.append(char)
            elif ord(char) < 256:  # Extended ASCII (accented chars) - keep these
                cleaned_chars.append(char)
            else:  # Other Unicode - replace with space or skip
                cleaned_chars.append(' ')
        text = ''.join(cleaned_chars)

        # Clean up multiple spaces
        while '  ' in text:
            text = text.replace('  ', ' ')

        # Replace problematic characters for reportlab XML
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        text = text.replace('\n', ' ')
        text = text.replace('\r', '')

        # Limit length to prevent overflow
        if max_length and len(text) > max_length:
            text = text[:max_length - 3] + "..."
        return text.strip()

    def _format_clickable_ref(self, ref_text: str, contract_text: str = '') -> str:
        """Format a reference string as a clickable internal PDF link with snippet.

        Converts refs like "Page 3, Section 4.1" to clickable links that jump
        to the corresponding page in the appended contract text.
        Includes a short snippet from the referenced page for context.
        """
        if not ref_text or ref_text == 'N/A':
            return ""

        # Extract page number from reference (e.g., "Page 3" or "Pages 3-4")
        page_match = re.search(r'[Pp]age[s]?\s*(\d+)', str(ref_text))
        if page_match:
            page_num = page_match.group(1)
            anchor_name = f"contract_page_{page_num}"
            clean_ref = self._clean_text(str(ref_text), max_length=100)

            # Extract a snippet from the referenced page if contract text is available
            snippet = ""
            if contract_text:
                # Find the page marker and extract text after it
                page_pattern = re.compile(rf'\[PAGE\s*{page_num}\](.*?)(?:\[PAGE\s*\d+\]|$)', re.IGNORECASE | re.DOTALL)
                match = page_pattern.search(contract_text)
                if match:
                    page_content = match.group(1).strip()
                    # Get first 80 chars as snippet, clean it up
                    if page_content:
                        snippet_text = page_content[:120].replace('\n', ' ').strip()
                        # Truncate at word boundary
                        if len(snippet_text) >= 80:
                            last_space = snippet_text[:80].rfind(' ')
                            if last_space > 40:
                                snippet_text = snippet_text[:last_space]
                        snippet = self._clean_text(snippet_text, max_length=80)

            # Build the clickable reference with optional snippet
            if snippet:
                return f'<a href="#{anchor_name}" color="blue"><i>(Ref: {clean_ref})</i></a> <font size="8" color="gray">["{snippet}..."]</font>'
            else:
                return f'<a href="#{anchor_name}" color="blue"><i>(Ref: {clean_ref})</i></a>'
        else:
            # No page number found, just return plain ref
            clean_ref = self._clean_text(str(ref_text), max_length=100)
            return f"<i>(Ref: {clean_ref})</i>"

    def _format_value_for_pdf(self, value: Any, indent: int = 0) -> str:
        """Format a value (potentially nested dict/list) into readable text for PDF."""
        if value is None:
            return "N/A"

        if isinstance(value, str):
            return self._clean_text(value, max_length=None)

        if isinstance(value, (int, float, bool)):
            return str(value)

        if isinstance(value, list):
            if not value:
                return "None"
            # For simple lists, join with commas
            if all(isinstance(item, str) for item in value):
                return ", ".join(str(item) for item in value[:5])  # Limit to 5 items
            # For complex lists, format each item
            parts = []
            for item in value[:5]:
                parts.append(self._format_value_for_pdf(item, indent + 1))
            return "; ".join(parts)

        if isinstance(value, dict):
            # Format dict as readable key-value pairs
            parts = []
            for k, v in value.items():
                # Clean up key name (replace underscores, capitalize)
                key_name = k.replace('_', ' ').title()
                formatted_value = self._format_value_for_pdf(v, indent + 1)
                if formatted_value and formatted_value != "N/A":
                    parts.append(f"{key_name}: {formatted_value}")
            return "; ".join(parts) if parts else "N/A"

        return str(value)

    def _extract_text_from_pdf(self, content: bytes) -> str:
        """Extract text from PDF content using pypdf or PyPDF2.

        Includes clear page markers for document reference tracking.
        """
        if not PDF_SUPPORT or pypdf_module is None:
            return "[ERROR: PDF library not available. Install with: pip install pypdf]"

        try:
            pdf_file = io.BytesIO(content)
            pdf_reader = pypdf_module.PdfReader(pdf_file)

            text_parts = []
            for page_num, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                if page_text:
                    # Clear page markers for AI to reference
                    text_parts.append(f"[PAGE {page_num + 1}]\n{page_text}\n[END PAGE {page_num + 1}]")

            return "\n\n".join(text_parts)
        except Exception as e:
            logging.error(f"PDF extraction error: {e}")
            return f"[ERROR: Failed to extract PDF text: {e}]"

    def _extract_text_from_docx(self, content: bytes) -> str:
        """Extract text from DOCX content."""
        if not DOCX_SUPPORT or DocxDocument is None:
            return "[ERROR: python-docx not available. Install with: pip install python-docx]"

        try:
            doc_file = io.BytesIO(content)
            doc = DocxDocument(doc_file)

            text_parts = []
            for para in doc.paragraphs:
                if para.text.strip():
                    text_parts.append(para.text)

            # Also extract tables
            for table in doc.tables:
                for row in table.rows:
                    row_text = " | ".join(cell.text.strip() for cell in row.cells)
                    if row_text.strip():
                        text_parts.append(row_text)

            return "\n\n".join(text_parts)
        except Exception as e:
            logging.error(f"DOCX extraction error: {e}")
            return f"[ERROR: Failed to extract DOCX text: {e}]"

    def _extract_text(self, file_path: str, content: bytes) -> str:
        """Extract text based on file extension."""
        ext = file_path.lower().split('.')[-1]

        if ext == 'pdf':
            return self._extract_text_from_pdf(content)
        elif ext in ['docx', 'doc']:
            return self._extract_text_from_docx(content)
        elif ext == 'txt':
            return content.decode('utf-8', errors='ignore')
        else:
            return f"[ERROR: Unsupported file format: {ext}. Supported: pdf, docx, txt]"

    def _extract_json_from_response(self, response: str) -> Dict:
        """Extract JSON from AI response, handling various formats."""
        if not response:
            logging.error("_extract_json_from_response: Empty response received")
            return {"parse_error": True, "raw_analysis": response, "error_type": "empty_response"}

        # Clean up common issues in AI responses
        cleaned_response = response.strip()

        # Remove control characters that can break JSON parsing
        cleaned_response = re.sub(r'[\x00-\x1f\x7f-\x9f]', ' ', cleaned_response)

        # Check for truncated JSON (common when hitting token limits)
        # If it starts with { but doesn't end with }, try to repair it
        if cleaned_response.startswith('{') and not cleaned_response.rstrip().endswith('}'):
            logging.warning("_extract_json_from_response: Detected possibly truncated JSON, attempting repair...")
            # Try to find the last complete key-value pair and close the JSON
            repaired = self._repair_truncated_json(cleaned_response)
            if repaired:
                try:
                    result = json.loads(repaired)
                    logging.info(f"_extract_json_from_response: Parsed from repaired truncated JSON, keys: {list(result.keys())}")
                    return result
                except json.JSONDecodeError as e:
                    logging.warning(f"_extract_json_from_response: Repaired JSON still invalid: {e}")

        # Try 1: Look for ```json code block
        json_match = re.search(r'```json\s*(.*?)\s*```', cleaned_response, re.DOTALL)
        if json_match:
            try:
                result = json.loads(json_match.group(1))
                logging.info(f"_extract_json_from_response: Parsed from ```json block, keys: {list(result.keys())}")
                return result
            except json.JSONDecodeError as e:
                logging.warning(f"_extract_json_from_response: Failed to parse ```json block: {e}")

        # Try 2: Look for ``` code block without json tag
        code_match = re.search(r'```\s*(.*?)\s*```', cleaned_response, re.DOTALL)
        if code_match:
            code_content = code_match.group(1).strip()
            if code_content.startswith('{'):
                try:
                    result = json.loads(code_content)
                    logging.info(f"_extract_json_from_response: Parsed from ``` block, keys: {list(result.keys())}")
                    return result
                except json.JSONDecodeError as e:
                    logging.warning(f"_extract_json_from_response: Failed to parse ``` block: {e}")

        # Try 3: Look for first { to last } (the JSON object)
        first_brace = cleaned_response.find('{')
        last_brace = cleaned_response.rfind('}')
        if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
            json_str = cleaned_response[first_brace:last_brace + 1]
            try:
                result = json.loads(json_str)
                logging.info(f"_extract_json_from_response: Parsed from braces, keys: {list(result.keys())}")
                return result
            except json.JSONDecodeError as e:
                # Try to fix common JSON issues
                logging.warning(f"_extract_json_from_response: Initial brace parse failed: {e}")

                # Apply multiple fixes in sequence
                fixed_json = json_str

                # Fix 1: Remove trailing commas before ] or }
                fixed_json = re.sub(r',\s*([}\]])', r'\1', fixed_json)

                # Fix 2: Fix missing commas between } and { or ] and [
                fixed_json = re.sub(r'}\s*{', '},{', fixed_json)
                fixed_json = re.sub(r']\s*\[', '],[', fixed_json)

                # Fix 3: Fix missing commas between } and "
                fixed_json = re.sub(r'}\s*"', '},"', fixed_json)
                fixed_json = re.sub(r']\s*"', '],"', fixed_json)

                # Fix 4: Fix newlines inside strings (convert to spaces)
                # This is tricky - need to only fix inside strings
                # For now, just remove literal newlines that aren't escaped
                fixed_json = re.sub(r'(?<!\\)\n', ' ', fixed_json)

                try:
                    result = json.loads(fixed_json)
                    logging.info(f"_extract_json_from_response: Parsed after JSON fixes, keys: {list(result.keys())}")
                    return result
                except json.JSONDecodeError as e2:
                    logging.warning(f"_extract_json_from_response: JSON fixes didn't help: {e2}")

                # Try to find and fix the specific position of the error
                try:
                    # Sometimes the AI includes extra text after the JSON
                    # Try parsing incrementally to find where valid JSON ends
                    for end_pos in range(last_brace, first_brace, -1):
                        if cleaned_response[end_pos] == '}':
                            try:
                                result = json.loads(cleaned_response[first_brace:end_pos + 1])
                                logging.info(f"_extract_json_from_response: Parsed with truncated end, keys: {list(result.keys())}")
                                return result
                            except json.JSONDecodeError:
                                continue
                except Exception:
                    pass

        # Try 4: Direct parse (if entire response is JSON)
        try:
            result = json.loads(cleaned_response)
            logging.info(f"_extract_json_from_response: Parsed directly, keys: {list(result.keys())}")
            return result
        except json.JSONDecodeError as e:
            logging.warning(f"_extract_json_from_response: Direct parse failed: {e}")

        # Failed to parse - log detailed error info
        logging.error(f"_extract_json_from_response: ALL PARSE ATTEMPTS FAILED")
        logging.error(f"Response length: {len(response)}")
        logging.error(f"Response starts with: {response[:200]}")
        logging.error(f"Response ends with: {response[-200:] if len(response) > 200 else response}")

        return {"parse_error": True, "raw_analysis": response, "error_type": "json_parse_failed"}

    def _repair_truncated_json(self, json_str: str) -> Optional[str]:
        """Attempt to repair truncated JSON by closing unclosed brackets/braces."""
        try:
            # Track the nesting level
            stack = []
            in_string = False
            escape_next = False
            last_complete_pos = 0

            for i, char in enumerate(json_str):
                if escape_next:
                    escape_next = False
                    continue

                if char == '\\' and in_string:
                    escape_next = True
                    continue

                if char == '"' and not escape_next:
                    in_string = not in_string
                    continue

                if in_string:
                    continue

                if char == '{':
                    stack.append('}')
                elif char == '[':
                    stack.append(']')
                elif char in '}]':
                    if stack and stack[-1] == char:
                        stack.pop()
                        last_complete_pos = i + 1

                # Track positions after complete key-value pairs
                if char == ',' and not in_string:
                    last_complete_pos = i + 1

            # If we're still in a string, try to close it
            if in_string:
                json_str = json_str + '"'

            # Find the last complete structure and close everything
            # Try to truncate at the last comma and close
            if stack:
                # Find last comma outside of string
                truncate_pos = json_str.rfind(',')
                if truncate_pos > 0:
                    # Truncate at last comma and close all open brackets
                    repaired = json_str[:truncate_pos]
                    repaired += ''.join(reversed(stack))
                    return repaired
                else:
                    # Just close all open brackets
                    return json_str + ''.join(reversed(stack))

            return json_str

        except Exception as e:
            logging.warning(f"_repair_truncated_json failed: {e}")
            return None

    def _call_openai(self, system_prompt: str, user_prompt: str, max_tokens: int = 4000) -> str:
        """Call Azure OpenAI with the given prompts. Handles model-specific parameter differences."""
        if not self.openai_client:
            return "[ERROR: OpenAI client not initialized]"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        # Try different parameter combinations for model compatibility
        # gpt-5.x models may not support temperature or max_tokens
        param_combinations = [
            # Try minimal params first (most compatible with newer models)
            {"model": self.deployment_name, "messages": messages, "max_completion_tokens": max_tokens},
            # Try with max_tokens instead
            {"model": self.deployment_name, "messages": messages, "max_tokens": max_tokens},
            # Try with temperature for older models
            {"model": self.deployment_name, "messages": messages, "max_tokens": max_tokens, "temperature": 0.3},
        ]

        last_error = None
        for params in param_combinations:
            try:
                response = self.openai_client.chat.completions.create(**params)
                return response.choices[0].message.content
            except Exception as e:
                error_msg = str(e).lower()
                # If it's a parameter compatibility error, try next combination
                if "unsupported" in error_msg or "not supported" in error_msg:
                    logging.info(f"Parameter compatibility issue, trying next combination: {e}")
                    last_error = e
                    continue
                # For other errors, fail immediately
                logging.error(f"OpenAI call failed: {e}")
                return f"[ERROR: OpenAI analysis failed: {e}]"

        # All combinations failed
        logging.error(f"All parameter combinations failed. Last error: {last_error}")
        return f"[ERROR: OpenAI analysis failed after trying multiple parameter combinations: {last_error}]"

    def _chunk_text(self, text: str, max_chars: int = 30000) -> List[str]:
        """Split text into chunks for processing large documents."""
        if len(text) <= max_chars:
            return [text]

        chunks = []
        current_chunk = ""

        # Split by paragraphs to maintain context
        paragraphs = text.split('\n\n')

        for para in paragraphs:
            if len(current_chunk) + len(para) < max_chars:
                current_chunk += para + "\n\n"
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = para + "\n\n"

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    def _analyze_full_contract(self, text: str, file_name: str) -> Dict:
        """Perform comprehensive contract analysis from LABEL perspective."""
        system_prompt = """You are an expert contract analyst working for a MAJOR RECORD LABEL (Label perspective).
Your job is to analyze contracts and assess them from the LABEL'S business interests.

This is a BUSINESS ANALYSIS tool for internal use. You are analyzing an ACTUAL contract document.
The document text includes [PAGE N] markers showing where each page begins - use these for references.

Analyze the provided contract and extract structured information.
IMPORTANT: All assessments should be from the LABEL's perspective - what benefits the label, what risks the label faces.

REFERENCE FORMAT: Use the [PAGE N] markers in the text to identify page numbers.
- If you see content after "[PAGE 3]", reference it as "Page 3"
- If the document has visible section/article numbers, include them: "Page 3, Section 4.1"
- If no section numbers are visible, just use the page: "Page 3"
- References help readers locate content but don't need to be formal citations

Return your analysis as a valid JSON object with the following structure:
{
    "contract_type": "type of contract (e.g., Recording Agreement, Licensing Deal, Service Agreement)",
    "parties": [{"name": "party name", "role": "role in contract (Label/Artist/Licensor/etc)", "ref": "Page X"}],
    "effective_date": {"value": "date or null if not found", "ref": "Page X"},
    "term_duration": {"value": "duration description", "ref": "Page X, Section Y"},
    "financial_terms": {
        "advances": {"value": "amount or null", "ref": "Page X, Section Y"},
        "royalty_rates": {"value": "rates description", "ref": "Page X, Section Y"},
        "payment_schedule": {"value": "description or null", "ref": "Page X"},
        "label_investment": {"value": "total label financial commitment", "ref": "Page X"},
        "recoupment_terms": {"value": "how label recoups investment", "ref": "Page X, Section Y"},
        "other_payments": [{"description": "...", "ref": "Page X"}]
    },
    "rights_secured": [{"right": "description", "scope": "scope/territory", "exclusivity": true/false, "duration": "how long label holds rights", "ref": "Page X, Section Y"}],
    "label_protections": [{"clause": "protection description", "ref": "Page X, Section Y"}],
    "artist_obligations": [{"obligation": "what artist must do", "deadline": "when", "consequence_if_breached": "label remedy", "ref": "Page X, Section Y"}],
    "label_obligations": [{"obligation": "what label must do", "financial_impact": "cost to label", "ref": "Page X, Section Y"}],
    "termination_clauses": [{"trigger": "what triggers termination", "who_can_trigger": "label/artist/either", "label_impact": "effect on label", "ref": "Page X, Section Y"}],
    "key_dates": [{"event": "description", "date": "date or relative timing", "ref": "Page X"}],
    "artist_favorable_terms": [{"term": "term that favors artist MORE than industry standard", "concern": "why this is a concern for label", "ref": "Page X, Section Y"}],
    "missing_label_protections": ["standard label protections that appear to be missing"],
    "overall_assessment": "2-3 sentence assessment from LABEL's perspective - is this deal favorable to the label?"
}

Be thorough but concise. Extract actual values from the contract text.
Remember: You work for the LABEL. Artist-favorable terms are potential concerns.
ALWAYS include page/section references for every finding.

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
1. Output ONLY the JSON object - no other text before or after
2. Do NOT ask any questions - just analyze and output JSON immediately
3. Do NOT ask for confirmation or clarification - proceed with analysis
4. Do NOT mention length limits or offer to split output - just output the JSON
5. Start your response with { and end with } - nothing else
6. If information is missing, use null or "Not specified" - do not ask about it

Your response must be valid JSON starting with { and ending with }."""

        # Handle large documents by chunking
        chunks = self._chunk_text(text)

        if len(chunks) == 1:
            user_prompt = f"Analyze this contract:\n\n{text}"
            # Use larger max_tokens for full contract analysis to accommodate detailed JSON
            response = self._call_openai(system_prompt, user_prompt, max_tokens=16000)
        else:
            # For large documents, analyze chunks and synthesize
            chunk_analyses = []
            for i, chunk in enumerate(chunks):
                user_prompt = f"Analyze this section (Part {i+1} of {len(chunks)}) of a contract:\n\n{chunk}"
                chunk_response = self._call_openai(system_prompt, user_prompt, max_tokens=2000)
                chunk_analyses.append(chunk_response)

            # Synthesize the chunks
            synthesis_prompt = """You are synthesizing multiple partial analyses of a single contract.
Combine these analyses into one comprehensive JSON structure, removing duplicates and resolving any conflicts.

CRITICAL: Output ONLY valid JSON. Start with { and end with }. No other text.
Do NOT ask questions. Do NOT offer options. Just output the combined JSON immediately."""

            user_prompt = f"Combine these partial contract analyses:\n\n" + "\n\n---\n\n".join(chunk_analyses)
            response = self._call_openai(synthesis_prompt, user_prompt)

        # Parse the JSON response with retry logic for empty results
        essential_keys = ['contract_type', 'parties', 'rights_secured', 'financial_terms']
        max_retries = 3

        for attempt in range(max_retries):
            analysis = self._extract_json_from_response(response)

            # Check if analysis has essential keys (not just empty or error)
            has_essential_data = any(
                key in analysis and analysis[key]
                for key in essential_keys
            )

            if has_essential_data or analysis.get('parse_error'):
                # Either we got good data or a clear error - don't retry
                break

            if attempt < max_retries - 1:
                logging.warning(f"Full analysis returned empty (attempt {attempt + 1}/{max_retries}). Retrying...")
                # Retry with more forceful prompt
                retry_prompt = f"""IMPORTANT: Your previous response was empty or incomplete.
You MUST output a complete JSON object with contract analysis.

Analyze this contract NOW and output ONLY the JSON (start with {{ end with }}):

{text[:40000]}"""
                response = self._call_openai(system_prompt, retry_prompt, max_tokens=16000)

        # DEBUG: Enhanced logging for analysis result
        logging.info("=" * 40)
        logging.info("_analyze_full_contract - RESULT ANALYSIS")
        logging.info(f"Full analysis completed with keys: {list(analysis.keys())}")
        logging.info(f"Raw response length: {len(response) if response else 0}")
        logging.info(f"Raw response preview: {response[:500] if response else 'None'}")

        if analysis.get('parse_error'):
            logging.error(f"_analyze_full_contract - JSON PARSE FAILED!")
            logging.error(f"Raw analysis: {analysis.get('raw_analysis', '')[:1000]}")

        # Log specific key values
        logging.info(f"  - contract_type: {analysis.get('contract_type', 'MISSING')}")
        logging.info(f"  - parties: {len(analysis.get('parties', []))} found")
        logging.info(f"  - financial_terms: {type(analysis.get('financial_terms')).__name__}")
        logging.info(f"  - rights_secured: {len(analysis.get('rights_secured', []))} found")

        if not any(key in analysis for key in essential_keys):
            logging.warning(f"Analysis may be incomplete - no essential keys found!")
        logging.info("=" * 40)

        analysis["_metadata"] = {
            "file_name": file_name,
            "analyzed_at": datetime.now().isoformat(),
            "text_length": len(text),
            "chunks_processed": len(chunks),
            "retry_attempts": attempt + 1
        }
        return analysis

    def _extract_specific_clauses(self, text: str, clause_types: List[str]) -> Dict:
        """Extract specific types of clauses from the contract."""
        clause_descriptions = {
            "financial": "All financial terms including advances, royalties, payments, fees, revenue sharing, expenses",
            "rights": "All rights granted or reserved including intellectual property, licensing, usage rights, exclusivity",
            "obligations": "All obligations and duties of each party, deliverables, performance requirements",
            "termination": "Termination conditions, notice periods, breach definitions, consequences of termination",
            "exclusivity": "Exclusivity clauses, non-compete provisions, first refusal rights",
            "territory": "Geographic scope, territory definitions, regional limitations",
            "duration": "Term length, renewal options, extension conditions, effective dates"
        }

        types_to_extract = [ct for ct in clause_types if ct in clause_descriptions]
        if not types_to_extract:
            types_to_extract = list(clause_descriptions.keys())

        extraction_details = "\n".join([f"- {ct}: {clause_descriptions[ct]}" for ct in types_to_extract])

        system_prompt = f"""You are a contract clause extraction specialist.
Extract the following types of clauses from the contract:

{extraction_details}

CRITICAL: For EVERY clause extracted, you MUST include a document reference:
- "ref": "Page X, Section Y" or "ref": "Page X, Article Y"
The document text includes [PAGE N] markers - use these for exact page numbers.

Return a JSON object where each key is a clause type and the value is an array of extracted clauses.
Each clause should have: "text" (the clause text or summary - keep under 200 words), "ref" (Page X, Section Y), "key_points" (2-3 bullet points).

Example format:
{{
    "financial": [
        {{"text": "...", "ref": "Page 3, Section 4.1", "key_points": ["Advance of $X", "Royalty rate of Y%"]}}
    ]
}}

ALWAYS include page and section references for every extracted clause.

CRITICAL INSTRUCTIONS - YOU MUST FOLLOW THESE:
1. Output ONLY the JSON object - no other text before or after
2. Do NOT ask any questions - just extract and output JSON immediately
3. Do NOT ask for confirmation or clarification - proceed with extraction
4. Do NOT mention length limits or offer to split output - output the JSON directly
5. Start your response with {{ and end with }} - nothing else
6. If a clause type has no matches, use an empty array: "type": []
7. Keep each clause summary under 200 words - summarize if needed
8. Extract UP TO 3-5 most important clauses per category (prioritize key terms)

Your response must be valid JSON starting with {{ and ending with }}."""

        # For large documents, process only the most relevant text
        text_to_process = text[:35000]  # Reduced limit for better processing

        user_prompt = f"Extract clauses from this contract. Output ONLY valid JSON:\n\n{text_to_process}"
        response = self._call_openai(system_prompt, user_prompt, max_tokens=6000)

        # Add logging for debugging
        logging.info(f"_extract_specific_clauses - Response length: {len(response) if response else 0}")

        result = self._extract_json_from_response(response)

        # If parse failed, try with retry
        if result.get('parse_error'):
            logging.warning("_extract_specific_clauses - Initial parse failed, retrying...")
            retry_prompt = f"""IMPORTANT: Output ONLY valid JSON. No other text. Start with {{ end with }}.

Extract clauses from this contract into JSON format:
{text_to_process[:25000]}"""
            response = self._call_openai(system_prompt, retry_prompt, max_tokens=6000)
            result = self._extract_json_from_response(response)

        return result

    def _generate_summary(self, text: str, summary_type: str, audience: str) -> Dict:
        """Generate a summary tailored to the audience - FROM LABEL PERSPECTIVE."""
        audience_instructions = {
            "legal": "Use precise legal terminology. Include specific clause references. Highlight legal risks to the LABEL and compliance considerations.",
            "business": "Focus on commercial terms and business implications FOR THE LABEL. Emphasize label ROI, recoupment timeline, and operational impacts to the label.",
            "executive": "Provide a high-level overview for LABEL C-suite. Focus on label investment, rights secured, strategic value, and key risks to the label. Keep it concise."
        }

        length_instructions = {
            "executive": "Provide a brief 150-200 word summary with key bullet points.",
            "detailed": "Provide a comprehensive 400-500 word summary covering all major aspects.",
            "legal": "Provide a thorough legal summary of 300-400 words with specific clause references."
        }

        system_prompt = f"""You are a contract summarization expert working for a MAJOR RECORD LABEL.
Your summaries are FOR LABEL EXECUTIVES and should reflect the LABEL's interests and perspective.

{audience_instructions.get(audience, audience_instructions['business'])}
{length_instructions.get(summary_type, length_instructions['detailed'])}

IMPORTANT: Frame everything from the label's business perspective:
- "Label investment" instead of "artist advance"
- "Rights secured by label" instead of "rights granted"
- "Artist-favorable terms" = potential concerns for the label
- Risk assessment = risks TO THE LABEL

CRITICAL: Include document references (Page X, Section Y) for key claims.
The document text includes [PAGE N] markers - use these for exact page numbers.

CRITICAL: The recommendation MUST align with the risk level:
- LOW risk: "Proceed" or "Proceed as drafted"
- MEDIUM risk: "Proceed with caution; consider negotiating [specific terms]"
- HIGH risk: "Do not proceed without changes to [specific critical terms]" or "Renegotiate [specific issues] before proceeding"

Return a JSON object with:
{{
    "summary": "the main summary text FROM LABEL PERSPECTIVE",
    "key_points": [{{"point": "bullet point text", "ref": "Page X, Section Y"}}],
    "label_investment_total": {{"value": "total financial commitment from label", "ref": "Page X"}},
    "rights_secured": {{"value": "summary of rights label obtains", "ref": "Page X, Section Y"}},
    "critical_dates": [{{"event": "...", "date": "...", "ref": "Page X"}}],
    "action_items": ["any actions needed by label team"],
    "risk_level": "low/medium/high (risk TO THE LABEL)",
    "artist_leverage_concerns": [{{"concern": "term giving artist unusual leverage", "ref": "Page X, Section Y"}}],
    "recommendation": "recommendation aligned with risk level - if HIGH risk, must specify required changes before proceeding"
}}

ALWAYS include page/section references for key findings.

IMPORTANT: Do NOT ask clarifying questions. Do NOT ask for confirmation. Just execute the summary and return the JSON."""

        user_prompt = f"Summarize this contract for a {audience} audience:\n\n{text[:40000]}"
        response = self._call_openai(system_prompt, user_prompt)
        return self._extract_json_from_response(response)

    def _identify_risks(self, text: str) -> Dict:
        """Identify risks TO THE LABEL and deviations from standard terms."""
        system_prompt = """You are a contract risk analyst working for a MAJOR RECORD LABEL.
Your job is to identify risks TO THE LABEL, not to the artist.

IMPORTANT PERSPECTIVE:
- Artist-favorable terms = RISKS to the label (higher costs, less control, early reversion)
- High advances/royalties = FINANCIAL RISK to label
- Strong artist termination rights = OPERATIONAL RISK to label
- Early master reversion = ASSET RISK to label
- Creative control for artist = COMMERCIAL RISK to label
- Non-recoupable payments = DIRECT COST to label

CRITICAL: For EVERY risk identified, you MUST include a document reference:
- "ref": "Page X, Section Y" or "ref": "Page X, Article Y"
The document text includes [PAGE N] markers - use these for exact page numbers.

Analyze the contract for RISKS TO THE LABEL:
1. Financial exposure (high advances, guaranteed payments, non-recoupable costs)
2. Asset risks (early master reversion, limited rights duration, territory restrictions)
3. Operational risks (artist approval requirements, key man clauses, delivery delays)
4. Revenue risks (high royalty rates, favorable streaming splits, limited 360 participation)
5. Legal/compliance risks (regulatory, indemnification gaps)
6. Competitive risks (artist leverage, termination options)

Return a JSON object:
{
    "overall_risk_level": "low/medium/high (RISK TO LABEL)",
    "risk_score": 1-100 (higher = worse for label),
    "label_financial_exposure": "total potential label investment/loss",
    "risks": [
        {
            "category": "financial/asset/operational/revenue/legal/competitive",
            "severity": "low/medium/high/critical",
            "description": "what the risk TO THE LABEL is",
            "ref": "Page X, Section Y",
            "label_impact": "specific impact on label operations/finances",
            "recommendation": "how label should address this in negotiation"
        }
    ],
    "artist_favorable_terms": [
        {"term": "what favors the artist", "industry_standard": "what's typical", "label_impact": "why this hurts the label", "ref": "Page X, Section Y"}
    ],
    "missing_label_protections": ["standard label protections not found in this contract"],
    "negotiation_priorities": [{"priority": "item label should push back on", "ref": "Page X, Section Y"}],
    "deal_breakers": [{"issue": "term that may be unacceptable", "ref": "Page X, Section Y"}],
    "summary": "2-3 sentence risk summary FROM LABEL'S PERSPECTIVE"
}

ALWAYS cite the specific page and section for every risk and concern.

IMPORTANT: Do NOT ask clarifying questions. Do NOT ask for confirmation. Just execute the analysis and return the JSON."""

        user_prompt = f"Analyze risks in this contract:\n\n{text[:50000]}"
        response = self._call_openai(system_prompt, user_prompt)

        # DEBUG: Log the raw response before parsing
        logging.info(f"_identify_risks - Raw response length: {len(response) if response else 0}")
        logging.info(f"_identify_risks - Raw response preview: {response[:1000] if response else 'EMPTY'}")

        result = self._extract_json_from_response(response)

        # DEBUG: Log the parsed result
        logging.info(f"_identify_risks - Parsed result keys: {list(result.keys()) if isinstance(result, dict) else 'NOT DICT'}")
        if isinstance(result, dict) and result.get('parse_error'):
            logging.error(f"_identify_risks - JSON PARSE FAILED!")

        return result

    def _compare_contracts(self, text_a: str, text_b: str, name_a: str, name_b: str) -> Dict:
        """Compare two contracts using sectioned analysis for better coverage."""

        # For any substantial contracts, use sectioned comparison to avoid truncation
        # Sectioned mode analyzes each area (financial, rights, etc.) separately
        # This provides better coverage and avoids the model refusing due to incomplete text
        total_length = len(text_a) + len(text_b)
        max_single_contract = max(len(text_a), len(text_b))

        # Use sectioned mode if total > 30k OR if either contract alone is > 20k
        # This ensures we don't truncate important contract content
        use_sectioned = total_length > 30000 or max_single_contract > 20000

        if use_sectioned:
            return self._compare_contracts_sectioned(text_a, text_b, name_a, name_b)

        system_prompt = """You are a contract analysis assistant performing an EDUCATIONAL comparison of two recording agreements.
This is a BUSINESS ANALYSIS exercise for training purposes, NOT legal advice.

Your task: Compare these two contracts and identify factual differences in their terms.
Analyze which contract has more favorable terms from a BUSINESS perspective (lower financial commitments, stronger protections, better rights retention).

When comparing terms, note which contract (A or B) has:
- Lower advance/payment obligations
- Longer rights retention periods
- Broader territorial coverage
- More comprehensive protections
- Clearer deliverable requirements

CRITICAL: Include document references for BOTH contracts in the format:
- "ref_a": "Page X, Section Y" (for Contract A)
- "ref_b": "Page X, Section Y" (for Contract B)
The document text includes [PAGE N] markers - use these for exact page numbers.

Compare these two contracts and identify:
1. Key differences in financial terms, rights, obligations
2. Which contract has more protective clauses (from a business standpoint)
3. Which contract has higher financial exposure
4. Notable terms that differ significantly between the two

Return a JSON object:
{
    "similarity_score": 0-100,
    "contract_types_match": true/false,
    "more_label_favorable": "a/b/neutral (which contract has more protective business terms)",
    "key_differences": [
        {
            "aspect": "what's being compared",
            "contract_a": "terms in first contract",
            "contract_b": "terms in second contract",
            "ref_a": "Page X, Section Y",
            "ref_b": "Page X, Section Y",
            "label_preference": "a/b (which has stronger business protections)",
            "label_impact": "business significance of this difference"
        }
    ],
    "unique_to_a": [{"clause": "clause description", "ref": "Page X, Section Y"}],
    "unique_to_b": [{"clause": "clause description", "ref": "Page X, Section Y"}],
    "financial_comparison": {
        "contract_a": {"label_investment": "total financial commitment", "royalty_exposure": "royalty rates", "ref": "Page X"},
        "contract_b": {"label_investment": "total financial commitment", "royalty_exposure": "royalty rates", "ref": "Page X"},
        "lower_label_cost": "a/b",
        "better_label_margin": "a/b"
    },
    "rights_comparison": {
        "contract_a": {"rights_duration": "...", "territory": "...", "reversion": "...", "ref": "Page X, Section Y"},
        "contract_b": {"rights_duration": "...", "territory": "...", "reversion": "...", "ref": "Page X, Section Y"},
        "stronger_label_rights": "a/b"
    },
    "risk_comparison": {
        "contract_a_risk_level": "low/medium/high (financial/operational risk level)",
        "contract_b_risk_level": "low/medium/high (financial/operational risk level)",
        "lower_label_risk": "a/b"
    },
    "overall_assessment": "factual summary of which contract has more favorable business terms and key differences",
    "recommended_standard_terms": ["notable terms from either contract worth considering"]
}

ALWAYS include page/section references from both contracts for every comparison point.

IMPORTANT: This is an educational analysis. Provide factual comparisons. Do NOT ask clarifying questions. Just execute the comparison and return the JSON."""

        user_prompt = f"""Compare these two contracts:

=== CONTRACT A: {name_a} ===
{text_a[:30000]}

=== CONTRACT B: {name_b} ===
{text_b[:30000]}"""

        response = self._call_openai(system_prompt, user_prompt, max_tokens=6000)
        result = self._extract_json_from_response(response)
        result["_metadata"] = {
            "contract_a": name_a,
            "contract_b": name_b,
            "compared_at": datetime.now().isoformat(),
            "comparison_mode": "standard"
        }
        return result

    def _compare_contracts_sectioned(self, text_a: str, text_b: str, name_a: str, name_b: str) -> Dict:
        """Compare large contracts by analyzing sections separately then synthesizing."""
        logging.info(f"Using sectioned comparison for large contracts: {name_a} vs {name_b}")

        # Define comparison sections
        sections = {
            "financial": {
                "focus": "advances, royalties, recoupment, payment schedules, 360 terms, merchandise, touring splits",
                "analysis_criteria": "Compare total financial commitments, royalty rates, recoupment structures"
            },
            "rights": {
                "focus": "master ownership, duration of rights, territory, exclusivity, reversion triggers, publishing",
                "analysis_criteria": "Compare scope and duration of rights granted, territorial coverage, reversion terms"
            },
            "obligations": {
                "focus": "delivery requirements, album commitments, promotional obligations, key man clauses",
                "analysis_criteria": "Compare deliverable requirements, commitment levels, operational obligations"
            },
            "termination_risk": {
                "focus": "termination triggers, exit clauses, breach remedies, force majeure, key man provisions",
                "analysis_criteria": "Compare termination conditions, exit mechanisms, breach remedies"
            }
        }

        section_results = {}

        for section_name, section_info in sections.items():
            section_prompt = f"""You are a contract analysis assistant performing an EDUCATIONAL comparison of two recording agreements.
Focus ONLY on {section_name.upper()} terms in these two contracts.

FOCUS AREAS: {section_info['focus']}
ANALYSIS CRITERIA: {section_info['analysis_criteria']}

Extract and compare {section_name} terms from both contracts factually.

Return a JSON object with this EXACT structure:
{{
    "section": "{section_name}",
    "contract_a_terms": {{
        "summary": "brief summary of {section_name} terms in Contract A",
        "key_values": ["specific values/terms found"],
        "refs": ["Page X, Section Y"]
    }},
    "contract_b_terms": {{
        "summary": "brief summary of {section_name} terms in Contract B",
        "key_values": ["specific values/terms found"],
        "refs": ["Page X, Section Y"]
    }},
    "differences": [
        {{
            "aspect": "specific term being compared",
            "contract_a": "value/term in A",
            "contract_b": "value/term in B",
            "label_preference": "a/b/neutral (which has more favorable business terms)",
            "reason": "factual explanation of the difference"
        }}
    ],
    "section_winner": "a/b/neutral (which contract has more favorable terms in this section)",
    "section_assessment": "1-2 sentence factual assessment of key differences"
}}

IMPORTANT: This is educational analysis. Do NOT ask questions. Just analyze and return the JSON."""

            user_prompt = f"""Compare {section_name.upper()} terms:

=== CONTRACT A: {name_a} ===
{text_a[:50000]}

=== CONTRACT B: {name_b} ===
{text_b[:50000]}"""

            response = self._call_openai(section_prompt, user_prompt, max_tokens=3000)
            section_results[section_name] = self._extract_json_from_response(response)

        # Synthesize all section results into final comparison
        synthesis_prompt = """You are an educational contract analysis assistant synthesizing sectioned comparison results.

Based on the section-by-section analysis provided, create a comprehensive factual comparison summary.

Return a JSON object:
{
    "similarity_score": 0-100,
    "contract_types_match": true/false,
    "more_label_favorable": "a/b/neutral (which has more favorable business terms overall)",
    "section_winners": {
        "financial": "a/b/neutral",
        "rights": "a/b/neutral",
        "obligations": "a/b/neutral",
        "termination_risk": "a/b/neutral"
    },
    "key_differences": [
        {
            "aspect": "term being compared",
            "contract_a": "value in A",
            "contract_b": "value in B",
            "label_preference": "a/b (which has more favorable terms)",
            "label_impact": "business significance of this difference"
        }
    ],
    "financial_comparison": {
        "contract_a": {"label_investment": "total commitment amount", "royalty_exposure": "royalty rates"},
        "contract_b": {"label_investment": "total commitment amount", "royalty_exposure": "royalty rates"},
        "lower_label_cost": "a/b",
        "better_label_margin": "a/b"
    },
    "rights_comparison": {
        "contract_a": {"rights_duration": "...", "territory": "...", "reversion": "..."},
        "contract_b": {"rights_duration": "...", "territory": "...", "reversion": "..."},
        "stronger_label_rights": "a/b"
    },
    "risk_comparison": {
        "contract_a_risk_level": "low/medium/high",
        "contract_b_risk_level": "low/medium/high",
        "lower_label_risk": "a/b"
    },
    "deal_breakers": [{"contract": "a/b", "issue": "notable concern"}],
    "overall_assessment": "2-3 sentence factual summary of key differences between the contracts",
    "recommended_standard_terms": ["notable terms from either contract"]
}

IMPORTANT: This is educational analysis. Provide factual comparisons only."""

        synthesis_user = f"""Synthesize these section comparisons:

{json.dumps(section_results, indent=2, default=str)}

Contract A: {name_a}
Contract B: {name_b}"""

        synthesis_response = self._call_openai(synthesis_prompt, synthesis_user, max_tokens=4000)
        result = self._extract_json_from_response(synthesis_response)

        # Add section details and metadata
        result["_section_details"] = section_results
        result["_metadata"] = {
            "contract_a": name_a,
            "contract_b": name_b,
            "compared_at": datetime.now().isoformat(),
            "comparison_mode": "sectioned",
            "sections_analyzed": list(sections.keys())
        }

        return result

    def perform(self, **kwargs) -> str:
        """Execute contract analysis action."""
        try:
            action = kwargs.get('action', 'list_contracts')
            contract_name = kwargs.get('contract_name')
            contract_name_b = kwargs.get('contract_name_b')
            clause_types = kwargs.get('clause_types', [])
            summary_type = kwargs.get('summary_type', 'detailed')
            audience = kwargs.get('audience', 'business')

            # List contracts
            if action == 'list_contracts':
                files = self._list_files_in_folder()
                return json.dumps({
                    "status": "success",
                    "action": "list_contracts",
                    "contracts_folder": self.contracts_folder,
                    "files": files,
                    "count": len(files),
                    "supported_formats": ["pdf", "docx", "txt"],
                    "usage": "Use contract_name parameter with the file name to analyze"
                }, indent=2)

            # All other actions require a contract name
            if not contract_name:
                return json.dumps({
                    "status": "error",
                    "message": "contract_name is required for this action",
                    "available_contracts": self._list_files_in_folder()
                }, indent=2)

            # Read the contract
            file_path = f"{self.contracts_folder}/{contract_name}"
            content = self._read_file_content(file_path)

            if not content:
                return json.dumps({
                    "status": "error",
                    "message": f"Could not read contract: {contract_name}",
                    "path_tried": file_path,
                    "available_contracts": self._list_files_in_folder()
                }, indent=2)

            # Extract text
            text = self._extract_text(file_path, content)
            if text.startswith("[ERROR"):
                return json.dumps({
                    "status": "error",
                    "message": text
                }, indent=2)

            # Execute the requested action
            if action == 'full_workup':
                # Comprehensive analysis: runs everything in one go
                logging.info(f"Running full workup on {contract_name}")

                # 1. Full contract analysis
                analysis = self._analyze_full_contract(text, contract_name)

                # 2. Risk identification (run first - this is the authoritative risk source)
                risks = self._identify_risks(text)

                # 3. Executive summary for business audience
                summary = self._generate_summary(text, 'executive', 'business')

                # 4. Extract key clauses (all types)
                all_clause_types = ['financial', 'rights', 'obligations', 'termination', 'exclusivity', 'territory', 'duration']
                clauses = self._extract_specific_clauses(text, all_clause_types)

                # Synchronize risk levels - use risk assessment as authoritative source
                # This ensures consistency throughout the PDF report
                authoritative_risk_level = risks.get('overall_risk_level', 'unknown')
                authoritative_risk_score = risks.get('risk_score', 'N/A')
                if isinstance(summary, dict):
                    summary['risk_level'] = authoritative_risk_level
                    summary['risk_score'] = authoritative_risk_score

                # Compile full report (include contract text for PDF with clickable references)
                full_report = {
                    "contract": contract_name,
                    "analyzed_at": datetime.now().isoformat(),
                    "executive_summary": summary,
                    "full_analysis": analysis,
                    "risk_assessment": risks,
                    "extracted_clauses": clauses,
                    "text_length": len(text),
                    "_contract_text": text  # Include for PDF generation with clickable refs
                }

                # Save the analysis report to Azure storage
                save_result = self._save_analysis_report(contract_name, full_report)

                # Build concise chat response (fits on one screen)
                risk_level = risks.get('overall_risk_level', 'Unknown').upper()
                risk_score = risks.get('risk_score', 'N/A')
                risk_summary = risks.get('summary', '')

                # Get top 3 risks with references
                top_risks = []
                for r in risks.get('risks', [])[:3]:
                    if isinstance(r, dict):
                        ref = r.get('ref', 'N/A')
                        desc = r.get('description', '')[:80]
                        severity = r.get('severity', '').upper()
                        top_risks.append(f"- [{severity}] {desc} (Ref: {ref})")

                # Get key financial terms with references
                fin_terms = analysis.get('financial_terms', {})
                advances = fin_terms.get('advances', {})
                adv_val = advances.get('value', 'N/A') if isinstance(advances, dict) else advances
                adv_ref = advances.get('ref', '') if isinstance(advances, dict) else ''

                royalties = fin_terms.get('royalty_rates', {})
                roy_val = royalties.get('value', 'N/A') if isinstance(royalties, dict) else royalties
                roy_ref = royalties.get('ref', '') if isinstance(royalties, dict) else ''

                # Build the chat summary (short, fits one screen)
                chat_summary = {
                    "headline": f"Analysis Complete: {contract_name}",
                    "risk_level": risk_level,
                    "risk_score": f"{risk_score}/100",
                    "key_findings": [
                        f"Advance: {adv_val}" + (f" (Ref: {adv_ref})" if adv_ref else ""),
                        f"Royalty: {roy_val}" + (f" (Ref: {roy_ref})" if roy_ref else ""),
                    ],
                    "top_risks": top_risks,
                    "recommendation": summary.get('recommendation', '') if isinstance(summary, dict) else '',
                    "full_report": {
                        "message": "Full analysis with all details saved to PDF report:",
                        "download_url": save_result.get('download_url', 'Report generation failed'),
                        "report_name": save_result.get('report_name', ''),
                        "size_kb": save_result.get('size_kb', 0)
                    }
                }

                return json.dumps({
                    "status": "success",
                    "action": "full_workup",
                    "contract": contract_name,
                    "chat_response": chat_summary,
                    "_full_data": {
                        "executive_summary": summary,
                        "full_analysis": analysis,
                        "risk_assessment": risks,
                        "extracted_clauses": clauses,
                        "report_saved": save_result
                    },
                    "_metadata": {
                        "analyzed_at": datetime.now().isoformat(),
                        "file_name": contract_name,
                        "text_length": len(text)
                    }
                }, indent=2)

            elif action == 'analyze_contract':
                result = self._analyze_full_contract(text, contract_name)
                return json.dumps({
                    "status": "success",
                    "action": "analyze_contract",
                    "contract": contract_name,
                    "analysis": result
                }, indent=2)

            elif action == 'extract_clauses':
                result = self._extract_specific_clauses(text, clause_types)

                # Build concise chat summary
                clause_summary = []
                for clause_type, clauses in result.items():
                    if isinstance(clauses, list) and len(clauses) > 0:
                        # Get first clause of each type with its reference
                        first_clause = clauses[0]
                        if isinstance(first_clause, dict):
                            clause_summary.append({
                                "type": clause_type,
                                "count": len(clauses),
                                "sample": first_clause.get('text', '')[:100] + "..." if len(first_clause.get('text', '')) > 100 else first_clause.get('text', ''),
                                "ref": first_clause.get('ref', 'N/A')
                            })

                chat_summary = {
                    "headline": f"Clauses Extracted: {contract_name}",
                    "clause_types_found": list(result.keys()) if isinstance(result, dict) else [],
                    "summary": clause_summary
                }

                return json.dumps({
                    "status": "success",
                    "action": "extract_clauses",
                    "contract": contract_name,
                    "clause_types_requested": clause_types or "all",
                    "chat_response": chat_summary,
                    "_full_data": {"extractions": result}
                }, indent=2)

            elif action == 'summarize_contract':
                result = self._generate_summary(text, summary_type, audience)

                # Build concise chat response
                summary_text = result.get('summary', '') if isinstance(result, dict) else str(result)

                # Extract key points with refs
                key_points = []
                for pt in (result.get('key_points', []) if isinstance(result, dict) else [])[:4]:
                    if isinstance(pt, dict):
                        key_points.append({
                            "point": pt.get('point', ''),
                            "ref": pt.get('ref', 'N/A')
                        })
                    else:
                        key_points.append({"point": str(pt), "ref": "N/A"})

                chat_summary = {
                    "headline": f"Summary: {contract_name}",
                    "risk_level": result.get('risk_level', 'N/A') if isinstance(result, dict) else 'N/A',
                    "summary": summary_text[:300] + "..." if len(summary_text) > 300 else summary_text,
                    "key_points": key_points,
                    "recommendation": result.get('recommendation', '') if isinstance(result, dict) else ''
                }

                return json.dumps({
                    "status": "success",
                    "action": "summarize_contract",
                    "contract": contract_name,
                    "summary_type": summary_type,
                    "audience": audience,
                    "chat_response": chat_summary,
                    "_full_data": {"result": result}
                }, indent=2)

            elif action == 'identify_risks':
                result = self._identify_risks(text)

                # Build concise chat response
                risk_level = result.get('overall_risk_level', 'Unknown').upper()
                risk_score = result.get('risk_score', 'N/A')

                # Get top 3 risks with references
                top_risks = []
                for r in result.get('risks', [])[:3]:
                    if isinstance(r, dict):
                        ref = r.get('ref', 'N/A')
                        desc = r.get('description', '')[:100]
                        severity = r.get('severity', '').upper()
                        top_risks.append({
                            "severity": severity,
                            "description": desc,
                            "ref": ref
                        })

                # Get deal breakers with references
                deal_breakers = []
                for db in result.get('deal_breakers', [])[:2]:
                    if isinstance(db, dict):
                        deal_breakers.append({
                            "issue": db.get('issue', ''),
                            "ref": db.get('ref', 'N/A')
                        })

                chat_summary = {
                    "headline": f"Risk Analysis: {contract_name}",
                    "risk_level": risk_level,
                    "risk_score": f"{risk_score}/100",
                    "financial_exposure": result.get('label_financial_exposure', 'N/A'),
                    "top_risks": top_risks,
                    "deal_breakers": deal_breakers,
                    "summary": result.get('summary', '')
                }

                return json.dumps({
                    "status": "success",
                    "action": "identify_risks",
                    "contract": contract_name,
                    "chat_response": chat_summary,
                    "_full_data": {"risk_analysis": result}
                }, indent=2)

            elif action == 'compare_contracts':
                if not contract_name_b:
                    return json.dumps({
                        "status": "error",
                        "message": "contract_name_b is required for comparison",
                        "available_contracts": self._list_files_in_folder()
                    }, indent=2)

                # Read second contract
                file_path_b = f"{self.contracts_folder}/{contract_name_b}"
                content_b = self._read_file_content(file_path_b)

                if not content_b:
                    return json.dumps({
                        "status": "error",
                        "message": f"Could not read second contract: {contract_name_b}"
                    }, indent=2)

                text_b = self._extract_text(file_path_b, content_b)
                result = self._compare_contracts(text, text_b, contract_name, contract_name_b)

                # Build concise chat response
                more_favorable = result.get('more_label_favorable', 'neutral')
                winner = contract_name if more_favorable == 'a' else (contract_name_b if more_favorable == 'b' else 'Neither')

                # Get comparison mode from metadata
                metadata = result.get('_metadata', {})
                comparison_mode = metadata.get('comparison_mode', 'standard')

                # Get top key differences with refs
                key_diffs = []
                for diff in result.get('key_differences', [])[:5]:
                    if isinstance(diff, dict):
                        key_diffs.append({
                            "aspect": diff.get('aspect', ''),
                            "contract_a": diff.get('contract_a', '')[:60],
                            "contract_b": diff.get('contract_b', '')[:60],
                            "preference": diff.get('label_preference', '').upper(),
                            "impact": diff.get('label_impact', '')[:100] if diff.get('label_impact') else ''
                        })

                # Financial comparison
                fin_comp = result.get('financial_comparison', {})
                financial_summary = {
                    "contract_a_investment": fin_comp.get('contract_a', {}).get('label_investment', 'N/A') if isinstance(fin_comp.get('contract_a'), dict) else 'N/A',
                    "contract_b_investment": fin_comp.get('contract_b', {}).get('label_investment', 'N/A') if isinstance(fin_comp.get('contract_b'), dict) else 'N/A',
                    "lower_cost": fin_comp.get('lower_label_cost', 'N/A'),
                    "better_margin": fin_comp.get('better_label_margin', 'N/A')
                }

                # Rights comparison
                rights_comp = result.get('rights_comparison', {})
                rights_summary = {
                    "contract_a_duration": rights_comp.get('contract_a', {}).get('rights_duration', 'N/A') if isinstance(rights_comp.get('contract_a'), dict) else 'N/A',
                    "contract_b_duration": rights_comp.get('contract_b', {}).get('rights_duration', 'N/A') if isinstance(rights_comp.get('contract_b'), dict) else 'N/A',
                    "stronger_rights": rights_comp.get('stronger_label_rights', 'N/A')
                }

                # Risk comparison
                risk_comp = result.get('risk_comparison', {})

                # Section winners (for sectioned mode)
                section_winners = result.get('section_winners', {})

                # Deal breakers
                deal_breakers = []
                for db in result.get('deal_breakers', [])[:3]:
                    if isinstance(db, dict):
                        deal_breakers.append({
                            "contract": db.get('contract', ''),
                            "issue": db.get('issue', '')[:100]
                        })

                chat_summary = {
                    "headline": f"CONTRACT COMPARISON: {contract_name} vs {contract_name_b}",
                    "comparison_mode": comparison_mode,
                    "overall_winner": {
                        "more_favorable_to_label": winner,
                        "verdict": "Contract A" if more_favorable == 'a' else ("Contract B" if more_favorable == 'b' else "Neutral - Neither clearly better")
                    },
                    "section_breakdown": {
                        "financial": section_winners.get('financial', fin_comp.get('lower_label_cost', 'N/A')),
                        "rights": section_winners.get('rights', rights_comp.get('stronger_label_rights', 'N/A')),
                        "obligations": section_winners.get('obligations', 'N/A'),
                        "termination_risk": section_winners.get('termination_risk', risk_comp.get('lower_label_risk', 'N/A'))
                    },
                    "financial_comparison": financial_summary,
                    "rights_comparison": rights_summary,
                    "risk_comparison": {
                        "contract_a_risk": risk_comp.get('contract_a_risk_level', 'N/A'),
                        "contract_b_risk": risk_comp.get('contract_b_risk_level', 'N/A'),
                        "lower_risk": risk_comp.get('lower_label_risk', 'N/A')
                    },
                    "key_differences": key_diffs,
                    "deal_breakers": deal_breakers if deal_breakers else "None identified",
                    "overall_assessment": result.get('overall_assessment', ''),
                    "recommended_terms": result.get('recommended_standard_terms', [])[:3]
                }

                return json.dumps({
                    "status": "success",
                    "action": "compare_contracts",
                    "contract_a": contract_name,
                    "contract_b": contract_name_b,
                    "chat_response": chat_summary,
                    "_full_data": {"comparison": result}
                }, indent=2)

            else:
                return json.dumps({
                    "status": "error",
                    "message": f"Unknown action: {action}",
                    "valid_actions": ["list_contracts", "analyze_contract", "extract_clauses",
                                     "summarize_contract", "identify_risks", "compare_contracts"]
                }, indent=2)

        except Exception as e:
            logging.error(f"ContractAnalysisAgent error: {e}")
            return json.dumps({
                "status": "error",
                "message": str(e),
                "type": type(e).__name__
            }, indent=2)


if __name__ == "__main__":
    # Test the agent
    agent = ContractAnalysisAgent()

    print("Testing ContractAnalysisAgent...")
    print("\n1. Listing contracts:")
    print(agent.perform(action="list_contracts"))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9S8d5PjRrIv+lUYc/7Q6GI0sCQIvdgbDyAcQcKQBK2kmIU3hCMsAV1991egaTfdPTN7dO7uGymiu1FVWVmZWZm/LPfnB6Mq/TT/8OsHJoiiwdY3Iif58OmD7RRWHmRlkCagjE6MqO2cYpA7VprbQeINjMQeOEnp5KURJDH4bWClSZkbVlkM+KUqD3SRG8xphpv/tBpo3HKlcRN9uuE+D6Y2qB24QU8uKI7FoEwHpe8MIsN0ok8DNzK8YmDkZVCUv7hGneaGGTkD0FNcfBo451sfVmRUhQO+9Ix4TuLkRgkoOmfHqsqgdgZFFcdG3vfipvmV+MB2rKAAQ/olNo5OXnwerKosS3NATmP5TwNWneyuBPWd3jeLjbL4DKThnI04i5ziw6+//fHpQwB+//Drnx8ACwX49GFyG/hFSkVQ0ICdErSKjMQDxVkLJNzLNHPynib4ZDvu4PbXx8KJ3E+D//W/jo2Re8XPg1/+96Ao819/Twa3f79/6P/jLgNzHqQM2Lz2NgB/gCF9vlZ7bFbm7RMi/b9rxcE/BteuPntO+fGn68efPg1+ioDAvzwo8aefnze+F3xJjNh5QeNZ2bsNv5jvNf1iftX4ouUvZZsBPb5o+aQIsP/bHy+aXvXfXiq8aPq0qB+57QAjjhz7Ze9GZQdOYr1sfv/cNzWrIkic4iKu543/azAHAn2cFc9LA/dBHf/4SvQv9Nb/cwF/vQR6a/n85VL/8ulLkHxx08h28o8/f90qd8oqTwZhAezDruKs+Pjn15WuNlaURlkVv3/4tf+9siwwpt8/fHqr9pX3a+3nzL/T6KHOjeO++WU8LwvepHAZct/s8ss7HVVJ2VcDvuzjperPb9Ytrh7Asb/c5nvf7rffP2S2C4YCKtipdb7+Vp4B0T/epFQVhudcRbIunBcTJjNy8AM4sUETlP7F3/WMDS6FwAEaVw/7dALf//31aRAkvc/8B/aKkdHAa6eAXH6zp95Hn6ogdwbGo6/oe/nK/pK0fM7kr3+bATl5nubvWEIMrOtBWM8FFTwMwL447tJ/cHHv2WMNJnAfJ54a4q8/OFveF/TSMeyL3u49PK/Q0/+SGUC3/xgAy/nzVcP+C/7z2Wj/eqnvvrSPpfeJnoNOL6x/uZV8fOjnKxafqBRU/LcoEwx8klaRfWGk5/1BWL8Ovhr5mwT70X0pQei271P9MuB/p/K5K+wAKOT8Qu/9lwd13dDJl/7jo6Y+3XXy81cK6yt+BsIGEKT3Cx9///Abt1yqy98//PxvUeDX4/se2VyRST83+qnrFMCb3qfsO0HPraLoS5Pmxyp7LeL912CSxlnu+E5S9Hjujnd+HeQV8HJO7eQAWPVQNEgGaeIMvPRrIlHqeaDK5yBx04/AOpdVkvRN+r4H175B269t86thXjlCPw/4vuVXIOzryg/w7G4bNw//5TLsO4GPvcA/PXfDb/SNfR4sAVweBDf4bBkXSX4E0gBzJAdQ45erswT/96q4AvsA2EEvvR5pD4q0yi3nNZxwweF3Tm89tF8uny8svsET/vmm/UfA3V689h0WPUCor1vfq997vWP4L7eCm2h+ekD078OtK0PE54epenTae5Iw+GgApV2Q4iuDN3p9PMeZv/3kBomRWIER9b3mgeeXPcj8KTWjwLsI/vJnn5SAincE7ZytCDBYB2V7KwXyT/PLH3aVX+v98TUHdzZfupEiA/kK0PSNveImkpcMvyGLVZtYfp4mQXdTfwTmTFQAMwEtr19A/gKEecnejOKFxVyN5TXCem9lYFZWOeAZmC6wcuDdrBaYXZ5Wnp9W5cUCQU4FHEKPrl4R+tO+Lob25cIekMHF6q5IOwWTvB/tY3kvyio5JmmT/PTzd5EtQMbqPCf7+L0np8D0a6SAswK5YgIcKTDfjzej/DSwA6t8zTc/MenffnrC7x+g67cG+z1Urmy+QeVS+Lr2e+fZA8yLp7tqYfAxSICB2k+SyEv06idsr6sLMrWiwDpeMu7ccZ28n7uvTZqLF7uR/cfgz29B/j62PHNybwfzq5u0vxiXRjbwCGUQO5+Bxj/+/Dko0itM//g2on9wGHdPcgEDN/29mVn043nw5qDB/fc3W1wU8DiB+jYXE3uHr8vwwdBu0/kilNsyxluNegUBY0m80r8nNBd//GaDh9ByASH3mN5bxPSm/Lu6bw63DyJfa/6ViPbXG27GqK+x/yHi3cwCZDV0B3zEoAA+sMcXX4cAozdkp6iiRwh1+XYndbOwj89N56nxveH7mCqILuDTCvpUzDd6OFpkwFc5AwDMyqKP+j1oKKzccZI3QuL3u6T13SV9BunkG7n4f8cZXSs9RMwnzW8f+7ZvBUXB6ZWRDfBbnL9o+3F2f90EVP5yhwS/vRKvegvKe9j1Yhi3dZjffsX/eMNDPneq+fvu9Ap53X68tz4c9x0Z3f/1S5ePbZ4sZF5l9NuvY+SPt1sXPbAEAfyRwv3LtfnbCv5Kep8NUDWxe9z5y+C3P+90/vpj8GfP1V+Dj0vHBYkRGNZfP7+JOXvt9VjmAZFcl0K/rUXQ4Mu16j8e5uZ1RA+kruVgYH/+9VowteteTX37B1q3FbBbyTstv9RGP3PuNa/twLfq0cxfWMO96s0oBgCrOA/tX+/jah3P+7gZyfeR/+mn14Sep60RlcFrI78WAWjcrza/NXxQ6Tb8B0rfMf6Hus84fPj6eje3+fG8m7dE8HoPr8vg7kMvKx69/7x7n48FQCEAhd686DsutG/2xGm9CRJ8x7AjAOtvKwj3ZfQLhImc0vmRtYMn4OoWkK9/vd/giqOu3f/5+OUvGEWQdzoD0/ILsI9+P+S2bPimU+jHdTVAMJrb9ADjGECD3j3cPcHNpntvcEmWbyZ+UVO/uv9W2L/1sLwaZ+9Srhb4dQ83m7n3cDehb/bw9rLng7u7YI37H2/L27HSGAAm27ivIN8s5G66T4tfteLnUPxuw+8ju1saAnr7820JvliXvGT6D6Dm4m77NPK6WVBcwIvdg5zHNOfXN23lSt4GECFKDftLlV/M8wn+uQWrJxX6sS+vSOoJUnNvGxXv9nPl5jJXXu3mSflVwu9SK0AC+eVovkrpVgaoIG9ExL++E0j+X9mqeLLk9B37FN+ftFw83R1gXpo9cX1vQ/ULO8DSjW8a5r+Q0/xrec2/lNv8y/nNM3O9TKgXVvaGTb0t0hjMzu+S6H83z3zckHqYZ99jK+9ndd8/hd5ZkXWi5+us94XHO3s/vbqy/CwJ+5G1yn/LRH45pr91Nj+dLm+Z4Y8o4L6cd5sL3yH/bywAfsfi3ysJ8N1zvLH8+ASpvZXzPen308OiZZ8GXiNCUDpx8fHn70r9Ho5v9PszP1/OXPSz4Pb558H/HiDvZIXXrOi66n1tMkgBiDEs/7LKew3WPT59yI/ewU09lZuAwdhvHPz2Xo74fChPCXw7of1a4Pc08c/3G908Bxjeo1+9quJ72j3bEr9L+btaFpejL9eduMeBXsN/b473rBpA5T8A2Pz9w+fPn6/g8rr7/nabXsug1RXBvVfxu/gEqn6dye9bNbhM6lcn07+Yxkxu84O7h8UfSWOezvAvLtDdJTD2c+XjbbKB3APMta8yvEvhM2j82x/vnH14wBLPTfI/CbO98J5/L257KuaHvcsX8wtkuXnPUxS91/ffggDvg+33lx6jz38z/t8Owv0YAnhjN+7pyalPD5t7P74I++Z24JfbfvqzJOPpEue3Db4o89vnN/h6ukOYpUFSPi6mvbLK0if5t1pvR8as7OPgx6dcP7a7rop+z0wFbpT4vqXTrPx2qHnk4DtDzO8fLtV7y8tuo7h8+C4v/OCBs/JH/O5fb5T1EvnBsT1y35tAVv786ZGp3z8APn7/8Ld6+NW1xX9jeeppTv5sP+HV9cGvLeZS73vc+9PZ9duv+Kuh+mmdPjTj99D8tODdtbCrQvr+Hv/6gYWg50sU31wHek0eP/0nRa6vHe/fGrye+uJnOn4bEwL+7ucx+qWA2+//00HtlkP9XfHs+fGU74hl33+e5Yci1vMdwie2+zdtEb50Di/3CP8vb/W9YOf/J3t9fVbyf3Wz75sh9t7D9Yji9fdvhtYnI7usVoE/vzcc9z+SH8t4rnZkO0Y0MHPnclXi25bUV//yUP1ta7LNl+b0rOXdrLDvMyvb/LZdPaP/3XoKiqK6OD3bvLJ5+fBjUOje9Puh0N8GTi5nBemHM5P/oTtojzvRzjlL+xNlL4HA5eLOl6/rPcjz79qYemYl10n25MP3gKw3c5b/JFDyPBj+B+6C3DYfvlqD/W+iBgAnMyN33r9l89qtiC/mG67lu9X1oyeyv3VH4ov51S2J6+iC4p1LEn/jWflvyf7JhYkC4PjEfuPOxLN7E5erYd99c+KL+ddrd2VuB+0vtL55g+KL+Srnz+9R/Aeo/+tbFS+k+tK9vyGc71HbZWfK/MaFhi/mp0fx/PxN/P3V1LstJl37erGj9Onl7Ps7oHoMQtGXx7ukz8H1pfAWZu5Ver+dOBXgI3rNfTdBkjh5v1vw/O6S+1VP/f7bT9fk9ONXk/jV6uZP99zeCfp7Xe9B/cdpDyj1RzvzNB48bIF+LYZbyQsBPGyavnWe6bGbL5du/vFA6X6J81l5L7wentlGbn8rUenX4OzAvcPKby3E9VXfBZeg/CW8vLe7dXEHmMPvBJig5fcttV14+254afR7e9etZ9Dudqzu8u07IeaDNRnPiTx+v+dAI+SP76dmvkHN/BFq2eO+2zNq11n2WPo8y/om2QCY2UuZXUleS55tRQE1vlHrncWib+VF/MMhzCcR99WTl335i3n2CGIfG7815R7rfgf0f1Q5iNu1U5T3Qxt3Rl6xDNDrM9E8tHtr+fFNWj//wJLkozl9H6fm38ip+UOcRmnj5IBM8Qp717IrO32Nb+ciplOWoAlQpBckXxO8FV8pXiu9ky++cRB/ebml9K5hXi8yvWabT0reN8xbxR+zyvvlp2tG+dDTe2Z5q/ZwbeqtRfF3qP2Lhvl9zJp/K7M/ZptFmaeJBwzmSvBVRh/qXI3q8QrbjxpVcfyGSYFs7VWDun1/bk6v3iBxrNstlB5VFYOPfSQvrh9BftNDilcYvlX4cm/1Ys/weel73bNP17n+x9e18H/3utbTvP6+PvWwMfx90OO9pbFvLbn+vWcsVEVf0hN9MFFljV5OV6ry1VLXoC5eS4/e8QTPwOx1+ePZpzeb3hf+r0b37dPGz8D/lzK9ztW+3ZXCuwki6Ks3kGtGeX+CZkBf9/PeS0Oe1GberH3PQn7/oFzToMEvg1tCMrAix8ijdnCNWpeLKz92SvM+OS+22595/qaoHuDQdbHi2dx+Aa5++vS90fobh6gffOur/T041B/0vO93+uR+8Zs9v7iD/B7wuJ82fbilfFn1e5Pyy4qX0d3c+NeyvNW4DetHbeA1MHwDRs+B7zvrzi8gy5M4+O22z6LTN+3vCZa5S/CFZF7UeLGV/+m7iJvfJG7+MPGrxt6g+6Y6f1SbL3Ls+xGAS0r8L664XxK4Zx/uDqm/dHR/BaE/rfVNf/ziJPsrW7WPNd4NgU9OLTj29VrYmwcXQIX7IsjDNbsbAvhP2g/4anHuO7YErksO37kp8Gxh4UUc/p/eSnjhG/61fYTC+Xe9pXM7MnDbxujvh11+eQ+91EYU2F+eHCH87ZUHul4/QP8DZy3f3AcLviL51X7T6zb3x/drxTlbTlYOuMuPPm8wgGt4oaL7uy8XeX90f3/9jb7BpRjI9fbkyw8r+HuV+0yx/eE05+dXa92P8vQ/QZ3PX67z5Mvzuk8F8+GvTx/6pCGvrir/8OuH//qvgRxYeVqkbjlYWf1rHHmV9JdbeinqT56IyfvjB0XQY75rvSxPw1sylrqDf/6/dnC53Fku++QiL+DCN/rLOkHyaE+Pd/WNXqT//DzQAeUUxGEQyKPBkta035NLUd9rBuagk/cX58y2dH4BedMv/S995vTPbxP/nLX/vFwVANV7/peT6cAyMjCrnc/92La+k9xGYhnJ7S1IBxiDBTi5PhnXO4E0urxYANgpjv2jl3YAnHb/TsuFNpDVrz2xf/7zn6ZR+L8n1/cb8cH1BEYBgwoP7Ax++aVfzYx61PF74lh+Ovjpz79+GvyfwXutLsT7PjQQd26aABxKIH0ZGLlX9XGov1hRlP1mT6+JP/+6CRaQ6Xce+mMjlxc0Lw9nBskRxMGblFci/Qs2HAF07vYHiYK4v1x1eSap/DyYuoMHfm+XFouBMfABLAbBtk8gbw+5GGA4D5Ls950KAAsLt/10eTym7/WfZm5cWIy/9M75nwN5og3KNI36O5H9o0SXm8NGkiYBEP+DDVy/AyL5T8WAuZP4DJILMKbLM3mZnxu3PlzjqheQXt+b92/lDRKn+T3pn+F0elFdAOtVPJdjy4F1U+kvlyf2+ngMFFvc+74fbbYHemoUfQaT3NAwEL5zeeK0f1tq4FWB3efi/8/NpAr/sgl3Xb2+ULppwb5p5WKDF8fy6+BVfwMUXuVZCgLK4Paiaj+TAQeAZnl9ePTBjT55TrV/P8O5GP31PQ2+H9Xq/qgG22/orC6P9RS/vlLjcd+pgAfXzdSfP93qqUDj9PSyfPH4kpWWp/bVm1y2cNtfLz+Kq43aqXU1zydPsV53827vmRYDevpL1uPK/hGwB6LAmu4PLd4fVv316aOr+k4HVW4c93uMj1jhge3XJdA/tBpYDtDhh18TEP8/feh95ivPsvYvsN5fYSz691uBtwNM9/fh+7+uMbP/7cXbt1dRALu7jfDzoH/e8dnzZYOm9zy9UYN50haDn/rvgzT56ekjjLdpYb36qtnlldmkij/8+tuLeA0KnnQF/noZui/v0z6L2+DL1+EYfHwei8GHrwLxhz8+XYIQGDeIKcBr9PHlfk70a9nowFs55eM7qZeFu/up6MjxjOjTw1Ngnx7f5n061r4S+Pte6zKYe7XXmHl6MeNrhla3C3P3W2HX+xtA8jcJPckv75n7p8GThPrT4EkO3HP88KDXpeT6nNenwX2ht5dpf+mtZ+QrTm8fjDw32gvnT7Hv16wr/Q4y8PVPn5i8vhH6YPbFfUY7n73PIE+5PpIMwgqI0f2k/IIh2OhzZrs//fzhNdE9B9+vSO/5sYLr46TPj5cMPgKx2rcHg15azw2ovtr509PJrxhSf2sPDP7BeB7fcf5o5oHj9svjt1d6P/Xh4G43dzt6alv3ir1nuFT72o4AQ/fzM33r29x/rJeaPQ7q+c4io7y+2vznh/uu98153KASqJ4b+S9FHyRg9DMCugV/X4M9KPsXQNSNAqgIAjkgMTJBIMRHlmNTDoo4Y8okDXxojhzcIIkRYeOWNRo5hDse45jrOLZp2qASNR5ihoGPKbz3B5cA0af+cdBzZVqIi44odAzqUyaG4SNk7CAuTo1I1wCEMcceIwhiPjY9Asx5G+qVyV6ID3ju4kGvI/7zgzkiQE2RKKb09d8EhjBqi1vhech58HTorveH7QShhWZd5dICFcwJZCy5CqmQo+OFWOsXGDtb0HxRNt7kRJyOHL6M54oGwa1NQh3UuMdIGDrjTbzeTIKlWcT29jy2FVqKl/GBWx534rydQGMYDl34rEHDIY7qR4hSmDPM8vPhZpfaUkkgCb12YLXsJvD4FM9sez5MRbxEUYaF0TDvjvsuMB1HsOoQo/QRFKq7XT7hmBxGXbIJK8Op3aVc77eLw5m2O3gocF0jtJBS88lRJ5vG3NUQzJCigRjtzipMCJYxNkOdMyJ60jZuVvOUNnM3rPckZdFDFxdDZeZ2WyZkQhfoxay7c7tlSVP3XbfOEnJkN1qaVMcTiSMQU54Itas4Ul/ubDI+Z+4SSQx4ZyYYhZej8cQFvsCR6HRlnkeRLGnHeeqfJS2r6+k5wcs9IphtBHtHGmJ8hczdSo1s38kRy7akVIX3u6DFrKMOmYwrYNCs0ndiCY+RA2R5WEOFuROiwsh3yrLpGEfkJqagTGxo7jDVEu0aLhuJjocq/twRtt6iW+3NrmoLmzSV2gRqaZfyOZ2UFH2OJ23o6CeSUnmfk1WpEWVcxxgoWeBw1UEjXWaiVTYmA7ysZrUIu2TaHc25oTtcl4vOqT7Tkw2hiccOE5gxxOijFKthe0VODlPOLSyFGu4lYsKWi7m8E8HccBeT1Y5edhQ0QrXVZI8MNaYybSVlyBM9oR2/1nj5hOL17pQgo7iGs+NikqgmvlKHNJJsaBebGxLB2csua6Qxvg4op8vRsy1qYdc6EgqvqApjOQQq7NIlPXjJTpQsOrITWl8c1jZ5XsU4inUTAj54ArbfrTcCNIKHNXqidicY3Yq0PWE6jKHzbETlmRwNuYnTqK6Lzr3JNGIdiRcldh3vQomr92M2GTOQL9NcGW5n9N5nDvoKwtYHhiLMg4wwLh2T67BG1tTYpCexTA/pClocnHUjGnzYmUZaYhLCSlPViBfzTZthVWLpy0NYyotATQtgSvjOTRN6P0cP7WR7LgrzMIMwBu4mBVL7eWeupvvJcLWnofK8XwaTdl9MpYPQNsCGfJXQy2I4sxqE0lgFw+uxqnsd+AnLcKLoiekfKMcmcSuii20IB5XuaOnZL9RsXKxdf6zWLi2ciflysSNHFTPZ0wxbwXAC/hdhBlaTBSniCxgmcLHeqd1whDRWNj7D8BinSP8s2BzONxyFCNJsEeOV52gRxK+WueuMlCigwwKW1XDPetx+CXg1VhMNMCPGaVpVtQSxJ2K8EQgkF0UrPuEFqtRjiOrg1qR357FPBqvpFvPUzXS5oEUm0XFC4xirg3Ei9cd+WwvprpFDf+qvG0a1kqDw0A0ZZ/i8YJEt2pFTN8ILskKpITGsZEnaeEti7lAq10BOqR5cfL3pTtQ+k+lz4U2WdGFzS4SUdsS84lWl2J0UgbJVVGvqeFy46xrJvYwoRsHJyGM+TnHvYM2Gui+NtyEk8zsDNk8FxM4Sal0z5urMIpMAYgixaMSWxCkbyuWmXkLxfk3rzVGp1b1dH6YyAalF6zNKK8jn2ticKBdHYdSHIHWXm2LTiBpseiSkOVU3Urs5ZIHsVgMhhcWrZDnm4dGBUMMjpFkm4VIICYrJMXtI5ji5HLtJRljiAc7FxkwkzKVdS3MaS5QcKinXFdKYcnGMpzDrsSKuDel9iYiHSeFMohObjXzIYbYFOt3UMF0sjvBwyC+Fut0P9Wk9lqawvxbns0WyoMvMYZQpt0Lg8QjO4MXcaxVKDQR+EXaEfMZZuqY3Z6Zyt7BEmMXQ3MkbulBJUsjhAGH2C3dSki2fcJyErYIlEnooJKdnUyHi9WG1X5kBNZtl9llpCWINw14IbE7f5KlgHwLGzTFzOVFyJx1N7Hnlcs5R21v2Pu2Q444jZHrczNhsxxP2YpvEAiQPpxsd8fQNLTOWFa0sddkuUhpfVE5UOqtwxsPOvLWXOX5ceN2YC+L9/px6S6+Tub1XHcidrwxNvHNPhZAQDkuNHCBaPZm2oQvN6eiEisi0PljeFj74pKt6G08ldisp8HT0tOSpY1wVrqmEyVifpcwBFkCwQkPPFzRiFMZT7jSS91ON36Hm1th3M2AdLpuntdhoiKAlegEnhQp35klaSewB9gLcmhYi7hvTKarlqEclkFBRkstpG2bV1Px0EQfehDgvDDkz/aU6cilryLSBz53QtQ5wJpZsjsQoODcnRF7DQ4ny/MV6wdudyre0dDBOwwULAsaGRlSXYV1CaCs1YxuLa6U8L0OLVr0sWM8ODePM3MUuhVP0sGu29QLviK2+yhk7PlmnlrYh1lvbS8piRoF5ysS0bSV6Nvc2iUhDdTBMZ1Ilp+hxLSG7hVcn7fLIkWSDaAuexDsqJ4ZUDcW4NiIIuGYgWzTx4dYXonLZRqVaJRwmTtiNskJ24mqintpj6GdQy3KOqRwTaW+3oeysuEM+jYxT7Fazw86I0EPKKpvYV9HtnrdnmwJZLawZpm8WSKY40BSCSxDfXGZOWOftqgliOJlt14XFyvSu2eDQljxsG7dUmE2jZXyar8YL9bSgnY6bnzBoX7IIPRcQdedAyX5xnrv+dq6vp6PJkkyt1ZTDONuw0XXjnkSCmNAMUDHkhzIDT5odNw8PPu/rs4atIcJeiztsr0hNvqaQDiDkhCUk6sSPljNNUJNpvFtRPjbhBXTKlitKwulDvB5S0HxJuPpqGbAxvptZG92I0XFcSBJRKYfQNpzN8ShtFqQ+wYTA9o4zQ5jmGXY8KpuZn05n6EzzTmA6AaTuUIJb6w4lmUdkpDTcibKHrCALKp1Pt+R+GZ5g0hgXTXg+H/bB1lSaenaKw2KUHWc0ffAqwTskxHith0sXlZu5DpFT+rg2w5Iz9Gkp1st8cbCOAKetJl43N3n6sCBxg7NWtUWXZmPMwlCSGp4Rzmu7y1RuSwuyL+sG68BlsVt59M4ZK0dJcLjyuAqYYalMloINi+VaOFsoVM2TdbNt9MDyYyWzmgAVQ3M1mmEWPzYbbRzYbEfwBLadhUFZ2TGFRMKikViJHjZxoNGTkTQbOzmvFNyy3SiQMa1ZhwlW8EEhsbnOjGfsnENBpjJxzxsXYSB9r6aK3wrWTlZ8uYliZGg6rNsBb1eowtxZHsxAwJ0mXmmIpMbq0Vzl8LEzUro0MLcdtSwiGkuX4+wNe4xollpOYs8jCKE2afzQunWtyS5EkSZe1RAG4IfabM0huYQtkUTmMKba49WUXXJWWu51OGq9bMGsjW6xXru87FkGltVEuWa0lSCIB0vjUqUwpBV/UK2wMCbp3iem7M7a+9iYMhT4zBWj6egIFUsEXrH0uIPcFeksFJ7emDGd0FuuEclVbs5XbQ6A1lQpSKFG+C49yCaxXzQoR0+azuIUzxK9+ljhEL48ZnQ0pFx1vT/h3HhbpQxBrJRQx6fs2a2beZrCc99SyGa0ccTF1iEiOME9BVZG86GHa8pouZLm+CToApryogBANizDzsKJC/zdJt97UX7wThYn5mssy6HK2OzjfAsCxHqex8DZd3nqlLl/QLs02UMnnlxBdj3qLLr1tKBeeO6CPKmI6fOmEJ1WvnQWTa44oNMlLoJYcULqhTGnO5BFtQy91zULoxIy8zRhfVI2LtyN/JOmlfKUCeR4aO0CvZqbmmlAw+UcpKc7bIi7qz3U2bZAiTEnOPaGr/bi2IVcOx4tIpqc8PstPyqATXPDLI4g/2hufRNzIVg5B9PRRp23o2VkQ4p04jdQuzGGWuG3ZqEvdMXO95y60Eayi6z8kQ+XJC4dU+zY7ei4qzF/q5DJdHroRtMQ5C7mSYjttdUsRHS+4I8gqAm+7y1KbmRHh+1RAnnbIrY9fyYQDmxNmB3IU+ZYWwddaglasyfPw0nIsV4aKQqEKcRMSRaWlLjK6bDcNVOWjdHVmob5ip3JDJsvpDiblSDgqtMFFQsZJKb1eOIB7B2fRupalRY0hObm+LSMyxjOjPV0d4YhaDwdeRJMc+cS3c+mpJQczwW/pqbtiYPFoz0vqm2YMZpsjmUiTiyasFChMFWCPkw3UElBmptHo4SAEgoT9oa6ofcwRvKTNMbI6dYY44t6A8ebedEQkq1mk5W7BvOW4LETOcx5leG3oh2aWy93hHPBwsdk5AjN9thOzqt2lFHq0RbRCu7aahyflmYOkKcw9Dm2JcVySBgAzEQn0VZxUp1pGRjrctrwaSOeCTyVM4uxpUJ3xiSS56qq19Kqi931fHnEt1lUyvyer6N5Bi2EIz8ZqTtSgnaOtaYjgBZ0dOMNaXHKoJpBHXAC2lSNEZOuGSogGJRZwTn+drSWTkPBCZeiKtGHcCKnbW3FVOHtN5SGxOKOXXYRhjAHhQPEhfxg4NPVyeH0toDmjO/PUBWea1TKsy4qHU47kgKjBVkPwU9FHt7MA1mW9i1teAHINbAy4WGC21hMIdjn+FTolMR5Ccj3/INNnuTKjybsee3qdLvi9FGl1Yi+rmZrHl/Z+2aX0ttSHWFw6nN6NG3bxbQ4RZnubVZ7lwceNQ9QiMo31mmerJYUPLS3dTdeDBnDDcpWpk/pvj63VIlZ3Hg1lOXl+iSi9ckLiWa3GeVyWE/WCzkSOxHbCrZzoP2Delj4I1dfmNJoLOIhie+lDsJ2xZLS5emh8BbiaYpDcuSPnMnWDaKJUXpRVoa7bp13wmnHTeZ6O3XjyXbI+gg5myRTT1ewoq1n06raajLWSIlYcZst6jtK086OSSpUEkd0U9ZEa/4cMOU0nie7WSccotXEsfgYwB0mitRdZ/DNiBlH/hZ4JQUplBKZIKuxjQuH495DPFZoJwawe4xpkpHgHNQFPDuURqSzi2B5wtaQ2hyGCss6mGGDFAHp9HgpaXIZR4Y1PrrO/GxCXYQgwrjZdDpjsWpnsSWnuXOTE8JpgkD7ODuVeaSFvFuxHB+ffCJ25ke/DTx5TUkbPTLTFZ1HKTF1hcNWEOddu3YE3TCG1E7dBTymnEeTfTxabTSQqq+n3MLmcSa3FcajUszIN2GaqUqzizl86U5CvPUCNzjkezWwllBqQak3DpjiSBhgjqhwUJYQXpLVmcJdE9vGpdeJjedlZerVw3XJc3u/3pQS0gRUvMa2iDcJg4NDM6VGx6ZiyT5dyfORh+w2JwgRS8ffFKvyNLQmHUcb3CEq9d0K5D1rfNcRM+7oYVoKL5R9PletfUBs17oceelkn+EgFzooasUNIW4lidkCkxcnjpQoIgKuwKMYex4yeeWM4kWLl1YOE/vlfJ0kU8fa0hqzEEZDOhYlA6TMLINQMSPrJqMvVSfTxGCqOKvzflTgKQwgqXpmmbN8ji0gfQCYcQXWKkPWCIs6j0t/MhctQGuxT8Oc5U8M1q2SEj8frHFcTZCdXhVCt2pshN9Y9NqcjuM5sYhaqyTXkuJsbLsj4ykxt/f6Fq1Xx4lBrZe6MhdzcrLmsq2n8KQKHZAwqGCAqTe5qqEwMW6cbV4MJT5aoVNibW9d4HzOiRGOz1YjhLvMPsz5Ob1U9vN6WVV+RYLEPApKcnh2M1Rijx5Tp0t8xqF+5okHgxSOdIe3ynyoEhKQ2442J0kROmMBHjsbwTnaU3GChXJTbneeLK/V1X4xYTXuEKrns0LHRrhdj3D3VK1X/kxNOk5WS7Ngp8ejnhyYojgffL/FioMt0mI9nQZVa9kVf9oXx5M1ZzGdYvdbsdF3E7gCuXZESwuW9gNknEOsHVpE6dWjMT+Cq67EmmwXypCanKJEHA7D0lEODDOron2WGyttmSq4zQVbyT5le+Bx1YUlK8QRkUpSJJghSTuHzSpS85TYExlZYJVi0Fk71wNTbhZmc+bpXDt7iQNTfI5B2GKITMVuPQpVbZNgXFFt5jubaCb1St0vR1AG06fZbOFyvtbOZFEG6N0Y8e20UlFI4/GpAalrW+bDI4BHiRIqRkyJqDNslLIEyeheZpzVnpmtuRMf0fF4GNFARBRzEENJV/uV8Zmdslx+mHjqrFyvavdgrzwrJgoZnqupCXEHejfRy6mr0lxI8igPr09tUHKkrMonh/CRs+VmGZXugIgABhcQcq3EJiuQZ8UmFbpC0qMqujGywTrmUCx0mA8LmIw6FHZc9nhw6ySMIAgSheWeGyIZUs+6sSJI54W4ot3yXOLbszVOKmHeDb0FB+n0sTlmS4IDkJDz8yKjZxAS1k06M8ZNyNT4YsOIQq5XgYaOLG5/2GxrfsUpsjUuC8hxEjM4aAhAQag3s0bRZMLGvNYcZ0Uy2UwP1bYdHpZ7BUnQs+XMEJowIbYzZ8MN44daS02giTjXFzxlsqgfUMNqopCUtWobs5jWCkhsEmN0zg7cETFc7rjNXGLh7Mulf2Rkp2ylppstFMV0R/lWH4a05M/n0DAhvD0ZnxvEZmT2oJuo62eqh6lzdR0SVh6C0N3OUVjkGys4T/F10yZ17s/Fo3GGJDucOW0+U/GNVuMjUxIP5Gy8XS2VYOQ2ZDBzdgAVCrycULAHzTwDxcJ8e5wa0nnZYRVNqM4KYBV1O51kZ8+i2crwOBAU8lE8nI+HJ72SNE5GizrFp6Sfnp0cYXxyLXhHZinrDM+wy8MyKztiyUiYT9nrzpiPm2llz7aVDQfO0NS4CDuMcGsT7uaUvsbKA22cNyY6kzpyT9eUBmkj+JzsYDQUqGXGOltZ3+rsxMTkTCBkGN3SGK+Iin44tvmI8tddIQvrftNAYi0xOJgViiBhXiQ1TrkO1MBwTrEgXzqeKUhlc4g29irkTapgRaV7ObWXRzmDO0SC+JSxg1Ja9tteKDXEoXY9XNUelyLz3aZ29g40Hja42lGEm8zH8AivKALQTRpb3IL8H6AHOfVGFY2yCgDphiwWubc4FoJcuB4PFaSjprsTAcfCXjsNu2ayVEfnTnYZBNGlwFdX9Jw/6djExGdhqlhs04z3YU57dj0RD6cKPYWlIp6KbL5l/fOIcbmkQNDjspFoODrgshKKrqGea6R2yQNmxQeQZMhevSyPu0JDJeBgOM5dM7Cko2xY2nyTjwswPVXSJzVPyTx/DtneKBsvyXkVNovJtIq4jTpjiJUa0c7Uhlfr45Q8JbkfsvJ5u4GomIiMEIM8R9X0MblsiT3EqWOGQ7bleFOc8tVhPp4vEZU90GHZ7oNdc2ShzsWZlWuYqy0eaiAAS2M7IOJma0NbROsw29Akty5CVuJCVE/wMbdOHI3Rx9l4j86g0Zy0MDMuVuJ8OT80TEElizSuk4UWb8OWP48yzHNIplkYOb+HRBPnZWLFiLU5kTaJzM6ZdYGiRQeyOvksE9jMOWgVOgtO6sHcHlwyGB6rvN2cqpLPdsN1RPLBQdzmUEGsHZLcqkPkMJxzq/HonKSB1J5QNne32n6+GbKiVbh0trHMgO3cbaFEMTwTK7fpsiiCQWyTNpiFHfJqIUSUsK7wcn5k0qTRV4tNM9LYgjBDSIbixrBqwUJnzn5s6Ugcy/78cD6isqbkx9Vob2wODD/ukNOMWBxi+zgjVocdZZ98O8FC1FIKWJudCEND7PWQPuult2MrfLHA1+vDUmyxZI2kEDvTVINc+eGRaJf1+igUmlYtUwPSzwaTbfDUSmaiW1rFSnP3zEFGcBti5fqAQ9EYgqd5LkJLE9nu8nKPr0YaDx2NcMZhYYy1ZHHsiHkHLPvQhZkJkyYz25/oWUu2KX084kMWVZvIOLJo3J6NVDvKdkpsJ/umw7UCFWlfOe5r2aNgxA2Wa4zBhKFdLgky1hjcE0EYHoqUXNDSzGwykoC7Q0JsdrYYjXZD4HIN2Z5oHh0M54WFxasuhRkJzi1TbM8jEiaG1faoKDgUVw4025rcMajDw2m8VsjS5SE2tnWat7eITSYHXDlqc7wOIzyxyWzrS9FJEfex0YgCNksYN2qVY75EwNQhWsvsTLazXagduq7LO7MY5ZDKHq9nI8jv8GwsCup+HxlquJNWkExEQxrE2WDWqXJTdLzaWGFgIGtsTADsgI6gM3SC7Wk9nDJzxEp2EZ8WYqUXidGuVoR/Ur22mGupJmiIdhgCtIALi1jbkeTeMUXdkNZ6m58i3FvplhjptinWJ21TF2UnDaV6iWfqTiXq6nQiUXOn43HbIeedC5GhC5cqP5HhbLLkySUpbGfzrhmNXKU8bA24OVadmzCtK4JZ0Pm7POrqfArxxyor12M7LfcnxrKxbhiTJgYlxbEm9fZUaUW4p40sQlbTstXjKlZGKKzhaaTiDoyfR9TYJ4oSJmbD05F3lCMiI2zE6l3NicsFbUf+eh/OhIPqh/gI01ljadlbb7NDAiknsUnNovvzSqzH9Ag+HPEJZEUqEm2GWbrjCVwYrjaCJuxhH0R3tYxhSNp7DW6fbc0OF+JaoAIYm0eIXlGhUTvNMRWnqyMUjGwLmx8qBSUhRtOGrV2zY8hX17iNseqeo7ESY9stWZVl5BThfFElxImtg9SSGdrJFiIITEPNk2kuYh00KIMEhlyo2VUFpcoKnlMk2tWkYIU0ki+NMCq8sPHFgpkmp9D2MndJmQQW1iGjtCm7mpvJ3GfitUw2AfD3OHyyfAeW07Bb7pbj3ARJjWqMjGS8m6nxYcaD+LloAXSUDQ+zhtkOGZ6P2Nlz2RqxM5CvIk3WntEJ5mDwEoZOVBiOhuaoSPkRoifkXrS7BJ4IDWySi1ELEme19YSZvj7l2+V0Tnp7U6FyWAyRhhgrVDFFuqU8wmHJhmE2hfV6ucmGFVmKuwm0V+x0dxzSEVk0aLFKxgiA2fwx1xwlO4CQxsOTakStm1xQmWK/WOK7Q7xk1fUOye0SVdoNu5tBzoG3ivm2IMt9qiMSTVYqQ6usFVulaONmUky93PFDyx8e8oJMWDZjF0nn79cuLUA6Jx2BcaXmbI4lmi6vR+oMnSsNLHGn0Nox9gRJ5+W0PNNDilOJDJ4rHFYt/UbwsIkWBFOPRg8LgTssDLdGtPwM3C/IHUcsvkKtTbucsMOFcjoZ04Q3anOI6WEzOqQHPY0ZNRQSbrueF4wVNPzKa4en5W5oqEPc5KPxOJmjrB5PzE17bI/8bgJCfD110OnkCPthfJhGezZnaVVmWwtzhl2aNjHp8wW1PcLyqsNQYz3JtjwoYIwTtTMkgCZMgDMFfDH3h0PV3ba6wm3Oe8N0DtgsE31tOS4toVx3Z2MyP6jdAXEYbRePmxE9FgClODFJpOInWFA5/oLbJ9XRhcaOJeu+U+SkD3EUO6EwryjK2ZhtF2PD7EbBqhaB703Y2VmfpuOKc3IfNY7R5sRyRAiSdq9ddbVrTlRiI6IqT2Cnk6Xvs1RN61rm0FiZnN2RrSc0czh5p1OMQUojkWu3NERiUR/QdCX4Z5M/7pF6SxE5Ce3UFCGHMhrsCo/RoioKYp0MKsaeEnG9PElJQCP82cujvVTNnJzGzIAkU+I42RnDXTDy3Ck/JNfjHcsmHC5HUyMId9tEMzt3ISQCAPuTIhdW4n6EOwSqoFuKZJ31zJkB80N3DclH3qwU4+mkrk2KpHXN8DJjhC3cQ50KtCbSEaLEs3ViNpA4UhfzBUrjhgOCMFe60KlMnQQNIsGf0L4rrt3xZlpzwVIqp7zLbuDNSanMpcvMHYD1o27c6vxsCs1WWqGA7CPCllAo+fp5byX2fLSO9UW0OJKcG6mV62M06F+I0akzb1o5MFsiJtZNwWuRPJVtK5046Gy4dJMqLfJ6OzJzKs9be5InRTS3Oni+J/0FNg/PChY0hBuOGndiTWqPlOBTGrS4K2Hqwh3iu+2eqerE4zcohYkAexU0wIxVvR/GRwSg32M9hbot1LXbRUgNV2W23hBppZmQlKx37DjNW6TAzPk55YnwlCy7GAZqS3EmWzDiRDrHLLFsT1y1rVJuw59jyJS2I2/ht8tc3e5WQ3wJ8+Nc2lMGXMAyc8oVySf0c7fVfDXXtt02Fw7Wtlt6S33CYxWJaZUndfr2POGTNR65LUTHcdTs80gXE2/p7u14Uvjm9AAE2WSj3OaFkeI1Izgmh24C+9TqAG9X+ww9uALBubtj18WkJfkSeuRZLaoJQ2HGFDm3Tta828+0eodCHWJrHX3CiqlM7xY7N8jHBOcE7WYpQCrctnymRGMA3MY1I1fNvFFARB0SauhCCLnoYHezmC8dvEYaUujcRnE5IVvT9bSWNqyqI6OcdhOflD27ofIMJLH7Kj2xEJIvuuMQQk6eO5kHJF828xGy7Eh5h2CjIyzqthENN4I/3TqUR2jyvt6AeF3PGn7o7iTIrefVaMc0JGBkuGiKYuIw1fZcEvN8jWvmODqu9sVCOzpttj8KBGuN5olL21wtnyOVCCxO1lnazGDPFpamYa8CpCqOQuueYX+568jVcZ0yzthUBHKLWWNJGbcYZe+mC29PLLqhtp2OZCygmfV2Pstr1YcsKrEXXMmo0hblhaYol/o47iwRbjPcioKZEgxhQSEKeV5PGEGD1qzINcBkWEMaWVNDPG6rA5ojJTkWrGaWqRJZDNFReuazgKNNe8gfu+XyLMmbETJSYeC0sHo29RPVmiZGyh9yajspLHftHdA1RSacLByPhnVchZK2wJVhurFm8HLJ2RxKOnLTeDVu5Pkk3fBrfJvshrW4MRrOZo/6bjzWj+x6a5ciZQYqhgcdMosYimxOhyCjPPbcMhsGCwx0F6FHl18n1DzJZwsPP2+aY6aFhF9pISq4+BbSimWCra292ZSBgpRaKm8WZeAHxqlcQuuoUFwM3boLZHXcSHaUE0YXK2dYiGe1XcyrOIDwaTg8LrxoF+v72AnSXC4mDe5uWKqJHRSh8LGcnxQertGzMJov222Xn9vhspWw80YtD6i7mTkOyHJzvDoJMylP2ZGMNna3aaCUnMpVam6i3PVrm55tUN6mGjk/u5YGQQ6Vki61aKHd1jwfTnPYgG1PoWswO+HdqBNEaAHzRbQfneDWmlK8MyLgypXkDiZKazYm4anvRq7GinI+nIOMGMEO5zrH8yW5x5U+nT6Hi11ErsI9cFDtDK8SDD6NT/HYMUx3G+cI0XCTvNrqzWrhhltH0mY6HCkeBbzmVO+KtLblktw0ZMCdBXGPHiN+1LorVTfDdUKTkH6sInJ02sBjL92Op3O4zs1iC4/8qHJIN4DGxGajjfPSXkx5lGsQW2JJEToPTzbCFC6LjmFm7wyDHZZXQ3HGhUIb4/vawtkziSAoxuGdpW4Ic0VpoZi2m8POsZcnkOAuR6f19kRNamSZJXm4NeOQOo7xKY7ss9kQtclqpqosyRTcGIlpFiHaY9TxiEhQML/AfIVzJ8NJRSxal9l5HVzm4aHTss3MKmxNnNozfCo46VaCVvyxgZwoKHRsvjQd7LCb71F4RUALwx6nLkDmymYOn+Foq2A0pu5Pc5RayKecMTBTmDlou25OjZWlEyPKqhoNNt3GlJGky5nNqT4RNuTqpeBUDQD9J5o0gpVJqJGTstrBBBEgWQuesAunanWwZafelfZqHi70CAuRTuHPE9/xawCkZzaxMeTDFuTdGeZkbghgit0524wSCH3BRP5qtdykWjPZJ0U4gzfNAeSrq2jXWUvVKACK44xNtmWOgXweAVSquJKV6Ydwq8l53UyCKbUN+Cq29NPG5Q9jOTaZod4t1isrUoR6m46n7nFYWYdI2hP4foPbpp9LYhQwmaG1dLl2TN+Sx1CSKTrBpoIPAKywwNa83qrTIHRwSBj59oJcGFNCIH0/C6dg+KktNWdRHcvExiPWrjLioulWyyEtmba1Nz6u7Bk7cySOUo7S3M19cQ8Z68XuyNJWNglTHZaUdoqo+Bj4NXVen9fnFK+KM4+NPRkSwsqa7ibHBZ/skZU8Dg1uIvPrXSlBQRdlUXKaOXHHr82cFcfDxeQA4LFrglCsEyd5yjpkuxuBJIiaoqKhakB6whggI3O8JWRr7ErzWPbGc3dhWIY8YUayEm0aBVL8zNrIQzTLLAfrSFVwQn+v9EdWU1ceWcttYJ5PcbbBdiK9DKoCW6/wWGqH8+GOJCptsUH9RXRYrFXEmIbMQgN5/5YQT+sJL/InWpG3wpo+0TNFw6XgxCURClkxWUA0u1X5lKPoBN0g5tgP14258Ha6fB57iuKkG2U8c6xiL55o0Tq5KNNo9QnOI6hk40ix3Q74ej+bIdoMYxPfEFcK4U0WvgosgZ2VxUTbjy0qYjDqTBwzbuYOJ4riL6Y5sTxO8my73TEdhPItcziC0G/F3A5dLwzhVG6TKE/LmZeVZwfDeDCtJVzOTvyGXOCrTRLsjZVZGRusjrAo4wAGcN1ztdfimU9kSb0BrmLJ7HHDzLz6BPrhlWS19BY7e4t2zEaC8tW4kXJmOAdolm4PY+yYlIcpU0jamdR0aUrwCuTbDAMHyUJSXOE011p3sWWnnWXLrFfaJ4ra6vPJrF4PZwU3gjfH8Bhnu3nAd92SiKc4fXKW6/lxWBua1DJrA6Q0sbjHtNVcgugomGZ2jrPtlAuX7nKWngPCUgqig4vmKMpoMiQRDklUSV9ASoCY7KIeWhJjKIdqQzdCOGREJujcuFlvOcFbzydCOTp6CI/kk2Za0dPReVdudkORXbDDKtYEw3clc6UfIK3a50O/FJcnfzqbexHlhaujqQ+baAbcIyG0u62QrrtFsyqDHTJPlsSGR8yCsE4agunSkCYZneLQhYgKpEzq4s6gV0fWnnrNqchnR76mmEM6PECnNdzZtrOa0OhYOyPeSCiJWMI8Fc+0asQHCyX0YGspCoR7NMgdTuhZa1baHF6lToxx6VhuN8EmGWtS4kKpX7pzrgk3QWZuVmOaj2q/HptoTUKaije1Bsu2Vok7V23sOuRqfDr16qRuOxM7eVSJU+PVzhVQTa8gOAJ9Y8Rp0qz1pdk21mEWV3h2mjeCOdRSizvOt0lOZ5C0izZVidUu8OM1xIirqTs77G1/SKBJU5xWue5AET9bQFvKXsFcWm+5YUyxu5SY1Aq/AinYiFc6f+ji5gIdWhVTI+x4u0xC7MCiutAwJ4DwNhFPQEWqh4HdgFRXGC+YoW+uk7Cy1UMJYO6hOyeYeQpDdS8zZwxaZCkQ4VhrDLsNxpNaRDddkYkCpXSy00nO9NDl8zT3VIGe0NtC3Gkq7+4le0eoJYMQU4gWXd6DmwIaWVnNFXA13tcIdoSAMS/jZRPp3k7BpJ0FoyeUdFcRtthOTsPMocbxoaXh5nAW8FrKMnFDS7lxPkA2szysmVWz2gm5X3RHME1ms2Mm5CgpGRHCn+AZfigCZbYtTXK5o7Ryox3nq/mUqqsDkqXdsDE9mcoNaKUxfL9YKtqz0bbtojbTzQlOj01zps7Ite8k9RIe4bUQjYLRFIkSgbVcxh5G+iaaB+lUHm61MLaVjlhINCTxY1RDzhAOZ02wcZfemFyyYys5wBiLnxi38BdBMm5arCTFqTqZWKV7WlFuKEqL3Z4byhpLVbOzpmJ13cpHfrWOunQCQUkzrzGzUXK7InOxKPbtlpqyrjucO1bA65sCoZolNubHzlrTVmk1jGZW6aDUyEEDEDbdkyGh7hh0qhVjdTrFJhXbnpGMOLJ5HJ+UGbNaV8UOUtPJbIJIuOOdu2iabBbmIqtRwNexXPPBMN6DimMmPPMHDEQxbTg0SZDeHylNoPDJfo9uR1CqMl60oaDzBsDd0tyeh+dkjkIsORRNwzjvQFQxwgpV3DwkKDVXdrHEQ7tdvB5OdQaVqc0YmVHbSEMmfAAtNsWqaejzGQ3gHUp5XcUjCC9ZNeMv/NSVfDjmrSYuFqW4oSzE55rTaH0ez+fUqKi3Z58/xd2qSLuVPdEVl8jddjrzq9NOOHUjjIPDLWFXewuH6RWR8EcRLc14rc53Z4/JXNiBcCfM5jPXETcjmOJKuTB3LZyIU51QJ5uQB5CynM0TQQ3WVROThNPg/jFYo9JWHI5HBd2i84ikVDTUeTMiNwHkzXwGlg7K3OK18VgcEfsNSXGGtcr9iAhXQ9KdG8XYnyg7edbkTOvNGjBr5bPZ6Gw1CkWqKyhyJsPLFcntGXG3Ic5QWOznfNlOp/mqqJ2u41CMrHm4DJwjLkOqvogU9DDGD/MF1KJlg6MbYuINc3ZzGEnzXbGzoBnLnsoAqlBDIp3TsPZG8XAMkuv/j6bzVnJWC4LwAxEIb0K890ZAhvfe8/S/tm7dRIFUWtCcme7+4EibO+HnlVr5HGn+9Ky/+71SnwAfzc1PghwyyzPksyXm8jxNIDQ4yKazr2FgqxLfcV4qENiVP16LFVv/xNPVfPWgbRv4SzYWC6E/TZ5bIzflt+KJ2amUwzX4J8z0VK+agyRaFeOynIlJM46Rxl6upJRWQjlHKROL3/kES3bmhBBzU4bmlmzLL3m3Au49rXdQ/WOpaSZmVOVm8ENhq1FmgQZJ4tWIChQFiwlBM0aJ5DBi+rtbX5DiqiBdXTzFsaLxzyzSqBgkx76blvtnCUtWaiGkGVnmshlM2mCY3mLSra02LHrFm/6TE1/1c8cvDhUrYQBLQSwk6HVtPu0a2IqfRqYRz6xwcJhCgOXgTOXH2ninR7vLGjena7SbQuTvU/lR8XGEeY63avIALY11D+QJyrd6WW7Q9Ha+AGAmU8dJMs6+ddcq4tx5xQoqsq6qJ24To5rvGUiO7M/3w0xlP27EQRzGupcR3Up6h9Wnn3W9o5/Qp5DxQTo/ZPoByrsFk3Z8o48Y0ORiskUocd56DA5S1kKpmRY9lKOSr2WmbUj+OfsvhVH598U2o1hxsF+mMnZuZgYn+qx0mvKTnP6J1rwMIa2ttWWtK9/ZxlUyTKYGN0PT2af8KARPIhwX8aiy0cx+BRJY7LCEdLiMnskv8C6qPspStND11CrHZtC36CXc8ECN6Lg5idr8rfPyo7VfnlemmyMGuI1umF9sg+X99HsZU1uftXqZCtI7g8f6DUuI+obIXxRVwimrcSlSJZtnrRxAJ109vRCgcRdhjQOnK1lBjOpyq/5nibShwfSUmMr06LeN5vi1M4ifxi3bUzdGeg5wn0ebwwz7Ld5MFiWz/BLtZFazWSBF2Le9wXc8H5IUrFmz8fFEwY33xMPRKWjru1gSUijOjjHT8C03pjPw/A0Jc52w+STUdL2VhHXLdiM+UyMCGIpcgDuCA9riZ7oIYfEWak2aioaNx9nJEoA5BQJ6IT6brw1XNh197pUHnTRIiKxCeBdZF6KtFuwd6LHor7YhT9yrTmz9u2SO594GfNYu9Pv1a5qI0h0f9skj9rKwWXF3CnhaMgDR8IkqDP8MSmYbDf5zr603H6hLtCGqGXQHCfCDtb21HCw4W6a7aRTYDxnPDPGng5AmMkosz83TSCdWOk32/FpuAjOtj7TvQRFoDZ5jbs16FkynG4Y4QsC1RR4jUfpjzH57Prsew+9yibsVfQVdS7reOaAqxZimuaiVrPNpnFN/wMSGiIFbMphPIzHg5pfyUFlYMx4lfzlRZsD3beuhZIK4ttW0zFYpjwGutBBE8n7i0qncKgT68SOe2mnjYJGGRRVFw3lqfKkfNN9kSxBic0shNRg+uJ933ho3wuTCHYUC5C9DjR2B5hEYoejGZajJreqS0ogiIOJIQ3JdXHokkWpVBZPvd+i9z4ikUIPOQx+LJq6piWXvejeFBVEY0phMwP1wswpnNpRE+Q7yptcD/cZfvzqn+UAvnMTkV1x3wGjDj9g1NpQgZ1kQO4aENgaz4zfFeucFZqnLDJVVnCaWZF4HNDhEEA9LiuP3nEHr4jT97THfWAf9mIxiy2bO60s3pXxPYVkrNzexJVp8I4yTuhXK9HOs4lm9LlAsue8SJcZ2lMzx5VHB0rziWs+V17CNlgo0J2fh+HUNkYu8JLt4w+oobDCCziVKhxNxN/A4CZbFSAHUGvsmmVN3bX0O5HkBM6W2AwgRSFK/64CgTT0X6/eDRi4eBhS6vU1MPEkO3+qZiwLFUI7LM98U8HipNXwoQRHo/Eas4xNCMQQxAn6xLJeRX7TGNRf4IGEN+j9rUFnAjJQGJhc0dQjwt0YfoxSWLdAqmqht9yNTymtW0q+NCqALs3qBhBoRnPGMnCi5jdwV6/glNcwh+Sg0xXNCBJzXQeYnEylNevx129IKos5d5/u3TAOAWN4vmG/Jh5Z9u+Y982OLd+/U0pbdoWhrqobV+k6FxQjyygBHeJDmjEvL4E8PMr+DQE7Pth/3Vw7rs0epi2x8wCKThRUSKFAT1U68IU253YOGMKiIl19sULt4uGPrqzZ7Qif5AmIpugCmTEllU+YNDp9c4DsMvbcS6YWj5LqMhALngEgtOjo3m1K5ouSfTuukacTxUZPqVHWq0XY6DWRE+Ws/tBfOoR462S5lux0u6CPfhCE//CO+Ocr1pWZZEhBnba2en3PZjVPdAwl3D9xdGe1bvmmQjYQiKNE2GBrqgI3uyMcak3sFKLuBon6MKYGZf1X5BgDxgctx4XBkkIh1cagW5bD8A8DAnhqLQr0lWUr1g4wnYdQA2jlOj6HklX793yd7bqnK4q+7ub8Fo1PI9LoROR62/oqHn2wUGfs+cFswOCg63YyqJNwuAeFsgA3V7Vg+VuXaOv1Mdw+51RwpdW5wlym4rvQfGqEKjMZLQQQdBVqsHUoROCZRvo1v4BveGEsDWyelWrMNwI4tGiFlGCAOCdSrmmMkTIjs2a9jlxTGm/emUlvbyxppOo0T2a9q1cf8cKht5pI1Ht6LU5Psyi094N+dDEPA87XOx2pE3Oij/3yuiWibTfvRpLCJuVOWDgDwc7j1iZPuHuOR5b5/sFDqU/p2Vqz8gAR0yisFfJa1+SzcoNvqHgWaX3xx35UMqh3HRS+1Fg89obDvuvVy6mQx0/GBofwBhMPoI4hsBxQnGnRzVkKpcPblvsq3IYi5SBGivPdiWUzaqiEBfk5/xI8KEj5aXlMDtWqPaDwuvGU12UAGells0QjFmptVL75YnUl0FhWttP4KPQzSxH/SnDNnk0EQDfYGKaEk5uJ4ExEm7gRH64zYglCLH2EjxrcKucvH3B7xadYHMfA2IS3HI7nWJLM9YrKdos+VE1pmLwVtI0msl82nKySKuzvgpjcRMRB5ixveWwUbK9xSyGxRaHWQpJCYO9v5N997nI4PMNuFElX42yl3ykDmJljza8BqOLjnQB7q23fN8qJImbOJ5VY/39z1rxyVKK3DCYIVngi0lOZI3I+RFyqnrm46wzZaum2dqQk5uwgRf471vKSuGPd3UrmW5Gq2yo8X/IjcVDAqj0gJuEgX83ut9C5TfEVYAHg18yeSzKZcCRaSL3aNfvp1ZkXcvS+cXvCTqc5N8zo4gSEuIxCJ0yrf/OjlWRClE41IJjdYF/VTVWDrHAQsClZC5p4bZlfgw3tfN9T4wRfsyeB3io3cb2X4yR+f5D7uNSpxe2EZWLWy6vQbDHPjot7WECftusl3KRHSNH+LNS3fW/5B6DXirAB5iXZ3/WN8t5FGc+4TwrNytRx3lacHYuab3U+otCzZJLUfHZ2TGfzHfDcMv5a0ZLyWBhCYftArBtgHjp4u3PO0prdTMD62rmQiMuoCOPIJiLFPtakTeS93MXquYLSqAiO8ZFrJfqe2GUP6CzTSXLkhmBuTCu5ocGSiu57lQ/fhhUQTkUpBHuxWXWul7g8T/rVjKAmvxm6Rz1mYFreWdxGFiAiHC+Vn+VccgYZf1wf9vMzHt4SoxOqSQkHLglwsZfjXZYYUYZfUi4ik6NaDDcQEuGSl7B/3N8IBdh58GkZ0mpR0o1qxaZelVjQDR0M5VVSLJGFo9hFGOBe/M2qSA3AjbCEXbvccNwLIwBkRw/dtHS+vrdyde3uo7b8HNbUfjAL80ysH89cLd+fu23yfQ07tQPP8NKov8uyN0xSKp24QxkUxstbQ66Bw563ejwVvewVfHIisCTsnVb3OagjoerUmSsyShJQIUxc2z8i6tMKnHCTLP9w2r7M+T+rffp1P63xSCiqbVDS/sajc1Vrk15Xn8lTU1dFGJKycF5C1Us2okd7yqpNNVyDu90E0iOaXy6vKRGn0eTilkyEs0fg958VQaxbP9Yl09ezYOtPGe53JMLEoC8e2MKkNGEDL78MRfoNXCqAksXhS/rICPzNNxjjr/3vcJ3PuhHQsLuRafv2mfY1gGu6ROknqY3RHRqP892LQmILs/UZNrcORjgPgzt+nCNQBfNyvH+EElhgqyvqa+1iPl708Ol8e8GPTfpdVvVTNcvfhul+eLWOvCpADAqLRgDju+IStLkwDOcNGu5uYBkYrGtf4k7hEeFJDl6Prr+Ekk67PCh3S3iGWu95XysVw9iuxeWnO6qf+anhgcsUgKGcDSAcTJceLP3XvOIoe4s/utMyggDxjWp27KSt+invPqE7Pz1L1FpHZfl0ctaKkVu2vSF12yJbVKuGPp/FZdJztlXzzESfNESkGyaMoE42oz9Djz48/TCo1uMVc+gPy0G+TkUVvVCiNvnry4XpLOUGgaktlqYXvL+o+ADk9Hd4V4nS3phvSkSWInFSKo27avvIGwAmP9bABqrQvP46OM0Sanjmvqy4fQFiqp73z4fSHxyK5Tl+ODZOV0KCtCRjklLjiu8tky/0U0Y4+cuMqzFtj306zYdDyvKFSfFtfrzhvFyiBpsB4MERd6BjP5a8nb1CCjW8p1Ca4uIPZLcInpcPWfY7wvJulyQV2ODvjvXGQ7gigYiGSqvpK++aoctByxrxoh9vzFTh4u2w+hOd+19EipdvNBlRwiP86IGtGBT1UttqxK0Jeg1xRUM0E1G4kxYwwjHjRPfE3PoFiOO4zzhOCbko6The/9W3OmuFs0T7ueH0Gn098ftCYtrLlEXW42TKimzIh8/3XYR4zEo2GLQE+re96OlAltpkrydgIJx7ZEKB+otlZ7XOguCFVuumqjiAzUdVEer99bb+r7dbARxWXfUJplxpuVVcbuhYHEKMHbh/QjJ/rN/Dpb/tECpe66VLIt+6a3tH3WCEobG/NgbNVH99d4kmhQv3gC0tej0+HdV2kiy4wnrUvfCTeAVBBqUmjVBNyap9pF0tU9PwGSOEKk3Q79zIwg2pILjkNjqf5EYgfVeX590oMOcOkkkD26JjvEcMCANDPM3bZr56Vs5VXUxg3GQcfAIVk2/jwtf/GlKEbqt7tlCvXC/42xWzdBhUzMiSBA+V8THuc6hHidMFDhyYDnNXksy/7c9NAmqpXfiDA9VCc0uY8s78rnyhcZuRLO3oBR9S+C/nFXMOuEbk1uZC+zeg80oQ4q6S9DTS5VcHPUWhQVGouOZFJ+EZp6hrzAjffjL6r8pPRyrKLiYPQbruqsMow2PtzCwjzQx5Xwceznb2BQkL2VDup+F2f055mlXJv4FkrAqFWS9/A+s8I5FlplSTuEVSRlnNJfrzxcpCvz+esS6rK+8M4UHWblPt0vI/56S+Zs3BAzx9JKmBSuzTJnvtjeoQN/hp5FmnWCMaIqrq0O0b+HLSItz1mysNkPaGCSN3ZKHiS99Et5AcI1+T6b5GnVbxY3k8PU6npCjP46ojzyh/iA+DpL/TpBRJOPMK6BZpQJZPKEpviFA3MA6yA/lOF7QWp8fqjjatV4901CC3hp89hAJhGvbRG3EzOG+FxWwvSHi6Tbb9+hZMjnM2GSorlw6CywkZENdvxVGdXDkE0qwYeW4pMvOK17z+ontUaT4WIwY35vvv0Uje2lO+iHXvizVYa2ROHuGxF0UBPZ6leC8MePTgLqBuxBCo9mF1c2K877ReRnLrYcHu/+ixbbyLuMTqGcp3VIw+BRwDTyVDd4EERw6015NAeXOVeaBfXU98TB39ljbmXBWlAwQ2sLxGMa71vO1cq89kjc2tQGmk48SC8ldwT05GdqSpcaCuNMz0kLi6Pwux0agzyA9cXS0FtoFTiGFxSFJCPFUAaBNzuH4ijXyquxPw54TCg2UWdtPgMku+KuonwmRbqQDbCxIqAVrnsQcKyOojcxcbPMkS8UH3IS+lastu0N/u0/lOSeuUVv+H/zggrwCCidPYyR8Au39Eo6ytMaw++d/zXkhJcBN623Rki7z6b/94cKtXwzBNyaFXxvG3gt6u/n4fjZyTu0hL3OLbVXT6Xt4OGhuHHSjAbheyFzXJe9xJcI/3aD7e7fjMdr/fyPXMOU+6XVigEOmcstjzxWAc4wzfQjDsSr7ZXfL5Asw/QbO7rLE7BWDdlW9uoUf5Yalo4eQL3zbuXCwnEuiK+q5Fmsomf1vAb/Dhav5h1OxPPOz0+adnya47mm7J/X+rBCNnneiaIkCCm6eo95fFZsqv4TAETMVcKYFGQZZGiqeoTSmRIRcWErC30/elaIKDe9KW/jPB1/cNFjELc4OxRddypYAGxG9rqiazUDNuJmJRE79oa+KPW5oFFZ8otT7Bk3zt8sq5IJgt6RlGBBAbqpllB8fD7pZSw7pg11MCfCRCo6I+G45oiJVUGu/Ov0srwEFYS8RS8sB3fZ/bNCwm5YYIGKhw7AslX/Hi+R/0VgO3OGBCvvFmnn4DjMTMTtbUdpOejHCeVhb/D/fgmrTctFPkjBEQqUD6sidO/uCn91pHvXycUt/7jYAGjz7YSI7gNxucq0DI7nR6KrZRvVsUTgixb+QBNB0mdNcPXjZlUArikRH2AJzoiSs4cXRZHEAIgAOwHxCpZYyU4Qllk7dT0MvCV7mjlRk4HfE6aszBm9hY4juDHQiIG3ZLZ6LpRX1U8wX0WXT/koF39cB5ZH8E4iOk1tv2wqwQgiw0jUR0gmd9Hiu2fEtbnD1tLXfb6ZxSlcYNppLyR6ld4+i8xsVkDAdg4CSfhusArzDXvDFPFGjWkCCiLTo5rN75iWfUj6ARLGSidEYG8Qxhsjfx6aaf1pGQjkjl3Owqk5hdeqyGMaBXMNrq1BuKrmpqCVD/CIBhSkmLZMd3Ojfz9B/QD2mmBpVXardvvubGSOcLaoP/CXOVq38yxDlh/zISxiV/m6aRPs7/MKZfafbh5Qbexg5PjxvlArCxW6htzj/JAkYBR6mVWxoYrmXGxY1qLzqNK2SpSPWOIycKmy3S/Kd04McajZwcv8fT77rc2aaROAiQGj4cRgomz8MzA1AkOEk5d8PlZ1PoBNVKirzS88tplXG2MDvOSxx+RCVg1P8O8OHzYeKE8NDkvaHE14QL9Q+VhvqpQ5Brvi+ht/e22atMlbjSPcXUxSA+egnN5UCIQNCUUhDqDU9iRO9H5TY0pfluCWIkX9SDJWjG/py6leTiCR/Az4uYv8WjEg7FuVPu6tJ0tx/8EXyZrj47wFQUke9Cm5VgGdQDLn9wvYzmQ4LPNfSKsE7RJsPO3y08qyH0ZsucKohaMb+QuezV8vXOMJu3YCoQhdFfXejNDBMdN50XLv4Lw7m6IVKkyjMX6FcmQZxCpC5SklHwZoVfTc4ZyvIJF2F4zCWiBatFyB6Kq2+ZDZ+C64zwleaC1mbVnO/B7jCBmRm8rNatnSblbEwAPnZAADATWPLfACAMzC9NlmYvs7/oQHroNGSQ6/DBJsxSRxd4qjzL0Ka/ABwTaT050rvEzbvkaJnJoRUwJQyZwt3KTFaP5DufQz1Cy5pOuTnAWO+8RC/TPbtHziumimDWI/Wi814xNYeDfmFlKpv05F6ZHbWSsHleE35Txi069VTO6TxOmiPUjXCM88Xhpg6wCuiTYbcv7kVjwbn55HDWcJJIqiMZ6lYGY2EzsA0HOEAAsZQjLr/VWmHl7XJOVTSv82M+Z6HaFPw6rq3eXFLbcsO8S5MDXHyGLOXPT1+kf7RWsSco/DPdfOJLpn6HkIWjex4lcgNmeB1flGUGsCFWENFiJYjO4Na/Rq4yKpj72aONN0vJmD4VsEgZQWHoG1Sx6E1QKiowkqBd1AY+FirWzXgg6IIuZdBLGZj9AS0vLNhjsSpm1ysJPVeKQ07TkAU43hr/SVgmkP+bEqt7EvDf6qt+vSfjtTtRWohVkOIRthVAeExucAWxiFcQ7mw7GxvPEy+qWvQ6X5+g8IA6VDm3k9Wkq38I05+Isq3g/8wl8yw86mQBlej0BobpyMnm8w98TZum8lhrGUN5iQEqULuQv3pbIJggKr1ZEN75Jw+6r9hBrWlqCsi6tip9BZn18ROtXgBlWXBWhTvpVWITIeqRJnzRhLENdOkzzPdIjintcW3RGuenuiq8CXtkNFziS7N09AMSYGAVO3k3JdnYKDcjJCK4TpYH1mwYlkB7ZgHvbsN3bIfyRtBqXK7+guszqxKh8By+pZkrY7tVdFrVPUVTjj+ExW76sTqCO/d2emsrMmUKf5lWRreQ1aqQ+LrwjnbnjwxsVP9XjCL/DpRTcKdmMR+jFu6THsExm5T8JNZkYePKiAFM3mBsCwNGh7cSc1ockHfEzw1qxLbhfTnqQRQDflT+Cz7pQvFzWOC1Hp+8tQCsntASsHby5MEBDy3Hq/VGPsQZywo9xL4argWqkYxDEuknuTyt8av4nysnMCzM7rvEVeCfVmx6CNgGLUJ+s28N+twhNIkWsHtQjL2LHZoWuRD6/yJKe9Sw0CrUXo3/H+APGzY+bTbLCTqaZ4sgUQG2UaiBHUA09cbF0LvHgPNbdKFbgB7Irshszkn4TzQo5vmy87PZPvziFKezDgVSt/WrLXlU0rE8ZK8tI5iw9eVym3Xwjvkkmfvk+Dt1xv9VhOquMQ1atFOW++Vsr4Zd7DtlmKaRNYVZ6D9o+7S/BQhONXGXqX7e1e19qWQJpZr0W+JUPdr26WXMFyKZ+AIKiOrKZhE/5Nj38LUPVYROmIfJ2+nnBackGbk0aI3ESHrSRQD8eQ/tzNQP0rAek9kXdVw4Jj40ubrNm3iR1uRQaHuzoiLGKlNBAdTZaWE8zwyzfjLKibLoB7RyqTPNjk0En7B3kHPN+uccbb+kSJLmULVXcSY0zcONXhsVZUrED2g5CLr8h0SGUuSLRFAcc7MpjNLUTp8k86oz5Ru1kxi0xa2IndwS58OV67JgteAdjdY2H6pzYk4L4OopmHpj5Wnsxc0XmweqKhnuICbjLvST6uMcHA7zAdY4vd6ptn0a01iUTlnOKHabgdalO+2Gfh/v9MfJr1spV27nd4R8M3d4hOPHLn/SlPiKjjz6uuxs19oiNthC/cBGp33jGgFvYfTf5zp/FyL97Pq+QhDemMBdhrC/V+3d5RgiDUqEJm44USfbWuB6WZijosqjr3e9vBza4j+SPAVObHxlLB/2gxAhSB3dRZi3jc3ovYOqDnyDpa1ORDL9+mEdPXMf7qX3xURvTOZCKMFsSp7mtVq32Kse4QJZPbtMoUI7dWZbHp6AzyACQFKQAcsM+BP3BkXw+7neP52qPAHK84Z+Ke/L0URZDvKpSCNAOe53RUHcHTJAtJ35t2nYfM/qW6BCotl/1J8Ak62Coun3qFbrwqJvfV0TA1yVXbkcZ9kAj4GT+IswrVFdPbdsvnMwLpPSpBu+RyimyvDt+4JybKFesrGsSw2rrBN7yy4e6P/bpiG6TIZS6xCo6FBzfVaj97CkMR3BIObiDVGkDjpg73fRFhJKFTu2W4uel+41rLV/sUSNPrvk8sL3310yHPH4N2ycK5paEPKNKvOfhF2vmrnY74A1I+jMYnFiE0Lzt+l7yYT+QrYIutl8MsuMmn39yDH+PyD5HL/TP7Xt6wVr8sivtMP61B3+XIHf+PpaGBlymGfcOh5Ia9qPXmHS4FIPejDfspO/pmT5zUclKPAcm9mPiJD0bwmYbPGquaYqHS2I+1H2urQeFRlohys9Teq2ANlS6PboLKcQEL9Ioq/VBHMCZGD8UVn4umtHsOCU4mtgmAK128RbmT4rKp0SCIvN9liksAWXMp5vMPXK96Rnl4IJAOBHk8fwHgkuL9TgZbP1Ib0ipu8PkaI466uC8B3tqeIqSE05Su+lDyasULA5sc9CCh4HTkhUkkQ/XOrdJat3bGEtJoATrKUF5cFgNRCriEEqSOz/B9k0hJLtW0XFlfUJ0dxPPz8gF4+bohficneFYTpuQ7J17yLIdUkwpteCk06SzjL2kzFwvmrZZmLnUVdTo/eFC5/xIAw+sHN6nR52sqDe0xGHaaBdZZ1FC1x0GHOgbqMVo1BahXehh4fdOLQ54fmIoo1S5a5Pl65buIrYaESsJ2rxH1kOFDzxHUTmbN3TvSdjQJ+o6LN/YZ/qLJIcJHzywGFDd1dPg7eUSHTVuFI7La9ngsyunT1MicJ4KF/z8UMqMa/nvyFsjO5KmI9w7mUa+Xk3Y49mJA3gys87Vp0/TC8ZTotcVkoU5bENj4LB3eMWXP0VSuV52dJGWIW8ViXVBeUSSYAsEfNJfQLm0jbWEWwAzx+t4LzdsFEmXUTohRSKDazFnMZ3y9yIeGIcllUpnxILDgatxipWvLNbFIs2Xbra9j2wRNAp9Ek7P8AUqJZOeCA/LtuWR5GTJ5rzh6jRiXnpxgScVrvst26JnRug4RFoZQVWlZm93LGPwa7BbY5q+Syxn7CKioeRhqRKj1v6jZJiWec9YHypXtb+3vQFspOwP+ur6/nlSerH4UlGZ3lceT7COpeDlF3rsvKuTR9PmXI7sA/7vdzwg+LSID7wECzrRyVecJ341NyFYHursP8h5qgAydMHHvEyn4ufx9CWCAorlUyunzdB9/fZONYJDkPUQHWFat3eRQmD5vbTEudGheHPzAbXciZlBxPBNJua5b1XK996kweYyiE6CXv3IXhi6Px0fo66JGV0hJ185m/I+kGUVGPVwQJSDBsl6tDu+frQcSg6Sk3bAWpbRFLWKQDlnZ6eY37xphS8Je5eZXdbIbTvioBYDlrzVpirlrFzjMwEx6uZpSvSpTcJUMwfwA65BpJPLVHkdMe8Y+c5/W4kOySbC14h+sR323qUTqf151ShHIzG1blLzVsI/lkCnePSIC9WieRXZ4qzKKM6dkdvfv/Zhf/tIOpLKSkmOv2DzLueeuFb1QPcSWiesh4l+zjP+56iiJS2tnhBxza+CgsB3f/S8o8+RBvJIH8NOsn27W5C7AtNtyFN7PbpTFd0ZXsD2u6zn0xKDBiCnsmvISml7DeiRlw4JoIorIRHsflO8UBB03aXAidfLi3zRVyWuk2n1bIn69bkca+I2+yIjvNOVw7ASr0v8duo+KMK5YttppH9FCLyj4KR87Crd+AFAEuxxKI+1aL3/QJoVYRPLiJj/KQS35QpFtau7AD/9oWbZpkTM/TGqM0rtmmitTqGgBvuCdgYGCo09E3fhAnSy+nsccD0/XRR+pPfm90xOlJSxlHnju18L/D5o75cwUCVKOAu/CJ794kFMdkiKiIohvJue4+gH3WMDMGNBvHyu7lbBRvf9F9AcV3T9ELz3VqIFLyMeZD9a+OSLiS0hP1DsAUIlGxqYadJcrpZ/IcTYI4qmeQQYphbAgmis+I77yFE1nVc79bxiuVbZxMjGZCEnEDduI9CvkHbyiBHGxvRg0NxpVe/+USak2BccTVjBZcKJ4hoYHYerTSuZ8jT5FEeqXadfvtgsPRZSlW/Vj5GOi36WePaL+krvQ9bLzO5FyP7IP9kH67vsqk3qsGfgVPEVj6C1IGtExKchk7OTqaqEdkXx/BU1dEV2SaXWhkjU/AE0wg2GT9yZZWxqbHpOqO2KbELd9gS69CYQHH/qEKTK8DOHHziDI/VKHONwjc4DK+T8NVv3c5H0ZwxxVhOjNUDKq4jlgp09U/heeSnWEBQhLnfiKAIwnVhvYzdvxJT3ogV+n4gajo6Ln6WlTNs3TguOYBoc2g8wjfMKzcqzyqyfN53ISkixd+aziruv3n1ObWTInWheb1vs7oNEFu+IXh2I/jld5FPx0oclGZyi551mrwtpvvkFpNt31c7PkxQS33n7u6+c/UCIfgwpbZOWJRgIzj3eKppW+4qgNFN1oyAfaijJT/S8svZE6DR7BPBzHyxbrdM+kw8rqdDLS4f7dAL/JRHA2lx9Lj2sJfjqJQWzcbCR7tLlbw8R86zzl4UV2WiP2oevgkx2u+CmgwdxQVEygYwDuQaV5lhuCgaEUa9Mb7lcJDYq3jnyEqQP877sSo1b/9ytGrSKETkHhYK1dfYL5EvK6av5Uu63ykMHQ6CbQGiKDtw/dFtxkooq3ONz6nc4X1uJ2m72tdgbOPWXGLBOxg8uA/G3iZi0ADq5/Q5ojT56BZD9yArPx3GG8ARhR0EqDO8uW0l952zuCYORWfx+AegWuUHneNKOQTYmLrN2Ru+LjafcolSnaC9p2cPe5yM/PV9KHeC1jwVoY+gfmLUlm0AhAxs30XxxJ1G/YcKm2D5RyGn82EqNPXMxe+6Jv37eYHnwmhd2y9/iHdUyDkTyrgjla/LpA0NyTHW4e3g0D2VlV+VFfaLHMW7nGBBS/OHRcjW9kpQW1nMq6D0d4+QD1ZzRucIFS3/T65AlNCiaFXkuEqxuFcQ+H1Ci74AtO82dRD+6Y7J1D+xi2ZqTB8L08kdeP6nzMdp2vwiJ0BBEc//+XRRSGxxgAGm7Y0L/3G35FEg0RM+hOT0psw3KPMR7PpMT77u8t1fWQtSI8gn8Cx8P+dKK8JWKoRNWFG1dPOsMOzCslXUzRvRzTRl+82o4xEhdMW/wc/9Muh5tputgFd6UmHj6bhEZEYzX4DMl8WdDWY7nye/b2rj59kvxzjnfmwe9PU1CWMfG/NDwlHBIVl0gg7aJJwqNRkT39UxXRNpAKqN3OOmHSQIG58fshx4uoDp8qP5G8+UMs0aTESQNDA7g+Ie+pshOQPGSWsN7zk8ITQEkUxbkddzDZJ2ExF715sOpiyvxmz5CnsqsPAEOAWxzk4D2UwYcjVPNbOzW15Oth03atE8B5z0+RP7HmVyX/akTDY2XgE94zfY54P391tXGBEwU+vjGs9v6sHe7JXhYN2axsMBYNLmo/oj7x5WtIQi5B+0Qz6e56RgA7ZOqDc1DB4yfQyJuqfCYqo4JQ46r65ibzby15a46yFA/XqWEi8Ay4Lv1JfwbmIwSbcRo0FSFFu4iGrllh0l8CNdiG9kdOFrpQjsnqsB7WkP24V0et+gLqXLdavJmoWmU/FhWbnQAJx918a1OJKGA/mxUZekYiFK5tMTviS8KSZQ4YBpE/ODhtlAo9QugsMqbYDqmA6phVRqIXQ/6z1jFnlV8f6+vStX7ZPFwA+l6q5V+0nWJEU8n+W4/Mk8Z7efXHMERr+tyH6jV4G1tHLzSGMB1P9o85+gCjVH05WxPVEHWHkPis0gO8PnxxiIv6vK5WenzjUEoUpXMiRhSr6NjZ/TEADK3KiGU0k2L3+1aob4xVAMDNMGnng6Mo8Kizidv7D7W7B8FAXVVfR363L8b1avJfskktvpfwD+uTvlNm92ak32Xu8BdxvLztpE7EWtmEL82oBXnajTDS5+Z5vkaXDPEzngEMx3ybGJlKy6zsj1LQiZLBunM2cy/3F2AaMdE5RQUfqkUEyfkWo8hYSQSq/abkREpfYzrW9ZDvBUwgCact1Ej41xk002bODpfwBT+viudNIzA7Qje+HHjUrLHs1hSSzl1TofQFqmqD6j3VTzwuicWLZrovghm0XYsUA65EURhzHsmB4RQbQTwILHwiSPrZqhfbiDfuAUfPx2or/I8/pvUhNSaxxyvPjx8PF22sgdrGac146qn5THoJVO/JqIrRR3dOtS9bouXdgo3fiDTIAbmTi78HX4nL5n94vDekrXhHB3SvjGdFyIMufwAcf+udDKRSNO/9t9Gj4NvlyIBtFEj5y3xYLt/isOy3wXc2sSFLxnv+mwgryy/cZiFIaYA/PyeEtTotGYvaSFCsa+8FeuOULeBEAx6DKDZV83a5q02c7WnmIYTYNx4AkAu2QhgaJz/O6KiT/TCGxy3e4af6Y5mf8GTNK34zHKhB9WtTW9BmTs1E/EVYKMvyW04UYOlZIUF2HKLXhGgaNOg5hS6qTz+z8QL1n3qGsOKH28Db6GJHsUZsxtxY7hwdkmS0OeiG8zk78mQdlonqRVDMks7wvKjmxnSJhoh3PVWe3a8kekAyFSDZUD1c4l0Qenn4ulBHu33Yxf6ilXB6sLRBcQN7xYEYgATzYx6664sy/ViwNvF53su3Q2ohNNMprWWt+d4kT3lJEc4fhEV+C/nICcJmr5Mjy5fifYGTWo/NVlWjTG95xRbiIxL0O4nIH86mn+MSfZ6HfveNb4uFi0vi9HlS1xelH2SCW9HRMeiDUgZjdz3nCLog6qzOjocHaB768kTsC1Qny3TtJ90/2KDcE47Amjz4cJowdsT6TFQqA3oq2F5IaaHjR6h1WmD0SFSAdDo7tdZZP7dS572B4IFXWr6fh8Dqygw5zsb4SSQTm43OOT5bI4PdYcTX2L/CdUW5zTAdhAzZE6r+VsKCb3SbTjIL5UxqQ8SIdtXiTqsEFXp8RRMd5WtUrigMPbppwlpfVLDF3bOVP/4VFWRMQXyrKskGBN0umbve2aSAKniQLaEvPpzixtqIw9LZ75RYwMMB/dQ4FmtVsIrXRXE4W/Cm5ziZ82SnrW9jXQIxIzy3tFiu/U2dc+QQK8+O+ZxysBq+J/MJdBrbcrFdpTAQ7osW85DntohosyRqk6xvNECn8eGanWQ5YAgWbUv7UCUG3DlctgNP6XT3OcEjUC0eJi/xrfE2JXRotdyOFoFfV1BJ2jVvZj5SHs5Nw1I0h4rWW/LHcDpZvqiGEXm0WnvyMrM6PVJwLTv3N0/84A6yjYS+ipPQLBFzTlTN/yeh2incZK9wT3qwUG6v1yOqYRByXWcj7p/nho3RMC5ajFlheQ7fgca0uit1oU4+gZmQj3iLb97+htRDkHoUU/Q+Jp/jfwsZDvf47qVn6zQCTq8Eo598CjEki/Rr/aSD/v8y5tBaRi41S+TuN4yXO0T7UKxMcGdidRgJmAX6UxfL78b+PAG1VHxDd1v5ZcSvFh05vBCO7av401EDTrUPQnXGblUhTE2XkB3m1eg0fScw8Lxv/XsZkFcm5WsjCm+RQ3ukzT93B2uV5JtYfrmoLWPQ0nkKqVdST0me/AiIP3VyOEi+svLHHzojzMr4DejJtSqzPeXts/rTGL3u0/48ep5Dk2XpKTQdqxQE+QfhxF7RduGc0r4Dex5ZFP5pr110RM9JYAG41UnIrBFSN95uf3Fyx9lYip/Nnh6l+t3S2CGVANx/ECGcSSps8MQvDvtfkaBe1XAN3bTnVRCJDqKlrkitF/C8QFPPN0uXXsLkfWgmOREbYBZsxgSNscQVJ31xRvgbkwq/gRvxQWvBRKsZIekp6lO8EnVE45Dj/75iQlF+El/T4xDFkk7p7BSra7fugmsCtXvl1zbyJabVdICeG6WFhVYBMr+lNJPhJGFeV+9oBqy0V7065TCCDW8LN1pqKJCY6iJp7dXSchu9KkE2avAL93XiWpc+Kcq/bhtpcuR8C/El8gBK+A2MXu+lBKN21bczItWt1DHB4I2vkBV3tzT4cDxC+T34K+ejDQNzMefa8OG6IKGwm+G3qMhc9S8pgJEEj5NvZeSqd+fhGBpOlJR6bo9JiTZX7MLRytqgpyNP/I48g4uwIZZoQ1N7cUDuYfHUnRvJf/F4jMBRfehyR1MxfY2J/zy5+K5w17QhOg6Jm3aMvO+t9WuUTNkNT7bfbTZn/ddJn5RFC1UgOwj7tuGL6syMgp80i/1k3eNf/jMFT3oB7PUImgEhCMWTyerq2vdcPZeppA9mj0QE0L6IB0//xIAdWGWIxCRyl+LxF7VoBbcbQAnrDMO4cqmqBSsDEfbXK0yBx8ZY3ByklVJRbsbi8zIMYdX4bNM3o7lux6vXWQjcrE+eAo9FvBUAC7tqpn88NN88pMfozxgAlhyVTsZ0UFLJwDCNv69t/QckHDt1K9z24scu60Br/odXnGn1G1HsJv31n5VdfgTrHU6uaRhgLyZ4Zy5bYYl45U3up77O9toQd1aeihe/OGzEA04k6H96mi8272zv+KBmmCg5Ajmjz01swSixRpmqzmv4EE6mWnUYf6Msd6jzf21Wr5HE8xsMFucxqHFDSKfMWEGyYNdtd52isOJaojc3jN0vxbhkohyC9n6YQDJdtkLk0bCrgzZIPHxfZo2qs5MmroEyv428kf9AhrLB2wU9srDn4ZGg6AS15QLt588AIdA1BzoQ0oPI+7PG5dko8Q2dYohyBfZtwn9hGOh8TN3PZnF7j+3c68mNCliUlq/4iGw5r44NsJDoj6A/r4Ks/8o+ZcykylfhZa3lgOND3gwCQZYe9/khMBeYNC21VKaHrN1ZQFTSfsS+EbbFOh92icqsErXPjmNeBoc80lxq7wYI+eBqDg1WqU56Ij4aU9ux7gQIhYIPlGgblzrJSmcAfKCA5ucSMWAeQG5FMvPdB5sGR4xtlA9iUlxqbrJ9zaIs/Ko+W1FQsNWretTtJeixf2Bf6I3EKoGkw2efrHtEi6PlS13+njbpWlgZ/5Rdd3+tFehpRg1jfWai8CX4O++AjW0UvQDC7xSfcZTNtm0jN+7YYZch3I/9HI8GQbSc5IZHqPgB6TMssVNNksxz5i6GhBymQ2BhPeGXrGJgxOLteYmCOXQ5t1pW8fkLTabrvCXeaKpwRE8nTLTHt0w9RaND+woEAwhSzKY7PQq3zv2BAmvTwieDfNVF6BfmD+P5sLXaf2RmdnZm5Uu6QUJgOQSiTo2R0fBuq7NkJXeuyJy8t+tsvMJo3broN4pc54VQCaYM5mkTLtJPvsMAYy4Lbn0q9mWAI+Ai9IdtjuiMx+jn4qvcYr6KrvM9WHOO0M2Tvyy41MQniHxpWtQzGXctpNh3x7n2PVHPsFMX2M8JzRylpWPtQtC1zcbAwvNmJr/9TtP1a2FdzNHXgArJTHg9nwaZxWE9uR5EJ4OozSmLs2PNH110HAA+unfbDocN05JbrfI2lSdgXe3S2HYeDU80eH3Hg/Pk4o/ak/yqHskoOQxiJ6PRdBUNjmuge2wWPErxhoOmMlRvyXIqfTk0ilhWAKYOsEHK45ypH4GvTO03nPB4nXI64JY8r0iW9mSt2+CbavvaMYiwzu2fXbTTaZX/EiUhVtFzKRPT6C1VO3K6+DIePomkE7iMYhfkRO282fhi4mYtc0We1A6BjPaH9KE6rbWbPk30em+V3ay9KExQ9+mzKaCFNxYnVXgUe+O+oBz8cGnVQ1dTyhXZTVess3v3hCHRH9wNADQYbuPz3q0yjNO1k8ekDW93vdbcN9gsK6kFF4FWCPM/9fYdexMi2zJd/m3dDfe9Y6i8BTej0YtvPemAKnf/fLdO62Z5SxYpMhzTihBJyKqUGYODAy+9qfRbXe/owyAk0vfRVeCBLV486GJybbqYgr6zshscZAMuMQhoc+gzLsh8QYFEcOw6okF4qGKlsCI2NgO7xC89tLet48kryl0Bb1c7y+aLuI8s8aHRb5H2mXlhyjaKhnqC0oH26rgBBTroQgDiuc/GsZb0R1pgDfD7VJGMiRGpr95N+rGui+zqcZSdMMVEiIRnI+g1pEl6T4qh3hV7NtE88Y8sy91koRtSktxZ2dh+jp9cSuxigpwPxaagnrFg9+K8IEo64LFMZ6YyeUD85rF3W+hraGvJmxYQ4eVeajjRGTNbgdcQMMxkjt+2kfyRnUxyIkRB17UI85rYS1wK/zmhXqTX4EKGXE3SpSuSBKqdc/jrb3o83vKvWbw8Mwn4G/yaZrpxVi1fkn7z0mOIzLcNAmw6xKw3p6zsxASmw9UlZi4z+IN0auQ0SpKVZbp6zEWzf7CNx5az1ERv2Q4kTsJiF0TtwYKIM1DEerEtm9H32qg3d7YNYc4lvCP8OD9YfFhjIYWvRjaeS9aohlGshTEecagvc8zKlNxafAzL5lUyQFM8PhOnhIcRPC6qy2qomYefZlYCnW+jJl9r7RVFlkBCAg3gsCy3GReJi/jEiHjJZdT+FksecwQe9US4xhShibqXmeB89K+XY2DdegLqQURzCZ86aDni9SiXuOjU+AexOJ6xVHWJf3dr6kT0kSyvlYWoX3OzT/NMwZZL97Y9x1yXiH15YWeWhG5m/28zF+tFLxx8wadJygXIfXMHGY6bW4PpJ2Vh+ULYBa41RV/wPGd//kIZ90fsjPDbzVPdrat/XVzvj2omB9CCx6YH7/57PEMNv77lAmuXS4RLyAZ8RV2zGXMe6v6MH5vq4i3dI6VJvdf1AWCn2qbqs9D0rRm4JyyzgMsmrtvsuNLwVZPcO4yIEKffJT1rpITWDfFZKIBMAFTCCSi4ZmE9yUcwO+KXIw0EAF1TvFXgyHatw+Sg26+9scMIyj0tljtKxFa77wtD+jx71ja7uhxWbl/7FeOaSIMPwaJ+ix2Hqac69LAFFndthvM9AoQ5eggcYsJRCROPuowtZ3Bj92TvIVU090apw1/tHagDxPAMs1Y4ewLFdMqqkFTUndXFIKhXPGFMFV6vLovOim8qYICgvhyIGg5FVyiIusOIqOl4XzwZEwQH60qgDvPCWYDGV9R0jLuldTjHS1WRLtqeDJsHArL6ZK6+szfXpdokHtFtEQrI9vVVqhW8y7DkK7KgFs0WBWMSvqZx7oKNIIFxlkZro+VYA9Xn07UYHRFhW8XZJ4VRiK64FuKI3Dq9OFAO9L2Bnca+FgXAidVM4rovn37n1/EPTCdEIzlWzsn5YjYcUl9mFJWiUUr7PVQuUTNX1/s3T/OmfWH3u6GNuhppwVHy83WRx4EWUVnBi7twtzj+HtR4UGVAhl+We305n1ugVAY0zpwEearhip9KAjD6DobAVXVktZlzM+CyM2BdisHiILmohSjepygafCuXR61N5hASzLDYLEG6MpKGvGRgstYGYpWiwMHx8B1hwEr1o852HN+Hxk4MLA9VNnAx0cdVtYVJqYhbFwv4sXCoKMp1T48JlnHyfwohfwFwI9MBe6I+3hYutJUMCcHxhqIfOoFJWmbT0Hx80ycW9c6hzZciUR3DJe0Nnib7lRPuxDE+ZcXoF1YoxbKmNXvW1563yJTv6GQgBlLkWz7pWhQTsFRRDS0FS6pXe3clqo9FjTNpTjmPc3UWFal7ZfksBp4MaLi6/I/7Ep0FQiXbQ0Yuma+sKBrKncE1FJSIuMcrPcZQfz9XYqOYuVZmS5deXn7oYVrCoGpYY90FcvxGw2YSt97CI5q0iPOE5WD6qHc9hLAb9He8e66UoFveD9jiLh/1WEGQ6b3XpKZoFOitIlidMJM1npJdt7yauURqaKSwytrXvCiSlhFzXslWnhH5Dghs+feVWSSvpxSL5eBrJR1TzRcDW2jmQQca07zRrk4K7nooGwfBHOH/X6pV7KqbH4JesILrR/I+1LmkJgubzBVaZenfzZ/jZXzvTfhIxqhHUU/W3rZhNfGV+MMQheOVumP3xSwwFzM+KyR15bqhZV83D97H+peh3FpXEJ+Znv8xQ+qh91CfjdYy7O+BxPvu+66LKVYIoLyACDizVU36HRDUstxvkez7AUo3NZ0DsDARZh7I964ue2NPTSZZge2R93trN6fO/sdax4dYbZAlvLD5uXq7R/iAG9bN22nej+8Ip0z9No1Q120tgMiL91CIQ14dgr1JHVsPmaU+C6ubESn2Qey8ftwMpdO/oKTjFYQU+y0L3ShPXaIb9Nya8ssXqwc+fZ3XKO0GphFB/r1i5A8ovHDTWz9xaBicCxSlkA+SUv5BTdKFPITCMl0gJBPj4L8d/h5pV2rQOP+KN3JOOr9/bMjMaegX5+HAYNDvzv7yrDBPUMzfVRp4RHfbNDGj6vKdrn0n/oaGc9jNda21unFo63RFRVruSIQhI6XiFDb50xlayoFu322TdgaJ9qzRvobnQaXQNULMWmPGgyEkqCPMPOA6T36PQ+sxcoOK4BYGVxXqi7eUXi2EVGu2Pw9izXlB1Lcw6vyXUCg1LPn8IsvoHTXwuL+6Cz0qkxRwNLcYrEbY933un+Ay7N8nkR1gizR4G5msHB9sjRt1zOIb3MJ33qyhr70eMbdpqTXE6zikTOPn8tYWfyj1K62AgPv2KcIeE+T4UXYWIHqciDal6TwMolxfliG+GB6RMa+izYrvmCJyvtbZFSPWURxbVi/Oy63IYSwL6aal6Y/Jvb1aY+K9OL7HGIS7t+l5qQi8YIo0mzN8aMgxmc7VKhyJJckCRlL4gNmXf/NZ9/b3og37oPJ0B+HDNcQtm4cz0tlDnYXlX4VT9ZwpJMeDcSpnrKeNmOWXhduZwOOq2mu9NPZO3r57JGl+sj5CGJAfRlYatM3S0foZ9ZJbkm9vQ4g6gXx4+FcgHgKWPPJ0wXjmhC87oo5RO6zk6OY1Icn2hE1x3BV1cNXNkqgbWtPH/St7NssZMucZcHl0pRtVaLyY+gWKdiSHG2fOD3zoHJ4Ms+TJDKyZIaZyC+qNJ5s2X35y4r2AnroS0ngGQhfhM8/9BI3RhOnKbRP8FEiOhGqZfu00fp7dkk+5yoz0W/XwxBeHZyiKPJ20qGuosjocgUTfeQy4N6PYW5p1oheZhEzGxGT0XR3FRo+dMsX4fvBAMtJUUsdTNp6c84npBM7YlTxN6gjYLl4rjLPYnpN8o0XmEwlb6vd7DVN0yB290ALxZOgqLYHW7o6NvGRNh+Ejq7JWbNoJpWBfu2LzyCPqJnt3NI9VeNrag3ZPjyLujp5pRfDwxbnAXMQEi+IOzqlWDx9nILzQsSdT64p7q019u3e+mRjisyrHlgC3TVwOsiv58lkD8sDqz7Ei8rLbf4R8+91GTI+dnAUrAC3o6S28l6vHJSU2jvEoCT/1fyYol8Y476B/QG36QeIEZnyugqqQCCHeAq9auCbGxJ7wfO1xgTJy4YeyXYnxnszKQJtNyYkxFAnlRtxBoiVoVIv4VhVZDjj4CI97+N0E/zLFaPYQYIBdFC+lK8jxUvXNWypgtT8A1nxuuTn8qGXLKJZExBQuBpWDrgfV78ehX5GA2A5zRGlX/sWiZxU6hego6pSEXO0tuqZ9BUFirp74RKcNKzLDJfw3qvbsRaZmoZ6oVBJwV3SOSJi9gsNcy7swJoG7Ut2uyMCvUaATIEKfJhIjzJrWOXSO1scWjSqVvf9K89pRpDhUqmOPycgfp5GCNjS8hWK63wrS64qvaM/zMbAT0fuYNjCmdbed9z5gZfappZjhU13fbVKGNRq2zHHuh3BWkXBkxJ8nn6saj7S+IxOaxyLRoERKJWrnAwQnfEeBpAwO3rISjchSO9F8tHEJ7ESfdoXinKJhFbjTsNddd2y9/45S3bYI6acbDTYIidD3s3kU25jn/U65/OmM4Nr6/wAe3Yu3MnCz6wxLXHQUSuqRXzmSG9/eh7ZI9M54X11Mb9+kFhzXh4XlqthkK96cZit8iFliJFOW5uEuohaawkVSXzxINKfY6egsGXPTdZgZCmshyFnxOYGyX5zwotjL3/2ceFYqpc/kyp419XhCn48InmK9/U7DmT+p9oXi4Mlus67Hs3IsVzGhJJ+NiRrETS8vU2+B6COZis3ZhqcVOVOx8ZrdF0SenyAZAmCiTfdW5pvzTkU0Qw76EXyL9jv92H0/Zxg7X72a3tm21ZfFi290qitRL+/sEri39OZF/D10m3CZt+zjpWs/fO/aQHp7kDMfTx9EKuOQP84ESnvCaC8d2zKQTnepVW/ug4r+GJfxwZwd3nxc3YvlGtj4IkjdbFDkWYlhemb4uQpeoqJR9TH/QwzsnNJ32MyADXIbpe7j8dZLDQzUK7ckYohv0ZFmDiM0v7sjN55nbZlERv4Tau7MUfwgMrOTRIM4toueiNTM77oA7qNIwiBl/ji+mnN/ZGK10GOKhj7IrBQBYZfqSmCdK1o6lPtNFWtQAlnk4u83cjnpCFL3kzbPPF2YfSU7xFaIKrHwT+6COKYI44/lHrNTrdp2qO5EcCU682NTDxndiXGg0ks5UnwTWxGeQ8J6Y8dY/alfDSpMIBd4nxygwUfzw9OKT/QmmHT2rvrgpnmGOdyZx9XVgQs75Jo1lqdZmrXiG0zzIYLA/ZvFR3YcZggcEazaRgOnlwOPWoRuLh6fPULPaZA4dqz6VBFgB8cTC42kJBqsVTxm8wJggPZyld8lPKdMQYo94VstW0pxE7E+5S7jzW/ubf66qY0E62Iy8GXjH5FBDgcAzYdfqsJUIXTOQAllgcPtlwlSAGYr896rj3PJA/wz0zknegFM2Zhq/UAwFAQwVwROuZw2DiuqSRyNJcEHGZlLX36z/y93wv5vUedI84B80DV84xRzfhxkKaR3cMVqxgaJiXMs6Zz+/jCFCUJ8NHAzWW4Q92YebjqU9jEUfR6tPG704B2Mf00YADjjNZPIM5wzK/ffhV1lw9xn//689daxUs+jfWw/ZWOw7bE6fZXPMTdtdbrX3GZD9sf0/WEPPMQnHgCiOTnOFAizTM6hx9fRCdkjOIJkaMxiRFYhqYpQTydj6JQpMjzLEmyZxJN4UgcoxSN/vr7799+Tct4PAiG9IHwX7+WPM7+/HetP/9/cP77t19LWj9g4D+gH2zdXj6DJV5+z+o1XfL8CZymfFl//998v/+T7/d/8v1EXuuW9/8ulZ/brz+Hvet++7XF5fqD64nKyyXe6nFY/7ME/5PrGfyT7efG/0nY5WXc/eA7nupP3H8w/oH8+vtfakD3KQfoAAA= -->
