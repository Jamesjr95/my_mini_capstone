'''Give hyperlink notifications with news'''



import requests
import webbrowser
from win10toast_click import ToastNotifier 


def open_url():
        try:
            webbrowser.open_new(url)
            print('Opening URL...')
        except:
            print('Failed to open URL. Unsupported variable type.')

toaster = ToastNotifier()

news_options = {
    '1': 'science',
    '2': 'business',
    '3': 'entertainment',
    '4': 'general',
    '5': 'health',
    '6': 'sports',
    '7': 'technology'
}


i = 0  
while True:
    
    print('Get news notifications')

    for label, option in news_options.items():
        print(f'\n{label}. {option}')

    user_news = input('\nEnter the number of the topic you want\n\n>> ')

    user_news = news_options.get(user_news)


    response = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&category={user_news}&apiKey=')
    data = response.json()['articles']
    
    name = (data[i]['source']['name']) # name of creator of article
    title = (data[i]['title'])
    url = (data[i]['url'])

    

    toaster = ToastNotifier() # create an instance of toaster

    toaster.show_toast(
        (data[i]['title']), #headline of the news article
        (data[i]['source']['name']), #name of the creator
        icon_path=None,
        duration=5,
        threaded=True,
        callback_on_click=open_url
    )
    
    i += 1
    
    more_news = input('\nTo continue type continue or type q to quit\n\n >>')
    
    if more_news == 'q':
        break
    else:
        continue
    
    













