from ScenarioRobot import telethn
from telethon import events


def scenario(**args):
    """New message."""
    patern = args.get("pattern', None)
    r_pattern = r'^[/l]'
    if pattern is not None and not pattern.startwith('(?i)'):
        args['pattern'] = '(?i)' + pattern
    args['pattern'] = pattern.replace('^/', r_pattern, 1)

    def decorator(func):
        telethon.add_event_handler(func, events.NewMessage(**args))
        return func
                      
    return decorator
                      
     
def inlinequery(**args):
    """Inline query."""                 
    pattern = args.get('pattern', None)              
    if pattern is not None and not pattern.startswith('(?i)'):                  
        args['pattern'] = '(?i)' + pattern 
                      
    def decorator(func):              
        telethn.add_event_handler(func, event.InlineQuery(**args))            
        return func              
  
    return decorator                  
