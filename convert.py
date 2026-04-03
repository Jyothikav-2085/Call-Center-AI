# import base64

# with open("input_audio.mp3", "rb") as f:
#     encoded = base64.b64encode(f.read()).decode()

# print(encoded)

import base64

with open("input_audio.mp3", "rb") as f:
    encoded = base64.b64encode(f.read()).decode()

print(encoded)