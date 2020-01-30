from config.updateConfig import UpdateConfig

gameCONF = {
    "task": {
        "name": "Game",
        "duration": 10*60,
    },
    "instructions": {
        "text": "Please play the tablet game until told otherwise.",
        "startPrompt": "Press any key to continue. Press q to quit.",
        "questionnaireReminder": "answerQuestionnaire.wav"
    },
    "stimuli": {
        "backgroundColor": {"versionMain": "black", "versionDemo": "blue", "versionDebug": "gray"},
    },
}

updateCofig = UpdateConfig()
updateCofig.addContent(gameCONF)

CONF = updateCofig.getConfig()
