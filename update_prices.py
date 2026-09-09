import re

with open('d:/Apps/Brochser_Xanocode/brochure1.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(match):
    h4 = match.group(1)
    p = match.group(2)
    return f'''<div class="card-hover p-6 flex flex-col">
                        <h4 class="text-lg font-bold mb-2">{h4}</h4>
                        <p class="text-muted-foreground text-sm mb-4">{p}</p>
                        <div class="mt-auto pt-3 border-t border-border flex items-center justify-between">
                            <span class="text-xs font-medium text-muted-foreground uppercase tracking-wider">Starts at</span>
                            <span class="font-bold text-sm">₹4,999</span>
                        </div>
                    </div>'''

pattern = r'<div class="card-hover p-6">\s*<h4 class="text-lg font-bold mb-2">(.*?)</h4>\s*<p class="text-muted-foreground text-sm">(.*?)</p>\s*</div>'

new_content = re.sub(pattern, replacer, content)

with open('d:/Apps/Brochser_Xanocode/brochure1.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Prices updated!")
