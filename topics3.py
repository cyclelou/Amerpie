import os
import re

topics = set()

for filename in os.listdir(r'C:\Users\lplummer\Obsidian\Obsync\Quotes'):
    if filename.endswith('.md'):
        with open(os.path.join(r'C:\Users\lplummer\Obsidian\Obsync\Quotes', filename), 'r', encoding='utf-8') as file:
            content = file.readlines()
            found_topics = False
            for line in content:
                if found_topics:
                    if line.startswith('- '):
                        topic = line.strip('- ').strip()  # Remove hyphen, extra spaces
                        topics.add(topic)
                    else:
                        found_topics = False  

                if line.strip() == 'topics:':
                    found_topics = True

print(topics)