
#To install language_check, type "pip install language_check" in command prompt.
import language_check

#create an object with respect to particular language ,here en-US indicates American english
lang=language_check.LanguageTool('en-US')

#consider some text
text="i is student"

#check() is used to find mistakes and it also provides suggestions to replace mistakes with all possible alternatives and those are stored in errors
errors=lang.check(text)

print("number of errors:"+str(len(errors)))

for i in errors:
    print(i)

#correct() replaces mistakes with available alternatives.If there are more than one alternative then it will consider first altenative to replace the mistake.
print("-------------------after correction-----------------------")
print(language_check.correct(text,errors))
