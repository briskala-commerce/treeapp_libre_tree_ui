import os

base_dir = "/Users/marktplaats/Desktop/social"

def get_profile_col(prefix):
    return f"""
    <aside class="profile-col">
      <div class="p-search-header">
        <div class="p-search-box">
          <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.35-4.35"></path></svg>
          <input type="text" placeholder="Search...">
        </div>
      </div>
      <div class="p-scroll-area">
        <div class="footer-tabs">
          <button class="ft-tab" onclick="location.href='{prefix}popular/hot.html'"><svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg> Popular</button>
          <button class="ft-tab" onclick="location.href='{prefix}all/hot.html'"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg> All</button>
          <button class="ft-tab" onclick="location.href='{prefix}discover/index.html'"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg> Discover</button>
        </div>
      </div>
    </aside>
"""

storage_svg = '<svg viewBox="0 0 24 24"><path d="M2 20h20v-4H2v4zm2-3h2v2H4v-2zM2 4v4h20V4H2zm4 3H4V5h2v2zm-4 7h20v-4H2v4zm4-3H4v2h2v-2z"></path></svg>'

for root, dirs, files in os.walk(base_dir):
    if 'node_modules' in root or '.git' in root: continue
    
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(base_dir, root)
            prefix = '' if rel_path == '.' else rel_path + '/'
            
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Restore profile-col if missing
            if '<aside class="profile-col">' not in content:
                content = content.replace('  </div>\n\n  <script>', get_profile_col(prefix) + '\n  </div>\n\n  <script>')
                # Sometimes it might not match perfectly.
                if '<aside class="profile-col">' not in content:
                     content = content.replace('  </div>\n</body>', get_profile_col(prefix) + '\n  </div>\n</body>')

            # Restore storage SVG
            if '<div class="s-storage-header">' in content and storage_svg not in content:
                content = content.replace('<div class="s-storage-header">', '<div class="s-storage-header">\n          ' + storage_svg)
            
            with open(filepath, 'w') as f:
                f.write(content)

print("Restoration script complete.")
