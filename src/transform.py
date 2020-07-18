import math


def rel_luminance(rgb_8):

    r_norm = rgb_8[0] / 255
    g_norm = rgb_8[1] / 255
    b_norm = rgb_8[2] / 255

    if r_norm <= 0.03928:
        r_lum = r_norm / 12.92
    else:
        r_lum = ((r_norm + 0.055) / 1.055) ** 2.4

    if g_norm <= 0.03928:
        g_lum = g_norm / 12.92
    else:
        g_lum = ((g_norm + 0.055) / 1.055) ** 2.4

    if b_norm <= 0.03928:
        b_lum = b_norm / 12.92
    else:
        b_lum = ((b_norm + 0.055) / 1.055) ** 2.4

    rel_lum = 0.2126 * r_lum + 0.7152 * g_lum + 0.0722 * b_lum

    return rel_lum


def contrast_ratio(rgb_1, rgb_2):

    lum_1 = rel_luminance(rgb_1)
    lum_2 = rel_luminance(rgb_2)

    lt_dk = sorted([lum_1, lum_2])

    return (lt_dk[1] + 0.05) / (lt_dk[0] + 0.05)


if __name__ == '__main__':
    rgb_1 = (233, 251, 233)
    rgb_2 = (23, 130, 23)
    print(contrast_ratio(rgb_1, rgb_2))