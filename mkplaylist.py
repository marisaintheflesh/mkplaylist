import os
import markdown2
from jinja2 import Environment, FileSystemLoader
import re

fol = 'C:\\BigShinyTunes\\'
ext = ('.mp3')
mp3s = []


def remove_multiple_newline(text_to_replace):
    return re.sub(r"\n+", "\n", text_to_replace.replace("\r\n", "\n"))


def main():
    md = "# Marisa's Big Shiny Tunes\n"
    for f in os.listdir(fol):
        if f.endswith(ext):
            mp3s.append(f.rsplit('.', 1)[0])
        else:
            continue
        
    for m in mp3s:
        md += "  * " + m + "\n"
        
    md2html = markdown2.markdown(md)
    md2html = remove_multiple_newline(md2html)
    
    env = Environment(loader=FileSystemLoader("templates/"))
    t = env.get_template("template.html")
    playlist = t.render(md=md2html)
    open("Marisa's Big Shiny Tunes.html", "w").write(playlist)
    print("Wrote 'Marisa's Big Shiny Tunes.html'...")
    print("Done.")
    exit(0)


if __name__ == '__main__':
    main()

