# mem0r1a

El <a href="http://www.cverdad.org.pe/ifinal/index.php">Informe Final de la Comisión de la Verdad y la Reconciliación en el Perú</a> es un documento que consta de nueve volúmenes y ocho mil páginas. Se trata quizás del documento más importante en la historia peruana reciente, documentando no solamente 20 años de violencia política en el Perú, sino también la complejidad de un panorama económico y social que dio lugar al surgimiento y desarrollo de dicha violencia.

Dado su alcance masivo, el documento es difícil de acceder y procesar para la gran mayoría de lectores. mem0r1a busca desarrollar un conjunto de herramientas y recursos para "minar" y analizar el texto del informe, convirtiéndolo en una base de datos que pueda ser analizada utilizando herramientas computacionales.

No pretende sustituir o desincentivar la lectura del texto mismo del informe, sino todo lo contrario. Al brindar una visión amplia de los patrones del contenido del informe, permite a investigadores y lectores identificar áreas de interés y segmentos que ameriten un análisis más detallado. mem0r1a busca ser un complemento de investigación para personas que estén ya trabajando con el informe, así como un canal introductorio para aquellos que no están familiarizados con su contenido.

<hr />

The Final Report of the <a href="http://www.cverdad.org.pe/ingles/ifinal/index.php">Peruvian Truth and Reconciliation Commission Final Report</a> is a nine-volume, eight thousand-page document. It is perhaps the single most important document in recent Peruvian history, documenting not only 20 years of political violence in Peru, but also a complex social and economic landscape that led to the outbreak and development of said violence.

Because of its massive scope, the document is very hard to access and process for most readers. mem0r1a wants to develop a set of tools and resources to "mine" and analyse the text of the report, turning it into a dataset that can be analysed using computational tools.

It is not intended to substitute or discourage a traditional reading of the text, but precisely the opposite. By providing high-level overviews and patterns of the contents of the Final Report, it should provide researchers and readers with the means to identify areas of interest or segments that merit further analysis, on which they can then zoom in and look at in detail. It is meant to be both a research companion for people already working with the Report, as well as an introductory channel for people unfamiliarised with it to get broad-level perspectives of its contents.

### Development

mem0r1a's first iteration, as CVRanalytics, was built on Python and used the NLTK (natural language toolkit) module to do some basic natural language processing and analysis. This version is available under the protoypes/cronologia folder, and is limited to the "Timeline of Events" subsection of the document, a chronological description of the main historical occurrences between 1978-2000. The Timeline included in the Report is structured on a yearly basis and includes subheadings for key topical areas, which have been treated as categories for events. From this data, the program can generate simple tables mapping the occurrences of specific terms over time, or generate slices of events based on year or category. The purpose of the current implementation is to serve as proof-of-concept of what can be accomplished using this type of analysis, to later expand this approach to the full text of the Report. I've share some of the preliminary analysis of this subset of data using simple word frequencies and frequent bigrams to illustrate how we can use computational analysis to surface preliminary leads we can expand in investigation.

### Credits

mem0r1a was originally developed by <a href="http://marisca.pe">Eduardo Marisca</a> at <a href="http://web.mit.edu">MIT</a>, as a class project in exploratory programming for Nick Montfort's Workshop in Comparative Media. The code is freely available for anyone to use, and <a href="http://cverdad.org.pe/ifinal/index.php">the document of the Report itself</a> is in the public domain under Peruvian legislation.
