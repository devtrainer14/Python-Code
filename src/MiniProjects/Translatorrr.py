'''
Created on Jun 28, 2019

@author: sipika
'''
from translate import Translator

translator= Translator(from_lang="EN",to_lang="IT")
translation = translator.translate("how are you?")
print(translation)