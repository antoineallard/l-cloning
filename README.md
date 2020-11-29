## L-cloning

The file `lcloning.py` provides the function `save_lcloned_edgelist` that reads an edgelist from a textfile, generates a random _L_-cloned graph, and writes its edgelist into a new textfile.  The original graph is assumed to be **simple**, **unweighted**, **undirected** and **without self-loops**. The name of the copies of each vertex in the _L_-cloned graph is appended "_##", where ## corresponds to the layer's number (between 0 and _L_-1).


The function can be called from another script
```python
from lcloning import save_lcloned_edgelist

save_lcloned_edgelist(original_el_fname, l_cloned_el_fname, L, sep, comment, header)
```
where
```
original_el_fname : string
    path to the file containing the original edgelistin which each line
    corresponds to an undirected edge. The name of the two vertices are
    treated as strings and must correspond to the first two columns of
    each line.
l_cloned_el_fname : string
    path to the file that will contain the L-cloned edgelist
L : int
    number of copies
sep : string (optional; default: any white space)
    character(s) used to separate the columns on a single line
comment : string (optional; default: #)
    any line beginning with this character is ignored
header : bool (optional; default: True)
    add a header to the l-cloned edgelist
```
or can be executed by running
```python
run lcloning.py original_el_fname l_cloned_el_fname L
```

See the validation notebook for further examples.


#### Reference

Network cloning unfolds the effect of clustering on dynamical processes<br>
Ali Faqeeh, Sergey Melnik, and James P. Gleeson<br>
Phys. Rev. E 91:052807 (2015)<br>
doi: [10.1103/PhysRevE.91.052807](http://doi.org/10.1103/PhysRevE.91.052807)
