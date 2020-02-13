<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link href="CSS/product-catalog.css" rel="stylesheet" type="text/css">
	<!--The following script tag downloads a font from the Adobe Edge Web Fonts server for use within the web page. We recommend that you do not modify it.-->
	<script>var __adobewebfontsappname__="dreamweaver"</script>
	<script src="http://use.edgefonts.net/montserrat:n4:default;source-sans-pro:n2:default.js" type="text/javascript"></script>
	<script type="text/javascript">
	 function openPage(pageURL)
		 {
		 window.location.href = pageURL;
		 }
	</script>
</head>
<jsp:include page="basic-layout.jsp"></jsp:include>
<body>
<div id="content">
   
    <section class="mainContent">
      <div class="productRow"><!-- Each product row contains info of 3 elements -->
        <article class="productInfo"><!-- Each individual product description -->
          	<div><img class="productImage" alt="sample" src="images/Mobile Covers/cherry-wood-phone.jpg"></div>
          	<p class="price">$50</p>
          	<p class="productContent">Cherry wood Iphone case</p>
			<button type="button" name="button" value="Customize" class="buyButton" onclick="openPage('prodct-details.jsp')">Customize</button>
        </article>
        <article class="productInfo"><!-- Each individual product description -->
			<div><img class="productImage" alt="sample" src="images/Mobile Covers/maple-wood-phone.jpg">
				</div>
			<p class="price">$50</p>
          	<p class="productContent">Maple wood Iphone case</p>
          	<button type="button" name="button" value="Customize" class="buyButton" onclick="openPage('prodct-details.jsp')">Customize</button>
        </article>
        <article class="productInfo"> <!-- Each individual product description -->
          	<div><img class="productImage" alt="sample" src="images/Mobile Covers/walnut-phone.jpg">
				</div>
          	<p class="price">$50</p>
          	<p class="productContent">Walnut wood Iphone case</p>
          	<button type="button" name="button" value="Customize" class="buyButton" onclick="openPage('prodct-details.jsp')">Customize</button>
        </article>
      </div>
     <div class="productRow"><!-- Each product row contains info of 3 elements -->
        <article class="productInfo"><!-- Each individual product description -->
          	<div><img class="productImage" alt="sample" src="images/Mobile Covers/oak-wood-phone.jpg"></div>
          	<p class="price">$25</p>
          	<p class="productContent">Oak wood Iphone case</p>
			<button type="button" name="button" value="Customize" class="buyButton" onclick="openPage('prodct-details.jsp')">Customize</button>
        </article>
        <article class="productInfo"><!-- Each individual product description -->
			<div><img class="productImage" alt="sample" src="images/Mobile Covers/pine-wood-phone.jpg">
				</div>
			<p class="price">$50</p>
          	<p class="productContent">Pine wood Iphone case</p>
          	<button type="button" name="button" value="Customize" class="buyButton" onclick="openPage('prodct-details.jsp')">Customize</button>
        </article>
        <article class="productInfo"> <!-- Each individual product description -->
          	<div><img class="productImage" alt="sample" src="images/Mobile Covers/cherry-wood-placard.jpg">
				</div>
          	<p class="price">$50</p>
          	<p class="productContent">Cherry wood Placard</p>
          	<button type="button" name="button" value="Customize" class="buyButton" onclick="openPage('prodct-details.jsp')">Customize</button>
        </article>
      </div>
      <div class="productRow"><!-- Each product row contains info of 3 elements -->
        <article class="productInfo"><!-- Each individual product description -->
          	<div><img class="productImage" alt="sample" src="images/Mobile Covers/walnut-wood-placard.jpg"></div>
          	<p class="price">$25</p>
          	<p class="productContent">Walnut wood Placard</p>
			<button type="button" name="button" value="Customize" class="buyButton" onclick="openPage('prodct-details.jsp')">Customize</button>
        </article>
        <article class="productInfo"><!-- Each individual product description -->
			<div><img class="productImage" alt="sample" src="images/Mobile Covers/maple-wood-placard.jpg">
				</div>
			<p class="price">$50</p>
          	<p class="productContent">Maple wood Placard</p>
          	<button type="button" name="button" value="Customize" class="buyButton" onclick="openPage('prodct-details.jsp')">Customize</button>
        </article>
        <article class="productInfo"> <!-- Each individual product description -->
          	<div><img class="productImage" alt="sample" src="images/Mobile Covers/walnut-wood-desk.jpg">
				</div>
          	<p class="price">$50</p>
          	<p class="productContent">Walnut wood Desk name plate</p>
          	<button type="button" name="button" value="Customize" class="buyButton" onclick="openPage('prodct-details.jsp')">Customize</button>
        </article>
      </div>
    </section>
  </div>
<div class="pages">
	<div class="pagination">
		<a href="#">&laquo;</a>
  		<a class="active" href="#">1</a>
  		<a href="#">2</a>
		<a href="#">3</a>
  		<a href="#">&raquo;</a>
	</div>
</div>
</body>
</html>
