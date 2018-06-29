from django import template
register = template.Library()

@register.filter
def counter(obj):
    return obj.votes.count()
