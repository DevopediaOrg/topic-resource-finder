# Overview

Authors write articles on tech topics on Devopedia. Each article can be extended by an algorithm that pulls in content relevant to that topic. This goal of this project is to identify relevant content given a topic.

For example, let's say we're looking at an article titled "Data Science". The algorithm would identify videos, books, projects, etc. relevant to this topic. More specifically, consider the following categories of content:
* GitHub/GitLab/BitBucket projects
* Videos
* MOOC courses
* Books
* Tutorials or Jupyter Notebooks
* Blog posts


# Deliverables

Project must be implemented in Python3 with a modular design. Provide basic documentation and example output. Designing a nice web-based UI to show the results is optional. It's sufficient to write output to files or a database.

Code should support the following:
* Find content in each of the categories listed above.
* Get the metadata (stars, likes, comments, views, word count, playing time for videos, etc.) of each content.
* Use the content and metadata to give suitable ranking. While ranking, give priority to more likes or stars; to more recent content; to videos shorter than 12 minutes; to reputed sources; etc.
* Pick the top three content in each category based on ranking. Output these along with URLs so that we may embed them into Devopedia articles at a later point.
