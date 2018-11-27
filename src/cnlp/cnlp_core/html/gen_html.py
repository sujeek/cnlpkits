# -*- encoding=utf-8 -*-


def tag(name, cls=None, *content,  **attrs):
    """生成一个多标签的html页面"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        print attr_str
        return '<%s%s />' % (name,attr_str)


print tag('p')
print tag('p',None,'hello','world')

my_tag = {'name':'img','title':'helloworld','src':'sum.jpg'}
print tag(**my_tag)


