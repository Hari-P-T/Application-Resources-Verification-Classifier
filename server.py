import urllib.parse
from googlesearch import search
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

def search_app(app_name):
    query = f'{app_name} Play Store'
    play_store_results = search(query, num_results=1)
    
    query = f'{app_name} App Store'
    app_store_results = search(query, num_results=1)

    query = f'{app_name} Microsoft Store'
    microsoft_store_results = search(query, num_results=1)
    
    return list(play_store_results), list(app_store_results), list(microsoft_store_results)

def check_untrusted_sources(untrusted_urls, download_keyword, blacklist, extensions):
    untrusted_urls_list = []
    
    for url in untrusted_urls:
        url_domain = urllib.parse.urlparse(url).netloc.lower()
        url_path = urllib.parse.urlparse(url).path.lower()
        
        if (download_keyword in url.lower()) or (url_domain in blacklist) or any(url_path.endswith(extension) for extension in extensions):
            untrusted_urls_list.append(url)
    
    return untrusted_urls_list



def mc(task):
    # Main program
    app_name = task

    play_store_results, app_store_results, microsoft_store_results = search_app(app_name)
    trusted_urls = set()

    # Filter and include only URLs from the trusted sources
    for url in play_store_results:
        if 'play.google.com' in url:
            trusted_urls.add(url)
    for url in app_store_results:
        if 'apps.apple.com' in url:
            trusted_urls.add(url)
    for url in microsoft_store_results:
        if 'microsoft.com' in url:
            trusted_urls.add(url)
    
    blacklist = ['aptoide.com', 'apkpure.com', 'apkcombo.com', 'uptodown.com', 'apkmirror.com', 'softonic.com']
    extensions = ['.apk', '.xapk']
    untrusted_urls = search(app_name)
    
    untrusted_urls_list = check_untrusted_sources(untrusted_urls, 'download', blacklist, extensions)
    
    # Remove trusted URLs from untrusted URLs
    untrusted_urls_list = list(set(untrusted_urls_list) - trusted_urls)
    trusted_urls_list = list(trusted_urls)
    
    # Filter out URLs from support.google.com, youtube.com, and imdb.com
    trusted_urls_list = [url for url in trusted_urls_list if urllib.parse.urlparse(url).netloc.lower() not in ['support.google.com', 'youtube.com', 'imdb.com']]
    untrusted_urls_list = [url for url in untrusted_urls_list if urllib.parse.urlparse(url).netloc.lower() not in ['support.google.com', 'youtube.com', 'imdb.com']]
    
    result = "<div class='result' style='color: white; display: flex; align-items: center; justify-content: center; background: #4070f4;'>Trusted URLs:</div>"
    
    for url in trusted_urls_list:
        result += "<div class='result trusted' style='color: white; display: flex; align-items: center; justify-content: center; background: #4070f4;'>" + url + "</div>"
    
    if len(untrusted_urls_list) > 0:
        result += "<div class='result' style='min-height: 100vh; color: white; display: flex; align-items: center; justify-content: center; background: #4070f4;'>Untrusted URLs:</div>"
    
        for url in untrusted_urls_list:
            result += "<div class='result untrusted' style='color: white; display: flex; align-items: center; justify-content: center; background: #4070f4;'>" + url + "</div>"
    else:
        result += "<div class='result' style='color: white; display: flex; align-items: center; justify-content: center; background: #4070f4;'>No untrusted URLs found.</div>"
    
    return result


 
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task = request.form['content']
        #return(task)
        ot = mc(task)
        return(ot)

    else:
        return render_template('index.html')
 

if __name__ == '__main__':
    app.run(debug=True)

