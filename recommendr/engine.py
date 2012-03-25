import sys
import urllib2 
import json
import operator

num_rec = 3

api_call = 'http://api.tumblr.com/v2/blog/{0}/posts?api_key=FqwjMWpbllZ4IKjNQXXMc8FQ6Mz2VaZnpn4wGX6kBjiOTb11zw&reblog_info=true&notes_info=true&limit=20'
KEY = 'FqwjMWpbllZ4IKjNQXXMc8FQ6Mz2VaZnpn4wGX6kBjiOTb11zw'
URL = 'http://api.tumblr.com/v2/blog/%s/%s?api_key=' + KEY


def recommend(blog_url):
    raw_info = urllib2.urlopen(api_call.format(blog_url))
    html_dict = json.loads(raw_info.read())
    raw_info.close()
    
    freq_data = {}
    for post in html_dict['response']['posts']:
	
	if 'reblogged_from_url' in post:
	    raw_fd = post['reblogged_from_url']
	    first_degree_url = raw_fd[:raw_fd.find('post/')]
	    if first_degree_url not in freq_data:
		freq_data[first_degree_url] = 0
	    freq_data[first_degree_url] += 5
	
	if 'reblogged_root_url' in post: 
	    raw_source = post['reblogged_root_url']
	    source_url = raw_source[:raw_source.find('post/')]
	    if source_url not in freq_data:
		freq_data[source_url] = 0
	    freq_data[source_url] += 3
	
	if 'notes' in post:
	    for reblog in post['notes']:
		peer_url = reblog['blog_url']
		if peer_url not in freq_data:
		    freq_data[peer_url] = 0
		freq_data[peer_url] += 1

    original_url = 'http://{0}/'.format(blog_url)
    if original_url in freq_data:
	freq_data[original_url] = 0
    sorted_data = sorted(freq_data.iteritems(), key=operator.itemgetter(1),
			 reverse = True)

    recommend = []
    for i in range(3):
	recommend.append(sorted_data[i][0])
    
    print(recommend)
    return recommend

def get_blog_metadata(blog):
    raw_info = urllib2.urlopen(URL % (blog, 'info'))
    info_html = raw_info.read()
    info_dict = json.loads(info_html)
    return info_dict['response']['blog']

def preview_entries(blog):        
    raw_posts = urllib2.urlopen(URL % (blog, 'posts'))
    posts_html = raw_posts.read()
    posts_dict = json.loads(posts_html)
    
    entries = []
    
    photos = 0
    notphotos = 0
    limit = 1
    for x in posts_dict['response']['posts']:
        if photos < limit and x['type'] == 'photo':
            entries.append(x)
            photos += 1
        if notphotos < limit and x['type'] != 'photo':
            entries.append(x)
            notphotos += 1
            
    return entries


if __name__ == '__main__':
    recommend(sys.argv[1])
