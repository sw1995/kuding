from django import template

register = template.Library()

# @register
@register.filter(name="strf_time")
def strf_time(value):
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(value/1000))



@register.filter(name="strd_time")
def strd_time(value):
    import time
    return time.strftime("%Y-%m-%d", time.localtime(value / 1000))