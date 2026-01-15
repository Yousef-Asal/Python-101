
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("-"*30)
        func(*args,**kwargs)
        print("*"*40)
    return wrapper

@my_decorator
def print_text(*args, **kwargs):
    if "skip_first_n" in kwargs:
        skipped_lines = kwargs['skip_first_n']
    else:
        skipped_lines = 0
            
    for text in args:

        if "letter_case" in kwargs and skipped_lines <= 0:
            
            if kwargs['letter_case'] == "upper":
                text = text.upper()
            elif kwargs['letter_case'] == "lower":
                text = text.lower()

        if "add_newlines" in kwargs and skipped_lines <= 0:
            if kwargs['add_newlines']:
                text += '\n'
        
        skipped_lines -= 1
        print(text)

text1 = 'The kitten chased a rolling ball.'
text2 = 'He saved the file and closed it.'
text3 = 'Clouds drifted slowly across the sky.'
text4 = 'A single typo changed the result.'

print_text(text1,text2)
print_text(text1,text2,text3,letter_case= 'lower',skip_first_n=0)
print_text(text1,text2,text3,text4, letter_case= 'upper',add_newlines=False,skip_first_n=2)
print_text(text1,text2,text3,text4,add_newlines=True,skip_first_n=1)
