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

This turns this:

```
Moon, E., & Howison, J. (2024). A dynamic perspective on software modularity in open source software (OSS) development: A configurational approach. Information and Organization, 34(1), 100499. https://doi.org/10.1016/j.infoandorg.2023.100499 

Du, C., Cohoon, J., Lopez, P., & Howison, J. (2022). Understanding progress in software citation: A study of software citation in the CORD-19 corpus. PeerJ Computer Science, 8, e1022. https://doi.org/10.7717/peerj-cs.1022 

Howison, J., & Bullard, J. (2015). Software in the scientific literature: Problems with seeing, finding, and using software mentioned in the biology literature. Journal of the Association for Information Science and Technology (JASIST), Article first published online: 13 May 2015. DOI: 10.1002/asi.23538 19 Pages/8625 words. 
```

into

```
@article{0,
  author = {Moon, E and Howison, J},
  title = {A dynamic perspective on software modularity in open source software (OSS) development: A configurational approach},
  journal = {Information and Organization},
  date = {2024},
  year = {2024},
  pages = {100499},
  volume = {34},
  number = {1},
  doi = {10.1016/j.infoandorg.2023.100499}
}

@article{1,
  author = {Du, C and Cohoon, J and Lopez, P and Howison, J},
  title = {Understanding progress in software citation: A study of software citation in the CORD-19 corpus},
  journal = {PeerJ Computer Science},
  date = {2022},
  year = {2022},
  pages = {8--e1022},
  doi = {10.7717/peerj-cs.1022}
}

@article{2,
  author = {Howison, J and Bullard, J},
  title = {Software in the scientific literature: Problems with seeing, finding, and using software mentioned in the biology literature},
  journal = {Journal of the Association for Information Science and Technology},
  date = {2015-05},
  year = {2015},
  month = {5},
  number = {13},
  doi = {10.1002/asi.2353819Pages/8625words}
}
```