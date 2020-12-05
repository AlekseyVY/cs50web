from django.shortcuts import render
from django import forms

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def page(request, title):
    if util.get_entry(title):
        return render(request, "encyclopedia/page.html", {
            "entry": util.get_entry(title),
            "title": title
        })
    else:
        return render(request, "encyclopedia/404.html")


def get_search(request):
    query = request.GET.get('q')
    full_list = util.list_entries()
    def str_search(full_list, query):
        items = []
        for item in full_list:
            if query in item:
                items.append(item) 
        if len(items) == 1:
            return items[0]
        elif len(items) == 0:
            return False
        else:
            return items
    found = str_search(full_list, query)
    if type(found) == str:
        return render(request, "encyclopedia/search.html", {
            "entry": util.get_entry(found)
        })
    elif found == False:
        return render(request, "encyclopedia/404.html")
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": found
    })

class wikiForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

def new_page(request):
    if request.method == "POST":
        form = wikiForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title):
                return render(request, "encyclopedia/error.html", {
                    "error": title
                })
            else:
                util.save_entry(title, content)
                return render(request, "encyclopedia/page.html", {
                    "entry": util.get_entry(title),
                    "title": title
                })
        else:
            return render(request, "encyclopedia/newPage.html", {
                "Form": wikiForm()
            })
    else:
        return render(request, "encyclopedia/newPage.html", {
            "entry": "Here You can add new Page to WIKI!",
            "Form": wikiForm()
})