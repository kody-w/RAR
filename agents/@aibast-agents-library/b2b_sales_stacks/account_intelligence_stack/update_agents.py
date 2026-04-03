"""
Quick script to update remaining agents with connector support
"""

import re

agents_to_update = [
    "risk_assessment_agent.py",
    "action_prioritization_agent.py",
    "deal_tracking_agent.py"
]

for agent_file in agents_to_update:
    print(f"Updating {agent_file}...")

    with open(agent_file, 'r') as f:
        content = f.read()

    # Add connector path to sys.path if not present
    if "sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))" not in content:
        content = content.replace(
            "sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../')))",
            "sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../')))\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))"
        )

    # Add connector imports if not present
    if "from connectors" not in content:
        content = content.replace(
            "from agents.basic_agent import BasicAgent",
            "from agents.basic_agent import BasicAgent\nfrom connectors.crm_connector import CRMConnector\nfrom connectors.azure_openai_connector import AzureOpenAIConnector"
        )

    # Update __init__ to accept connector_token
    content = re.sub(
        r'def __init__\(self\):',
        'def __init__(self, connector_token: str = None):',
        content
    )

    # Add connector initialization after super().__init__
    if "self.crm_connector = CRMConnector" not in content:
        content = re.sub(
            r'(super\(\).__init__\(name=self\.name, metadata=self\.metadata\))',
            r'\1\n\n        # Initialize connectors\n        self.crm_connector = CRMConnector(connector_token)\n        self.openai_connector = AzureOpenAIConnector(connector_token)',
            content
        )

    with open(agent_file, 'w') as f:
        f.write(content)

    print(f"✅ Updated {agent_file}")

print("\n✅ All agents updated with connector support!")
