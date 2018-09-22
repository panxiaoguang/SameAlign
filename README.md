# SameAlign
One key to find the same protein sequence
<h2>Required environment:</h2>
<a href="https://www.python.org/" target="_blank"> Python3</a>
<h2>Algorithm adopted:</h2>
<p style="text-indent: 2em;">In general, the protein sequences downloaded from the <a href="https://www.uniprot.org/">uniprot</a> database have redundant sequences, so once you want to determine the exact protein that a particular strain contains, you need to remove the similar protein sequences.Since proteins are divided into four categories: polar amino acids, acidic amino acids, basic amino acids, and hydrophobic amino acids, we believe that the sequence is consistent when amino acids of the same length are of the same nature at the same site.</p>
<h2>Amino acid classification:</h2>
<ul>
<li class="success">Polar amino acid  : Gly, Ser, Thr, Tyr, Gys, Gln,Asn</li>
<li class="danger"> Acidic amino acids  : Asp,Glu</li>
<li class="primary">Alkaline amino acids  : Arg,Lys,His</li>
<li style="color: black;">Hydrophobic amino acids , Ala, Val, Ile, Leu, Pro, Trp, Phe, Met</li>
</ul>
<h2>Usage:</h2>
If it's Windows, enter CMD</br>
cd goes into the desired directory</br>
<code>Python -i fastafile</code>
<h2>Results:</h2>
<p style="text-indent: 2em;">You can get all non-duplicated AC number list output, plus the same AC number will give a hint.</p>
