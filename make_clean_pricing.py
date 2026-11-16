import re

with open('academics/PREC_115/unessay/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Refined, effortless, broadcast-clean cards that are visible, funny, but not tryhardy

standard_content = """              <!-- Clean Broadcast-Ready Feature Blocks -->
              <div class="space-y-3.5 mb-8 text-left">
                <div class="p-3.5 rounded-2xl bg-canvas border border-softBorder">
                  <div class="text-sm font-bold text-inkDark flex items-center justify-between">
                    <span>Ad-Supported Thoughts</span>
                    <span class="text-[11px] font-mono font-semibold px-2 py-0.5 rounded-full bg-rose-100 text-rose-700">10 Min Ads</span>
                  </div>
                  <div class="text-xs text-inkMuted mt-1">Unskippable commercial audio injected into your daydream loop.</div>
                </div>

                <div class="p-3.5 rounded-2xl bg-canvas border border-softBorder">
                  <div class="text-sm font-bold text-inkDark flex items-center justify-between">
                    <span>2:00 PM Bandwidth Curfew</span>
                    <span class="text-[11px] font-mono font-semibold px-2 py-0.5 rounded-full bg-amber-100 text-amber-800">2G Speed</span>
                  </div>
                  <div class="text-xs text-inkMuted mt-1">Cognitive speeds throttle in the afternoon to save server bandwidth.</div>
                </div>

                <div class="p-3.5 rounded-2xl bg-canvas border border-softBorder">
                  <div class="text-sm font-bold text-inkDark flex items-center justify-between">
                    <span>5-Hour Sleep Cap</span>
                    <span class="text-[11px] font-mono font-semibold px-2 py-0.5 rounded-full bg-slate-200 text-slate-700">Strict Limit</span>
                  </div>
                  <div class="text-xs text-inkMuted mt-1">Forced early waking; rest of the night reserved for sponsored audio.</div>
                </div>

                <div class="p-3 rounded-2xl bg-red-50/60 border border-red-200/60 flex items-center justify-between text-xs font-mono font-bold">
                  <span class="text-red-900">BRAIN RESTOCKING FEE:</span>
                  <span class="text-alertRed text-sm font-extrabold">$5,000 USD</span>
                </div>
              </div>"""

gold_content = """              <!-- Clean Broadcast-Ready Feature Blocks -->
              <div class="space-y-3.5 mb-8 text-left">
                <div class="p-3.5 rounded-2xl bg-blue-50/60 border border-blue-200/60">
                  <div class="text-sm font-bold text-inkDark flex items-center justify-between">
                    <span>Sleep Compressed: 8h -> 3h</span>
                    <span class="text-[11px] font-mono font-bold px-2 py-0.5 rounded-full bg-blue-100 text-electricCobalt">266% Speed</span>
                  </div>
                  <div class="text-xs text-inkMuted mt-1">Wake up fully recharged before sunrise, ready to out-work peers.</div>
                </div>

                <div class="p-3.5 rounded-2xl bg-canvas border border-softBorder">
                  <div class="text-sm font-bold text-inkDark flex items-center justify-between">
                    <span>Zero Thought Ads</span>
                    <span class="text-[11px] font-mono font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800">100% Ad-Free</span>
                  </div>
                  <div class="text-xs text-inkMuted mt-1">Complete commercial suppression during active business hours.</div>
                </div>

                <div class="p-3.5 rounded-2xl bg-canvas border border-softBorder">
                  <div class="text-sm font-bold text-inkDark flex items-center justify-between">
                    <span>No Afternoon Lag</span>
                    <span class="text-[11px] font-mono font-bold px-2 py-0.5 rounded-full bg-blue-100 text-electricCobalt">+180% Focus</span>
                  </div>
                  <div class="text-xs text-inkMuted mt-1">Priority neural bandwidth prevents afternoon cognitive fatigue.</div>
                </div>

                <div class="p-3.5 rounded-2xl bg-canvas border border-softBorder">
                  <div class="text-sm font-bold text-inkDark flex items-center justify-between">
                    <span>Memory Cache Protection</span>
                    <span class="text-[11px] font-mono font-bold px-2 py-0.5 rounded-full bg-slate-200 text-slate-700">1080p Secure</span>
                  </div>
                  <div class="text-xs text-inkMuted mt-1">Protects long-term personal memories from weekly auto-deletion.</div>
                </div>
              </div>"""

platinum_content = """              <!-- Clean Broadcast-Ready Feature Blocks -->
              <div class="space-y-3.5 mb-8 text-left">
                <div class="p-3.5 rounded-2xl bg-gradient-to-r from-blue-900 to-indigo-900 text-white shadow-sm">
                  <div class="text-base font-black tracking-tight flex items-center justify-between">
                    <span>Sleep Deprecated (0.0h)</span>
                    <span class="text-[11px] font-mono font-extrabold px-2 py-0.5 rounded-full bg-cyan-400 text-black">Work 24/7</span>
                  </div>
                  <div class="text-xs text-blue-200 mt-1">Permanently eliminates biological sleep. Work 120 hours in a row.</div>
                </div>

                <div class="p-3.5 rounded-2xl bg-canvas border border-softBorder">
                  <div class="text-sm font-bold text-inkDark flex items-center justify-between">
                    <span>Bereavement Override</span>
                    <span class="text-[11px] font-mono font-bold px-2 py-0.5 rounded-full bg-amber-100 text-amber-900">Zero Grief</span>
                  </div>
                  <div class="text-xs text-inkMuted mt-1">Converts personal tragedy into immediate analytical focus.</div>
                </div>

                <div class="p-3.5 rounded-2xl bg-canvas border border-softBorder">
                  <div class="text-sm font-bold text-inkDark flex items-center justify-between">
                    <span>Double Salary Guarantee</span>
                    <span class="text-[11px] font-mono font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800">2x Promoted</span>
                  </div>
                  <div class="text-xs text-inkMuted mt-1">Automatic corporate promotion priority over Standard-tier staff.</div>
                </div>

                <div class="p-3.5 rounded-2xl bg-canvas border border-softBorder">
                  <div class="text-sm font-bold text-inkDark flex items-center justify-between">
                    <span>4K Memory Upscaling</span>
                    <span class="text-[11px] font-mono font-bold px-2 py-0.5 rounded-full bg-indigo-100 text-indigo-900">Lossless</span>
                  </div>
                  <div class="text-xs text-inkMuted mt-1">Lossless archival of every corporate spreadsheet and presentation.</div>
                </div>
              </div>"""

# Standard block replacement
pattern_std = r'<!-- High-Impact Ad Spec Blocks -->.*?</div>\s*</div>\s*<button onclick="openCheckoutModal\(\'Standard\''
replacement_std = standard_content + '\n            <button onclick="openCheckoutModal(\'Standard\''
html = re.sub(pattern_std, replacement_std, html, flags=re.DOTALL)

# Gold block replacement
pattern_gold = r'<!-- High-Impact Ad Spec Blocks -->.*?</div>\s*</div>\s*<button onclick="openCheckoutModal\(\'Gold\''
replacement_gold = gold_content + '\n            <button onclick="openCheckoutModal(\'Gold\''
html = re.sub(pattern_gold, replacement_gold, html, flags=re.DOTALL)

# Platinum block replacement
pattern_plat = r'<!-- High-Impact Ad Spec Blocks -->.*?</div>\s*</div>\s*<button onclick="openCheckoutModal\(\'Platinum\''
replacement_plat = platinum_content + '\n            <button onclick="openCheckoutModal(\'Platinum\''
html = re.sub(pattern_plat, replacement_plat, html, flags=re.DOTALL)

# Clean up button labels so they are sharp and not tryhard
html = html.replace('Accept Free Tier Trap', 'Select Standard ($0)')
html = html.replace('Pay $4,999/mo to Keep Up', 'Upgrade to Gold ($4,999/mo)')
html = html.replace('Subscribe for $14,999/mo', 'Activate Platinum ($14,999/mo)')

# Card subheadings: clean, subtle satire
html = html.replace('For interns, couriers, and the working class.', 'For interns and clinical trials.')
html = html.replace('The minimum required to keep your job.', 'The minimum required to keep up with enterprise pace.')
html = html.replace('For managers who work 120 hours in a row and double their salary.', 'For managers who work 120 consecutive hours.')

with open('academics/PREC_115/unessay/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with clean, visible, non-tryhardy satirical copy!")
