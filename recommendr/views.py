from django.http import HttpResponse
from recommendr.engine import recommend, get_blog_metadata, preview_entries

def query(request, blog_url):
    print get_blog_metadata(blog_url)
    print preview_entries(blog_url)
    return HttpResponse('<html><body>%s</html><body>' % recommend(blog_url)[0])
