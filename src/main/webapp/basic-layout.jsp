<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link href="CSS/basic-layout.css" rel="stylesheet" type="text/css">
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
<header>
	<div id="mainWrapper"> 
    <!-- This is the header content. It contains Logo and links -->
    <div onclick="openPage('product-catalog.jsp');" id="logo"> WoodsEngraved
      <!-- <img src="logoImage.png" alt="sample logo"> -->
      <!-- Company Logo text -->
    &nbsp; </div>
    <div id="headerLinks">
	  <a href="Login.jsp" title="Login/Register">Login/Register</a>
    </div>
	<div id="filterBar">
		<div class="home" onclick="openPage('product-catalog.jsp');"><button id="homebtn">Home</button></div>
  		<div class="categories">
    		<button id="categorybtn" title="Category">Categories 
      			<i class="fa fa-caret-down"></i>
    		</button>
    		<div class="dropdown-categories">
      			<a href="#">Phone cases</a>
      			<a href="#">Placard</a>
      			<a href="#">Desk Nameplate</a>
				<a href="#">Invitation Card</a>
				<a href="#">Coaster</a>
    		</div>
	  	</div>
		<div class="occasions">
    		<button id="occasionBtn" title="Occasion">Occasions 
      			<i class="fa fa-caret-down"></i>
    		</button>
    		<div class="dropdown-occasions">
      			<a href="Occasion1.jsp">Christmas</a>
      			<a href="Occasion1.jsp">Mother's Day/Father's Day</a>
      			<a href="Occasion1.jsp">Graduation</a>
				<a href="Occasion1.jsp">Valentine's Day</a>
				<a href="Occasion1.jsp">Weddings</a>
    		</div>
  		</div> 
	</div> 
</div>	
</header>


<body>

</body>
<!-- Footer -->
<div id="footerBar"></div>
<footer>
	<div class="footerlinks">
		<p><a href="about-us.jsp">About us</a></p>
	</div>
</footer>


</html>
