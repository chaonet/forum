# coding: utf-8

from django.core.paginator import Paginator

def paginator(lists, page_no, per_page_num=1):
    p = Paginator(lists, per_page_num)
    if page_no < 0:
        page_no = 1
    if page_no > p.num_pages:
        page_no = p.num_pages
    page_list = [i for i in range(page_no - 5, page_no + 6) if i > 0 and i <= p.num_pages]
    page = p.page(page_no)
    previous_link = page_list[0] - 1
    next_link = page_list[-1] + 1
    first_link = page_list[0] - 2
    last_link = page_list[-1] + 2
    return {"per_page_list":page.object_list,
            "has_previous":previous_link>0, "has_next":next_link<=p.num_pages,
            "has_first":first_link>0, "has_last":last_link<=p.num_pages,
            "previous_link":previous_link,
            "next_link":next_link,
            "current_no":page_no,
            "pages_num":p.num_pages,
            "page_list":page_list
           }