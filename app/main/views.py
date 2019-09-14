from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source,get_articles,search_articles
# from .forms import ReviewForm
# from ..models import Review


# Views
@main.route('/')
def index():


    '''
    View root page function that returns the index page and its data.
    '''

    title = 'Home - Welcome to the News Website'

    #Getting Science Sources
    science_source = get_source('science')

    #Getting Business Sources
    business_source = get_source('business')

    #Getting Entertainment Sources
    entertainment_source = get_source('entertainment')

    #Getting General Sources
    general_source = get_source('general')

    #Getting Health Sources
    health_source = get_source('health')

    #Getting Sports Sources
    sports_source = get_source('sports')

    #Getting Technology Sources
    technology_source = get_source('technology')

    search_article = requests.args.get('article_query')

    # if search_article:
    #     return redirect(url_for('search',query=search_article))
    # else:
    return render_template('index.html', title = title, science = science_source, business = business_source, entertainment = entertainment_source, sports = sports_source, health = health_source, general = general_source, technology = technology_source)


@main.route('/source/<id>')
def source(id):
    '''
    View source page function that returns the source and its articles.
    '''
    all_articles = get_article(id)
    title = f'Welcome to the News Website -- {id.upper()}'
    id_up = id.upper()

    return render_template('source.html', article = all_articles, title = title, id_up = id_up)


@main.route('/search/')
def search_main():
    '''
    View root page function that returns the search page and the form.
    '''
    title = 'Welcome to the News Website -- Search'

    search_article = requests.args.get('article_query')

    if search_article:
        return redirect(url_for('.search',query=search_article))
        return render_template('search.html', title = title)
    else:
        return render_template('search.html', title = title)


@main.route('/search/<query>')
def search(query):
    '''
    View function to display the search results
    '''
    query_list = query.split(" ")
    query_format = "+".join(query_list)
    searched_articles = search_article(query_format)
    title = f'Search results for "{query}"'
    return render_template('search.html',article = searched_articles,query=query)    