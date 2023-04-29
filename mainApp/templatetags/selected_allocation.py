import calendar

from django import template
from ..models import Hydrant, Reservoir, check_up_reservoir, check_up_hydrant

register = template.Library()


@register.simple_tag
def volume_level(length,width,depth):
    return length*width*depth

@register.simple_tag
def recent_check_up(id):
    r = Reservoir.objects.get(id=id)
    c_r = check_up_reservoir.objects.filter(Reservoir=r,confirmed=True).order_by('-created_at')
    return c_r[0].created_at if c_r else None  

@register.simple_tag
def recent_hydrant_check_up(id):
    r = Hydrant.objects.get(id=id)
    c_r = check_up_hydrant.objects.filter(Hydrant=r,confirmed=True).order_by('-created_at')
    return c_r[0].created_at if c_r else None  

@register.simple_tag
def amount_of_water_in_percent(id):
    r = Reservoir.objects.get(id=id)
    c_r = check_up_reservoir.objects.filter(Reservoir=r,confirmed=True).order_by('-created_at').first()
    print("________________")
    if c_r is not None:
        print(c_r.id)
        distance=check_up_reservoir.objects.get(id=c_r.id)
        print(distance.distance)
        return r.length*r.width*r.depth-(distance.distance*r.width*r.length)
    # check_up_reservoir=objects.filter
    print("________________")
    return None