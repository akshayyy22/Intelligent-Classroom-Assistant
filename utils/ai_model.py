import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def correct_text(text):
    return tool.correct(text)
