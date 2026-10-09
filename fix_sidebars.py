import os
import re

base_dir = "/Users/marktplaats/Desktop/social"

def get_base_sidebar(prefix, content_html):
    return f"""<aside class="profile-col">
      <div class="p-search-header">
        <div class="p-search-box">
          <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.35-4.35"></path></svg>
          <input type="text" placeholder="Search...">
        </div>
      </div>
      <div class="p-scroll-area">
{content_html}
        <div class="footer-tabs">
          <button class="ft-tab" onclick="location.href='{prefix}popular/hot.html'"><svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg> Popular</button>
          <button class="ft-tab" onclick="location.href='{prefix}all/hot.html'"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg> All</button>
          <button class="ft-tab" onclick="location.href='{prefix}discover/index.html'"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg> Discover</button>
        </div>
      </div>
    </aside>"""

profile_card_html = """
        <div class="p-header-img"><div class="p-pattern"></div></div>
        <div class="p-avatar-position"><div class="p-avatar-large" style="background:var(--accent);">FM</div></div>
        <div class="p-details">
          <div class="p-name-badge">
            <span class="p-display-name">Fredy Mercury</span>
            <div class="p-verify-icon"><svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"></path></svg></div>
          </div>
          <div class="p-username">@fredy</div>
          <div class="p-biography">Designer & Developer. Creating the next generation of social experiences.</div>
          <div class="p-counter-row">
            <div class="p-counter"><strong>1,204</strong> Followers</div>
            <div class="p-counter"><strong>432</strong> Following</div>
          </div>
          <button class="p-big-follow-btn">Follow</button>
        </div>
"""

events_html = """
        <div class="p-nav-tabs">
          <div class="p-nav-tab active">Recent</div>
          <div class="p-nav-tab">Events</div>
        </div>
        <div class="p-events-grid">
          <div class="p-event-card">
            <div class="p-event-img" style="background:#fef2f2;">🎭</div>
            <div class="p-event-body">
              <div class="p-event-title">Art Expo</div>
              <div class="p-event-location"><svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg> Tokyo</div>
            </div>
          </div>
          <div class="p-event-card">
            <div class="p-event-img" style="background:#f0fdf4;">🎮</div>
            <div class="p-event-body">
              <div class="p-event-title">Game Jam</div>
              <div class="p-event-location"><svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg> Online</div>
            </div>
          </div>
        </div>
"""

trending_html = """
        <div class="trending-lands">
          <div class="t-label">Trending Lands</div>
          <div class="t-land">
            <div class="t-land-icon">🌳</div>
            <div class="t-land-info">
              <div class="t-land-name">l/nature</div>
              <div class="t-land-posts">1.2k posts today</div>
            </div>
          </div>
          <div class="t-land">
            <div class="t-land-icon">💻</div>
            <div class="t-land-info">
              <div class="t-land-name">l/tech</div>
              <div class="t-land-posts">850 posts today</div>
            </div>
          </div>
          <div class="t-land">
            <div class="t-land-icon">🎨</div>
            <div class="t-land-info">
              <div class="t-land-name">l/art</div>
              <div class="t-land-posts">432 posts today</div>
            </div>
          </div>
        </div>
"""

for root, dirs, files in os.walk(base_dir):
    if 'node_modules' in root or '.git' in root: continue
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(base_dir, root)
            prefix = '' if rel_path == '.' else rel_path + '/'
            
            if "profile" in filepath:
                content = events_html + trending_html
            elif "discover" in filepath or "popular" in filepath or "all" in filepath:
                content = trending_html
            else:
                content = profile_card_html + trending_html
                
            new_sidebar = get_base_sidebar(prefix, content)
            
            with open(filepath, 'r') as f:
                html = f.read()
            
            html = re.sub(r'<aside class="profile-col">.*?</aside>', new_sidebar, html, flags=re.DOTALL)
            
            with open(filepath, 'w') as f:
                f.write(html)

print("Sidebars updated.")
