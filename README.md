CVRanalytics
============

Computational text analysis and data processing of the Peruvian Truth and Reconciliation Commission Final Report

The Final Report is a nine-volume, eight thousand-page document, which because of its massive scope becomes very hard to access for most readers. The purpose of CVRAnalytics is to develop tools and resources to "mine" the text of the report treating it as a dataset and applying techniques from computational natural language processing, in order to identify salient patterns in the text which might perhaps go unnoticed when performing a close reading.

It is not intended to substitute or discourage a standard reading of the text, but precisely the opposite. By providing high-level overviews and patterns of the contents of the Final Report, it should provide researchers and readers with the means to identify areas of interest or segments that merit further analysis, on which they can then zoom in and look at in detail. It is meant to be both a research companion for people already working with the Report, as well as an introductory channel for people unfamiliarised with it to get broad-level perspectives of its contents.

CVRanalytics is built on Python using the NLTK (natural language toolkit) module. The current version is limited to the "Timeline of Events" subsection of the document, a chronological description of the main historical occurrences during the time of political violence in Peru, 1978-2000. The Timeline included in the Report is structured on a yearly basis and includes subheadings for key topical areas, which have been treated as categories for events. From this data, the program can generate simple tables mapping the occurrences of specific terms over time, or generate slices of events based on year or category. The purpose of the current implementation is to serve as proof-of-concept of what can be accomplished using this type of analysis, to later expand this approach to the full text of the Report.

In doing so, CVRanalytics provides a way to validate hypothesis on the text itself and to explore how it has been constructed, what elements have salience and what is absent from it. Over time, CVRanalytics can become not only an exploratory tool but also a critical one, allowing for further interrogation and research beyond that considered in the Report itself.
