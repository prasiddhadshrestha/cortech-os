import re

with open('academics/PREC_115/unessay/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Clean up <style>: Remove neon-beam-scanner, rotateNeonBeam, and crazy heavy glow
old_style_regex = r'<style>.*?</style>'

new_style = """<style>
    body {
      background-color: #F8F9FA;
      color: #0A0D14;
      -webkit-font-smoothing: antialiased;
    }
    .clean-card {
      background: #FFFFFF;
      border: 1px solid rgba(10, 13, 20, 0.08);
      box-shadow: 0 4px 16px -2px rgba(10, 13, 20, 0.04);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .clean-card:hover {
      border-color: rgba(15, 98, 254, 0.4);
      box-shadow: 0 10px 24px -4px rgba(15, 98, 254, 0.12);
      transform: translateY(-3px);
    }
    .platinum-card-featured {
      background: #FFFFFF;
      border: 2px solid #0F62FE !important;
      box-shadow: 0 10px 30px -4px rgba(15, 98, 254, 0.18), 0 0 0 1px #0F62FE !important;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .platinum-card-featured:hover {
      box-shadow: 0 14px 36px -4px rgba(15, 98, 254, 0.25), 0 0 20px rgba(15, 98, 254, 0.2) !important;
      transform: translateY(-4px);
    }
    .subtle-grid {
      background-image: radial-gradient(rgba(10, 13, 20, 0.06) 1px, transparent 1px);
      background-size: 28px 28px;
    }
    .badge-pill {
      background: rgba(15, 98, 254, 0.08);
      color: #0F62FE;
    }
  </style>"""

html = re.sub(old_style_regex, new_style, html, flags=re.DOTALL)

# 2. Replace the entire plans section with the ultra-compact, viewport-fitted version (~600px total height)
old_plans_regex = r'<section id="plans".*?</section>'

new_plans = """<section id="plans" class="pt-8 pb-10 px-6 bg-white border-t border-softBorder">
      <div class="max-w-5xl mx-auto">
        <!-- Compact Centered Header -->
        <div class="text-center max-w-xl mx-auto mb-6">
          <p class="text-[11px] font-mono font-bold text-electricCobalt uppercase tracking-widest mb-1">Workforce Licensing</p>
          <h2 class="font-display text-2xl sm:text-3xl font-extrabold text-inkDark tracking-tight mb-1">Choose your cognitive tax bracket.</h2>
          <p class="text-inkMuted text-xs mb-3">In today's economy, you get the thoughts you can afford.</p>

          <!-- Monthly / Annual Toggle -->
          <div class="inline-flex items-center gap-1.5 p-1 rounded-full bg-neutral-100 border border-softBorder">
            <button id="monthlyBtn" onclick="setBilling('monthly')" class="px-4 py-1 rounded-full text-xs font-bold bg-inkDark text-white transition-all">Monthly</button>
            <button id="annualBtn" onclick="setBilling('annual')" class="px-4 py-1 rounded-full text-xs font-bold text-inkMuted hover:text-inkDark transition-all flex items-center gap-1">
              <span>Annual</span>
              <span class="text-[10px] font-bold text-electricCobalt">Save 20%</span>
            </button>
          </div>
        </div>

        <!-- Compact 3-Card Grid (Fits on a single screen without scrolling) -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-5 items-stretch">

          <!-- Standard -->
          <div class="clean-card rounded-2xl p-5 flex flex-col justify-between bg-white border border-softBorder">
            <div>
              <div class="flex justify-between items-center mb-1">
                <h3 class="font-display text-lg font-bold text-inkDark">Standard</h3>
                <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded-full bg-neutral-100 text-inkMuted border border-neutral-200">Free Tier</span>
              </div>
              <p class="text-[11px] text-inkMuted mb-3">For interns and clinical trials.</p>
              
              <div class="mb-3">
                <span class="text-3xl font-display font-extrabold text-inkDark">$0</span>
                <span class="text-xs text-inkMuted">/ month</span>
              </div>

              <!-- Compact Feature List -->
              <div class="space-y-2 mb-4 text-xs">
                <div class="p-2 rounded-xl bg-neutral-50 border border-neutral-200/60 flex items-center justify-between">
                  <span class="font-medium text-inkDark">Ad-Supported Thoughts</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-rose-100 text-rose-700">10 Min Ads</span>
                </div>
                <div class="p-2 rounded-xl bg-neutral-50 border border-neutral-200/60 flex items-center justify-between">
                  <span class="font-medium text-inkDark">2:00 PM Bandwidth Curfew</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">2G Speed</span>
                </div>
                <div class="p-2 rounded-xl bg-neutral-50 border border-neutral-200/60 flex items-center justify-between">
                  <span class="font-medium text-inkDark">5-Hour Sleep Cap</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-neutral-200 text-neutral-700">Strict Cap</span>
                </div>
                <div class="p-2 rounded-xl bg-red-50 border border-red-200/60 flex items-center justify-between font-mono">
                  <span class="font-bold text-red-900 text-[11px]">EXIT RESTOCKING FEE</span>
                  <span class="text-alertRed font-extrabold text-xs">$5,000 USD</span>
                </div>
              </div>
            </div>

            <button onclick="openCheckoutModal('Standard', '$0/mo')" class="w-full py-2.5 rounded-xl border border-softBorder text-xs font-bold text-inkDark hover:bg-neutral-100 transition-all">
              Select Standard ($0)
            </button>
          </div>

          <!-- Gold -->
          <div class="clean-card rounded-2xl p-5 flex flex-col justify-between bg-white border border-softBorder">
            <div>
              <div class="flex justify-between items-center mb-1">
                <h3 class="font-display text-lg font-bold text-inkDark">Gold</h3>
                <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded-full bg-blue-100 text-electricCobalt">Popular</span>
              </div>
              <p class="text-[11px] text-inkMuted mb-3">Keep up with enterprise pace.</p>
              
              <div class="mb-3">
                <span id="goldPrice" class="text-3xl font-display font-extrabold text-inkDark">$4,999</span>
                <span class="text-xs text-inkMuted">/ month</span>
              </div>

              <!-- Compact Feature List -->
              <div class="space-y-2 mb-4 text-xs">
                <div class="p-2 rounded-xl bg-blue-50/70 border border-blue-200/70 flex items-center justify-between">
                  <span class="font-bold text-inkDark">Sleep: 8h -> 3h</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-blue-100 text-electricCobalt">266% Speed</span>
                </div>
                <div class="p-2 rounded-xl bg-neutral-50 border border-neutral-200/60 flex items-center justify-between">
                  <span class="font-medium text-inkDark">Zero Thought Ads</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-emerald-100 text-emerald-800">100% Ad-Free</span>
                </div>
                <div class="p-2 rounded-xl bg-neutral-50 border border-neutral-200/60 flex items-center justify-between">
                  <span class="font-medium text-inkDark">No Afternoon Lag</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-blue-100 text-electricCobalt">+180% Focus</span>
                </div>
                <div class="p-2 rounded-xl bg-neutral-50 border border-neutral-200/60 flex items-center justify-between">
                  <span class="font-medium text-inkDark">Memory Protection</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-neutral-200 text-neutral-700">1080p Recall</span>
                </div>
              </div>
            </div>

            <button onclick="openCheckoutModal('Gold', document.getElementById('goldPrice').textContent + '/mo')" class="w-full py-2.5 rounded-xl bg-inkDark text-white text-xs font-bold hover:bg-neutral-800 transition-all shadow-sm">
              Upgrade to Gold ($4,999/mo)
            </button>
          </div>

          <!-- Platinum (Featured: Clean, crisp, white, no rolling beam) -->
          <div class="clean-card platinum-card-featured rounded-2xl p-5 flex flex-col justify-between bg-white relative">
            <div class="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-0.5 rounded-full bg-electricCobalt text-white text-[10px] font-mono font-bold tracking-wide shadow-sm">
              Ryan's Plan (Executive)
            </div>
            <div>
              <div class="flex justify-between items-center mb-1">
                <h3 class="font-display text-lg font-bold text-inkDark">Platinum</h3>
                <span class="text-[10px] font-mono font-extrabold px-2 py-0.5 rounded-full bg-blue-100 text-electricCobalt">100X Scale</span>
              </div>
              <p class="text-[11px] text-inkMuted mb-3">For managers working 120h straight.</p>
              
              <div class="mb-3">
                <span id="platinumPrice" class="text-3xl font-display font-extrabold text-electricCobalt">$14,999</span>
                <span class="text-xs text-inkMuted">/ month</span>
              </div>

              <!-- Compact Feature List (Light, clean, high contrast) -->
              <div class="space-y-2 mb-4 text-xs">
                <div class="p-2 rounded-xl bg-blue-50/80 border border-blue-200 flex items-center justify-between">
                  <span class="font-extrabold text-electricCobalt">Sleep Deprecated (0.0h)</span>
                  <span class="font-mono text-[10px] font-extrabold px-1.5 py-0.5 rounded bg-electricCobalt text-white">Work 24/7</span>
                </div>
                <div class="p-2 rounded-xl bg-neutral-50 border border-neutral-200/60 flex items-center justify-between">
                  <span class="font-bold text-inkDark">Bereavement Override</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-amber-100 text-amber-900">Zero Grief</span>
                </div>
                <div class="p-2 rounded-xl bg-neutral-50 border border-neutral-200/60 flex items-center justify-between">
                  <span class="font-bold text-inkDark">Double Salary Guarantee</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-emerald-100 text-emerald-800">2x Velocity</span>
                </div>
                <div class="p-2 rounded-xl bg-neutral-50 border border-neutral-200/60 flex items-center justify-between">
                  <span class="font-bold text-inkDark">4K Memory Recall</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-indigo-100 text-indigo-900">Spreadsheets</span>
                </div>
              </div>
            </div>

            <button onclick="openCheckoutModal('Platinum', document.getElementById('platinumPrice').textContent + '/mo')" class="w-full py-2.5 rounded-xl bg-electricCobalt text-white text-xs font-bold hover:bg-electricHover transition-all shadow-md shadow-blue-500/20">
              Activate Platinum ($14,999/mo)
            </button>
          </div>

        </div>

        <p class="text-center text-[11px] text-inkMuted mt-4">
          All plans non-refundable. Questions? Call <strong class="text-inkDark">1-800-MY-BRAIN</strong>.
        </p>
      </div>
    </section>"""

html = re.sub(old_plans_regex, new_plans, html, flags=re.DOTALL)

with open('academics/PREC_115/unessay/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully replaced plans section with ultra-compact viewport-fitted layout!")
