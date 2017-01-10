from django import forms


# This is creating the datalist to be used by the form
class ListTextWidget(forms.TextInput):

    # Name:     __init__
    # Purpose:  Constructor
    def __init__(self, data_list, name, *args, **kwargs):
        super(ListTextWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._list = data_list
        self.attrs.update({'list':'list__%s' % self._name})

    # Name:     render
    # Purpose:  This is writing the datalist html code to be used by the form
    # Return:   The html text and the html code for the datalist
    def render(self, name, value, attrs=None):
        text_html = super(ListTextWidget, self).render(name, value, attrs=attrs)
        data_list = '<datalist id="list__%s">' % self._name
        for item in self._list:
            data_list += '<option value="%s">' % item
        data_list += '</datalist>'

        return text_html + data_list
