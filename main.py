import time

'''
Terminal display functions
'''


def display_banner(print_cool: bool=True) -> None:
    display_text_list: list = [
    

'___  _  _ _ _    ___  _ _  _ ____            ',
'|__] |  | | |    |  \ | |\ | | __            ',
'|__] |__| | |___ |__/ | | \| |__]            ',
'____ ____ ____ ___ ___  ____ _ _  _ ___ ____ ',
'|___ |  | |  |  |  |__] |__/ | |\ |  |  [__  ',
'|    |__| |__|  |  |    |  \ | | \|  |  ___] \n',
                                             
    'Homealone Specifications, 2024\n'
    ]
    
    for line in display_text_list:
        if print_cool:
            display_cool(line)
        else:
            print(line)


def display_cool(text: str) -> None:
    print(text)
    time.sleep(0.1)


def main():
    """ Terminal prompts
    """

    display_banner()

    input_image_data()
    

if __name__ == "__main__":
    main()