import requests
import json
from aqt import mw
from anki.hooks import addHook
from anki.importing.noteimp import NoteImporter, ForeignNote
import os
from datetime import datetime

Config = mw.addonManager.getConfig(__name__)

class CambridgeImporter(NoteImporter):
    importMode = 0
    allowHTML = True

    def __init__(self, col, wordlist_id):
        NoteImporter.__init__(self, col, "")
        self.records = None
        self.wordlist_id = wordlist_id

    def getRecords(self):
        words = []
        i = 0
        no_words = False

        while not no_words:
            res = requests.get(f'https://dictionary.cambridge.org/plus/wordlist/{self.wordlist_id}/entries/{i}/', headers={'user-agent': 'Mozilla: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3 Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/43.4.'})
            data = res.json()
            if len(data) > 0:
                words = words + data
                i += 1
            else:
                no_words = True

        return words

    def updateModel(self, model):
        models = mw.col.models
        fieldNames = models.fieldNames(model)
        toAdd = ['Word', 'Definition']

        for key in toAdd:
            if key not in fieldNames:
                field = models.newField(key)
                models.addField(model, field)
                fieldNames = models.fieldNames(model)

    def fields(self):
        return len(self.model['flds'])

    def foreignNotes(self):
        notes = []

        for record in self.getRecords():
            note = ForeignNote()

            modelFields = self.model['flds']

            for field in modelFields:
                key = field['name']

                if key == 'Definition':
                    note.fields.append(record["definition"])
                elif key == 'Word':
                    note.fields.append(f'<a href="{record["entryUrl"]}">{record["headword"]}</a>')

            notes.append(note)

        return notes

def importer(col, deck, modelName, wordlist_id):
    did = mw.col.decks.id(deck)
    mw.col.decks.select(did)

    model = mw.col.models.byName(modelName)

    if not model:
        model = mw.col.models.new(modelName)
        mw.col.models.add(model)

        template = mw.col.models.newTemplate(Config['model_name'])
        mw.col.models.addTemplate(model, template)

    model['did'] = did

    deck = mw.col.decks.get(did)
    deck['mid'] = model['id']
    mw.col.decks.save(deck)

    cambridge_importer = CambridgeImporter(mw.col, wordlist_id)
    cambridge_importer.updateModel(model)
    cambridge_importer.initMapping()
    cambridge_importer.run()

def hook():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "words.json"), "r+", encoding="utf-8") as updateFile:
        update = json.load(updateFile)
        if (datetime.now() - datetime.fromtimestamp(update['latestSync'])).days >= 1:
            importer(mw.col, Config['deck_name'], Config['model_name'], Config['cambridge_id'])
            update['latestSync'] = datetime.timestamp(datetime.now())
            updateFile.seek(0)
            json.dump(update, updateFile)

addHook("profileLoaded", hook)
