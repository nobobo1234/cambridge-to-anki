# Cambridge Wordlist to Anki

**This plugin is only compatible with Anki 2.1.**

So you are learning English and you spent a great deal of time creating a beautiful wordlist on the Cambridge Dictionary site but the built-in quiz function is not intelligent enough? That is where this Anki plugin comes to the rescue. It provides an one-way sync between your Cambridge wordlist and Anki. This removes the arduous work of copying over your new words in your wordlist to Anki, so that you can focus on getting your wordlist in your long-term memory. 

This Anki plugin periodically syncs your Cambridge wordlist with your Anki deck, this all happens about once every day in the background if you start up Anki, so you don't have to press any additional buttons. Thank you to (Sirupsen)[https://github.com/sirupsen] and his Anki-Airtable plugin for providing the code foundations for this plugin.

If you _do_ happen to work at Cambridge University, let this be a call that we need a better quiz system for the current wordlists in Cambridge Dictionary+

## How to set it up
1. Go over to the [release page](https://github.com/nobobo1234/cambridge-to-anki) and download the latest ``.ankiaddon`` file.
2. Start up Anki and create a deck that will store your Cambridge wordlist, give it whatever name you fancy.
3. Under the Tools menu, press ``Manage Note Types``.  
![Manage Note Types](https://i.imgur.com/hWRVod1.gif)
3. A menu will pop up, press `Add` button, then press `Add: Basic` and fill in any name you like.  
![Add](https://i.ibb.co/NFXg34x/afbeelding.png)
![Add:Basic](https://i.ibb.co/bXKSJWv/afbeelding.png)
4. Now from the manage note types popup, select your newly made type and click ``Cards...`` in the right sidebar.  
![Cards...](https://i.imgur.com/pw6CRcX.png)
5. Now this step is very important, in the ``Front Template`` input box change the default ``{{FrontSide}}`` to ``{{Definition}}`` or ``{{Word}}`` depending which way you want to learn. Put in the former if you want to learn definition - word or the latter if you want to learn word - definition. Now in the ``Back Template`` input box change the default ``{{FrontSide}}`` to the one you subsituted it with just now, and change the ``{{Back}}`` to the opposite option of what you chose for ``{{FrontSide}}``. It'll look something like the picture beneath. You can customize this further to your looking if you know more about Anki.
![Customize Card](https://i.imgur.com/9OHAN7T.png)
4. Now from the Tools menu (the same menu as the one Manage Note Types was in) select Add-ons.
5. Now click the button ``Install from file...`` and select the ``.ankiaddon`` file you downloaded in the first step. DO NOT RESTART ANKI ALREADY.   
![Install from file](https://i.imgur.com/yACUAlj.png)
6. Select the newly installed "Cambridge to Anki" plugin from the list and press the ``Config`` button in the right sidebar. A window like the one underneath should pop up.  
![config](https://i.ibb.co/RhxxWrD/afbeelding.png)
7. The ID after ``"cambridge_id"`` should be replaced with the ID of your wordlist. Your ID can be found in the URL of your wordlist. E.g. if the url is ``https://dictionary.cambridge.org/plus/wordlist/12345678_cpe-words`` your id is ``12345678`` (do not replace the colon). The ``"deck_name"`` property should be replaced with the exact name of the deck you created in step 2. The ``"model_name"`` property should be replaced with the name of the Note Type you created in step 5.
8. Restart Anki and profit. The syncing will happen by itself now \o/