from django.http import HttpResponse, HttpResponseRedirect
from recommendr.engine import recommend, get_blog_metadata, preview_entries, get_all_metadata
from django.shortcuts import render_to_response
from django.template import RequestContext
from recommendr.blog_form import BlogForm

def query(request, blog_url):
    recommendations = recommend(blog_url)
    
    info1 = get_blog_metadata(recommendations[0])
    info2 = get_blog_metadata(recommendations[1])
    info3 = get_blog_metadata(recommendations[2])

    first1 = preview_entries(recommendations[0])[0]
    first2 = preview_entries(recommendations[1])[0]
    first3 = preview_entries(recommendations[2])[0]

    last1 = preview_entries(recommendations[0])[1]
    last2 = preview_entries(recommendations[1])[1]
    last3 = preview_entries(recommendations[2])[1]  

    NO_SOURCE = "No source"
    first1_content = ""
    last1_content = ""
    first2_content = ""
    last2_content = ""
    first3_content = ""
    last3_content = ""
    first1_source_url = ""
    last1_source_url = ""
    first2_source_url = ""
    last2_source_url = ""
    first3_source_url = ""
    last3_source_url = ""
    first1_source_title = NO_SOURCE
    last1_source_title = NO_SOURCE
    first2_source_title = NO_SOURCE
    last2_source_title = NO_SOURCE
    first3_source_title = NO_SOURCE
    last3_source_title = NO_SOURCE

    if(first1['type'] == "photo"):
        first1_content = first1['photos'][0]['alt_sizes'][2]['url']

    if(last1['type'] == "photo"):
        last1_content = last1['photos'][0]['alt_sizes'][2]['url']

    if(first2['type'] == "photo"):
        first2_content = first2['photos'][0]['alt_sizes'][2]['url']

    if(last2['type'] == "photo"):
        last2_content = last2['photos'][0]['alt_sizes'][2]['url']

    if(first3['type'] == "photo"):
        first3_content = first3['photos'][0]['alt_sizes'][2]['url']

    if(last3['type'] == "photo"):
        last3_content = last3['photos'][0]['alt_sizes'][2]['url']

    if('source_url' in first1):
        first1_source_url = first1['source_url']

    if('source_url' in last1):
        last1_source_url = last1['source_url']

    if('source_url' in first2):
        first2_source_url = first2['source_url']

    if('source_url' in last2):
        last2_source_url = last2['source_url']

    if('source_url' in first3):
        first3_source_url = first3['source_url']

    if('source_url' in last3):
        last3_source_url = last3['source_url']

    if('source_url' in first1):
        first1_source_title = first1['source_title']

    if('source_url' in last1):
        last1_source_title = last1['source_title']

    if('source_url' in first2):
        first2_source_title = first2['source_title']

    if('source_url' in last2):
        last2_source_title = last2['source_title']

    if('source_url' in first3):
        first3_source_title = first3['source_title']

    if('source_url' in last3):
        last3_source_title = last3['source_title']

    i_hate_django = {
    'form' : BlogForm(),
    'status' : "yes",
   	'info1_url' : info1['url'],
   	'info1_title' : info1['title'],
   	'info1_name' : info1['name'],
   	'first1_post_url' : first1['post_url'],
   	'first1_type' : first1['type'],
   	'first1_content' : first1_content,
   	'first1_note_count' : first1['note_count'],
   	'first1_source_url' : first1_source_url,
    'first1_source_title' : first1_source_title,
   	'last1_post_url' : last1['post_url'],
   	'last1_type' : last1['type'],
   	'last1_content' : last1_content,
   	'last1_note_count' : last1['note_count'],
   	'last1_source_url' : last1_source_url,
   	'last1_source_title' : last1_source_title,    

   	'info2_url' : info2['url'],
   	'info2_title' : info2['title'],
   	'info2_name' : info2['name'],
   	'first2_post_url' : first2['post_url'],
   	'first2_type' : first2['type'],
   	'first2_content' : first2_content,
   	'first2_note_count' : first2['note_count'],
   	'first2_source_url' : first2_source_url,
   	'first2_source_title' : first2_source_title,
   	'last2_post_url' : last2['post_url'],
   	'last2_type' : last2['type'],
   	'last2_content' : last2_content,
   	'last2_note_count' : last2['note_count'],
   	'last2_source_url' : last2_source_url,
   	'last2_source_title' : last2_source_title,    

   	'info3_url' : info3['url'],
   	'info3_title' : info3['title'],
   	'info3_name' : info3['name'],
   	'first3_post_url' : first3['post_url'],
   	'first3_type' : first3['type'],
   	'first3_content' : first3_content,
   	'first3_note_count' : first3['note_count'],
   	'first3_source_url' : first3_source_url,
   	'first3_source_title' : first3_source_title,
   	'last3_post_url' : last3['post_url'],
   	'last3_type' : last3['type'],
   	'last3_content' : last3_content,
   	'last3_note_count' : last3['note_count'],
   	'last3_source_url' : last3_source_url,
   	'last3_source_title' : last3_source_title

   	}

    return render_to_response('base.html', i_hate_django, context_instance = RequestContext(request))

def index(request):
	return render_to_response('base.html', {'form' : BlogForm(), 'status' : 'no'}, context_instance = RequestContext(request))

def submit_url(request):
    if request.method == 'POST': # If the form has been submitted...
        form = BlogForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            blog_url = form.cleaned_data['blog_url']
            return HttpResponseRedirect('/{0}'.format(blog_url)) # Redirect after POST
    else:
        form = BlogForm() # An unbound form

    return render_to_response('base.html', {
        'form': form
    }, context_instance = RequestContext(request))