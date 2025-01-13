import math

AB = int(input().strip())
BC = int(input().strip())

AC = math.sqrt(AB**2 + BC**2)
MB = AC / 2

cos_MBC = BC / (2 * MB)
angle_MBC_rad = math.acos(cos_MBC)
angle_MBC_deg = round(math.degrees(angle_MBC_rad))

print(f"{angle_MBC_deg}\u00B0")
