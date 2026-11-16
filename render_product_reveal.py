import os
import math
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Canvas specs
W, H = 1920, 1080
FPS = 30
DURATION = 5.0 # seconds
TOTAL_FRAMES = int(FPS * DURATION)

# Load chip image
chip_path = 'academics/PREC_115/unessay/cortech_chip_transparent.png'
chip_base = Image.open(chip_path).convert('RGBA')

# Windows fonts
font_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 40)
font_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 18)
font_callout_h = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 20)
font_callout_b = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 15)
font_mono = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 14)

# Temp dir for frames
temp_dir = 'academics/PREC_115/unessay/temp_product_frames'
os.makedirs(temp_dir, exist_ok=True)

print(f"Rendering {TOTAL_FRAMES} frames of CortechOS 3D Product Motion...")

for frame_idx in range(TOTAL_FRAMES):
    t = frame_idx / FPS # current time in seconds
    progress = frame_idx / TOTAL_FRAMES

    # 1. Background studio canvas (Deep Obsidian to Midnight Navy)
    frame = Image.new('RGB', (W, H), (6, 9, 15))
    draw = ImageDraw.Draw(frame)

    # Ambient radial studio spotlight behind the chip
    cx, cy = W // 2, H // 2
    for r in range(450, 0, -12):
        alpha = int(45 * (1 - r / 450))
        draw.ellipse([cx - r, cy - r + 30, cx + r, cy + r + 30], fill=(12 + alpha//2, 22 + alpha, 45 + alpha*2))

    # Grid floor (perspective lines receding)
    floor_y = 780
    for i in range(-12, 13):
        x_top = cx + i * 40
        x_bot = cx + i * 160
        draw.line([(x_top, floor_y), (x_bot, H)], fill=(20, 32, 52), width=1)
    for y_line in range(floor_y, H, 35):
        draw.line([(0, y_line), (W, y_line)], fill=(16, 26, 44), width=1)

    # 2. Holographic Pedestal Ring beneath chip
    pedestal_y = 740
    # Rotating pulse on pedestal
    ring_angle = (t * 60) % 360
    pedestal_w = 460 + math.sin(t * 3) * 15
    pedestal_h = 100
    
    # Outer ring
    draw.ellipse([cx - pedestal_w//2, pedestal_y - pedestal_h//2, cx + pedestal_w//2, pedestal_y + pedestal_h//2], outline=(15, 98, 254, 120), width=2)
    # Inner ring
    inner_w, inner_h = pedestal_w * 0.7, pedestal_h * 0.7
    draw.ellipse([cx - inner_w//2, pedestal_y - inner_h//2, cx + inner_w//2, pedestal_y + inner_h//2], outline=(0, 240, 255, 180), width=1)

    # Rotating tick dots on outer ring
    for deg in range(0, 360, 45):
        rad = math.radians(deg + ring_angle)
        dx = cx + (pedestal_w // 2) * math.cos(rad)
        dy = pedestal_y + (pedestal_h // 2) * math.sin(rad)
        draw.ellipse([dx - 3, dy - 2, dx + 3, dy + 2], fill=(0, 240, 255))

    # 3. Chip Hover Physics & 3D Tilt
    hover_y = cy - 30 + math.sin(t * math.pi * 1.5) * 22
    chip_scale = 1.65 + math.sin(t * math.pi * 0.8) * 0.08
    chip_angle = math.sin(t * math.pi * 1.2) * 4.0 # subtle wobble

    # Scale and rotate chip
    new_w = int(chip_base.width * chip_scale)
    new_h = int(chip_base.height * chip_scale)
    scaled_chip = chip_base.resize((new_w, new_h), Image.Resampling.BICUBIC)
    if abs(chip_angle) > 0.1:
        rotated_chip = scaled_chip.rotate(chip_angle, resample=Image.Resampling.BICUBIC, expand=True)
    else:
        rotated_chip = scaled_chip

    # Drop shadow on the pedestal
    shadow_w = int(new_w * 0.8)
    shadow_h = 35
    shadow_y = pedestal_y - 10
    shadow_img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_img)
    s_draw.ellipse([cx - shadow_w//2, shadow_y - shadow_h//2, cx + shadow_w//2, shadow_y + shadow_h//2], fill=(0, 0, 0, 160))
    shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(14))
    frame.paste(shadow_img, (0, 0), shadow_img)

    # Paste chip
    chip_x = int(cx - rotated_chip.width // 2)
    chip_y = int(hover_y - rotated_chip.height // 2)
    frame.paste(rotated_chip, (chip_x, chip_y), rotated_chip)

    # 4. Cinematic Laser / Anamorphic Flare Sweep (from t=1.2s to t=3.2s)
    if 1.0 <= t <= 3.5:
        flare_progress = (t - 1.0) / 2.5
        flare_x = int(cx - 350 + flare_progress * 700)
        flare_img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        f_draw = ImageDraw.Draw(flare_img)
        
        # Horizontal cyan anamorphic beam
        f_draw.line([(flare_x - 300, hover_y), (flare_x + 300, hover_y)], fill=(0, 240, 255, 140), width=3)
        f_draw.line([(flare_x - 120, hover_y), (flare_x + 120, hover_y)], fill=(255, 255, 255, 220), width=6)
        # Vertical glint
        f_draw.line([(flare_x, hover_y - 80), (flare_x, hover_y + 80)], fill=(0, 240, 255, 120), width=2)
        # Glow orb
        f_draw.ellipse([flare_x - 40, hover_y - 40, flare_x + 40, hover_y + 40], fill=(255, 255, 255, 180))
        flare_img = flare_img.filter(ImageFilter.GaussianBlur(8))
        frame.paste(flare_img, (0, 0), flare_img)

    # 5. Holographic HUD Callouts & Telemetry
    hud_overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    h_draw = ImageDraw.Draw(hud_overlay)

    # HUD Opacity fade-in (0 to 1 over first 0.8s)
    hud_alpha = min(1.0, t / 0.8)
    a_byte = int(255 * hud_alpha)

    # Top Title Badge
    h_draw.text((120, 80), "CORTECH-C1™ // NEURAL ACCELERATOR", fill=(255, 255, 255, a_byte), font=font_title)
    h_draw.text((120, 135), "THE AI-ASSISTED MONOPOLY PROCESSOR FOR HUMAN CONSCIOUSNESS", fill=(0, 240, 255, a_byte), font=font_sub)
    h_draw.line([(120, 170), (850, 170)], fill=(15, 98, 254, int(150 * hud_alpha)), width=1)

    # Top Right Status Telemetry
    h_draw.ellipse([W - 320, 92, W - 306, 106], fill=(34, 197, 94, a_byte))
    h_draw.text((W - 290, 88), "HARDWARE STATUS: ONLINE", fill=(148, 163, 184, a_byte), font=font_mono)
    h_draw.text((W - 320, 118), "SERIES: C-8891 // DIE SIZE: 4.8mm", fill=(100, 116, 139, a_byte), font=font_mono)

    # Callout 1 (Top Right: Head Synapse Core)
    node1_x = cx + 80
    node1_y = hover_y - 80
    box1_x = cx + 320
    box1_y = hover_y - 160
    h_draw.line([(node1_x, node1_y), (box1_x - 30, box1_y + 25), (box1_x + 320, box1_y + 25)], fill=(0, 240, 255, a_byte), width=2)
    h_draw.ellipse([node1_x - 5, node1_y - 5, node1_x + 5, node1_y + 5], fill=(0, 240, 255, a_byte))
    h_draw.text((box1_x, box1_y), "SYNAPSE CO-PROCESSOR // 4.2 GHz", fill=(255, 255, 255, a_byte), font=font_callout_h)
    h_draw.text((box1_x, box1_y + 32), "1,024 High-Bandwidth Neural Electrodes", fill=(148, 163, 184, a_byte), font=font_callout_b)

    # Callout 2 (Left: Spine Compression Engine)
    node2_x = cx - 110
    node2_y = hover_y + 20
    box2_x = cx - 580
    box2_y = hover_y - 20
    h_draw.line([(node2_x, node2_y), (box2_x + 320, box2_y + 25), (box2_x, box2_y + 25)], fill=(15, 98, 254, a_byte), width=2)
    h_draw.ellipse([node2_x - 5, node2_y - 5, node2_x + 5, node2_y + 5], fill=(15, 98, 254, a_byte))
    h_draw.text((box2_x, box2_y), "SLEEP COMPRESSION BLOCK", fill=(255, 255, 255, a_byte), font=font_callout_h)
    h_draw.text((box2_x, box2_y + 32), "8h Biological Rest -> 3h Realized Output", fill=(148, 163, 184, a_byte), font=font_callout_b)

    # Callout 3 (Bottom Right: Outpatient Docking Legs)
    node3_x = cx + 60
    node3_y = hover_y + 110
    box3_x = cx + 320
    box3_y = hover_y + 90
    h_draw.line([(node3_x, node3_y), (box3_x - 30, box3_y + 25), (box3_x + 320, box3_y + 25)], fill=(245, 158, 11, a_byte), width=2)
    h_draw.ellipse([node3_x - 5, node3_y - 5, node3_x + 5, node3_y + 5], fill=(245, 158, 11, a_byte))
    h_draw.text((box3_x, box3_y), "CRANIAL DOCKING INTERFACE", fill=(245, 158, 11, a_byte), font=font_callout_h)
    h_draw.text((box3_x, box3_y + 32), "15-Minute Outpatient Procedure • 0% Down-Time", fill=(148, 163, 184, a_byte), font=font_callout_b)

    # Bottom Footer
    h_draw.line([(120, H - 90), (W - 120, H - 90)], fill=(255, 255, 255, int(40 * hud_alpha)), width=1)
    h_draw.text((120, H - 70), "COMPATIBLE WITH GOLD & PLATINUM TIERS  •  100% RENTED INTELLECTUAL PROPERTY  •  PATENT PENDING", fill=(100, 116, 139, a_byte), font=font_mono)
    h_draw.text((W - 360, H - 70), "© 2026 CORTECHOS™ CORP.", fill=(100, 116, 139, a_byte), font=font_mono)

    # Composite HUD
    frame.paste(hud_overlay, (0, 0), hud_overlay)

    # Save frame
    frame_filename = os.path.join(temp_dir, f"frame_{frame_idx:04d}.png")
    frame.save(frame_filename)

print("Frames rendered successfully. Encoding to MP4 via ffmpeg...")

# Encode to MP4 via ffmpeg
out_mp4 = 'academics/PREC_115/unessay/cortech_product_reveal.mp4'
cmd = [
    'ffmpeg', '-y',
    '-framerate', str(FPS),
    '-i', os.path.join(temp_dir, 'frame_%04d.png'),
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    '-crf', '18',
    out_mp4
]
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    print(f"SUCCESS: Generated {out_mp4}")
else:
    print("FFmpeg error:", res.stderr)

# Clean up temp frames
for f in os.listdir(temp_dir):
    os.remove(os.path.join(temp_dir, f))
os.rmdir(temp_dir)
print("Cleaned up temporary frames.")
