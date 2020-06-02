from config.updateConfig import UpdateConfig

gameCONF = {
    "task": {
        "name": "Game",
        "duration":  {"versionMain": 10*60, "versionDemo": 10, "versionDebug": 1},
    },
    "instructions": {
        "text": "Please play the tablet game until told otherwise.",
        "startPrompt": "start.wav",
        "endPrompt": "end.wav",
        "questionnaireReminder": "answerQuestionnaire.wav"
    },
    "stimuli": {
        "backgroundColor": {"versionMain": "black", "versionDemo": "blue", "versionDebug": "gray"},
    },
}

updateCofig = UpdateConfig()
updateCofig.addContent(gameCONF)

CONF = updateCofig.getConfig()
