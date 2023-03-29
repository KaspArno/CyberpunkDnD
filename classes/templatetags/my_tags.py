from django import template

register = template.Library()

@register.filter
def make_sequence(n):
    return range(n)

@register.filter
def add_suffix(n):
    j = n % 10
    k = n % 100

    if (j == 1 and k != 11): return f"{n}st"
    if (j == 2 and k != 12): return f"{n}nd"
    if (j == 3 and k != 13): return f"{n}rd"
    return f"{n}th"