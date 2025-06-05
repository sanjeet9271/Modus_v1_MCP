import os
import json

class ComponentRegistry:
    """Registry for Modus components, handling component details and examples"""
    
    def __init__(self):
        # Paths for knowledge base files
        self.base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.db_path = os.path.join(self.base_path, "Knowledge Base", "db.json")
        self.db_ui_path = os.path.join(self.base_path, "Knowledge Base", "db_ui.json")
        self.kb_path = os.path.join(self.base_path, "Knowledge Base", "From_KB.md")
        self.ui_kb_path = os.path.join(self.base_path, "Knowledge Base", "UI_KB.md")
        self.angular_kb_path = os.path.join(self.base_path, "Knowledge Base", "angular_KB.md")
        self.icons_path = os.path.join(self.base_path, "Knowledge Base", "modus_icons.json")
    
    def get_all_components(self):
        """Get list of all available components (both form and UI)"""
        try:
            components = []
            
            # Get form components
            with open(self.db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if "components" in data and "form" in data["components"]:
                    components.extend(list(data["components"]["form"].keys()))
            
            # Get UI components
            with open(self.db_ui_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if "components" in data and "ui" in data["components"]:
                    components.extend(list(data["components"]["ui"].keys()))
            
            return components
        except Exception as e:
            print(f"Error getting component list: {e}")
            return []
    
    def get_component_properties_and_events(self, component_name):
        """Get properties, events and description for a specific component"""
        try:
            # Check form components first
            with open(self.db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if ("components" in data and 
                "form" in data["components"] and 
                component_name in data["components"]["form"]):
                
                component_data = data["components"]["form"][component_name]
                return {
                    "properties": component_data.get("properties", []),
                    "events": component_data.get("events", []),
                    "methods": component_data.get("methods", []),
                    "description": component_data.get("description", "")
                }
            
            # If not found in form components, check UI components
            with open(self.db_ui_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if ("components" in data and 
                "ui" in data["components"] and 
                component_name in data["components"]["ui"]):
                
                component_data = data["components"]["ui"][component_name]
                return {
                    "properties": component_data.get("properties", []),
                    "events": component_data.get("events", []),
                    "methods": component_data.get("methods", []),
                    "description": component_data.get("description", "")                
                    }
            
            return {"properties": [], "events": [], "methods": [], "description": ""}
        
        except Exception as e:
            print(f"Error getting component properties: {e}")
            return {"properties": [], "events": [], "methods": [], "description": ""}
        
    def _extract_kb_examples(self, content, component_name, framework=None):
        """Extract examples for a specific component from the knowledge base
        
        Args:
            content: The content to extract from
            component_name: The component name to find examples for
            framework: The framework to use - 'angular' for Angular examples, otherwise React
            
        Returns:
            list: List of examples for the component
        """
        examples = []
        try:
            # If angular framework is specified, extract from angular KB
            if framework == "angular":
                return self._extract_examples_from_content(self.angular_kb_path, component_name, framework="angular")
            
            # Default behavior for React
            modus_list = ["ModusTable", "ModusTabs", "ModusToast", "ModusToolbar", "ModusTooltip"]
            if component_name.startswith("Modus") or component_name in modus_list:
                examples = self._extract_examples_from_content(self.ui_kb_path, component_name)
                if not examples:
                    examples = self._extract_examples_from_content(self.kb_path, component_name)
            else:
                examples = self._extract_examples_from_content(self.kb_path, component_name)
                if not examples:
                    examples = self._extract_examples_from_content(self.ui_kb_path, component_name)
            
            return examples       
        except Exception as e:
            print(f"Error extracting examples: {e}")
            return []
    
    def _extract_examples_from_content(self, kb_path, component_name, framework=None):
            """Helper method to extract examples from a specific KB file"""
            try:
                with open(kb_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                examples = []
                
                # Find the component section more robustly using regex-like pattern matching
                print(component_name)
                component_marker = f"# <{component_name}>"
                start_index = content.find(component_marker)
                
                if start_index == -1:
                    print(f"Component {component_name} not found in {kb_path}")
                    return []
                
                # Find the next component section or end of file
                next_component_index = content.find("# <", start_index + len(component_marker))
                
                if next_component_index == -1:
                    # If this is the last component in the file
                    component_section = content[start_index:]
                else:
                    component_section = content[start_index:next_component_index]
                
                # Extract examples from the component section
                prompts = component_section.split("## Prompt")
                
                # Skip the first split which contains the component header
                for i, prompt in enumerate(prompts[1:], 1):
                    example = {
                        "prompt_number": i,
                        "question": "",
                        "code": ""
                    }
                    
                    # Extract the user question
                    question_parts = prompt.split("**User Question:**")
                    if len(question_parts) > 1:
                        answer_parts = question_parts[1].split("**Agent Answer:**")
                        if len(answer_parts) > 0:
                            example["question"] = answer_parts[0].strip()
                    
                    # Extract the code example - handle both tsx/jsx for React and HTML/TypeScript for Angular
                    if framework == "angular":
                        # For Angular, look for HTML and TypeScript blocks
                        html_start = prompt.find("```html")
                        ts_start = prompt.find("```typescript")
                        
                        if html_start != -1:
                            html_end = prompt.find("```", html_start + 7)
                            if html_end != -1:
                                html_code = prompt[html_start + 7:html_end].strip()
                                
                                # Add HTML code
                                if example["code"]:
                                    example["code"] += "\n\n/* HTML Template */\n" + html_code
                                else:
                                    example["code"] = "/* HTML Template */\n" + html_code
                        
                        if ts_start != -1:
                            ts_end = prompt.find("```", ts_start + 13)
                            if ts_end != -1:
                                ts_code = prompt[ts_start + 13:ts_end].strip()
                                
                                # Add TypeScript code
                                if example["code"]:
                                    example["code"] += "\n\n/* TypeScript Component */\n" + ts_code
                                else:
                                    example["code"] = "/* TypeScript Component */\n" + ts_code
                    else:
                        # Original React handling
                        code_start = prompt.find("```tsx")
                        if code_start == -1:
                            code_start = prompt.find("```jsx")
                            code_type_len = 6  # "```jsx" length
                        else:
                            code_type_len = 6  # "```tsx" length
                        
                        code_end = prompt.find("```", code_start + code_type_len) if code_start != -1 else -1
                        
                        if code_start != -1 and code_end != -1:
                            example["code"] = prompt[code_start + code_type_len:code_end].strip()
                    
                    examples.append(example)
                
                return examples
            except Exception as e:
                print(f"Error extracting examples from {kb_path}: {e}")
                return []
            
    def get_installation_guidelines(self):
        """Get installation and usage guidelines"""
        try:
            guidelines_path = os.path.join(self.base_path, "Knowledge Base", "Modus_Components_Guidelines.md")
            with open(guidelines_path, 'r', encoding='utf-8') as f:
                guidelines = f.read()
            return guidelines
        except Exception as e:
            print(f"Error loading guidelines: {e}")
            return "Guidelines not available."
            
    def get_all_icon_names(self):
        """Get a list of all available Modus icon names"""
        try:
            with open(self.icons_path, 'r', encoding='utf-8') as f:
                icons_data = json.load(f)
            return icons_data.get("icons", [])
        except Exception as e:
            print(f"Error loading icon names: {e}")
            return []
            
    def get_icon_names_by_char(self, char_prefix):
        """Get a list of icon names starting with a specific character
        
        Args:
            char_prefix (str): The character prefix to filter icons by
            
        Returns:
            list: List of icon names starting with the specified character
        """
        try:
            if not char_prefix:
                return []
                
            all_icons = self.get_all_icon_names()
            
            # Convert to lowercase for case-insensitive matching
            prefix = char_prefix.lower()
            
            # Filter icons starting with the specified character
            matching_icons = [icon for icon in all_icons if icon.lower().startswith(prefix)]
            
            return matching_icons
        except Exception as e:
            print(f"Error getting icons by character prefix: {e}")
            return []