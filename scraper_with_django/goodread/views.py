from django.shortcuts import render

from .forms import SearchByKeywordForm
from .tasks import good_reads_search_by_keyword_task


# Create your views here.


def search_by_keyword_view(request):
    if request.method == 'POST':
        form = SearchByKeywordForm(request.POST, )
        if form.is_valid():
            # data = {
            #     'keyword': form.cleaned_data['keyword'],
            #     'search_type': form.cleaned_data['search_type'],
            #     'page_count': form.cleaned_data['page_count'],
            # }

            result = good_reads_search_by_keyword_task.delay(
                keyword=form.cleaned_data['keyword'],
                search_type=form.cleaned_data['search_type'],
                page_count=form.cleaned_data['page_count'],
            )
            print('good_reads_search_by_keyword_task', result)
    else:
        form = SearchByKeywordForm()

    return render(request, 'goodread/search_by_keyword.html', {'form': form})
