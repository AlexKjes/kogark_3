def triangle(position,  x0,  x1,  x2, clip=1):
    value = 0.0
    if x0 <= position <= x1:
        value = (position - x0) / (x1 - x0)
    elif x1 <= position <= x2:
        value = (x2 - position) / (x1 - x0)
    if value > clip:
        value = clip
    return value


def grade(position,  x0,  x1,  clip=1):
    if position >= x1:
        value = 1.0
    elif position <= x0:
        value = 0.0
    else:
        value = (position - x0) / (x1 - x0)
    if value > clip:
        value = clip
    return value


def reverse_grade(position,  x0,  x1,  clip=1):
    if position <= x0:
        value = 1.0
    elif position >= x1:
        value = 0.0
    else:
        value = (x1 - position) / (x1 - x0)
    if value > clip:
        value = clip
    return value