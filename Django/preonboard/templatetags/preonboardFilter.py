from django import template


register = template.Library()


@register.filter #이 어노테이션 적용시 템플릿에서 해당 함수를 필터로 사용가능.
def sub(value, arg):
    return value - arg