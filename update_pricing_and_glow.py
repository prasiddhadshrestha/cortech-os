import re

# 1. Update index.html
with open('academics/PREC_115/unessay/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update prices
html = html.replace('($499)', '($4,999)')
html = html.replace('($1,499)', '($14,999)')
html = html.replace('Unlocked at $499/mo', 'Unlocked at $4,999/mo')
html = html.replace("Can't afford $499 a month", "Can't afford $4,999 a month")
html = html.replace('Platinum Member ($1,499/mo)', 'Platinum Member ($14,999/mo)')
html = html.replace('id="goldPrice" class="text-4xl font-display font-extrabold text-inkDark">$499</span>', 'id="goldPrice" class="text-4xl font-display font-extrabold text-inkDark">$4,999</span>')
html = html.replace('Pay $499/mo to Keep Up', 'Pay $4,999/mo to Keep Up')
html = html.replace('id="platinumPrice" class="text-4xl font-display font-extrabold text-inkDark">$1,499</span>', 'id="platinumPrice" class="text-4xl font-display font-extrabold text-inkDark">$14,999</span>')
html = html.replace('Subscribe for $1,499/mo', 'Subscribe for $14,999/mo')
html = html.replace('id="checkoutSubtitle">$1,499/mo billed automatically', 'id="checkoutSubtitle">$14,999/mo billed automatically')

# JS object updates
html = html.replace("Gold membership ($499/mo)", "Gold membership ($4,999/mo)")
html = html.replace("value: '$499 / mo'", "value: '$4,999 / mo'")
html = html.replace("Platinum members ($1,499/mo)", "Platinum members ($14,999/mo)")
html = html.replace("value: '$1,499 / mo'", "value: '$14,999 / mo'")
html = html.replace("Ryan K.", "Ryan G.")

# Annual billing switcher
html = html.replace("goldPrice.textContent = '$499';", "goldPrice.textContent = '$4,999';")
html = html.replace("platPrice.textContent = '$1,499';", "platPrice.textContent = '$14,999';")
html = html.replace("goldPrice.textContent = '$399';", "goldPrice.textContent = '$4,199';")
html = html.replace("platPrice.textContent = '$1,199';", "platPrice.textContent = '$12,499';")

# 2. Add high-intensity glowing border lights CSS
old_style = """<style>
    body {
      background-color: #F8F9FA;
      color: #0A0D14;
      -webkit-font-smoothing: antialiased;
    }
    .clean-card {
      background: #FFFFFF;
      border: 1px solid rgba(10, 13, 20, 0.08);
      box-shadow: 0 4px 20px -2px rgba(10, 13, 20, 0.03);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .clean-card:hover {
      border-color: rgba(15, 98, 254, 0.3);
      box-shadow: 0 12px 32px -4px rgba(15, 98, 254, 0.08);
      transform: translateY(-2px);
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

new_style = """<style>
    body {
      background-color: #F8F9FA;
      color: #0A0D14;
      -webkit-font-smoothing: antialiased;
    }
    .clean-card {
      background: #FFFFFF;
      border: 1px solid rgba(10, 13, 20, 0.08);
      box-shadow: 0 4px 20px -2px rgba(10, 13, 20, 0.03);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }
    .clean-card:hover {
      border-color: #0F62FE;
      box-shadow: 0 0 35px rgba(15, 98, 254, 0.35), 0 16px 36px -4px rgba(15, 98, 254, 0.18);
      transform: translateY(-6px);
    }
    /* Gold Card Glowing Light */
    .gold-card:hover {
      border-color: #0F62FE !important;
      box-shadow: 0 0 45px rgba(15, 98, 254, 0.45), 0 0 80px rgba(0, 240, 255, 0.25), 0 20px 40px -4px rgba(15, 98, 254, 0.22) !important;
      transform: translateY(-7px) !important;
    }
    /* Permanent Animated Neon Border Beam for Platinum */
    .platinum-card-beam {
      position: relative;
      border: 2px solid #0F62FE !important;
      box-shadow: 0 0 40px rgba(15, 98, 254, 0.35), 0 0 80px rgba(15, 98, 254, 0.18), 0 16px 36px -4px rgba(0, 0, 0, 0.08) !important;
      overflow: hidden;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .platinum-card-beam:hover {
      border-color: #00F0FF !important;
      box-shadow: 0 0 65px rgba(0, 240, 255, 0.65), 0 0 120px rgba(15, 98, 254, 0.45), 0 24px 50px -10px rgba(0, 0, 0, 0.2) !important;
      transform: translateY(-8px) !important;
    }
    .neon-beam-scanner {
      position: absolute;
      inset: -2px;
      border-radius: 24px;
      padding: 2px;
      background: conic-gradient(from 0deg, transparent 0%, #0F62FE 20%, #00F0FF 45%, #0F62FE 70%, transparent 100%);
      -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      animation: rotateNeonBeam 3.2s linear infinite;
      pointer-events: none;
    }
    @keyframes rotateNeonBeam {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
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

html = html.replace(old_style, new_style)

# Apply classes to Gold and Platinum cards in the pricing grid
html = html.replace('<!-- Gold -->\n          <div class="clean-card rounded-3xl p-8 flex flex-col justify-between">', '<!-- Gold -->\n          <div class="clean-card gold-card rounded-3xl p-8 flex flex-col justify-between">')

old_plat_markup = """          <!-- Platinum (Featured) -->
          <div class="clean-card rounded-3xl p-8 flex flex-col justify-between border-2 border-electricCobalt relative shadow-lg">"""

new_plat_markup = """          <!-- Platinum (Featured with Glowing Border Lights) -->
          <div class="clean-card platinum-card-beam rounded-3xl p-8 flex flex-col justify-between relative">
            <div class="neon-beam-scanner"></div>"""

html = html.replace(old_plat_markup, new_plat_markup)

with open('academics/PREC_115/unessay/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html with $4,999 and $14,999 plus glowing border lights!")

# 2. Update cortech_motion_reel.html
with open('academics/PREC_115/unessay/cortech_motion_reel.html', 'r', encoding='utf-8') as f:
    reel = f.read()

reel = reel.replace('$499', '$4,999')
reel = reel.replace('$1,499', '$14,999')
reel = reel.replace('FOCUS: GOLD ($499/MO)', 'FOCUS: GOLD ($4,999/MO)')
reel = reel.replace('FOCUS: PLATINUM ($1,499/MO)', 'FOCUS: PLATINUM ($14,999/MO)')

with open('academics/PREC_115/unessay/cortech_motion_reel.html', 'w', encoding='utf-8') as f:
    f.write(reel)
print("Updated cortech_motion_reel.html with $4,999 and $14,999!")
