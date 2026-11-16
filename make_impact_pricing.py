import re

with open('academics/PREC_115/unessay/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the pricing section
# We want to replace the inner feature list of all three cards: Standard, Gold, and Platinum.

standard_replacement = """              <!-- High-Impact Ad Spec Blocks -->
              <div class="space-y-4 mb-8">
                <div class="p-3.5 rounded-2xl bg-white border border-softBorder shadow-sm">
                  <div class="text-[11px] font-mono font-bold uppercase tracking-wider text-inkMuted mb-0.5">Sleep Allocation</div>
                  <div class="text-base font-bold text-inkDark flex items-center justify-between">
                    <span>5 Hours Nightly Max</span>
                    <span class="text-xs px-2 py-0.5 rounded-full bg-amber-100 text-amber-800 font-mono font-semibold">Strict Cap</span>
                  </div>
                </div>

                <div class="p-3.5 rounded-2xl bg-white border border-softBorder shadow-sm">
                  <div class="text-[11px] font-mono font-bold uppercase tracking-wider text-rose-500 mb-0.5">Afternoon Bandwidth</div>
                  <div class="text-base font-bold text-inkDark flex items-center justify-between">
                    <span>Throttled to 2G</span>
                    <span class="text-xs px-2 py-0.5 rounded-full bg-rose-100 text-rose-700 font-mono font-semibold">Brain Lag</span>
                  </div>
                </div>

                <div class="p-3.5 rounded-2xl bg-rose-50/50 border border-rose-200 shadow-sm">
                  <div class="text-[11px] font-mono font-bold uppercase tracking-wider text-rose-600 mb-0.5">Thought Interruption</div>
                  <div class="text-base font-bold text-rose-900 leading-snug">
                    LoveMatch Ads Every 10 Mins
                  </div>
                  <div class="text-xs text-rose-700 mt-1 italic">"Feeling lonely? Try LoveMatch Premium!"</div>
                </div>

                <div class="p-3 rounded-2xl bg-neutral-100 border border-neutral-200 text-xs font-mono font-bold text-inkMuted flex justify-between items-center">
                  <span>CANCELLATION PENALTY:</span>
                  <span class="text-alertRed font-extrabold text-sm">$5,000 USD</span>
                </div>
              </div>"""

gold_replacement = """              <!-- High-Impact Ad Spec Blocks -->
              <div class="space-y-4 mb-8">
                <div class="p-3.5 rounded-2xl bg-blue-50/60 border border-blue-200/60 shadow-sm">
                  <div class="text-[11px] font-mono font-bold uppercase tracking-wider text-electricCobalt mb-0.5">Sleep Compression</div>
                  <div class="text-base font-bold text-inkDark flex items-center justify-between">
                    <span>8 Hours Compressed to 3</span>
                    <span class="text-xs px-2 py-0.5 rounded-full bg-blue-100 text-electricCobalt font-mono font-bold">266% Speed</span>
                  </div>
                  <div class="text-xs text-inkMuted mt-1">Wake up fully recharged at 4:30 AM before sunrise.</div>
                </div>

                <div class="p-3.5 rounded-2xl bg-white border border-softBorder shadow-sm">
                  <div class="text-[11px] font-mono font-bold uppercase tracking-wider text-electricCobalt mb-0.5">Cognitive Speed</div>
                  <div class="text-base font-bold text-inkDark flex items-center justify-between">
                    <span>Zero Afternoon Lag</span>
                    <span class="text-xs px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-mono font-bold">+180% Focus</span>
                  </div>
                </div>

                <div class="p-3.5 rounded-2xl bg-white border border-softBorder shadow-sm">
                  <div class="text-[11px] font-mono font-bold uppercase tracking-wider text-emerald-600 mb-0.5">Mental Privacy</div>
                  <div class="text-base font-bold text-inkDark flex items-center justify-between">
                    <span>100% Ad-Free Mind</span>
                    <span class="text-xs px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-mono font-bold">No Commercials</span>
                  </div>
                </div>
              </div>"""

platinum_replacement = """              <!-- High-Impact Ad Spec Blocks -->
              <div class="space-y-4 mb-8">
                <div class="p-4 rounded-2xl bg-gradient-to-r from-blue-900 to-indigo-900 text-white shadow-md">
                  <div class="text-[11px] font-mono font-bold uppercase tracking-wider text-cyan-300 mb-0.5">Sleep Requirement</div>
                  <div class="text-lg font-black tracking-tight flex items-center justify-between">
                    <span>0.0 Hours Required (∞)</span>
                    <span class="text-xs px-2.5 py-0.5 rounded-full bg-cyan-400 text-black font-mono font-extrabold">Work 24/7</span>
                  </div>
                  <div class="text-xs text-blue-200 mt-1">Work 120 hours in a row. Eliminate biological sleep completely.</div>
                </div>

                <div class="p-3.5 rounded-2xl bg-white border border-blue-200 shadow-sm">
                  <div class="text-[11px] font-mono font-bold uppercase tracking-wider text-electricCobalt mb-0.5">Career Velocity</div>
                  <div class="text-base font-black text-inkDark flex items-center justify-between">
                    <span>Double Salary Guarantee</span>
                    <span class="text-xs px-2 py-0.5 rounded-full bg-indigo-100 text-indigo-900 font-mono font-bold">2x Promoted</span>
                  </div>
                  <div class="text-xs text-inkMuted mt-1">Automatic promotion priority over Standard staff.</div>
                </div>

                <div class="p-3.5 rounded-2xl bg-amber-50/70 border border-amber-200 shadow-sm">
                  <div class="text-[11px] font-mono font-bold uppercase tracking-wider text-amber-700 mb-0.5">Emotional Assistant</div>
                  <div class="text-base font-black text-amber-950 flex items-center justify-between">
                    <span>Total Grief Override</span>
                    <span class="text-xs px-2 py-0.5 rounded-full bg-amber-200 text-amber-900 font-mono font-bold">Zero Sadness</span>
                  </div>
                  <div class="text-xs text-amber-800 mt-1 font-medium">Dog died? Finish 3 Excel sheets twenty minutes later.</div>
                </div>
              </div>"""

# Replace in Standard
old_std_ul_pattern = r'<ul class="space-y-3\.5 text-sm text-inkDark mb-8">.*?</ul>'
# Find first ul in Standard
match_std = re.search(old_std_ul_pattern, html, re.DOTALL)
if match_std:
    html = html[:match_std.start()] + standard_replacement + html[match_std.end():]
    print("Replaced Standard list with high-impact blocks!")

# Find in Gold
match_gold = re.search(old_std_ul_pattern, html, re.DOTALL)
if match_gold:
    html = html[:match_gold.start()] + gold_replacement + html[match_gold.end():]
    print("Replaced Gold list with high-impact blocks!")

# Find in Platinum
match_plat = re.search(old_std_ul_pattern, html, re.DOTALL)
if match_plat:
    html = html[:match_plat.start()] + platinum_replacement + html[match_plat.end():]
    print("Replaced Platinum list with high-impact blocks!")

with open('academics/PREC_115/unessay/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully!")
