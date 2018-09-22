from django import template

register = template.Library()

# @register
@register.filter(name="strf_time")
def strf_time(value):
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(value))



@register.filter(name="strd_time")
def strd_time(value):
    import time
    return time.strftime("%Y-%m-%d %H:%M", time.localtime(value))
