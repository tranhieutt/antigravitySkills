import os
import csv
import re

skills_dir = r"C:\Users\x1 carbon\.gemini\antigravity\skills"
csv_path = os.path.join(skills_dir, "skills.csv")

skills_data = []
idx = 1

for item in sorted(os.listdir(skills_dir)):
    item_path = os.path.join(skills_dir, item)
    if os.path.isdir(item_path):
        skill_md_path = os.path.join(item_path, "SKILL.md")
        if os.path.exists(skill_md_path):
            try:
                with open(skill_md_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                    # Extract Description from frontmatter
                    desc_match = re.search(r'^description:\s*(.*?)$', content, re.MULTILINE)
                    description = desc_match.group(1).strip('"\'').strip() if desc_match else ""
                    
                    # Try to extract "When to Use"
                    # Look for variations of When to use
                    when = ""
                    when_match = re.search(r'(?i)##?\s*When to Use\s*\n(.*?)(?=\n##? |\Z)', content, re.MULTILINE | re.DOTALL)
                    if not when_match:
                        # Sometimes it's written inside description frontmatter indirectly or not at all. If not found, use a fallback
                        # In the previous list of skills, it was sometimes just description
                        pass
                    else:
                        when = when_match.group(1).strip()
                    
                    skills_data.append([idx, item, description, when])
                    idx += 1
            except Exception as e:
                print(f"Error reading {skill_md_path}: {e}")

with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["STT", "Tên Skill", "Mô tả nội dung", "Khi nào dùng"])
    writer.writerows(skills_data)

print(f"Generated CSV with {len(skills_data)} skills at {csv_path}")
