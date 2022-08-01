from django import template
register = template.Library()


def phonenumber(value):
    phone = str(value)
    code = phone[0:2]
    first = phone[2:5]
    second = phone[5:8]
    third = phone[8:12]
    return code + '(' + first + ')' + ' ' + second + '-' + third

register.filter('phonenumber', phonenumber)