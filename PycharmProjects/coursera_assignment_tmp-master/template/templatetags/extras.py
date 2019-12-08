from django import template
register = template.Library()

@register.filter
def inc(value, a):
    ans = int(value)+int(a)
    return ans


@register.simple_tag
def division(value, b, to_int = False):
    ans = int(value) / int(b)
    if(to_int==False):
        return ans
    else:
        return int(ans)
