x = """

https://content.tupaki.com/h-upload/2024/04/23/364263-hwruvmus.gif
https://content.tupaki.com/h-upload/2024/04/23/364261-cjrlovqn.gif
https://content.tupaki.com/h-upload/2024/04/23/364264-im0tc4s5.gif
https://content.tupaki.com/h-upload/2024/04/23/364259-07ljlob0.gif
https://content.tupaki.com/h-upload/2024/04/23/364260-hukk4yga.gif
https://content.tupaki.com/h-upload/2024/04/23/364262-h9aw7plu.gif
https://content.tupaki.com/h-upload/2024/04/23/364265-l32warm3.gif
https://content.tupaki.com/h-upload/2024/04/23/364266-lvo0nds9.gif
https://content.tupaki.com/h-upload/2024/04/23/364267-nbgi5rm2.gif
https://content.tupaki.com/h-upload/2024/04/23/364268-1dpmwssc.gif
https://content.tupaki.com/h-upload/2024/04/23/364270-fn504zp1.gif
https://content.tupaki.com/h-upload/2024/04/23/364269-7xzgcvis.gif
https://content.tupaki.com/h-upload/2024/04/23/364272-lf5hf7qs.gif
https://content.tupaki.com/h-upload/2024/04/23/364273-l026egmx.gif
https://content.tupaki.com/h-upload/2024/04/23/364271-hkr8qpm1.gif
https://content.tupaki.com/h-upload/2024/04/23/364275-x5d2irzo.gif
https://content.tupaki.com/h-upload/2024/04/23/364274-pvlyq1sv.gif
https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif?width=500&amp;height=300

"""

# Split the string into individual URLs
urls = x.strip().split("\n")

# Format each URL into the desired <img> tag format
formatted = '\n'.join([f'<img src="{url}" href="{url}">' for url in urls])

print(formatted)