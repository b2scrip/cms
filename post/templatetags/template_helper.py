from django import template
register = template.Library()

@register.filter(name="css", is_safe=True)
def css_filter(form, css):
    if 'class' in form.field.widget.attrs:
        form.field.widget.attrs['class'] += " %s" % css
    else:
        form.field.widget.attrs['class'] = css
    return form
