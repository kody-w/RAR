---
name: "rar-discreetrappers-sharepoint-contract-analysis"
description: "Analyzes recording and entertainment contracts FROM THE LABEL'S PERSPECTIVE. Identifies risks to the label, flags artist-favorable terms, extracts clauses, and generates executive summaries for label decision-makers. Supports PDF, DOCX, and TXT formats."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/sharepoint_contract_analysis_agent", "rar_sha256": "6bfac36ced9e10e89b7a35b6e3a7464d3cc66e4f8832feedbbde899852aa3893", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.2", "author": "Bill Whalen", "tags": ["integrations", "sharepoint", "contracts", "analysis", "legal"]}
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

<!-- rci-capsule:v1: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 -->
