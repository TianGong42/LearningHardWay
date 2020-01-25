import random 
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website 
# 这句方法的意思是，通过urlopen函数，入参是链接，然后着行读取内容
# 并且将读取的每一行的前后的空格之类去除，然后使用utf-8的编码方式，最后转换成字符串，添加到WORDS列表里
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

# 转换方法，入参片段和短语
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

        for sentence in snippet, phrase:
            result = sentence[:]

            # fake class names
            for word in class_names:
                result = result.replace("%%%", word, 1)

            # fake other names
            for word in other_names:
                result = result.replace("***", word, 1)
            
            # fake parameter lists
            for word in param_names:
                result = result.replace("@@@", word, 1)

            results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        # 将PHRASES这个字段的键拼成一个list
        snippets = list(PHRASES.keys())
        print(snippets)
        # 使用random的shuffle方法，将snippets列表修修改为乱序
        random.shuffle(snippets)

        for snippet in snippets:
            # 然后在snippets列表中顺序取出东西，在字典PHRASES取出东西
            # 其实就是在PHRASES中乱序取出值
            phrase = PHRASES[snippet]
            # 然后就是将乱序后，但是依然成对的字典值，传入到convert函数中
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")