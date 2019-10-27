from pylatex import Document, Section, Subsection, Command,Package
from pylatex.utils import italic, NoEscape

doc = Document(default_filepath='basic',
              documentclass='article')

# doc.packages.append(Package("graph1"))
# doc.preamble.append(Command('date'))
with doc.create(Section('A second section')):
    doc.append('Some text.')
doc.generate_tex()
# doc.generate_pdf(filepath="basic.tex")