// Dom Elements
let navigation = document.getElementById("navigation");
let search_visualization_navigation = document.getElementById("serch_visualization_navigation");

navigation.innerHTML = ('\
<div class="navigation">\
<a href="../index.html"><img src="../branding/logo.png" height="45px" width="45px"/></a>\
<div class="navigation_top_links">\
  <a href="../404.html">Tutorial</a>\
  <a href="../404.html">Documentation</a>\
</div>\
</div>\
');

search_visualization_navigation.innerHTML = (`\
<div id="serch_visualization_navigation" class="serch_visualization_navigation">\
  <a href="./linear_search.html">Linear Search</a>\
  <a href="./jump_search.html">Jump Search</a>\
  <a href="./binary_search.html">Binary Search</a>\
  <a href="./interpolation_search.html">Interpolation Search</a>\
</div>\
`);
