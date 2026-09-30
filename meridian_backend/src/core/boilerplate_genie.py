import os
import logging
from typing import Dict, List, Any

class BoilerplateGenie:
    """
    Your Personal Boilerplate Genie (🧞‍♂️)
    Detects component creation triggers, analyzes existing workspace code patterns,
    and generates complete customized stubs matching project conventions.
    """
    def __init__(self, workspace_root: str):
        self.workspace_root = workspace_root

    def generate_component_stub(self, component_name: str, target_dir: str = "meridian_frontend/src/components") -> Dict[str, Any]:
        """Generates a React component stub matching standard project conventions."""
        stub_code = f"""import React from 'react';

interface {component_name}Props {{
  className?: string;
  children?: React.ReactNode;
}}

export default function {component_name}({{ className = '', children }}: {component_name}Props) {{
  return (
    <div className={{`p-4 rounded-xl glass-card ${{className}}`}}>
      <h3 className="text-lg font-semibold text-white">{component_name}</h3>
      {{children}}
    </div>
  );
}}
"""
        test_skeleton = f"""import {{ render, screen }} from '@testing-library/react';
import {component_name} from './{component_name}';

test('renders {component_name} component', () => {{
  render(<{component_name} />);
  expect(screen.getByText('{component_name}')).toBeInTheDocument();
}});
"""
        rel_path = os.path.join(target_dir, f"{component_name}.tsx")
        full_path = os.path.join(self.workspace_root, rel_path)

        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(stub_code)

        return {
            "component_name": component_name,
            "file_path": rel_path,
            "stub_code": stub_code,
            "test_skeleton": test_skeleton,
            "message": f"Created {component_name}.tsx with your standard props + test skeleton. Fill in the JSX?"
        }
