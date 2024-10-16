# Text reference conversion to bibtex using Grobid

Shows an example of processing textual citations (as contained in UT Austin's "publications database" or on CVs) into structured metadata.

Uses the Grobid system, documented here: https://grobid.readthedocs.io/en/latest/Grobid-service/#apiprocesscitationlist

First run docker image of Grobid:

```
docker run --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:0.8.0
```

Then the process_citations.py script accesses that docker image.  I ran this python code from another docker image (using repo2docker); if you are running python locally then you'll need to change the URL from `host.docker.internal` to `localhost`.

```
$ python process_citations.py plain_text_citations.txt
```

Demonstration script reads the plain text citations from a text file, then splits it on double newline, passing three text chunks to Grobid.  It requests results in the bibtex format.
