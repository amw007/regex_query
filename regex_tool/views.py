import re

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from regex_tool.form import RegexForm



def validate_regex(regex):
    try:
        re.compile(regex)
        is_valid = True

    except re.error:
        is_valid = False
    return is_valid


def regexquery(request):
    if request.method == 'POST':
        form = RegexForm(request.POST)
        if form.is_valid():
            action = request.POST['action']
            regex = form.cleaned_data['input_regex']
            string = form.cleaned_data['input_string']
            if validate_regex(regex):
                mapping = {'full': re.fullmatch,
                           'first': re.search,
                           'all': re.findall}
                matches = mapping[action](regex, string)
                if isinstance(matches, list):
                    context = {'form': form, 'match': ",".join(matches), 'after': True, 'is_valid': True}
                else:
                    context = {'form': form, 'match': matches.group() if matches else None, 'after': True,
                               'is_valid': True}
            else:
                context = {'form': form, 'is_valid': False, 'after': True}
            return render(request, 'input.html', context)
    else:
        return render(request, 'input.html', {'form': RegexForm, 'after': False})
