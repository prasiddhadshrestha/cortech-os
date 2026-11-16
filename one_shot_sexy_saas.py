import re

with open('academics/PREC_115/unessay/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update <style> with sexy dark SaaS pricing styles & gorgeous volumetric hover glow
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
    .subtle-grid {
      background-image: radial-gradient(rgba(10, 13, 20, 0.06) 1px, transparent 1px);
      background-size: 28px 28px;
    }
    .badge-pill {
      background: rgba(15, 98, 254, 0.08);
      color: #0F62FE;
    }

    /* Sexy Dark SaaS Pricing Section */
    .saas-dark-section {
      background: radial-gradient(circle at 50% 0%, #111C38 0%, #090E1A 55%, #05070D 100%);
      position: relative;
      overflow: hidden;
    }
    .saas-dark-section::before {
      content: '';
      position: absolute;
      inset: 0;
      background-size: 32px 32px;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
      pointer-events: none;
    }

    /* Sexy Dark Glass Cards */
    .dark-saas-card {
      background: rgba(13, 18, 30, 0.85);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid rgba(255, 255, 255, 0.10);
      box-shadow: 0 15px 35px -5px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(255, 255, 255, 0.12);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }
    .dark-saas-card:hover {
      transform: translateY(-6px);
    }

    /* Standard Card Hover Glow */
    .standard-hover:hover {
      border-color: rgba(239, 68, 68, 0.65) !important;
      box-shadow: 0 0 45px rgba(239, 68, 68, 0.3), 0 20px 45px -10px rgba(0, 0, 0, 0.75) !important;
    }

    /* Gold Card Hover Glow */
    .gold-hover:hover {
      border-color: rgba(0, 240, 255, 0.8) !important;
      box-shadow: 0 0 50px rgba(14, 165, 233, 0.45), 0 0 80px rgba(0, 240, 255, 0.25), 0 20px 45px -10px rgba(0, 0, 0, 0.75) !important;
    }

    /* Platinum Card: Permanent Subtle Aura + Exploding Radiant Neon Glow on Hover */
    .platinum-featured-saas {
      border: 2px solid #0F62FE !important;
      box-shadow: 0 0 35px rgba(15, 98, 254, 0.35), 0 15px 40px -5px rgba(0, 0, 0, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.25) !important;
    }
    .platinum-featured-saas:hover {
      border-color: #00F0FF !important;
      box-shadow: 0 0 75px rgba(0, 240, 255, 0.65), 0 0 130px rgba(15, 98, 254, 0.45), 0 25px 60px -10px rgba(0, 0, 0, 0.85) !important;
      transform: translateY(-8px) scale(1.02) !important;
    }
  </style>"""

html = re.sub(old_style_regex, new_style, html, flags=re.DOTALL)

# 2. Replace the plans section with the Sexy Dark Blue SaaS layout (ultra-compact, ~580px total height, fits 100% in viewport)
old_plans_regex = r'<section id="plans".*?</section>'

new_plans = """<section id="plans" class="saas-dark-section pt-7 pb-9 px-6 text-white border-t border-b border-white/10">
      <div class="max-w-5xl mx-auto relative z-10">
        
        <!-- Header: Sexy Dark SaaS Typography -->
        <div class="text-center max-w-xl mx-auto mb-5">
          <p class="text-[11px] font-mono font-bold text-cyan-400 uppercase tracking-widest mb-1">Workforce Licensing</p>
          <h2 class="font-display text-2xl sm:text-3xl font-black text-white tracking-tight mb-1">Choose your cognitive tax bracket.</h2>
          <p class="text-slate-400 text-xs mb-3">In today's economy, you get the thoughts you can afford.</p>

          <!-- Sleek Glassmorphism Billing Switcher -->
          <div class="inline-flex items-center gap-1.5 p-1 rounded-full bg-slate-900/80 border border-white/15 backdrop-blur-md">
            <button id="monthlyBtn" onclick="setBilling('monthly')" class="px-4 py-1 rounded-full text-xs font-bold bg-blue-600 text-white shadow-md shadow-blue-600/30 transition-all">Monthly</button>
            <button id="annualBtn" onclick="setBilling('annual')" class="px-4 py-1 rounded-full text-xs font-bold text-slate-300 hover:text-white transition-all flex items-center gap-1">
              <span>Annual</span>
              <span class="text-[10px] font-bold text-cyan-300 font-mono">Save 20%</span>
            </button>
          </div>
        </div>

        <!-- Compact 3-Card Grid (Ultra-sexy dark blue SaaS cards, fits on single laptop screen) -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-5 items-stretch">

          <!-- Standard ($0) -->
          <div class="dark-saas-card standard-hover rounded-2xl p-5 flex flex-col justify-between">
            <div>
              <div class="flex justify-between items-center mb-1">
                <h3 class="font-display text-lg font-bold text-white">Standard</h3>
                <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded-full bg-slate-800/80 text-slate-400 border border-slate-700">Free Tier</span>
              </div>
              <p class="text-[11px] text-slate-400 mb-2.5">For interns and clinical trials.</p>
              
              <div class="mb-3">
                <span class="text-3xl font-display font-black text-white">$0</span>
                <span class="text-xs font-mono text-slate-500">/ month</span>
              </div>

              <!-- Feature rows -->
              <div class="space-y-2 mb-4 text-xs">
                <div class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] flex items-center justify-between">
                  <span class="font-medium text-slate-200">Ad-Supported Thoughts</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/30">10 Min Ads</span>
                </div>
                <div class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] flex items-center justify-between">
                  <span class="font-medium text-slate-200">2:00 PM Bandwidth Curfew</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">2G Speed</span>
                </div>
                <div class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] flex items-center justify-between">
                  <span class="font-medium text-slate-200">5-Hour Sleep Cap</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">Strict Cap</span>
                </div>
                <div class="p-2 rounded-xl bg-rose-950/30 border border-rose-500/30 flex items-center justify-between font-mono">
                  <span class="font-bold text-rose-300 text-[11px]">EXIT RESTOCKING FEE</span>
                  <span class="text-rose-400 font-extrabold text-xs">$5,000 USD</span>
                </div>
              </div>
            </div>

            <button onclick="openCheckoutModal('Standard', '$0/mo')" class="w-full py-2.5 rounded-xl border border-white/20 text-xs font-bold text-slate-200 hover:bg-white/10 transition-all">
              Select Standard ($0)
            </button>
          </div>

          <!-- Gold ($4,999) -->
          <div class="dark-saas-card gold-hover rounded-2xl p-5 flex flex-col justify-between">
            <div>
              <div class="flex justify-between items-center mb-1">
                <h3 class="font-display text-lg font-bold text-white">Gold</h3>
                <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded-full bg-cyan-500/20 text-cyan-300 border border-cyan-500/40">Popular</span>
              </div>
              <p class="text-[11px] text-slate-400 mb-2.5">Keep up with enterprise pace.</p>
              
              <div class="mb-3">
                <span id="goldPrice" class="text-3xl font-display font-black text-cyan-400">$4,999</span>
                <span class="text-xs font-mono text-slate-500">/ month</span>
              </div>

              <!-- Feature rows -->
              <div class="space-y-2 mb-4 text-xs">
                <div class="p-2 rounded-xl bg-cyan-950/30 border border-cyan-500/30 flex items-center justify-between">
                  <span class="font-bold text-white">Sleep: 8h -> 3h</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-300">266% Speed</span>
                </div>
                <div class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] flex items-center justify-between">
                  <span class="font-medium text-slate-200">Zero Thought Ads</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">100% Ad-Free</span>
                </div>
                <div class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] flex items-center justify-between">
                  <span class="font-medium text-slate-200">No Afternoon Lag</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-300">+180% Focus</span>
                </div>
                <div class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] flex items-center justify-between">
                  <span class="font-medium text-slate-200">Memory Protection</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">1080p Recall</span>
                </div>
              </div>
            </div>

            <button onclick="openCheckoutModal('Gold', document.getElementById('goldPrice').textContent + '/mo')" class="w-full py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold shadow-lg shadow-blue-600/30 transition-all">
              Upgrade to Gold ($4,999/mo)
            </button>
          </div>

          <!-- Platinum ($14,999: Sexy featured dark card with electric blue glow) -->
          <div class="dark-saas-card platinum-featured-saas rounded-2xl p-5 flex flex-col justify-between">
            <div class="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-0.5 rounded-full bg-gradient-to-r from-blue-600 to-cyan-500 text-white text-[10px] font-mono font-extrabold tracking-wide shadow-md shadow-cyan-500/30">
              Ryan's Plan (Executive)
            </div>
            <div>
              <div class="flex justify-between items-center mb-1">
                <h3 class="font-display text-lg font-bold text-white">Platinum</h3>
                <span class="text-[10px] font-mono font-extrabold px-2 py-0.5 rounded-full bg-cyan-400/20 text-cyan-300 border border-cyan-400/40">100X Scale</span>
              </div>
              <p class="text-[11px] text-slate-400 mb-2.5">For managers working 120h straight.</p>
              
              <div class="mb-3">
                <span id="platinumPrice" class="text-3xl font-display font-black text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-400">$14,999</span>
                <span class="text-xs font-mono text-slate-500">/ month</span>
              </div>

              <!-- Feature rows -->
              <div class="space-y-2 mb-4 text-xs">
                <div class="p-2 rounded-xl bg-blue-950/40 border border-blue-500/40 flex items-center justify-between">
                  <span class="font-extrabold text-cyan-300">Sleep Deprecated (0.0h)</span>
                  <span class="font-mono text-[10px] font-extrabold px-1.5 py-0.5 rounded bg-cyan-400 text-black">Work 24/7</span>
                </div>
                <div class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] flex items-center justify-between">
                  <span class="font-bold text-white">Bereavement Override</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">Zero Grief</span>
                </div>
                <div class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] flex items-center justify-between">
                  <span class="font-bold text-white">Double Salary Guarantee</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">2x Velocity</span>
                </div>
                <div class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] flex items-center justify-between">
                  <span class="font-bold text-white">4K Memory Recall</span>
                  <span class="font-mono text-[10px] font-bold px-1.5 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/30">Spreadsheets</span>
                </div>
              </div>
            </div>

            <button onclick="openCheckoutModal('Platinum', document.getElementById('platinumPrice').textContent + '/mo')" class="w-full py-2.5 rounded-xl bg-gradient-to-r from-blue-600 via-indigo-600 to-cyan-500 hover:from-blue-500 hover:to-cyan-400 text-white text-xs font-black shadow-xl shadow-cyan-500/30 transition-all">
              Activate Platinum ($14,999/mo)
            </button>
          </div>

        </div>

        <p class="text-center text-[11px] font-mono text-slate-500 mt-3.5">
          All plans non-refundable. Questions? Call <strong class="text-slate-300">1-800-MY-BRAIN</strong>.
        </p>
      </div>
    </section>"""

html = re.sub(old_plans_regex, new_plans, html, flags=re.DOTALL)

# Ensure toggle button classes support the new dark background
html = html.replace("mBtn.className = 'px-5 py-2 rounded-full text-xs font-bold bg-inkDark text-white transition-all';", "mBtn.className = 'px-4 py-1 rounded-full text-xs font-bold bg-blue-600 text-white shadow-md shadow-blue-600/30 transition-all';")
html = html.replace("aBtn.className = 'px-5 py-2 rounded-full text-xs font-bold bg-inkDark text-white transition-all flex items-center gap-1.5';", "aBtn.className = 'px-4 py-1 rounded-full text-xs font-bold bg-blue-600 text-white shadow-md shadow-blue-600/30 transition-all flex items-center gap-1';")
html = html.replace("aBtn.className = 'px-5 py-2 rounded-full text-xs font-bold text-inkMuted hover:text-inkDark transition-all flex items-center gap-1.5';", "aBtn.className = 'px-4 py-1 rounded-full text-xs font-bold text-slate-300 hover:text-white transition-all flex items-center gap-1';")
html = html.replace("mBtn.className = 'px-5 py-2 rounded-full text-xs font-bold text-inkMuted hover:text-inkDark transition-all';", "mBtn.className = 'px-4 py-1 rounded-full text-xs font-bold text-slate-300 hover:text-white transition-all';")

with open('academics/PREC_115/unessay/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("ONE-SHOT COMPLETE: Sexy dark blue SaaS styling + glowing hover physics applied!")
