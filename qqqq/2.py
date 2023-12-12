def check_color(rgb):
    r, g, b = rgb
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        if g > (r + b) / 2 + 30:
            return "Green"
        else:
            return "Not Green"
    else:
        return "Value Out of Range"

color = input("RGB: ")
colors = [int(color) for color in color.split(',')]

colors = [(colors[i], colors[i + 1], colors[i + 2]) for i in range(0, len(colors), 3)]

for color in colors:
    result = check_color(color)
    print(f"{result}")
