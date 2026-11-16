import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

w, h = 1920, 1080

def create_card(filename, badge_text, badge_color, border_color, name_text, title_text, quote_text, footer_text, id_text):
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    
    font_name = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 44)
    font_badge = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 17)
    font_title = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 24)
    font_quote = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 24)
    font_fine = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 14)

    c_x1 = 120
    c_y1 = 760
    c_x2 = 1060
    c_y2 = 975
    c_r = 16

    # Shadow
    shadow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([c_x1 - 10, c_y1 - 5, c_x2 + 10, c_y2 + 25], radius=c_r + 4, fill=(0, 0, 0, 200))
    shadow = shadow.filter(ImageFilter.GaussianBlur(22))
    overlay = Image.alpha_composite(overlay, shadow)
    
    draw = ImageDraw.Draw(overlay)
    # Background glass
    draw.rounded_rectangle([c_x1, c_y1, c_x2, c_y2], radius=c_r, fill=(11, 16, 26, 235), outline=border_color, width=2)
    # Left accent bar
    draw.rounded_rectangle([c_x1, c_y1, c_x1 + 8, c_y2], radius=4, fill=badge_color)

    # Pill Badge
    b_x1 = c_x1 + 32
    b_y1 = c_y1 + 22
    b_x2 = b_x1 + 225
    b_y2 = b_y1 + 32
    draw.rounded_rectangle([b_x1, b_y1, b_x2, b_y2], radius=16, fill=(badge_color[0], badge_color[1], badge_color[2], 45), outline=badge_color, width=1)
    
    # Active indicator dot
    draw.ellipse([b_x1 + 14, b_y1 + 11, b_x1 + 24, b_y1 + 21], fill=badge_color)
    draw.text((b_x1 + 34, b_y1 + 5), badge_text, fill=(240, 245, 255, 255), font=font_badge)
    draw.text((b_x2 + 16, b_y1 + 7), id_text, fill=(148, 163, 184, 230), font=font_badge)

    # Name & Title
    draw.text((c_x1 + 32, c_y1 + 64), name_text, fill=(255, 255, 255, 255), font=font_name)
    draw.text((c_x1 + 250, c_y1 + 80), title_text, fill=(148, 163, 184, 255), font=font_title)

    # Dividing line
    draw.line([(c_x1 + 32, c_y1 + 128), (c_x2 - 32, c_y1 + 128)], fill=(255, 255, 255, 35), width=1)

    # Quote
    draw.text((c_x1 + 32, c_y1 + 142), quote_text, fill=(241, 245, 249, 255), font=font_quote)

    # Footnote
    draw.text((c_x1 + 32, c_y1 + 182), footer_text, fill=(100, 116, 139, 220), font=font_fine)

    out_path = os.path.join('academics/PREC_115/unessay', filename)
    overlay.save(out_path, 'PNG')
    print('Generated transparent lower third:', out_path)

# Ryan G (Platinum)
create_card(
    filename='ryan_lower_third_transparent.png',
    badge_text='CORTECH PLATINUM™',
    badge_color=(15, 98, 254, 255), # Electric Cobalt
    border_color=(15, 98, 254, 180),
    name_text='RYAN G.',
    title_text='|   Senior Optimization Associate',
    quote_text='"Has not slept in 120 hours. Views unconsciousness as unpaid downtime."',
    footer_text='VERIFIED ENTERPRISE TESTIMONIAL  •  EMOTIONAL LATENCY: 0.00ms  •  PAID SUBSCRIBER',
    id_text='ID: #00412-R | TIER: $1,999/MO'
)

# Michael T (Standard)
create_card(
    filename='michael_lower_third_transparent.png',
    badge_text='CORTECH STANDARD',
    badge_color=(220, 38, 38, 255), # Crimson Red
    border_color=(220, 38, 38, 180),
    name_text='MICHAEL T.',
    title_text='|   Junior Associate (Unoptimized)',
    quote_text='"Brain throttled to 2G. Currently experiencing audio ads in left ear."',
    footer_text='DELINQUENT RETENTION NOTICE  •  CANCELLATION PENALTY DUE: $5,000.00 USD',
    id_text='STATUS: AD-SUPPORTED ($0/MO)'
)
