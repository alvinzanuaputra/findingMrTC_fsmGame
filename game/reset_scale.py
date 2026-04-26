import re

path = r"c:\Users\User\Downloads\findingMrTC_fsmGame-main\findingMrTC_fsmGame-main\game\script.rpy"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Default scale adjustments based on user screenshots
content = content.replace("define scale_char_kalab_ap = 1.6", "define scale_char_kalab_ap = 1.0")
content = content.replace("define scale_char_kalab_santai = 1.6", "define scale_char_kalab_santai = 1.0")
content = content.replace("define scale_char_kalab_netics = 1.6", "define scale_char_kalab_netics = 1.0")
content = content.replace("define scale_char_kalab_kbj = 1.5", "define scale_char_kalab_kbj = 1.0")
content = content.replace("define scale_char_kalab_kcv = 1.6", "define scale_char_kalab_kcv = 1.0")
content = content.replace("define scale_char_kalab_pkt = 1.8", "define scale_char_kalab_pkt = 1.0")
content = content.replace("define scale_char_kalab_mci = 1.6", "define scale_char_kalab_mci = 1.0")
content = content.replace("define scale_char_kalab_giga = 1.6", "define scale_char_kalab_giga = 1.0")
content = content.replace("define scale_char_kating = 1.6", "define scale_char_kating = 1.0")
content = content.replace("define scale_char_tc = 1.6", "define scale_char_tc = 1.0")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done resetting scales to 1.0")
