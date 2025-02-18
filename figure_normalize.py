import re
import os
import glob
import shutil
from PIL import Image  # Requires Pillow package

output_path = 'final/paper.tex'
final_refs_name = 'refs.bib'

shutil.rmtree('final')
os.mkdir('final')

os.system('cp *.sty final')
os.system('cp *.eps final')
os.system('cp *.bst final')
os.system('cp *.cls final')

with open('paper.tex', 'r') as file:
    content = file.read()
    content = '\n'.join([x for x in content.splitlines() if not x.startswith('%')])

# also remove the graphicspath declaration
content = '\n'.join([x for x in content.splitlines() if not x.startswith(r'\graphicspath')])

# also adjust the bibliography declaration
content_new = []
for line in content.splitlines():
    if not line.startswith(r'\bibliography{'):
        content_new.append(line)
    else:
        content_new.append(r'\bibliography{' + final_refs_name + '}')
content = '\n'.join(content_new)

# Define the regex pattern to find \includegraphics commands
pattern = r'(\\includegraphics\[.*?\]{)(.*?)(})'

# Find all matches and replace them sequentially
matches = re.findall(pattern, content)
for i, match in enumerate(matches, start=1):
    print(match)
    # img = Image.open(f'cache/{match[1]}')
    # img.convert('RGB').save(f'final/fig{i}.jpg', format='JPEG', dpi=(600,600))
    # replacement = rf"{match[0]}fig{i}.jpg{match[2]}"

    os.system(f'cp cache/{match[1]} final/fig{i}.png')
    replacement = rf"{match[0]}fig{i}.png{match[2]}"
    content = content.replace("".join(match), replacement, 1)

# Write the updated content to a new file
with open(output_path, 'w') as file:
    file.write(content)

### DEALING WITH CITATIONS

def clean_unused_references(tex_file, bib_file, output_bib_file):
    # Step 1: Extract citation keys from the LaTeX file
    with open(tex_file, 'r') as file:
        tex_content = file.read()

    # Define regex patterns for \citep and \cite
    pattern = r'\\(citep|cite)\{([^}]+)\}'

    # Find all matches
    matches = re.findall(pattern, content)

    # Process matches
    used_citations = []
    for cite_type, cite_args in matches:
        # Split the comma-separated arguments
        used_citations.extend([key.strip() for key in cite_args.split(',')])
    used_citations = list(set(used_citations))

    # Step 2: Read and filter the bibliography file
    with open(bib_file, 'r') as file:
        bib_content = '\n'.join([x for x in file.read().splitlines() if not x.startswith('%')])

    # Split the bibliography into individual entries
    bib_entries = re.split(r'(?<=\n)(?=@)', bib_content)
    filtered_entries = []

    for entry in bib_entries:        
        # Extract the citation key from each entry
        match = re.match(r'@\w+\{([^,]+),', entry, re.DOTALL)
        if match:
            citation_key = match.group(1).strip()
            if citation_key in used_citations:
                filtered_entries.append(entry)  # Add back the leading '@'

    # Step 3: Write the filtered bibliography to a new file
    with open(output_bib_file, 'w') as file:
        file.write('\n\n'.join(filtered_entries))

    print(f"Filtered bibliography saved to {output_bib_file}. {len(filtered_entries)} references retained.")

# Example usage
clean_unused_references(output_path, 'cache/refs.bib', f'final/{final_refs_name}')