# Project description
---

## News notifications
> A python program the gives you windows 10 desktop notifications with a hyperlink to the news article.

![Animation1](https://user-images.githubusercontent.com/92341570/141404622-3fbfe529-5f89-42ee-82a7-07125637cd6c.gif)


# Installation


```python
pip install win10toast-click
```

## Example

```python
# modules
import webbrowser
from win10toast_click import ToastNotifier 

# function 
page_url = 'http://example.com/'

def open_url():
    try: 
        webbrowser.open_new(page_url)
        print('Opening URL...')  
    except: 
        print('Failed to open URL. Unsupported variable type.')

# initialize 
toaster = ToastNotifier()

# showcase
toaster.show_toast(
    "Example two", # title
    "Click to open URL! >>", # message 
    icon_path=None, # 'icon_path' 
    duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
    threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
    callback_on_click=open_url # click notification to run function 
    )
```

[link to github page](https://github.com/Jade2290/win10toast-click)