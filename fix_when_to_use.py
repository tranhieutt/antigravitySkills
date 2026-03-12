import os
import re

skills_dir = r"C:\Users\x1 carbon\.gemini\antigravity\skills"
updated_count = 0

print("Starting to add 'When to Use' section to skills...")

for skill_name in sorted(os.listdir(skills_dir)):
    skill_path = os.path.join(skills_dir, skill_name)
    if not os.path.isdir(skill_path) or skill_name.startswith('.'):
        continue
        
    skill_md_path = os.path.join(skill_path, "SKILL.md")
    if not os.path.exists(skill_md_path):
        continue
        
    with open(skill_md_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Check if 'When to Use' is missing (case-insensitive check)
    if "## When to Use" not in content and "When to use" not in content and "when to use" not in content.lower():
        # Try to extract the description to make the 'When to Use' more meaningful
        desc_match = re.search(r'^description:\s*(.*?)$', content, re.MULTILINE)
        description = desc_match.group(1).strip('"\'').strip() if desc_match else f"working with the {skill_name} skill"
        
        # Determine behavior based on existing Markdown
        when_section = f"\n\n## When to Use\n\n- Use when {description}\n"
        
        # Append to the end of the content
        new_content = content.rstrip() + when_section
        
        try:
            with open(skill_md_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_count += 1
            print(f"Fixed: {skill_name}")
        except Exception as e:
            print(f"Error writing to {skill_md_path}: {e}")

print(f"\nSuccessfully added 'When to Use' section to {updated_count} skills.")
